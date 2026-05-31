import React, { useState, useRef, useEffect } from 'react';
import { Send, Loader2, BookOpen, Clock, X, Sparkles, Activity, CheckCircle2, Trash2, Zap, BrainCircuit, FileSignature, Download, ChevronUp, ChevronDown } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

// Local high-quality generated sketch-watercolor avatars
import mungerPhoto from './assets/munger.png';
import buffettPhoto from './assets/buffett.png';
import grahamPhoto from './assets/graham.png';
import russellPhoto from './assets/russell.png';
import maoZedongPhoto from './assets/mao_zedong.png';

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? 'http://127.0.0.1:8080';
const isLocalEnv = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

const generateUUID = () => {
  if (typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function') {
    return crypto.randomUUID();
  }
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    const r = (Math.random() * 16) | 0;
    const v = c === 'x' ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
};

const BOARD_MEMBERS = [
  { id: 'buffett', name: 'Warren Buffett', title: 'Chairman', photo: buffettPhoto, color: 'text-emerald-600', border: 'border-emerald-400', ring: 'ring-emerald-200' },
  { id: 'munger', name: 'Charlie Munger', title: 'Vice Chairman', photo: mungerPhoto, color: 'text-amber-600', border: 'border-amber-400', ring: 'ring-amber-200' },
  { id: 'mao_zedong', name: 'Mao Zedong', title: 'Strategic Mentor', photo: maoZedongPhoto, color: 'text-red-600', border: 'border-red-400', ring: 'ring-red-200' },
  { id: 'paul_graham', name: 'Paul Graham', title: 'Advisor', photo: grahamPhoto, color: 'text-indigo-600', border: 'border-indigo-400', ring: 'ring-indigo-200' },
  { id: 'russell', name: 'Bertrand Russell', title: 'Philosopher', photo: russellPhoto, color: 'text-slate-600', border: 'border-slate-400', ring: 'ring-slate-200' },
];

interface ChatMessage {
  role: 'user' | 'assistant' | 'secretary';
  content: string;
  member_id?: string;
  member_name?: string;
  quotes?: any[];
}

interface HistoryItem {
  filename: string;
  title: string;
  timestamp: number;
  session_id: string;
}

