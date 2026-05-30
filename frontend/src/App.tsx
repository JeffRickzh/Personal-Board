import React, { useState, useRef, useEffect } from 'react';
import { Send, Loader2, BookOpen, Clock, X, Sparkles, Activity, CheckCircle2 } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

// Local high-quality generated sketch-watercolor avatars
import mungerPhoto from './assets/munger.png';
import buffettPhoto from './assets/buffett.png';
import grahamPhoto from './assets/graham.png';

const BOARD_MEMBERS = [
  { id: 'munger', name: 'Charlie Munger', title: 'Vice Chairman', photo: mungerPhoto, color: 'text-amber-600', border: 'border-amber-400', ring: 'ring-amber-200' },
  { id: 'buffett', name: 'Warren Buffett', title: 'Chairman', photo: buffettPhoto, color: 'text-emerald-600', border: 'border-emerald-400', ring: 'ring-emerald-200' },
  { id: 'paul_graham', name: 'Paul Graham', title: 'Advisor', photo: grahamPhoto, color: 'text-indigo-600', border: 'border-indigo-400', ring: 'ring-indigo-200' },
];


interface MemberState {
  status: 'idle' | 'retrieving' | 'speaking' | 'done';
  message?: string;
  text: string;
  quotes: any[];
}

interface CurrentSession {
  [key: string]: MemberState;
}

interface HistoryItem {
  query: string;
  session: CurrentSession;
  resolution: string;
}

const MarkdownComponents: any = {
  h1: ({node, ...props}: any) => <h1 className="text-3xl font-bold mt-6 mb-4" {...props} />,
  h2: ({node, ...props}: any) => <h2 className="text-2xl font-bold mt-5 mb-3 text-slate-800" {...props} />,
  h3: ({node, ...props}: any) => <h3 className="text-xl font-bold mt-4 mb-2 text-slate-800" {...props} />,
  p: ({node, ...props}: any) => <p className="mb-4 leading-[1.8]" {...props} />,
  ul: ({node, ...props}: any) => <ul className="list-disc pl-6 mb-4 space-y-2" {...props} />,
  ol: ({node, ...props}: any) => <ol className="list-decimal pl-6 mb-4 space-y-2" {...props} />,
  li: ({node, ...props}: any) => <li className="leading-[1.8]" {...props} />,
  strong: ({node, ...props}: any) => <strong className="font-black text-slate-900" {...props} />,
  table: ({node, ...props}: any) => <div className="overflow-x-auto mb-4"><table className="min-w-full border border-slate-200 text-sm" {...props} /></div>,
  th: ({node, ...props}: any) => <th className="bg-slate-100 px-4 py-3 border border-slate-200 font-bold text-left" {...props} />,
  td: ({node, ...props}: any) => <td className="px-4 py-3 border border-slate-200" {...props} />,
  blockquote: ({node, ...props}: any) => <blockquote className="border-l-4 border-indigo-200 pl-4 italic text-slate-600 mb-4" {...props} />,
  code: ({node, className, ...props}: any) => {
    const isInline = !className || !className.includes('language-');
    return isInline ? <code className="bg-slate-100 px-1.5 py-0.5 rounded text-sm font-mono text-indigo-600" {...props} /> : <div className="bg-slate-900 text-slate-50 p-4 rounded-xl overflow-x-auto mb-4 font-mono text-sm"><code className={className} {...props} /></div>;
  }
};

