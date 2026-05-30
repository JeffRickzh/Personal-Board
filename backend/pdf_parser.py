import re
import zlib
import os

class NativePDFParser:
    @staticmethod
    def extract_text(filepath: str) -> str:
        """
        Extracts readable text from a PDF file using pure-Python zlib decompression
        and token matching. Requires zero external library dependencies.
        """
        if not os.path.exists(filepath):
            return ""
            
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
        except Exception as e:
            print(f"NativePDFParser: Error reading '{filepath}': {str(e)}")
            return ""

        # PDF stream objects are enclosed between 'stream' and 'endstream'
        # We capture them recursively using regex
        stream_pattern = re.compile(b'stream\r?\n(.*?)\r?\nendstream', re.DOTALL)
        streams = stream_pattern.findall(data)
        
        text_blocks = []
        
        for stream in streams:
            decompressed = None
            # Attempt to decompress stream content using zlib (Deflate algorithm)
            try:
                decompressed = zlib.decompress(stream)
            except Exception:
                try:
                    # Try raw deflate stream without headers (zlib fallback)
                    decompressed = zlib.decompress(stream, -zlib.MAX_WBITS)
                except Exception:
                    continue
                    
            if decompressed:
                # We check if the decompressed stream contains text operators: Tj, TJ, BT, ET
                if b'Tj' in decompressed or b'TJ' in decompressed or b'BT' in decompressed:
                    # Decode stream using latin-1 to keep byte mapping preserved for regex extraction
                    text_str = decompressed.decode('latin-1', errors='ignore')
                    
                    cleaned_matches = []
                    
                    # 1. Parse text elements inside standard parentheses: (Chinese/ASCII)
                    paren_matches = re.findall(r'\((.*?)\)', text_str)
                    for match in paren_matches:
                        # Unescape PDF special chars
                        clean = match.replace('\\)', ')').replace('\\(', '(').replace('\\\\', '\\')
                        cleaned_matches.append(clean)
                        
                    # 2. Parse text elements inside hex brackets: <4e60597d...> (UTF-16BE/UTF-8)
                    hex_matches = re.findall(r'<([0-9a-fA-F]+)>', text_str)
                    for h in hex_matches:
                        try:
                            b = bytes.fromhex(h)
                            if b.startswith(b'\xfe\xff'):
                                cleaned_matches.append(b[2:].decode('utf-16-be', errors='ignore'))
                            else:
                                cleaned_matches.append(b.decode('utf-8', errors='ignore'))
                        except Exception:
                            continue
                            
                    if cleaned_matches:
                        text_blocks.append(" ".join(cleaned_matches))
                        
        full_text = "\n".join(text_blocks)
        
        # 3. Resolve octal escape sequences (e.g. \344\275\240\345\245\275 -> 你好) common in older PDFs
        def replace_octal(match):
            octals = match.group(0).split('\\')[1:]
            try:
                b = bytes([int(o, 8) for o in octals])
                return b.decode('utf-8', errors='ignore')
            except Exception:
                return match.group(0)
                
        full_text = re.sub(r'(\\\d{3})+', replace_octal, full_text)
        
        # 4. Clean up excessive whitespaces or formatting residue
        full_text = re.sub(r'\s+', ' ', full_text).strip()
        
        return full_text
