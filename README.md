# 🦞💥 OpenClaw Uninstaller

[![PyPI version](https://img.shields.io/pypi/v/openclaw-uninstaller.svg)](https://pypi.org/project/openclaw-uninstaller/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-卸载工具-pink.svg)](https://openclaw.ai)
[![GitHub stars](https://img.shields.io/github/stars/dukaworks/openclaw-uninstaller.svg?style=social)](https://github.com/dukaworks/openclaw-uninstaller/stargazers)

> **卸载虾出品** 🦞  
> 温柔地说再见，彻底卸载 OpenClaw

<p align="center">
  <img src="https://raw.githubusercontent.com/dukaworks/openclaw-uninstaller/main/assets/goodbye.png" alt="Goodbye" width="400">
</p>

## ✨ 为什么要用卸载虾？

OpenClaw 是个好东西，但有时候你需要：
- 🧹 彻底清理重装
- 💾 迁移到新机器
- 🗑️ 暂时告别（还会回来的对吧？）

卸载虾会帮你：
- ✅ **彻底清理** - 删除所有文件、配置、环境变量
- 💾 **安全备份** - 保留配置，随时恢复
- 🛑 **停止服务** - 自动停止所有运行中的进程
- 🧹 **清理残留** - npm 包、缓存、shell 配置

## 🚀 快速开始

### 方式一：pip 安装（推荐）

```bash
# 安装
pip install openclaw-uninstaller

# 运行
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
pip install -r requirements.txt
python -m openclaw_uninstaller
```

## 🦞 卸载流程（有仪式感地告别）

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   🦞 步骤 1/5  停止服务        🛑 温柔地停止所有进程       │
│   ─────────────────────────────────────────────────────   │
│   💾 步骤 2/5  备份配置        📦 保留你的设置（可选）     │
│   ─────────────────────────────────────────────────────   │
│   📦 步骤 3/5  卸载 npm 包     🗑️  移除全局安装          │
│   ─────────────────────────────────────────────────────   │
│   🗑️  步骤 4/5  删除文件       💥 清理所有目录           │
│   ─────────────────────────────────────────────────────   │
│   🧹 步骤 5/5  清理环境        ✨ 移除环境变量            │
│                                                            │
│                    🎉 再见，OpenClaw！                     │
│                                                            │
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

[█░░░░░░░░░░░░░░] 步骤 1/5
🛑 停止 OpenClaw 服务

✅ 所有 OpenClaw 服务已停止

[██░░░░░░░░░░░░░] 步骤 2/5
💾 备份配置文件

✅ 配置已备份到: ~/.openclaw_backup/openclaw_backup_20250226_143000

    📦 💾 📦
    
    配置文件已安全备份
    随时欢迎回来！
    
    🦞 "记得想我哦~"

...

         🦞
        /  \
       │ 👋 │   ← 挥手告别
        \\  /
         🦞
    
    ✨ 感谢陪伴 ✨
    有缘再会！
    
    OpenClaw 已完全移除
```

## 📋 清理内容清单

| 类型 | 内容 |
|------|------|
| **主目录** | `~/.openclaw` - 所有配置和数据 |
| **全局命令** | `/usr/local/bin/openclaw` 等 |
| **npm 包** | `openclaw`, `clawhub` 全局安装 |
| **缓存** | npx 缓存、npm 缓存 |
| **配置目录** | macOS/Windows 特定配置路径 |
| **环境变量** | `.bashrc`, `.zshrc` 中的 PATH |
| **进程** | 所有运行中的 OpenClaw 进程 |

## 🛠️ CLI 命令

```bash
# 交互式卸载（推荐）
openclaw-uninstall
ocu

# 快速卸载（不备份，直接删）
ocu --force

# 仅备份配置
ocu --backup-only

# 查看会删除什么（预览模式）
ocu --dry-run

# 查看帮助
ocu --help
```

## 🐛 常见问题

### Q: 卸载后想恢复怎么办？

如果选择了备份选项，配置文件会保存在 `~/.openclaw_backup/`。重新安装后，可以手动复制回去。

```bash
# 查看备份
ls ~/.openclaw_backup/

# 恢复配置（重新安装后）
cp -r ~/.openclaw_backup/openclaw_backup_xxx/* ~/.openclaw/
```

### Q: 卸载不彻底？

可能需要 `sudo` 权限删除某些系统路径：

```bash
sudo ocu
```

### Q: 误删了怎么办？

如果备份了，配置可以恢复。如果没有备份... 🦞 卸载虾只能帮你到这里了。

## 🤝 贡献

欢迎提交 Issue 和 PR！

### 新功能想法

- [ ] GUI 界面（Tkinter/Qt）
- [ ] 定时自动卸载（？）
- [ ] 卸载后自动重装最新版
- [ ] 卸载仪式动画（烟花效果）

## 📊 相关项目

- 🦞 [OpenClaw Feishu Deployer](https://github.com/dukaworks/openclaw-feishu-deployer) - 一键部署
- 🏠 [OpenClaw 官网](https://openclaw.ai)
- 📚 [OpenClaw 文档](https://docs.openclaw.ai)

## 📝 更新日志

查看 [CHANGELOG.md](CHANGELOG.md)

## ⚖️ 许可证

[MIT License](LICENSE) © 2025 Duka Works

---

<p align="center">
  <br>
  🦞 <strong>卸载虾说："再见是为了更好的重逢"</strong> 🦞
  <br><br>
  <a href="https://github.com/dukaworks/openclaw-uninstaller">GitHub</a> •
  <a href="https://pypi.org/project/openclaw-uninstaller">PyPI</a> •
  <a href="https://openclaw.ai">OpenClaw</a>
</p>
