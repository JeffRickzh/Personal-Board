#!/bin/bash
# 一键部署脚本 (仅适用于 Ubuntu 22.04 / 24.04)
# 请使用 root 权限运行此脚本：sudo bash deploy.sh

set -e

echo "=================================================="
echo "开始部署 Personal Board (个人董事会) 项目..."
echo "=================================================="

# 1. 更新系统并安装依赖
echo ">> 1. 安装基础依赖 (Python, Nginx, Node.js)..."
apt-get update
apt-get install -y python3 python3-pip python3-venv nginx git curl

# 安装 Node.js (20.x)
if ! command -v node &> /dev/null; then
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
    apt-get install -y nodejs
fi

# 2. 设置项目目录
PROJECT_DIR="/var/www/personal-board"
echo ">> 2. 配置项目目录: $PROJECT_DIR"
if [ ! -d "$PROJECT_DIR" ]; then
    # 在这里假设您已经把项目代码传到了服务器，或者是从git拉取
    echo "请手动将项目代码放到 $PROJECT_DIR 目录下！"
    echo "您可以执行: git clone <your-repo-url> $PROJECT_DIR"
    exit 1
fi

cd $PROJECT_DIR

# 3. 后端环境配置
echo ">> 3. 配置后端 (FastAPI)..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 配置 Systemd 守护进程来运行后端
echo ">> 创建后端 Systemd 服务..."
cat <<EOF > /etc/systemd/system/personal-board-backend.service
[Unit]
Description=Personal Board FastAPI Backend
After=network.target

[Service]
User=root
WorkingDirectory=$PROJECT_DIR/backend
Environment="PATH=$PROJECT_DIR/backend/venv/bin"
ExecStart=$PROJECT_DIR/backend/venv/bin/uvicorn main:app --host 127.0.0.1 --port 8080
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable personal-board-backend
systemctl restart personal-board-backend

# 4. 前端打包
echo ">> 4. 编译前端 (React/Vite)..."
cd $PROJECT_DIR/frontend
# 修改 .env.production
echo "VITE_API_BASE_URL=" > .env.production
npm install
npm run build

# 5. 配置 Nginx
echo ">> 5. 配置 Nginx 代理..."
cp $PROJECT_DIR/deployment/nginx.conf.example /etc/nginx/sites-available/personal-board
if [ ! -f /etc/nginx/sites-enabled/personal-board ]; then
    ln -s /etc/nginx/sites-available/personal-board /etc/nginx/sites-enabled/
fi
# 删除默认配置
rm -f /etc/nginx/sites-enabled/default

nginx -t
systemctl restart nginx

echo "=================================================="
echo "部署完成！"
echo "现在您可以直接通过服务器的公网 IP 访问您的个人董事会了！"
echo "=================================================="
