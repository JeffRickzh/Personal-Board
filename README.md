# 🏛️ Personal Board of Directors (个人董事会)

> **“平庸的系统提供现成的答案，伟大的系统促使你提出正确的问题。”**
>
> 这是一个开源的 **AI 个人董事会智能决策沙盘**。它摒弃了市面上单调平庸的“单窗口线性对话”套壳，而是基于**多智能体对抗辩论（Multi-Agent Debate）**与**本地高精度晶格检索（Lattice RAG）**，构建起一个充满碰撞、辩证求真、且能够量化个人认知偏差的桌面决策终端。

---

## 🌟 核心技术亮点与特色功能

### 1. 多维晶格本地检索 (Worldly Wisdom Lattice RAG)
* **零依赖双语分词索引**：内置纯 Python 实现的字符级双语 Tokenizer（中文 Character Unigram/Bigram + 英文 Word-level），无需部署重型的外部数据库或大型向量服务。
* **引经据典，有据可查**：系统自动将董事的传记著作、致股东信、公开演讲（如《穷查理宝典》等）本地深度分片并建立 TF-IDF 倒排索引。每次决策咨询时，实时调取最相关的真实历史言论，前端直接渲染“历史论据版块”，确保董事的发言“灵魂附身”、字字有据。

### 2. 协作辩论与正式陈词 (Pro-Debate Pro Mode)
* **立场草拟（Round 1）**：开启 Pro 模式后，系统会让各位董事先在私下起草一份 150 字以内的独立核心立场，互相不干扰。
* **交叉交锋（Round 2）**：董事在正式发表流式陈词时，会引入其他同僚的手稿，在“思维格栅模型”上直接“点名”进行思想交火（如 *“我不同意保罗的观点，因为...”* 或 *“刚才沃伦提到了安全边际，但...”*），逼出更深刻的一阶与二阶因果效应。
* **决议纪要（Secretary Synthesis）**：最后由首席书记员（Secretary）进行全局复盘，凝练出共识、分歧碰撞点以及一份带安全红线的高质量可执行决议报告。

### 3. 时空纪元防火墙与认知边界过滤器 (Cognitive Epoch Firewalls)
* **防装死/防跳戏**：针对已故导师（如芒格、罗素、毛泽东等），设计了严苛的时空防火墙。如果用户提问 2023 年之后的科技或金融指标，他们会以智慧长者的超然维度进行降维推演，并用特有的老幽默进行自嘲（如 *“虽然我已经在天上打桥牌了，但常识在哪个时代都是一样的...”*）。
* **“太难篮子”机制**：巴菲特绝不预测大盘与短期走势，只关注核心护城河。遇到超出他们能力圈的问题，董事们会以生动的物理学、棒球规则故事，坦然承认这超出了其判定范围。
* **绝对无肢体描写**：强制剥离 AI 常见的 `(缓缓放下手中的可乐)`、`*叹了口气*` 等虚假舞台旁白，保持极其专业严谨的商业决策格调。

### 4. 离线高保真数据集生成与 LoRA 微调管线 (Dataset Curation Pipeline)
* **离线 Q&A 生成**：系统集成了 `dataset_curator.py`，能扫描 raw 语料，模拟顶尖财经记者向导师进行情境式、挑战性的深度提问，并以导师语气生成高质量的 Alpaca 格式 JSONL 问答数据集。
* **LoRA 模型烧制**：提供 `train_lora.py` 脚本，基于 Hugging Face Transformers、PEFT 和 TRL，支持将生成的问答集一键微调到 Qwen 等开源基座模型上，训练属于您自己的本地私有化董事模型。

---

## 📐 系统技术架构设计

以下是 **多智能体圆桌辩论数据流与决策综合引擎** 的核心架构：

```mermaid
graph TD
    A[用户提出商业战略咨询] --> B[零依赖 Tokenizer 分词]
    B --> C[Lattice RAG 倒排检索库]
    C -->|匹配 Top K 真实著作段落| D[动态系统 Prompt 组装]
    
    subgraph Pro 模式：协同草稿阶段
        D --> E1[查理·芒格: 草拟批判性手稿]
        D --> E2[沃伦·巴菲特: 草拟价值护城河手稿]
        D --> E3[保罗·格雷厄姆: 草拟初创黑客手稿]
    end
    
    E1 & E2 & E3 -->|交叉点名/交叉辩论| F[董事会流式正式发言 API/chat_stream]
    F -->|流式Token输出| G[前端动态董事席位渲染]
    F -->|发言上下文合并| H[首席书记员综合处理器 API/synthesize]
    H -->|专业纪要与安全边界| I[输出《最终执行决议报告》]
```

