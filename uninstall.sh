#!/bin/bash
# 🦞💥 OpenClaw 完全卸载脚本 - 一键脚本

set -e

echo ""
echo "    💥 ╔═══════════════════════════════════════╗"
echo "      ║     OpenClaw 完全卸载工具             ║"
echo "      ║        温柔地说再见 👋                ║"
echo "      ╚═══════════════════════════════════════╝"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未检测到 Python3"
    echo "卸载脚本需要 Python 3.7+"
    exit 1
fi

echo "✅ Python: $(python3 --version)"

# 尝试 pip 安装
if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
    PIP_CMD=$(command -v pip3 || command -v pip)
    
    echo ""
    echo "📦 尝试安装 openclaw-uninstaller..."
    
    if "$PIP_CMD" install -q openclaw-uninstaller 2>/dev/null; then
        echo "✅ 安装成功！"
        echo ""
        echo "🚀 启动卸载向导..."
        echo ""
        
        # 运行卸载
        if command -v openclaw-uninstall &> /dev/null; then
            openclaw-uninstall
        elif command -v ocu &> /dev/null; then
            ocu
        else
            python3 -m openclaw_uninstaller
        fi
        
        exit 0
    fi
fi

# pip 安装失败，直接下载运行
echo "⚠️ pip 安装失败，直接下载脚本运行..."

TEMP_DIR=$(mktemp -d)
SCRIPT_URL="https://raw.githubusercontent.com/dukaworks/openclaw-uninstaller/main/openclaw_uninstaller/uninstaller.py"

if command -v curl &> /dev/null; then
    curl -fsSL "$SCRIPT_URL" -o "$TEMP_DIR/uninstaller.py"
elif command -v wget &> /dev/null; then
    wget -q "$SCRIPT_URL" -O "$TEMP_DIR/uninstaller.py"
else
    echo "❌ 需要 curl 或 wget"
    exit 1
fi

echo "✅ 下载完成"
echo ""
echo "🚀 启动卸载向导..."
echo ""

python3 "$TEMP_DIR/uninstaller.py"

# 清理
rm -rf "$TEMP_DIR"