const MarkdownComponents: any = {
  h1: ({node, ...props}: any) => <h1 className="text-2xl font-bold mt-6 mb-4" {...props} />,
  h2: ({node, ...props}: any) => <h2 className="text-xl font-bold mt-5 mb-3 text-slate-800" {...props} />,
  h3: ({node, ...props}: any) => <h3 className="text-lg font-bold mt-4 mb-2 text-slate-800" {...props} />,
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
  
  const [historyList, setHistoryList] = useState<HistoryItem[]>([]);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [sessionId, setSessionId] = useState<string>('');
  const [mode, setMode] = useState<'fast' | 'pro'>('fast');
  const [participatingMembers, setParticipatingMembers] = useState<string[]>(BOARD_MEMBERS.map(m => m.id));
  
  const [isSynthesizing, setIsSynthesizing] = useState(false);
  const [currentStatus, setCurrentStatus] = useState<{member_id: string, state: string, message: string} | null>(null);
  const [systemMsg, setSystemMsg] = useState<string>('');
  const [isHeaderCollapsed, setIsHeaderCollapsed] = useState(true);

  const scrollRef = useRef<HTMLDivElement>(null);
  const shouldAutoScrollRef = useRef<boolean>(true);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [input]);

  const handleScroll = () => {
    if (scrollRef.current) {
      const { scrollTop, scrollHeight, clientHeight } = scrollRef.current;
      // If the user has scrolled up by more than 80px from the absolute bottom,
      // we disable auto-scrolling to prioritize the user's manual scrolling.
      const isNearBottom = scrollHeight - scrollTop - clientHeight < 80;
      shouldAutoScrollRef.current = isNearBottom;
    }
  };

  // Auto-scroll the main stage
  useEffect(() => {
    if (shouldAutoScrollRef.current && scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, currentStatus, systemMsg]);

  useEffect(() => {
    if (isDrawerOpen) {
      fetchHistoryList();
    }
  }, [isDrawerOpen]);

  const fetchHistoryList = async () => {
    try {
      if (isLocalEnv) {
        const res = await fetch(`${API_BASE}/api/history`);
        const data = await res.json();
        setHistoryList(data);
      } else {
        const historyStr = localStorage.getItem('board_history_list');
        if (historyStr) {
          setHistoryList(JSON.parse(historyStr));
        } else {
          setHistoryList([]);
        }
      }
    } catch (err) {
      console.error("Failed to fetch history list:", err);
    }
  };

  const loadHistoryFile = async (filename: string) => {
    try {
      let data: any = null;
      if (isLocalEnv) {
        const res = await fetch(`${API_BASE}/api/history/${encodeURIComponent(filename)}`);
        if (!res.ok) throw new Error(`Server returned status ${res.status}`);
        data = await res.json();
        if (data.error) throw new Error(data.error);
      } else {
        const dataStr = localStorage.getItem(`board_session_${filename}`);
        if (dataStr) {
          data = JSON.parse(dataStr);
        } else {
          throw new Error("Session not found in local storage.");
        }
      }

      if (data && data.messages) {
        shouldAutoScrollRef.current = true;
        setMessages(data.messages);
        setSessionId(data.session_id);
        setIsDrawerOpen(false);
      } else {
        throw new Error("No messages found in this record.");
      }
    } catch (err: any) {
      console.error(err);
      alert("Failed to load history record: " + err.message);
    }
  };

  const deleteHistoryFile = async (e: React.MouseEvent, filename: string) => {
    e.stopPropagation();
    try {
      if (isLocalEnv) {
        await fetch(`${API_BASE}/api/history/${filename}`, { method: 'DELETE' });
      } else {
        const historyStr = localStorage.getItem('board_history_list');
        if (historyStr) {
          let list = JSON.parse(historyStr);
          list = list.filter((item: HistoryItem) => item.filename !== filename);
          localStorage.setItem('board_history_list', JSON.stringify(list));
        }
        localStorage.removeItem(`board_session_${filename}`);
      }
      fetchHistoryList();
    } catch (err) {
      console.error(err);
    }
  };

  const saveSessionToLocal = (sid: string, msgs: ChatMessage[]) => {
    if (!msgs || msgs.length === 0 || isLocalEnv) return; // Do not save to local storage if in local env
    try {
      const firstUserMsg = msgs.find(m => m.role === 'user')?.content || '战略会议';
      const title = firstUserMsg.replace(/[\n\r\t]/g, ' ').trim().substring(0, 25);
      
      const sessionData = {
        session_id: sid,
        title: title,
        timestamp: Math.floor(Date.now() / 1000),
        messages: msgs
      };
      
      localStorage.setItem(`board_session_${sid}`, JSON.stringify(sessionData));
      
      const historyStr = localStorage.getItem('board_history_list');
      let list: HistoryItem[] = historyStr ? JSON.parse(historyStr) : [];
      
      const existingIdx = list.findIndex(item => item.filename === sid);
      if (existingIdx >= 0) {
        list[existingIdx].timestamp = sessionData.timestamp;
        list[existingIdx].title = title;
      } else {
        list.push({ filename: sid, title: title, timestamp: sessionData.timestamp, session_id: sid });
      }
      
      list.sort((a, b) => b.timestamp - a.timestamp);
      localStorage.setItem('board_history_list', JSON.stringify(list));
    } catch (err) {
      console.error("Failed to save session locally:", err);
    }
  };

  useEffect(() => {
    if (!isProcessing && !isSynthesizing && messages.length > 0 && sessionId) {
      saveSessionToLocal(sessionId, messages);
    }
  }, [isProcessing, isSynthesizing, messages, sessionId]);

  const toggleParticipation = (id: string) => {
    if (isProcessing) return;
    setParticipatingMembers(prev => 
      prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id]
    );
  };

  const handleSubmit = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!input.trim() || isProcessing) return;

    const query = input.trim();
    setInput('');
    setIsProcessing(true);
    setSystemMsg('');
    setCurrentStatus(null);
    shouldAutoScrollRef.current = true;
    
    // Create new session ID if it's the very first message
    const currentSessionId = sessionId || generateUUID();
    if (!sessionId) setSessionId(currentSessionId);

    const newMessages: ChatMessage[] = [...messages, { role: 'user', content: query }];
    setMessages(newMessages);

    try {
      const response = await fetch(`${API_BASE}/api/chat_stream`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          messages: newMessages, 
          board_member_ids: participatingMembers,
          mode: mode,
          session_id: currentSessionId
        })
      });

      if (!response.body) throw new Error('No readable stream');
      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');

      let buffer = '';
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        
        buffer += decoder.decode(value, { stream: true });
        const parts = buffer.split('\n\n');
        buffer = parts.pop() || '';
        
        for (const message of parts) {
          if (!message.trim()) continue;
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
            
            if (data.event === 'system') {
              setSystemMsg(data.message);
            } else if (data.event === 'status') {
              setCurrentStatus({member_id: data.member_id, state: data.state, message: data.message});
            } else if (data.event === 'quotes') {
               setMessages(prev => [...prev, { 
                 role: 'assistant', 
                 member_id: data.member_id, 
                 content: '', 
                 quotes: data.quotes 
               }]);
            } else if (data.event === 'token') {
               setMessages(prev => {
                 const lastMsg = prev[prev.length - 1];
                 if (lastMsg && lastMsg.role === 'assistant' && lastMsg.member_id === data.member_id) {
                    return [...prev.slice(0, -1), { ...lastMsg, content: lastMsg.content + data.text }];
                 }
                 return prev;
               });
            } else if (data.event === 'turn_end') {
               setCurrentStatus(null);
            } else if (data.event === 'error') {
               setMessages(prev => {
                 const lastMsg = prev[prev.length - 1];
                 if (lastMsg && lastMsg.role === 'assistant' && lastMsg.member_id === data.member_id) {
                    return [...prev.slice(0, -1), { ...lastMsg, content: lastMsg.content + `\n\n*(Error: ${data.message})*` }];
                 }
                 return prev;
               });
            } else if (data.event === 'board_end') {
               setIsProcessing(false);
               setSystemMsg('');
               if (data.session_id) setSessionId(data.session_id);
            }
          } catch (err) {
            console.error("Parse error", err, dataStr);
          }
        }
      }
    } catch (error: any) {
      console.error("API Error:", error);
      setIsProcessing(false);
      setMessages(prev => [...prev, { role: 'assistant', member_id: 'system', content: `⚠️ API Connection Error: ${error.message}` }]);
    }
  };

  const handleSynthesize = async () => {
    if (isProcessing || messages.length === 0) return;
    setIsProcessing(true);
    setIsSynthesizing(true);
    setSystemMsg('Chief Secretary is drafting the Executive Resolution...');

    try {
      const response = await fetch(`${API_BASE}/api/synthesize`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          messages: messages, 
          session_id: sessionId
        })
      });

      if (!response.body) throw new Error('No readable stream');
      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');

      let buffer = '';
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        
        buffer += decoder.decode(value, { stream: true });
        const parts = buffer.split('\n\n');
        buffer = parts.pop() || '';
        
        for (const message of parts) {
          if (!message.trim()) continue;
          let dataStr = '';
          message.split('\n').forEach(line => {
            if (line.startsWith('data: ')) dataStr += line.slice(6);
          });
          if (!dataStr) continue;
          
          try {
            const data = JSON.parse(dataStr);
            if (data.event === 'status') {
               setMessages(prev => [...prev, { role: 'secretary', content: '' }]);
            } else if (data.event === 'secretary_token') {
               setMessages(prev => {
                 const lastMsg = prev[prev.length - 1];
                 return [...prev.slice(0, -1), { ...lastMsg, content: lastMsg.content + data.text }];
               });
            } else if (data.event === 'synthesis_end') {
               setIsProcessing(false);
               setIsSynthesizing(false);
               setSystemMsg('');
            } else if (data.event === 'error') {
               setMessages(prev => {
                 const lastMsg = prev[prev.length - 1];
                 return [...prev.slice(0, -1), { ...lastMsg, content: lastMsg.content + `\n\n*(Error: ${data.message})*` }];
               });
            }
          } catch (err) {
            console.error("Parse error", err, dataStr);
          }
        }
      }
    } catch (error: any) {
      console.error("Synthesis Error:", error);
      setIsProcessing(false);
      setIsSynthesizing(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  const handleExportMarkdown = () => {
    if (messages.length === 0) return;

    // Get the first user query as the title or a fallback
    const firstUserMsg = messages.find(m => m.role === 'user')?.content || '战略决议';
    const cleanTitle = firstUserMsg.replace(/[\n\r\t]/g, ' ').trim().slice(0, 30);
    const dateStr = new Date().toLocaleString('zh-CN', { hour12: false });
    
    // Calculate active members
    const activeMembers = participatingMembers
      .map(id => BOARD_MEMBERS.find(m => m.id === id))
      .filter(Boolean)
      .map(m => `${m?.name} (${m?.title})`)
      .join(', ');

    let md = '';
    
    // 1. Grand Header with beautiful typography style
    md += `# 🏛️ 个人董事会决议与会议纪要\n`;
    md += `## *Executive Resolution & Council Transcript*\n\n`;
    
    md += `> **备忘录声明**: 本文件为个人董事会 (Personal Board of Directors) 决策会议的正式纪要。以下记录由人工智能引擎驱动，结合了商业巨擘与哲学先贤的多学科格栅模型及真实言论数据进行推演，供战略决策参考。\n\n`;
    
    // 2. Metadata Table
    md += `### 📊 会议基础信息 / Session Information\n\n`;
    md += `| 会议属性 (Field) | 会议数据 (Value) |\n`;
    md += `| :--- | :--- |\n`;
    md += `| **会议议题 / Title** | ${firstUserMsg.replace(/[\n\r\t]/g, ' ').trim().slice(0, 50)}${firstUserMsg.length > 50 ? '...' : ''} |\n`;
    md += `| **会议标识 / Session ID** | \`${sessionId || 'N/A'}\` |\n`;
    md += `| **会议模式 / Debate Mode** | ${mode === 'pro' ? '🧠 Pro 模式 (深度辩论)' : '⚡ Fast 模式 (快速顾问)'} |\n`;
    md += `| **参会董事 / Attendees** | ${activeMembers || '无'} |\n`;
    md += `| **导出时间 / Exported At** | ${dateStr} |\n\n`;
    
    md += `---\n\n`;

    // 3. Conversation History
    md += `# 💬 研讨及辩论实录 / Council Debates & Testimony\n\n`;

    messages.forEach((msg) => {
      if (msg.role === 'assistant') {
        const memberInfo = BOARD_MEMBERS.find(m => m.id === msg.member_id);
        const name = memberInfo?.name || '未知董事';
        const title = memberInfo?.title || 'Board Member';
        
        md += `### 💬 董事陈词: ${name} (${title})\n\n`;
        md += `${msg.content}\n\n`;
        md += `---\n\n`;
      } else if (msg.role === 'secretary') {
        md += `# 📝 最终决议草案 / Executive Consensus Resolution\n\n`;
        md += `### 🏢 首席书记员会议纪要 / Chief Board Secretary Report\n\n`;
        md += `> **签发机构**: 个人董事会秘书处 (Office of the Chief Secretary)  \n`;
        md += `> **当前状态**: 会后共识达成 & 终审归档  \n\n`;
        md += `${msg.content}\n\n`;
        md += `---\n\n`;
      }
    });

    // 4. Signatures Table for premium aesthetic
    md += `### ✍️ 董事会决议正式签署栏 / Executive Signatures\n\n`;
    md += `| 席位 / Title | 参会董事 / Director | 决议签署 / Signature | 归档确认 / Status |\n`;
    md += `| :--- | :--- | :--- | :--- |\n`;
    
    participatingMembers.forEach(id => {
      const memberInfo = BOARD_MEMBERS.find(m => m.id === id);
      if (memberInfo) {
        md += `| **${memberInfo.title}** | ${memberInfo.name} | *Approved & Signed via Engine* | 🟢 Verified |\n`;
      }
    });
    md += `| **Chief Board Secretary** | AI Secretary Executive | *Officially Recorded & Logged* | 🟢 Verified |\n\n`;

    md += `---\n`;
    md += `*个人董事会决策支撑系统 © 2026 Personal Board of Directors. 所有论点基于多学科格栅模型推演，保留最终解释权。*\n`;

    // 5. Trigger download in browser
    const blob = new Blob([md], { type: 'text/markdown;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    
    // Clean filename
    const safeFilename = cleanTitle
      .replace(/[\\/:*?"<>|]/g, '_')
      .replace(/\s+/g, '_')
      .slice(0, 30);
    
    link.href = url;
    link.setAttribute('download', `Board_Resolution_${safeFilename || 'Session'}.md`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const hasSecretaryResponse = messages.length > 0 && messages[messages.length - 1].role === 'secretary';

  return (
    <div className="flex flex-col h-screen w-full bg-slate-50 overflow-hidden relative font-sans selection:bg-indigo-100">
      
      {/* Abstract Ambient Background */}
      <div className="absolute top-0 left-0 w-full h-full pointer-events-none overflow-hidden z-0">
        <div className="absolute -top-[20%] -left-[10%] w-[50%] h-[50%] bg-indigo-200/40 rounded-full blur-[120px]" />
        <div className="absolute top-[40%] -right-[10%] w-[40%] h-[60%] bg-amber-100/40 rounded-full blur-[100px]" />
      </div>

      {/* TOP LEFT: History Drawer Button & New Chat */}
      <div className="absolute top-4 left-4 md:top-8 md:left-8 z-50 flex gap-2 md:gap-3">
        <button 
          onClick={() => setIsDrawerOpen(true)}
          className="flex items-center gap-1 md:gap-2 bg-white/80 hover:bg-white text-slate-700 px-3 py-2 md:px-5 md:py-3 rounded-full border border-slate-200 backdrop-blur-md shadow-sm transition-all"
        >
          <Clock size={16} className="md:w-[18px] md:h-[18px]" />
          <span className="text-[10px] md:text-sm font-bold tracking-widest uppercase text-slate-500">Records</span>
        </button>
        {messages.length > 0 && (
          <button 
            onClick={() => { setMessages([]); setSessionId(''); }}
            className="flex items-center justify-center bg-white/80 hover:bg-white text-slate-500 hover:text-indigo-600 px-3 py-2 md:w-12 md:h-12 rounded-full border border-slate-200 backdrop-blur-md shadow-sm transition-all"
            title="New Council Session"
          >
            <Sparkles size={16} className="md:w-[18px] md:h-[18px]" />
            <span className="text-[10px] md:hidden font-bold tracking-widest uppercase text-slate-500 ml-1">New</span>
          </button>
        )}
      </div>

      {/* TOP RIGHT: One-click Download / Export MD */}
      {messages.length > 0 && (
        <div className="absolute top-4 right-4 md:top-8 md:right-8 z-50">
          <button 
            onClick={handleExportMarkdown}
            className="flex items-center gap-1 md:gap-2 bg-slate-900 hover:bg-black text-white px-3 py-2 md:px-5 md:py-3 rounded-full border border-slate-800 shadow-md transition-all active:scale-95 duration-150"
            title="Export Session as Markdown"
          >
            <Download size={16} className="md:w-[18px] md:h-[18px]" />
            <span className="text-[10px] md:text-sm font-bold tracking-widest uppercase">Export MD</span>
          </button>
        </div>
      )}

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
              className="absolute top-0 left-0 h-full w-full md:w-[450px] bg-white/95 backdrop-blur-3xl border-r border-slate-200 z-50 flex flex-col shadow-2xl"
            >
              <div className="p-8 border-b border-slate-100 flex justify-between items-center">
                <h2 className="text-slate-800 font-bold text-lg tracking-wide flex items-center gap-2"><Clock size={20} className="text-slate-400" /> Board Records</h2>
                <button onClick={() => setIsDrawerOpen(false)} className="text-slate-400 hover:text-slate-800 transition-colors"><X size={24}/></button>
              </div>
              <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-6">
                {historyList.length === 0 ? (
                   <div className="text-slate-400 text-sm text-center mt-20 font-medium">No records yet.</div>
                ) : historyList.map((item, i) => {
                  return (
                    <div key={i} onClick={() => loadHistoryFile(item.filename)} className="group relative bg-slate-50 p-6 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow cursor-pointer flex flex-col">
                      <div className="flex justify-between items-start mb-3">
                        <div className="text-xs text-indigo-500 font-black tracking-widest uppercase">{new Date(item.timestamp * 1000).toLocaleString()}</div>
                        <button 
                          onClick={(e) => deleteHistoryFile(e, item.filename)} 
                          className="opacity-0 group-hover:opacity-100 text-slate-400 hover:text-red-500 transition-all"
                          title="Delete Record"
                        >
                          <Trash2 size={16} />
                        </button>
                      </div>
                      <p className="text-slate-800 text-base font-medium line-clamp-2">{item.title}</p>
                    </div>
                  );
                })}
              </div>
            </motion.div>
          </>
        )}
      </AnimatePresence>

      {/* HEADER: The Council Ring */}
      <header className={`w-full flex justify-center items-center z-10 transition-all duration-500 px-2 ${isHeaderCollapsed ? 'py-2 md:py-4' : 'py-4 md:py-10'}`}>
        <div className={`relative flex items-center justify-center bg-white/50 backdrop-blur-xl border border-slate-200/60 shadow-sm transition-all duration-500 ${isHeaderCollapsed ? 'px-4 md:px-8 py-2 md:py-3.5 gap-2 md:gap-6 rounded-[2rem]' : 'px-1 sm:px-4 md:px-12 py-3 md:py-6 gap-0 sm:gap-4 md:gap-12 rounded-[2rem] md:rounded-[3rem]'}`}>
          {BOARD_MEMBERS.map(member => {
            const isParticipating = participatingMembers.includes(member.id);
            const isCurrentSpeaker = currentStatus?.member_id === member.id;
            
            return (
              <div 
                key={member.id} 
                onClick={() => toggleParticipation(member.id)}
                className={`flex flex-col items-center transition-all duration-500 cursor-pointer ${!isParticipating ? 'opacity-40 grayscale' : 'hover:scale-105'} ${isCurrentSpeaker ? 'scale-105 opacity-100 grayscale-0' : ''}`}
                title={isParticipating ? "Click to exclude from next round" : "Click to include in next round"}
              >
                <div className="relative">
                  <div className={`rounded-full overflow-hidden border-2 transition-all duration-500 bg-white shadow-md ${isHeaderCollapsed ? 'w-8 h-8 md:w-10 md:h-10' : 'w-12 h-12 sm:w-14 sm:h-14 md:w-20 md:h-20 border-2 md:border-4'} ${isCurrentSpeaker ? `border-transparent ring-2 md:ring-4 ring-offset-1 md:ring-offset-2 ${member.ring}` : 'border-white'}`}>
                    <img src={member.photo} alt={member.name} className="w-full h-full object-cover" />
                  </div>
                  {isParticipating && (
                    <div className={`absolute -bottom-1 -right-1 bg-white rounded-full text-emerald-500 border border-slate-200 shadow-sm transition-all duration-300 ${isHeaderCollapsed ? 'p-0' : ''}`}>
                      <CheckCircle2 size={isHeaderCollapsed ? 14 : 24} className="fill-emerald-50" />
                    </div>
                  )}
                </div>
                
                {/* Names and speaking indicator are hidden when collapsed */}
                {!isHeaderCollapsed && (
                  <div className="flex flex-col items-center mt-2 md:mt-4 transition-all duration-300 w-14 md:w-auto text-center px-0.5">
                    <div className={`text-[9px] leading-tight md:text-sm font-bold tracking-tight md:tracking-wide break-words whitespace-pre-line ${isCurrentSpeaker ? 'text-slate-800 font-extrabold' : 'text-slate-500'}`}>{member.name.replace(' ', '\n')}</div>
                    <div className="text-[7.5px] leading-none md:text-[10px] uppercase tracking-normal md:tracking-widest text-slate-400 font-bold mt-1 md:mt-0">{member.title}</div>
                    {isCurrentSpeaker && (
                      <div className={`mt-1 md:mt-2 text-[8px] md:text-[10px] uppercase tracking-widest font-black animate-pulse ${member.color}`}>
                        {currentStatus.state === 'retrieving' ? 'Retrieving...' : 'Speaking...'}
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}

          {/* Sleek Collapse/Expand Toggle Tab */}
          <button 
            onClick={() => setIsHeaderCollapsed(!isHeaderCollapsed)}
            className="absolute -bottom-3 left-1/2 -translate-x-1/2 bg-white hover:bg-slate-900 text-slate-400 hover:text-white w-7 h-7 rounded-full border border-slate-200/80 shadow-md flex items-center justify-center transition-all duration-300 hover:scale-110 z-20 cursor-pointer"
            title={isHeaderCollapsed ? "展开面板" : "收起面板"}
          >
            {isHeaderCollapsed ? <ChevronDown size={14} /> : <ChevronUp size={14} />}
          </button>
        </div>
      </header>

      {/* MIDDLE: Focus Stage & Chat History */}
      <main className="flex-1 overflow-hidden relative z-10 w-full flex flex-col items-center">
        
        <div ref={scrollRef} onScroll={handleScroll} className="flex-1 w-full max-w-5xl overflow-y-auto px-4 md:px-8 pb-12 scrollbar-hide flex flex-col gap-6 md:gap-8">
          
          {messages.length === 0 ? (
            /* Welcome Screen */
            <div className="flex-1 flex flex-col items-center justify-center text-center max-w-2xl px-6 opacity-60 mx-auto mt-20">
              <Sparkles size={48} className="text-slate-300 mb-6 mx-auto" />
              <h1 className="text-3xl font-serif text-slate-800 mb-4">Strategic Council</h1>
              <p className="text-slate-500 text-lg leading-relaxed">Present your strategy. The board members will debate and analyze your proposal across multiple rounds.</p>
            </div>
          ) : (
            <div className="w-full max-w-4xl mx-auto flex flex-col gap-10 mt-4">
              
              {messages.map((msg, index) => {
                if (msg.role === 'user') {
                  return (
                    <motion.div 
                      key={index}
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      className="w-full flex justify-end"
                    >
                      <div className="bg-slate-900 text-white p-4 md:p-6 rounded-[1.5rem] md:rounded-[2rem] rounded-tr-sm max-w-[92%] md:max-w-[85%] shadow-md">
                        <div className="text-[10px] md:text-xs text-slate-400 font-bold uppercase tracking-widest mb-1.5 md:mb-2 flex items-center gap-2">
                           You <div className="w-1.5 h-1.5 rounded-full bg-indigo-500" />
                        </div>
                        <div className="text-base md:text-lg font-serif leading-relaxed whitespace-pre-wrap break-words">{msg.content}</div>
                      </div>
                    </motion.div>
                  );
                }

                if (msg.role === 'assistant') {
                  const member = BOARD_MEMBERS.find(m => m.id === msg.member_id);
                  if (!member && msg.member_id !== 'system') return null;
                  
                  return (
                    <motion.div 
                      key={index}
                      initial={{ opacity: 0, y: 30 }}
                      animate={{ opacity: 1, y: 0 }}
                      className={`w-full bg-white/70 backdrop-blur-md border border-slate-200/80 rounded-[1.5rem] md:rounded-[2rem] p-5 md:p-10 shadow-sm transition-all duration-500 ${msg.member_id === currentStatus?.member_id ? 'ring-2 ring-offset-2 ring-indigo-100 shadow-md bg-white' : ''}`}
                    >
                      <div className="flex items-center gap-3 md:gap-4 mb-4 md:mb-6 pb-3 md:pb-4 border-b border-slate-100">
                        {member ? (
                          <>
                            <div className="w-10 h-10 md:w-12 md:h-12 flex-shrink-0 rounded-full overflow-hidden border-2 border-white shadow-sm">
                              <img src={member.photo} alt={member.name} className="w-full h-full object-cover" />
                            </div>
                            <div>
                              <h3 className="text-base md:text-lg font-serif font-bold text-slate-800">{member.name}</h3>
                              <div className="text-[9px] md:text-[10px] uppercase tracking-widest text-slate-400 font-bold">{member.title}</div>
                            </div>
                          </>
                        ) : (
                           <div>
                              <h3 className="text-base md:text-lg font-serif font-bold text-red-600">System Message</h3>
                           </div>
                        )}
                      </div>

                      <div className="text-base md:text-lg font-serif text-slate-700 leading-loose tracking-wide break-words">
                        <ReactMarkdown remarkPlugins={[remarkGfm]} components={MarkdownComponents}>
                          {msg.content || ''}
                        </ReactMarkdown>
                        {msg.member_id === currentStatus?.member_id && !msg.content && (
                          <div className="text-slate-400 italic text-sm flex items-center gap-2 py-2 animate-pulse">
                            <Loader2 size={14} className="animate-spin text-slate-300" />
                            Drafting response...
                          </div>
                        )}
                      </div>

                      {/* Grounding Quotes Inline Search Style Capsules */}
                      {msg.quotes && msg.quotes.length > 0 && (
                        <div className="mt-8 pt-6 border-t border-slate-100 flex flex-wrap items-center gap-3">
                          <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest mr-2 flex items-center gap-1">
                            <BookOpen size={12} /> References:
                          </span>
                          {msg.quotes.map((q, idx) => (
                            <div key={idx} className="group relative cursor-help">
                              <div className="bg-slate-50 hover:bg-indigo-50 hover:text-indigo-600 border border-slate-200/80 hover:border-indigo-200 text-slate-500 px-3 py-1 rounded-full text-xs font-semibold flex items-center gap-1.5 transition-all shadow-sm">
                                <span className="w-1.5 h-1.5 rounded-full bg-slate-300 group-hover:bg-indigo-400" />
                                {q.source}
                              </div>
                              <div className="absolute bottom-full left-0 mb-3 w-[360px] p-5 bg-slate-900/95 backdrop-blur-xl text-slate-200 text-xs rounded-[1.25rem] shadow-[0_20px_50px_rgba(0,0,0,0.3)] border border-slate-800 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 pointer-events-none scale-95 origin-bottom-left group-hover:scale-100 flex flex-col gap-2">
                                <div className="font-serif font-semibold text-white border-b border-slate-800 pb-2 mb-1 truncate text-xs" title={q.source}>{q.source}</div>
                                <p className="leading-relaxed font-serif italic text-slate-300 max-h-48 overflow-y-auto pr-1">"{q.content}"</p>
                              </div>
                            </div>
                          ))}
                        </div>
                      )}
                    </motion.div>
                  );
                }

                if (msg.role === 'secretary') {
                  return (
                    <motion.div 
                      key={index}
                      initial={{ opacity: 0, y: 50, scale: 0.95 }}
                      animate={{ opacity: 1, y: 0, scale: 1 }}
                      className="w-full bg-white border border-slate-200/80 shadow-[0_30px_100px_rgba(0,0,0,0.06)] rounded-[1.5rem] md:rounded-[2.5rem] p-6 md:p-16 relative overflow-hidden"
                    >
                      <div className="absolute top-0 right-0 w-32 h-32 md:w-64 md:h-64 bg-indigo-50 rounded-bl-full -z-10" />
                      <div className="absolute bottom-0 left-0 w-32 h-32 md:w-64 md:h-64 bg-amber-50 rounded-tr-full -z-10" />
                      
                      <div className="flex items-center gap-3 md:gap-4 mb-6 md:mb-12 border-b border-slate-100 pb-4 md:pb-8">
                        <div className="w-10 h-10 md:w-12 md:h-12 flex-shrink-0 bg-slate-900 rounded-xl md:rounded-2xl flex items-center justify-center text-white shadow-lg">
                          <FileSignature size={20} />
                        </div>
                        <div>
                          <h2 className="text-lg md:text-2xl font-black text-slate-800 tracking-tight">Executive Resolution</h2>
                          <div className="text-[10px] md:text-sm font-bold text-slate-400 uppercase tracking-widest mt-1">Chief Secretary's Report</div>
                        </div>
                      </div>

                      <div className="text-base md:text-lg font-serif text-slate-700 leading-loose tracking-wide">
                        <ReactMarkdown remarkPlugins={[remarkGfm]} components={MarkdownComponents}>
                          {msg.content}
                        </ReactMarkdown>
                        {isSynthesizing && !msg.content && (
                           <span className="flex items-center gap-2 text-indigo-500 animate-pulse font-sans text-sm uppercase tracking-widest font-bold">
                             <Loader2 size={16} className="animate-spin" /> Synthesizing Board Consensus...
                           </span>
                        )}
                      </div>
                    </motion.div>
                  );
                }

                return null;
              })}

              {/* System Event Messages Display */}
              {systemMsg && (
                <div className="w-full text-center py-4">
                  <span className="inline-flex items-center gap-2 bg-indigo-50 text-indigo-600 px-4 py-2 rounded-full text-xs font-bold uppercase tracking-widest shadow-sm">
                    <Activity size={14} className="animate-pulse" /> {systemMsg}
                  </span>
                </div>
              )}

              {/* Synthesize Button at the end of the chat flow */}
              {messages.length > 0 && !hasSecretaryResponse && !isProcessing && (
                <div className="w-full flex justify-center py-8">
                  <button 
                    onClick={handleSynthesize}
                    className="group relative flex items-center gap-3 bg-white hover:bg-slate-900 text-slate-800 hover:text-white px-8 py-4 rounded-full border border-slate-200 hover:border-slate-900 shadow-sm hover:shadow-xl transition-all duration-300"
                  >
                    <FileSignature size={20} className="text-indigo-500 group-hover:text-white transition-colors" />
                    <span className="font-bold tracking-wide">Generate Executive Resolution</span>
                  </button>
                </div>
              )}
            </div>
          )}
        </div>
      </main>

      {/* BOTTOM INPUT DOCK */}
      <div className="w-full max-w-4xl mx-auto px-4 md:px-6 pb-4 md:pb-8 z-30 flex flex-col gap-2 md:gap-3">
        
        {/* Fast / Pro Toggle Switch */}
        <div className="flex justify-start px-1 md:px-2">
          <div className="bg-white/80 backdrop-blur-md border border-slate-200 p-1 rounded-full flex items-center gap-1 shadow-sm">
            <button
              onClick={() => setMode('fast')}
              className={`flex items-center gap-1 md:gap-1.5 px-3 py-1.5 md:px-4 md:py-1.5 rounded-full text-[10px] md:text-xs font-bold uppercase tracking-widest transition-all ${mode === 'fast' ? 'bg-slate-900 text-white shadow-md' : 'text-slate-500 hover:bg-slate-100'}`}
            >
              <Zap size={14} /> Fast
            </button>
            <button
              onClick={() => setMode('pro')}
              className={`flex items-center gap-1 md:gap-1.5 px-3 py-1.5 md:px-4 md:py-1.5 rounded-full text-[10px] md:text-xs font-bold uppercase tracking-widest transition-all ${mode === 'pro' ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-500 hover:bg-slate-100'}`}
            >
              <BrainCircuit size={14} /> Pro (Debate)
            </button>
          </div>
        </div>

        <div className="bg-white/90 backdrop-blur-2xl border border-white rounded-[1.5rem] md:rounded-[2rem] flex items-end shadow-[0_15px_50px_rgba(0,0,0,0.05)] p-2 md:p-3 relative transition-all">
          <textarea 
            ref={textareaRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={isProcessing}
            placeholder={isProcessing ? "Board is occupied..." : "Present your strategy..."}
            className="w-full bg-transparent text-slate-800 placeholder-slate-400 px-3 py-3 md:px-6 md:py-4 outline-none resize-none min-h-[50px] md:min-h-[60px] max-h-[150px] md:max-h-[300px] overflow-y-auto text-base md:text-lg font-serif disabled:opacity-50"
            rows={1}
          />
          <button 
            onClick={handleSubmit}
            disabled={!input.trim() || isProcessing || participatingMembers.length === 0}
            className="h-11 w-11 md:h-14 md:w-14 flex-shrink-0 bg-slate-900 text-white rounded-xl md:rounded-2xl flex items-center justify-center hover:bg-black transition-all shadow-[0_8px_20px_rgba(0,0,0,0.15)] m-0.5 md:m-1 disabled:opacity-50 disabled:shadow-none"
          >
            {isProcessing ? <Loader2 size={18} className="animate-spin" /> : <Send size={18} />}
          </button>
        </div>
      </div>
      
    </div>
  );
}