export default function App() {
  const [input, setInput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);
  
  const [history, setHistory] = useState<HistoryItem[]>([]);
  const [fileHistory, setFileHistory] = useState<{filename: string, timestamp: number}[]>([]);
  const [viewingHistory, setViewingHistory] = useState<string | null>(null);
  const [currentSession, setCurrentSession] = useState<CurrentSession>({});
  const [currentQuery, setCurrentQuery] = useState('');
  const [secretaryResolution, setSecretaryResolution] = useState('');
  const [secretaryStatus, setSecretaryStatus] = useState<'idle' | 'synthesizing' | 'done'>('idle');

  const activeMemberIds = BOARD_MEMBERS.map(m => m.id);
  const scrollRef = useRef<HTMLDivElement>(null);

  // Auto-scroll the main stage
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [currentSession, secretaryResolution]);

  useEffect(() => {
    if (isDrawerOpen) {
      fetch('http://127.0.0.1:8000/api/history')
        .then(res => res.json())
        .then(data => setFileHistory(data))
        .catch(console.error);
    }
  }, [isDrawerOpen]);

  const loadHistoryFile = async (filename: string) => {
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/history/${filename}`);
      const data = await res.json();
      if (data.content) {
        setViewingHistory(data.content);
        setIsDrawerOpen(false);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleSubmit = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!input.trim() || isProcessing) return;

    const query = input.trim();
    setInput('');
    setCurrentQuery(query);
    setIsProcessing(true);
    setCurrentSession({});
    setSecretaryResolution('');
    setSecretaryStatus('idle');
    setViewingHistory(null);

    try {
      const response = await fetch('http://127.0.0.1:8000/api/chat_stream', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: query, board_member_ids: activeMemberIds })
      });

      if (!response.body) throw new Error('No readable stream');
      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');

      let buffer = '';
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        
        buffer += decoder.decode(value, { stream: true });
        
        // Split the buffer by double newlines to isolate complete SSE messages
        const messages = buffer.split('\n\n');
        // Keep the last, potentially incomplete message in the buffer
        buffer = messages.pop() || '';
        
        for (const message of messages) {
          if (!message.trim()) continue;
          
          // An SSE message can contain multiple 'data: ' lines if split, though normally just one
          const lines = message.split('\n');
          let dataStr = '';
          for (const line of lines) {
            if (line.startsWith('data: ')) {
              dataStr += line.slice(6);
            }
          }
          
          if (!dataStr) continue;
          
          try {
            const data = JSON.parse(dataStr);
            
            if (data.event === 'status') {
              if (data.member_id === 'secretary') {
                 setSecretaryStatus('synthesizing');
              } else {
                setCurrentSession(prev => ({
                  ...prev,
                  [data.member_id]: { 
                    ...prev[data.member_id], 
                    status: data.state, 
                    message: data.message,
                    text: prev[data.member_id]?.text || '',
                    quotes: prev[data.member_id]?.quotes || []
                  }
                }));
              }
            } else if (data.event === 'quotes') {
              setCurrentSession(prev => ({
                ...prev,
                [data.member_id]: { 
                  ...prev[data.member_id], 
                  quotes: data.quotes 
                }
              }));
            } else if (data.event === 'token') {
              setCurrentSession(prev => ({
                ...prev,
                [data.member_id]: { 
                  ...prev[data.member_id], 
                  text: (prev[data.member_id]?.text || '') + data.text 
                }
              }));
            } else if (data.event === 'turn_end') {
              setCurrentSession(prev => ({
                ...prev,
                [data.member_id]: { 
                  ...prev[data.member_id], 
                  status: 'done' 
                }
              }));
            } else if (data.event === 'error') {
              setCurrentSession(prev => ({
                ...prev,
                [data.member_id]: { 
                  ...prev[data.member_id], 
                  status: 'done',
                  text: (prev[data.member_id]?.text || '') + `\n\n*(Error: ${data.message || '推理引擎执行失败'})*`
                }
              }));
            } else if (data.event === 'secretary_token') {
              setSecretaryResolution(prev => prev + data.text);
            } else if (data.event === 'board_end') {
              setIsProcessing(false);
              setSecretaryStatus('done');
              setHistory(prev => [...prev, {
                 query: query,
                 session: currentSession,
                 resolution: secretaryResolution
              }]);
            }
          } catch (err) {
            console.error("Parse error", err, dataStr);
          }
        }
      }
    } catch (error: any) {
      console.error("API Error:", error);
      setIsProcessing(false);
      
      // Immediately display connection error inside the first board member box so the user gets clear visual feedback
      const firstMemberId = activeMemberIds[0] || 'munger';
      setCurrentSession({
        [firstMemberId]: {
          status: 'done',
          text: `### ⚠️ API Connection Error\n\nFailed to connect to the backend server. Please make sure the Python server is running.\n\n*Error details: ${error.message || error}*`,
          quotes: []
        }
      });
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  // Determine active speaker for Focus Stage
  let activeMember = BOARD_MEMBERS.find(m => {
    const s = currentSession[m.id];
    return s && (s.status === 'retrieving' || s.status === 'speaking');
  });

  const isSecretaryActive = secretaryStatus === 'synthesizing' || secretaryStatus === 'done';

  return (
    <div className="flex flex-col h-screen w-full bg-slate-50 overflow-hidden relative font-sans selection:bg-indigo-100">
      
      {/* Abstract Ambient Background */}
      <div className="absolute top-0 left-0 w-full h-full pointer-events-none overflow-hidden z-0">
        <div className="absolute -top-[20%] -left-[10%] w-[50%] h-[50%] bg-indigo-200/40 rounded-full blur-[120px]" />
        <div className="absolute top-[40%] -right-[10%] w-[40%] h-[60%] bg-amber-100/40 rounded-full blur-[100px]" />
      </div>

      {/* TOP LEFT: History Drawer Button */}
      <div className="absolute top-8 left-8 z-50">
        <button 
          onClick={() => setIsDrawerOpen(true)}
          className="flex items-center gap-2 bg-white/80 hover:bg-white text-slate-700 px-5 py-3 rounded-full border border-slate-200 backdrop-blur-md shadow-sm transition-all"
        >
          <Clock size={18} />
          <span className="text-sm font-bold tracking-widest uppercase text-slate-500">Records</span>
        </button>
      </div>

      {/* History Drawer */}
      <AnimatePresence>
        {isDrawerOpen && (
          <>
            <motion.div 
              initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
              onClick={() => setIsDrawerOpen(false)}
              className="absolute inset-0 bg-slate-900/10 z-40 backdrop-blur-sm"
            />
            <motion.div 
              initial={{ x: '-100%' }} animate={{ x: 0 }} exit={{ x: '-100%' }}
              transition={{ type: 'spring', damping: 25, stiffness: 200 }}
              className="absolute top-0 left-0 h-full w-[450px] bg-white/95 backdrop-blur-3xl border-r border-slate-200 z-50 flex flex-col shadow-2xl"
            >
              <div className="p-8 border-b border-slate-100 flex justify-between items-center">
                <h2 className="text-slate-800 font-bold text-lg tracking-wide flex items-center gap-2"><Clock size={20} className="text-slate-400" /> Board Records</h2>
                <button onClick={() => setIsDrawerOpen(false)} className="text-slate-400 hover:text-slate-800 transition-colors"><X size={24}/></button>
              </div>
              <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-6">
                {fileHistory.length === 0 ? (
                   <div className="text-slate-400 text-sm text-center mt-20 font-medium">No records yet.</div>
                ) : fileHistory.map((item, i) => {
                  const title = item.filename.replace('.md', '').substring(16) || "Session";
                  return (
                    <div key={i} onClick={() => loadHistoryFile(item.filename)} className="bg-slate-50 p-6 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow cursor-pointer">
                      <div className="text-xs text-indigo-500 font-black tracking-widest uppercase mb-3">{new Date(item.timestamp * 1000).toLocaleString()}</div>
                      <p className="text-slate-800 text-base font-medium line-clamp-2">{title}</p>
                    </div>
                  );
                })}
              </div>
            </motion.div>
          </>
        )}
      </AnimatePresence>

      {/* HEADER: The Council Ring */}
      <header className="w-full flex justify-center items-center py-10 z-10">
        <div className="flex items-center gap-12 bg-white/50 backdrop-blur-xl px-12 py-6 rounded-[3rem] border border-slate-200/60 shadow-sm">
          {BOARD_MEMBERS.map(member => {
            const state = currentSession[member.id];
            const isActive = state?.status === 'retrieving' || state?.status === 'speaking';
            const isDone = state?.status === 'done';
            
            return (
              <div 
                key={member.id} 
                className={`flex flex-col items-center transition-all duration-500 ${isActive ? 'scale-110' : (isDone ? 'scale-95 opacity-60 grayscale' : 'scale-100')}`}
              >
                <div className="relative">
                  <div className={`w-20 h-20 rounded-full overflow-hidden border-4 transition-all duration-500 bg-white shadow-md ${isActive ? `border-transparent ring-4 ring-offset-2 ${member.ring}` : 'border-white'}`}>
                    <img src={member.photo} alt={member.name} className="w-full h-full object-cover" />
                  </div>
                  {isDone && (
                    <div className="absolute -bottom-1 -right-1 bg-white rounded-full text-emerald-500 border border-slate-200 shadow-sm">
                      <CheckCircle2 size={24} />
                    </div>
                  )}
                </div>
                <div className={`mt-4 text-sm font-bold tracking-wide ${isActive ? 'text-slate-800 font-extrabold' : 'text-slate-500'}`}>{member.name}</div>
                <div className="text-[10px] uppercase tracking-widest text-slate-400 font-bold">{member.title}</div>
                {isActive && (
                  <div className={`mt-2 text-[10px] uppercase tracking-widest font-black animate-pulse ${member.color}`}>
                    {state.status === 'retrieving' ? 'Retrieving Memory...' : 'Speaking...'}
                  </div>
                )}
              </div>
            );
          })}


        </div>
      </header>

      {/* MIDDLE: Focus Stage */}
      <main className="flex-1 overflow-hidden relative z-10 w-full flex flex-col items-center">
        
        <div ref={scrollRef} className="flex-1 w-full max-w-5xl overflow-y-auto px-8 pt-8 pb-12 scrollbar-hide flex flex-col gap-12">
          
          {viewingHistory ? (
            <div className="w-full max-w-4xl mx-auto bg-white border border-slate-200/80 shadow-[0_30px_100px_rgba(0,0,0,0.06)] rounded-[2.5rem] p-16 relative overflow-hidden mt-8 mb-12">
               <button onClick={() => setViewingHistory(null)} className="absolute top-8 right-8 text-slate-400 hover:text-slate-800 p-2 bg-slate-50 rounded-full transition-colors z-50">
                  <X size={20} />
               </button>
               <div className="text-lg font-serif text-slate-700 leading-loose tracking-wide">
                  <ReactMarkdown remarkPlugins={[remarkGfm]} components={MarkdownComponents}>
                    {viewingHistory}
                  </ReactMarkdown>
               </div>
            </div>
          ) : !currentQuery ? (
            /* Welcome Screen (Only show this when no active query is present) */
            <div className="flex-1 flex flex-col items-center justify-center text-center max-w-2xl px-6 opacity-60 mx-auto mt-32">
              <Sparkles size={48} className="text-slate-300 mb-6 mx-auto" />
              <h1 className="text-3xl font-serif text-slate-800 mb-4">Strategic Council</h1>
              <p className="text-slate-500 text-lg leading-relaxed">Present your case. The board members will sequentially analyze your strategy through their unique mental models.</p>
            </div>
          ) : (
            <>
              {/* Current Query Display (In Document Flow) */}
              <div className="w-full text-center px-6 pb-8 border-b border-slate-200/50 mb-4">
                 <div className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-3">Topic Under Review</div>
                 <h2 className="text-2xl font-serif text-slate-800 font-medium tracking-wide">"{currentQuery}"</h2>
              </div>

              <div className="w-full max-w-4xl mx-auto flex flex-col gap-16">
                
                {/* Sequential Director Speeches */}
                {BOARD_MEMBERS.map(member => {
                  const state = currentSession[member.id];
                  const hasStarted = !!state;
                  const isActive = state?.status === 'retrieving' || state?.status === 'speaking';
                  
                  return (
                    <motion.div 
                      key={member.id}
                      initial={{ opacity: 0, y: 30 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                      className={`w-full bg-white/70 backdrop-blur-md border border-slate-200/80 rounded-[2rem] p-10 shadow-sm transition-all duration-500 ${isActive ? 'ring-2 ring-offset-2 ring-indigo-100 shadow-md bg-white' : ''}`}
                    >
                      {/* Speaker Header */}
                      <div className="flex items-center justify-between mb-6 pb-4 border-b border-slate-100">
                        <div className="flex items-center gap-4">
                          <div className="w-12 h-12 rounded-full overflow-hidden border-2 border-white shadow-sm">
                            <img src={member.photo} alt={member.name} className="w-full h-full object-cover" />
                          </div>
                          <div>
                            <h3 className="text-lg font-serif font-bold text-slate-800">{member.name}</h3>
                            <div className="text-[10px] uppercase tracking-widest text-slate-400 font-bold">{member.title}</div>
                          </div>
                        </div>
                        
                        {/* Status Badge */}
                        {isActive && (
                          <span className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest animate-pulse ${member.color} bg-slate-50 border border-current`}>
                            <Loader2 size={10} className="animate-spin" />
                            {state.status === 'retrieving' ? 'Retrieving Memory...' : 'Speaking...'}
                          </span>
                        )}
                        
                        {state?.status === 'done' && (
                          <span className="flex items-center gap-1 px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest text-emerald-600 bg-emerald-50 border border-emerald-200">
                            <CheckCircle2 size={10} /> Done
                          </span>
                        )}
                        
                        {!hasStarted && (
                          <span className="px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest text-slate-400 bg-slate-50 border border-slate-200">
                            Queue
                          </span>
                        )}
                      </div>

                      {/* Speech Text Content */}
                      <div className="text-lg font-serif text-slate-700 leading-loose tracking-wide break-words">
                        {!hasStarted ? (
                          <div className="text-slate-400 italic text-sm flex items-center gap-2 py-4">
                            <span className="w-1.5 h-1.5 rounded-full bg-slate-300 animate-ping" />
                            Waiting to speak...
                          </div>
                        ) : state.status === 'retrieving' && !state.text ? (
                          <div className="text-slate-400 italic text-sm flex items-center gap-2 py-4">
                            <Loader2 size={14} className="animate-spin text-slate-300" />
                            {state.message || 'Retrieving Spearman Speeches & Checklists Grounding...'}
                          </div>
                        ) : (
                          <div>
                            <ReactMarkdown remarkPlugins={[remarkGfm]} components={MarkdownComponents}>
                              {state.text || ''}
                            </ReactMarkdown>
                            
                            {state.status === 'speaking' && !state.text && (
                              <div className="text-slate-400 italic text-sm flex items-center gap-2 py-4 animate-pulse">
                                <Loader2 size={14} className="animate-spin text-slate-300" />
                                Speaking...
                              </div>
                            )}
                          </div>
                        )}
                      </div>

                      {/* Grounding Quotes Inline Search Style Capsules */}
                      {hasStarted && state.quotes && state.quotes.length > 0 && (
                        <div className="mt-8 pt-6 border-t border-slate-100 flex flex-wrap items-center gap-3">
                          <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest mr-2 flex items-center gap-1">
                            <BookOpen size={12} /> Speeches Grounding:
                          </span>
                          {state.quotes.map((q, idx) => (
                            <div 
                              key={idx}
                              className="group relative cursor-help"
                            >
                              <div className="bg-slate-50 hover:bg-indigo-50 hover:text-indigo-600 border border-slate-200/80 hover:border-indigo-200 text-slate-500 px-3 py-1 rounded-full text-xs font-semibold flex items-center gap-1.5 transition-all shadow-sm">
                                <span className="w-1.5 h-1.5 rounded-full bg-slate-300 group-hover:bg-indigo-400" />
                                {q.source}
                              </div>
                              
                              {/* ABSOLUTE POSITIONED HIGH-END HOVER CARD TOOLTIP */}
                              <div className="absolute bottom-full left-0 mb-3 w-[360px] p-5 bg-slate-900/95 backdrop-blur-xl text-slate-200 text-xs rounded-[1.25rem] shadow-[0_20px_50px_rgba(0,0,0,0.3)] border border-slate-800 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 pointer-events-none scale-95 origin-bottom-left group-hover:scale-100 flex flex-col gap-2">
                                <div className="flex items-center gap-1.5 text-indigo-400 font-bold uppercase tracking-wider text-[10px]">
                                  <BookOpen size={10} /> Speeches Citation
                                </div>
                                <div className="font-serif font-semibold text-white border-b border-slate-800 pb-2 mb-1 truncate text-xs" title={q.source}>
                                  {q.source}
                                </div>
                                <p className="leading-relaxed font-serif italic text-slate-300 max-h-48 overflow-y-auto pr-1">
                                  "{q.content}"
                                </p>
                              </div>
                            </div>
                          ))}
                        </div>
                      )}
                    </motion.div>
                  );
                })}

                {/* Final Secretary Resolution */}
                {secretaryStatus !== 'idle' && (
                  <motion.div 
                    initial={{ opacity: 0, y: 50, scale: 0.95 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    transition={{ duration: 0.8, ease: "easeOut" }}
                    className="w-full bg-white border border-slate-200/80 shadow-[0_30px_100px_rgba(0,0,0,0.06)] rounded-[2.5rem] p-16 relative overflow-hidden"
                  >
                    {/* Decorative Elements */}
                    <div className="absolute top-0 right-0 w-64 h-64 bg-indigo-50 rounded-bl-full -z-10" />
                    <div className="absolute bottom-0 left-0 w-64 h-64 bg-amber-50 rounded-tr-full -z-10" />
                    
                    <div className="flex items-center gap-4 mb-12 border-b border-slate-100 pb-8">
                      <div className="w-12 h-12 bg-slate-900 rounded-2xl flex items-center justify-center text-white shadow-lg">
                        <Sparkles size={24} />
                      </div>
                      <div>
                        <h2 className="text-2xl font-black text-slate-800 tracking-tight">Executive Resolution</h2>
                        <div className="text-sm font-bold text-slate-400 uppercase tracking-widest mt-1">Chief Secretary's Report</div>
                      </div>
                    </div>

                    <div className="text-lg font-serif text-slate-700 leading-loose tracking-wide">
                      {secretaryResolution ? (
                        <ReactMarkdown remarkPlugins={[remarkGfm]} components={MarkdownComponents}>
                          {secretaryResolution}
                        </ReactMarkdown>
                      ) : (
                        <span className="flex items-center gap-2 text-indigo-500 animate-pulse font-sans text-sm uppercase tracking-widest font-bold">
                          <Loader2 size={16} className="animate-spin" /> Synthesizing Board Consensus...
                        </span>
                      )}
                    </div>
                  </motion.div>
                )}
              </div>
            </>
          )}
        </div>
      </main>

      {/* BOTTOM INPUT DOCK (In Document Flow) */}
      <div className="w-full max-w-4xl mx-auto px-6 pb-8 pt-4 z-30">
        <div className="bg-white/80 backdrop-blur-2xl border border-white rounded-[2rem] flex items-end shadow-[0_15px_50px_rgba(0,0,0,0.05)] p-3 relative transition-all">
          
          <textarea 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={isProcessing}
            placeholder={isProcessing ? "Board is occupied..." : "Present your strategy to the board..."}
            className="w-full bg-transparent text-slate-800 placeholder-slate-400 px-6 py-4 outline-none resize-none min-h-[60px] max-h-40 text-lg font-serif disabled:opacity-50"
            rows={1}
          />
          <button 
            onClick={handleSubmit}
            disabled={!input.trim() || isProcessing}
            className="h-14 w-14 flex-shrink-0 bg-slate-900 text-white rounded-2xl flex items-center justify-center hover:bg-black transition-all shadow-[0_8px_20px_rgba(0,0,0,0.15)] m-1 disabled:opacity-50 disabled:shadow-none"
          >
            {isProcessing ? <Loader2 size={20} className="animate-spin" /> : <Send size={20} />}
          </button>
        </div>
      </div>
      
    </div>
  );
}