---

## 📁 极简架构目录说明

经过开源重构后，项目的架构显得极其精炼、边界清晰：

```text
Personal-Board/
├── agents/                     # 董事人物设定层
│   ├── buffett/                # 沃伦·巴菲特 (persona.yaml 定义系统 Prompt 与思维模型)
│   ├── munger/                 # 查理·芒格
│   ├── paul_graham/            # 保罗·格雷厄姆
│   ├── russell/                # 伯特兰·罗素
│   └── mao_zedong/             # 东方战略家
├── board of directors/         # 历史文献知识库层 (RAG 检索的 raw txt/md/pdf)
│   ├── CharlieMungerTalk-master/
│   ├── Warren Buffett/
│   └── ...
├── backend/                    # FastAPI 后端服务层
│   ├── main.py                 # API 入口与多智能体流式分发器
│   ├── persona_engine.py       # Lattice RAG 倒排检索引擎 & QA 配套检索
│   ├── pdf_parser.py           # 零依赖纯 Python zlib 解压 PDF 解析器
│   ├── dataset_curator.py      # Alpaca 离线问答语料自动化合成器
│   ├── train_lora.py           # PyTorch / PEFT 微调训练管线
│   ├── requirements.txt        # 后端依赖配置
│   └── .env.example            # 后端环境变量模板
├── frontend/                   # React 顶奢前端界面层
│   ├── src/                    # 界面源码 (App.tsx + Glassmorphism 样式)
│   ├── package.json            # 前端依赖配置
│   └── vite.config.ts          # Vite 打包配置
├── deployment/                 # 生产一键部署与服务器代理配置
│   ├── deploy.sh               # Ubuntu Systemd 一键部署脚本
│   └── nginx.conf.example      # Nginx 双向代理配置
└── README.md                   # 本开源项目介绍
```

---

## 📦 内置资源与文件说明 (Pre-loaded Resources & Files)

**开箱即用，无需额外下载！**

本仓库中已**完整内置并开源**了所有核心文献和图像资源，用户克隆项目后即可立即享受极致的本地 RAG 检索体验：

### 1. 完整开源的文献知识库目录
项目根目录下的 `board of directors/` 文件夹中已完整预装了以下原始文献与语料切片（支持 `.md`、`.txt` 或 `.pdf` 格式）：
* **沃伦·巴菲特** (`board of directors/Warren Buffett/`)：预置历年致股东信、演讲及核心心智模型文档。
* **查理·芒格** (`board of directors/CharlieMungerTalk-master/`)：预置全套公开演讲集、Wesco/Daily Journal 历年年会问答语料。
* **保罗·格雷厄姆** (`board of directors/Paul Graham/`)：预置完整的科技、创业与商业随笔全集。
* **伯特兰·罗素** (`board of directors/russiu/`)：预置经典哲学论文与西方哲学思想精华集。
* **毛泽东** (`board of directors/Mao Zedong/`)：预置战略分析报告与文选。

### 2. 内置高保真微调训练语料集
后端 `backend/` 目录下已预装了核心的 **高保真历史问答微调集** (`backend/*_qa_dataset.jsonl`)。无需再运行语料合成，系统即可直接读取真实的问答历史，执行高精度的 Few-shot 语气拟真与思想碰撞。

### 3. 高清素描彩绘董事头像
前端的顶奢磨砂玻璃席位已内置了 5 位董事的高画质素描彩绘插画头像（存储在 `frontend/src/assets/`）：
* `buffett.png` | `munger.png` | `graham.png` | `russell.png` | `mao_zedong.png`
* 如需追加席位，请遵循根目录 `AVATAR_GUIDELINES.md` 的艺术风格生成并注册头像。

---

## 🔑 API 密钥与通信修改指南 (API Credentials & Settings)

项目的 API 密钥和接口端口完全采用组件解耦设计，非常容易修改。请根据您的使用场景进行如下配置：

### 1. 修改后端大模型 API 密钥 (LLM API Key)
后端的 API 密钥完全统一在本地环境配置文件 `backend/.env` 中进行读取。

