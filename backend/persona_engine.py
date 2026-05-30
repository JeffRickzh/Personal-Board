import os
import re
import math
from typing import List, Dict, Tuple

class PersonaEngine:
    def __init__(self, corpus_path: str):
        self.corpus_path = corpus_path
        self.chunks: List[Dict[str, str]] = [] # list of {"source": "...", "content": "..."}
        self.idf: Dict[str, float] = {}
        self.doc_vectors: List[Dict[str, float]] = []
        self.is_indexed = False
        
    def tokenize(self, text: str) -> List[str]:
        """
        A robust, zero-dependency bilingual tokenizer.
        - Chinese: character-level unigram + bigram
        - English/Alphanumeric: whole words
        """
        text = text.lower()
        # Extract Chinese character runs and alphanumeric runs
        words = re.findall(r'[\u4e00-\u9fa5]+|[a-z0-9]+', text)
        tokens = []
        for word in words:
            if re.match(r'[\u4e00-\u9fa5]+', word):
                # Chinese character sequence
                for i in range(len(word)):
                    tokens.append(word[i]) # unigram
                    if i < len(word) - 1:
                        tokens.append(word[i:i+2]) # bigram
            else:
                tokens.append(word) # Alphanumeric word (English token)
        return tokens

    def load_and_chunk(self):
        """
        Scan all subdirectories recursively for markdown and PDF files and segment them.
        """
        if not os.path.exists(self.corpus_path):
            print(f"Warning: Corpus path '{self.corpus_path}' not found.")
            return

        md_count = 0
        pdf_count = 0
        
        for root, _, files in os.walk(self.corpus_path):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    self.process_file(file_path, file)
                    md_count += 1
                elif file.endswith(".pdf"):
                    file_path = os.path.join(root, file)
                    self.process_pdf(file_path, file)
                    pdf_count += 1
                        
        print(f"Persona Engine [{os.path.basename(self.corpus_path)}]: Chunked {md_count} markdown and {pdf_count} PDF files into {len(self.chunks)} passages.")

    def _beautify_source(self, filename: str) -> str:
        source_name = filename.replace("-zh.md", "").replace(".md", "").replace(".pdf", "").replace("-", " ")
        # Heuristic mapping for common Munger files for backwards compatibility
        beautify_map = {
            "2005 The Psychology of Human Misjudgment": "2005年演讲《人类误判心理学》",
            "1994 A Lesson on Elementary Worldly Wisdom As It Relates To Investment Management Business": "1994年南加州大学《论普世智慧与投资商业的关系》",
            "1996 A Lesson on Elementary Worldly Wisdom Revisited Stanford Law School Practical Thought About Practical Thought": "1996年斯坦福法学院《再论普世智慧与现实思维》",
            "1996 Practical Thought About Practical Thought": "1996年演讲《关于现实思维的思考》",
            "1986 Harvard School Commencement Speech": "1986年哈佛学校毕业典礼演讲",
            "004 Munger's checklist": "《查理·芒格的492个问题清单》",
            "002 The Great Financial Scandal of 2003": "《2003年伟大的金融大丑闻》",
            "1998 The Need for More Multidisciplinary-Skills from Professionals Educational Implications": "1998年哈佛法学院《专业人士需要更多跨学科技能》",
        }
        for key, beauty in beautify_map.items():
            if key in source_name:
                return beauty
                
        # Heuristic for Wesco / Shareholder letters based on year
        if "letters" in filename.lower() or "shareholder" in filename.lower():
            year_match = re.search(r'\d{4}', filename)
            year = year_match.group(0) if year_match else ""
            if year:
                return f"{year}年致股东信"
                
        return source_name

    def process_pdf(self, filepath: str, filename: str):
        """
        Extract text from PDF using NativePDFParser, split into logical segments of 300-800 characters.
        """
        from pdf_parser import NativePDFParser
        
        text = NativePDFParser.extract_text(filepath)
        if not text or len(text.strip()) < 50:
            return
            
        source_name = self._beautify_source(filename)

        # Split PDF text into logical segments by punctuation or paragraph chunks
        # This keeps contextual sentences together
        sentences = re.split(r'(?<=[。？！；.?!;])\s*', text)
        
        current_chunk = []
        current_len = 0
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            
            s_len = len(sentence)
            # If combining this sentence exceeds 600 characters, store current chunk and start a new one
            if current_len + s_len > 600 and current_chunk:
                self.chunks.append({
                    "source": source_name,
                    "content": " ".join(current_chunk)
                })
                current_chunk = [sentence]
                current_len = s_len
            else:
                current_chunk.append(sentence)
                current_len += s_len
                
        if current_chunk:
            self.chunks.append({
                "source": source_name,
                "content": " ".join(current_chunk)
            })


    def process_file(self, filepath: str, filename: str):
        """
        Read a file, split into paragraphs/headers, and combine into chunks of 300-800 characters.
        """
        source_name = self._beautify_source(filename)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='gbk') as f:
                    content = f.read()
            except Exception:
                return

        # Strip frontmatter
        content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL)
        
        # Split by paragraph
        paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
        
        current_chunk = []
        current_len = 0
        
        for para in paragraphs:
            # Skip very short navigation lines or markdown formatting junk
            if len(para) < 15 and ("layout:" in para or "categories:" in para or "---" in para):
                continue
                
            para_len = len(para)
            if current_len + para_len > 600 and current_chunk:
                # Store the accumulated chunk
                self.chunks.append({
                    "source": source_name,
                    "content": "\n".join(current_chunk)
                })
                current_chunk = [para]
                current_len = para_len
            else:
                current_chunk.append(para)
                current_len += para_len
                
        if current_chunk:
            self.chunks.append({
                "source": source_name,
                "content": "\n".join(current_chunk)
            })

    def build_index(self):
        """
        Calculate TF-IDF terms across all chunks.
        """
        if not self.chunks:
            self.load_and_chunk()
            
        if not self.chunks:
            print(f"Persona Engine [{os.path.basename(self.corpus_path)}]: No chunks found, skipping index.")
            return

        doc_count = len(self.chunks)
        df: Dict[str, int] = {}
        
        # Step 1: Tokenize chunks and count Document Frequencies (DF)
        chunk_tokens: List[List[str]] = []
        for chunk in self.chunks:
            tokens = self.tokenize(chunk["content"])
            chunk_tokens.append(tokens)
            unique_tokens = set(tokens)
            for token in unique_tokens:
                df[token] = df.get(token, 0) + 1
                
        # Step 2: Calculate Inverse Document Frequency (IDF)
        for token, count in df.items():
            self.idf[token] = math.log((doc_count + 1) / (count + 0.5)) + 1
            
        # Step 3: Compute TF-IDF vectors for chunks
        for tokens in chunk_tokens:
            tf: Dict[str, float] = {}
            for token in tokens:
                tf[token] = tf.get(token, 0) + 1
                
            tfidf_vector: Dict[str, float] = {}
            for token, count in tf.items():
                # tf-idf = tf * idf
                tfidf_vector[token] = count * self.idf[token]
                
            # Normalize vector (L2 norm)
            norm = math.sqrt(sum(v * v for v in tfidf_vector.values()))
            if norm > 0:
                normalized_vector = {k: v / norm for k, v in tfidf_vector.items()}
            else:
                normalized_vector = tfidf_vector
                
            self.doc_vectors.append(normalized_vector)
            
        self.is_indexed = True
        print(f"Persona Engine [{os.path.basename(self.corpus_path)}]: Successfully built TF-IDF index for {len(self.chunks)} chunks.")

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, str]]:
        """
        Query the corpus and return the top_k most relevant passage chunks.
        """
        if not self.is_indexed:
            self.build_index()
            
        if not self.chunks:
            return []
            
        query_tokens = self.tokenize(query)
        if not query_tokens:
            return self.chunks[:top_k]
            
        # Compute query TF-IDF vector
        query_tf: Dict[str, float] = {}
        for token in query_tokens:
            query_tf[token] = query_tf.get(token, 0) + 1
            
        query_vector: Dict[str, float] = {}
        for token, count in query_tf.items():
            if token in self.idf:
                query_vector[token] = count * self.idf[token]
                
        query_norm = math.sqrt(sum(v * v for v in query_vector.values()))
        if query_norm > 0:
            query_vector = {k: v / query_norm for k, v in query_vector.items()}
            
        # Compute Cosine Similarities
        scores: List[Tuple[int, float]] = []
        for idx, doc_vector in enumerate(self.doc_vectors):
            score = 0.0
            # Dot product of query and doc vectors
            for token, q_val in query_vector.items():
                if token in doc_vector:
                    score += q_val * doc_vector[token]
            scores.append((idx, score))
            
        # Sort by score descending
        scores.sort(key=lambda x: x[1], reverse=True)
        
        # Return top_k matching chunks
        results = []
        for idx, score in scores[:top_k]:
            if score > 0.01: # Filter out absolute zero overlap
                results.append(self.chunks[idx])
                    
        # Fallback to top chunks
        while len(results) < top_k and len(self.chunks) > len(results):
            for c in self.chunks:
                if c not in results and len(results) < top_k:
                    results.append(c)
                    
        return results
