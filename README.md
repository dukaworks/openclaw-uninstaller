# 🦞💥 OpenClaw Uninstaller

[![PyPI version](https://img.shields.io/pypi/v/openclaw-uninstaller.svg)](https://pypi.org/project/openclaw-uninstaller/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **卸载虾出品** 🦞💥  
> 一键彻底卸载 OpenClaw - 温柔地说再见

<p align="center">
  <img src="https://raw.githubusercontent.com/dukaworks/openclaw-uninstaller/main/assets/goodbye.gif" alt="Goodbye" width="400">
</p>

## ✨ 特性

| 特性 | 描述 |
|------|------|
| 🦞 **可爱的 CLI** | 彩色界面 + 动画效果，卸载也能很有趣 |
| 💾 **智能备份** | 自动备份配置，随时欢迎回来 |
| 🧹 **彻底清理** | 删除所有文件、服务、环境变量 |
| 🛑 **安全停止** | 自动停止运行中的服务 |
| 🔍 **残留检测** | 扫描所有可能的安装位置 |
| 🛡️ **二次确认** | 防止误操作，安全卸载 |

## 🚀 快速开始

### 方式一：pip 安装（推荐）

```bash
pip install openclaw-uninstaller
openclaw-uninstall
# 或简写
ocu
```

### 方式二：一键脚本

```bash
curl -fsSL https://raw.githubusercontent.com/dukaworks/openclaw-uninstaller/main/uninstall.sh | bash
```

### 方式三：克隆运行

```bash
git clone https://github.com/dukaworks/openclaw-uninstaller.git
cd openclaw-uninstaller
python -m openclaw_uninstaller
```

## 📋 卸载流程

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   🛑 步骤 1/5  停止服务        🔍 查找并停止 OpenClaw      │
│   ─────────────────────────────────────────────────────   │
│   💾 步骤 2/5  备份配置        📦 保存重要配置（可选）      │
│   ─────────────────────────────────────────────────────   │
│   📦 步骤 3/5  卸载 npm 包     🗑️  npm uninstall          │
│   ─────────────────────────────────────────────────────   │
│   🗑️  步骤 4/5  删除文件        🧹  删除所有相关文件      │
│   ─────────────────────────────────────────────────────   │
│   🧹 步骤 5/5  清理环境        🧼  清理 PATH 和别名      │
│                                                            │
│                    ✨ 清理完成！👋 ✨                       │
└────────────────────────────────────────────────────────────┘
```

## 🖥️ 界面预览

```bash
$ openclaw-uninstall

    💥 ╔═══════════════════════════════════════╗
      ║     OpenClaw 完全卸载工具             ║
      ║        温柔地说再见 👋                ║
      ╚═══════════════════════════════════════╝

你好！我是卸载虾 🦞
我会帮你彻底移除 OpenClaw

发现 OpenClaw 安装在以下位置：
  - ~/.openclaw
  - /usr/local/bin/openclaw
  - ~/.npm-global/lib/node_modules/openclaw

⚠️  (╯°□°)╯ 等等！
    
    你真的要删除我吗？
    我还可以帮你做很多事情呢...

卸载选项：
1. 🗑️  完全删除（不保留配置）
2. 💾  备份后删除（推荐）
3. ❌  取消

请选择 (1/2/3): 2

[████░░░░░░░░░░░] 步骤 2/5
💾 备份配置文件

🦐 正在处理... 🦞 加油加载... ✅ 已备份: openclaw.json

📦 💾 📦
    
    配置文件已安全备份
    随时欢迎回来！
    
    🦞 "记得想我哦~"

✅ 清理完成！OpenClaw 已完全移除

         🦞
        /  \
       │ 👋 │   ← 挥手告别
        \  /
         🦞
    
    ✨ 感谢陪伴 ✨
    有缘再会！
```

## 🛠️ CLI 命令

```bash
openclaw-uninstall      # 交互式卸载
openclaw-uninstall -y   # 自动确认（危险！）
openclaw-uninstall --backup-only  # 仅备份
ocu                     # 简写命令
```

## 🔍 会清理什么？

| 位置 | 内容 |
|------|------|
| `~/.openclaw` | 主配置目录 |
| `/usr/local/bin/openclaw*` | 全局命令 |
| `~/.npm-global/` | npm 全局安装 |
| `~/.config/openclaw` | 配置缓存 |
| Shell 配置文件 | PATH、别名 |
| 运行中的进程 | Gateway 服务 |

## 💾 备份内容

选择备份后会保存：
- `openclaw.json` - 主配置
- `credentials/` - 凭证信息
- `identity/` - 身份配置
- `backup_info.json` - 备份元数据

备份位置：`~/.openclaw_backup/openclaw_backup_YYYYMMDD_HHMMSS/`

## 🐛 常见问题

### Q: 卸载后想重新安装？
```bash
# 没问题！随时欢迎回来
curl -fsSL https://openclaw.ai/install.sh | bash
```

### Q: 删除后还有残留？
```bash
# 手动检查这些位置
ls -la ~/.openclaw
ls -la ~/.npm-global/bin/openclaw*
which openclaw
```

### Q: 如何恢复备份？
```bash
# 备份在 ~/.openclaw_backup/
cp -r ~/.openclaw_backup/openclaw_backup_xxx/* ~/.openclaw/
```

## 🤝 贡献

欢迎提交 PR！让卸载也变得可爱 🦞

## 📄 许可证

MIT License © 2025 Duka Works

---

<p align="center">
  🦞💥 <strong>Made with love by 卸载虾</strong> 🦞💥
  <br>
  <a href="https://github.com/dukaworks/openclaw-uninstaller">GitHub</a> •
  <a href="https://pypi.org/project/openclaw-uninstaller">PyPI</a>
</p>