* **配置步骤**：
  1. 将 `backend/.env.example` 复制并重命名为 `backend/.env`。
  2. 用文本编辑器打开 `backend/.env`，修改以下参数：
     ```ini
     # 填入您的大模型服务商 API 密钥 (兼容 OpenAI SDK 格式，如小米 MiMo, OpenAI, DeepSeek, 零一万物等)
     MIMO_API_KEY=您的API密钥
     
     # 修改为对应模型提供商的接口 Base URL
     MIMO_BASE_URL=https://token-plan-cn.xiaomimimo.com/v1
     ```
* **更换模型名称**：
  若您希望使用不同的模型（例如 `gpt-4o` 或 `deepseek-chat`），可打开 [backend/main.py](file:///c:/Users/17968/AI%20projects/Personal%20Board/backend/main.py) 修改其中的模型参数（如第 214、245、401 行的 `model="mimo-v2.5"` 或 `model="mimo-v2.5-pro"` 字段）。

### 2. 前后端通信端口修改 (Ports & Base URL)
* **默认本地端口配置**：
  * **后端 FastAPI** 默认运行在 `http://127.0.0.1:8000` (开发模式) 或通过 Uvicorn 绑定到 `8080` (生产部署部署模式)。
  * **前端 React** 默认启动在 `http://localhost:5173`。
* **前端 API 通信基准地址修改**：
  前端的所有数据请求均以 `VITE_API_BASE_URL` 为基准地址，配置在以下位置：
  * **开发环境**：打开 [frontend/src/App.tsx](file:///c:/Users/17968/AI%20projects/Personal%20Board/frontend/src/App.tsx) 第 14 行，如果后端端口有变动（例如改成了 `9000`），直接修改默认 fallback 值即可：
    ```typescript
    const API_BASE = import.meta.env.VITE_API_BASE_URL ?? 'http://127.0.0.1:8000'; // 将 8080 改为您的实际后端地址
    ```
  * **生产部署环境**：打开 [frontend/.env.production](file:///c:/Users/17968/AI%20projects/Personal%20Board/frontend/.env.production)，配置生产服务器对应的 API 接口前缀：
    ```ini
    VITE_API_BASE_URL=http://your-server-ip:8080
    ```

---

## 🚀 极速本地部署与运行

### 1. 启动后端服务 (FastAPI)

1. 进入后端文件夹，创建并激活 Python 虚拟环境：
   ```bash
   cd backend
   python -m venv .venv
   
   # Windows 激活命令:
   .venv\Scripts\activate
   # macOS/Linux 激活命令:
   source .venv/bin/activate
   ```
2. 安装轻量依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 按照上一章的说明配置 `backend/.env` 的 `MIMO_API_KEY`。
4. 启动服务（默认运行在本地 `8000` 端口）：
   ```bash
   python main.py
   ```

### 2. 启动前端服务 (Vite + React)

1. 新开一个终端窗口，进入前端目录：
   ```bash
   cd frontend
   ```
2. 安装视觉交互依赖：
   ```bash
   npm install
   ```
3. 启动本地开发服务：
   ```bash
   npm run dev
   ```
4. 访问终端打印的调试地址（一般为 `http://localhost:5173`）即可开启圆桌会议沙盘！

---

## 🛠️ 高级进阶：语料合称与模型微调

如果您想完全私有化部署自己的董事，不依赖云端 API，您可以利用系统自带的语料处理工具：

* **自动化生产 Q&A 训练语料**：
  ```bash
  python dataset_curator.py --member munger --concurrency 3
  ```
  该命令会扫描 `board of directors` 下查理·芒格的历史发言，并在 `backend` 目录下生成 `munger_qa_dataset.jsonl` 数据集文件。
  
* **开启 LoRA 私有化训练**：
  ```bash
  python train_lora.py --dataset_path ./munger_qa_dataset.jsonl --epochs 3 --batch_size 4
  ```
  该脚本会启动大模型微调流程，将芒格独特的思维模型和文字风格固化至本地模型适配器（Adapters）中。

---

## 🔒 隐私与开源安全准则
* **绝对安全**：所有的 RAG 知识检索、文本切片、分词处理以及聊天历史（`chathistory/`）均在您**本地主机**上安全运行，敏感商业机密绝不会以向量或原始文档形式外流。
* **防泄露保护**：请务必确保您的 `.env` 配置文件被纳入了 `.gitignore`。开源发布时请勿提交 any 带有 API 密钥的临时测试脚本。
