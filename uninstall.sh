#!/bin/bash
# 🦞💥 OpenClaw Uninstaller - 一键卸载脚本

echo ""
echo "    💥 ╔═══════════════════════════════════════╗"
echo "      ║     OpenClaw 完全卸载工具             ║"
echo "      ║        温柔地说再见 👋                ║"
echo "      ╚═══════════════════════════════════════╝"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未检测到 Python3"
    echo "请手动删除 ~/.openclaw 目录"
    exit 1
fi

# 尝试 pip 安装
if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
    PIP_CMD=$(command -v pip3 || command -v pip)
    echo "📦 正在安装卸载工具..."
    "$PIP_CMD" install -q openclaw-uninstaller 2>/dev/null
    
    if command -v openclaw-uninstall &> /dev/null; then
        echo "✅ 安装成功，启动卸载向导..."
        echo ""
        openclaw-uninstall
        exit 0
    fi
fi

# 备用方案：直接下载运行
echo "📥 直接下载运行..."
TEMP_DIR=$(mktemp -d)
curl -fsSL "https://raw.githubusercontent.com/dukaworks/openclaw-uninstaller/main/openclaw_uninstaller/uninstaller.py" -o "$TEMP_DIR/uninstall.py"

if [ -f "$TEMP_DIR/uninstall.py" ]; then
    python3 "$TEMP_DIR/uninstall.py"
else
    echo "❌ 下载失败，请检查网络"
    exit 1
fi

rm -rf "$TEMP_DIR"
