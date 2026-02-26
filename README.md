# 🦞💥 OpenClaw Uninstaller

[![PyPI version](https://img.shields.io/pypi/v/openclaw-uninstaller.svg)](https://pypi.org/project/openclaw-uninstaller/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **卸载虾出品** 🦞💥  
> 一键彻底卸载 OpenClaw - **先存档，再告别**

<p align="center">
  <img src="https://raw.githubusercontent.com/dukaworks/openclaw-uninstaller/main/assets/goodbye.gif" alt="Goodbye" width="400">
</p>

## ✨ 新特性：联动快照

卸载前自动备份，重装后可完全恢复身份！

```bash
# 卸载时自动提示创建快照
openclaw-uninstall

# 📦 保存为 tar.gz（可导出到其他机器）
# 📁 或保存到快照目录（配合 ocs 恢复）
```

## 🚀 快速开始

### 安装

```bash
pip install openclaw-uninstaller
```

### 运行

```bash
openclaw-uninstall
# 或简写
ocu
```

## 📋 卸载流程（带快照保护）

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   🛑 步骤 1/4  停止服务        🔍 停止 OpenClaw 进程       │
│   ─────────────────────────────────────────────────────   │
│   💾 步骤 2/4  创建快照        📸 备份配置（可选）          │
│        - 📦 保存为 tar.gz（推荐，可迁移）                  │
│        - 📁 保存到快照目录（配合 ocs）                     │
│        - 🚫 跳过备份（危险！）                             │
│   ─────────────────────────────────────────────────────   │
│   📦 步骤 3/4  卸载 npm 包     🗑️  npm uninstall          │
│   ─────────────────────────────────────────────────────   │
│   🗑️  步骤 4/4  删除文件        🧹  清理所有文件          │
│                                                            │
│              ✨ 卸载完成 + 快照已保存 ✨                    │
└────────────────────────────────────────────────────────────┘
```

## 💾 快照功能详解

### 选项 1：保存为 tar.gz（推荐）

```
卸载前快照
选项:
1. 📦 保存为 tar.gz 文件（推荐，可导出到其他机器）
2. 📁 保存到快照目录（配合 ocs 命令恢复）
3. 🚫 跳过备份（配置将丢失！）

请选择 (1/2/3): 1
保存路径 [/home/user/Desktop]: 

       📸 ✨
      ╱    ╲
     │  💾  │   ← 快照已保存
      ╲    ╱
       ────
   你的身份已安全存档
   重装后可随时恢复！

✅ 快照已保存!
  📦 文件: /home/user/Desktop/openclaw_backup_20250115_143022.tar.gz
  💾 大小: 12.5 MB
  🔖 校验: a1b2c3d4
```

### 选项 2：保存到快照目录

```
请选择 (1/2/3): 2

（保存到 ~/.openclaw_snapshots/，配合 openclaw-snapshot 工具使用）

恢复命令：
  ocs list                           # 查看快照
  ocs restore openclaw_backup_xxx   # 恢复
```

## 🔄 完整恢复流程

### 场景：卸载后重装

```bash
# 1. 卸载（已创建快照）
openclaw-uninstall
# → 快照保存到 ~/Desktop/openclaw_backup_xxx.tar.gz

# 2. 重新安装 OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash

# 3. 安装快照工具
pip install openclaw-snapshot

# 4. 导入并恢复快照
ocs import ~/Desktop/openclaw_backup_xxx.tar.gz
ocs restore openclaw_backup_xxx

# 5. 重启服务
openclaw gateway restart

# 🎉 一切恢复原样！
```

### 场景：迁移到新机器

```bash
# 旧机器：导出快照
openclaw-uninstall
# → 选择选项 1，保存到 ~/Desktop/backup.tar.gz
scp ~/Desktop/backup.tar.gz new-machine:~/

# 新机器：导入快照
# 1. 安装 OpenClaw
# 2. pip install openclaw-snapshot
# 3. ocs import ~/backup.tar.gz
# 4. ocs restore backup
```

## 🎯 命令选项

```bash
openclaw-uninstall      # 交互式卸载（推荐）
openclaw-uninstall -y   # 自动确认（危险！）
ocu                     # 简写命令
```

## 🖥️ 界面预览

```bash
$ openclaw-uninstall

    💥 ╔═══════════════════════════════════════╗
      ║     OpenClaw 完全卸载工具             ║
      ║      💾 先存档，再告别 👋             ║
      ╚═══════════════════════════════════════╝

你好！我是卸载虾 🦞
我会帮你安全卸载 OpenClaw
先存档，再告别，随时可以回来~

[█░░░░░░░░░░░░░░] 步骤 2/4
💾 创建卸载前快照

卸载会删除 ~/.openclaw 目录
建议先创建快照，方便以后恢复身份

选项:
1. 📦 保存为 tar.gz 文件（推荐，可导出到其他机器）
2. 📁 保存到快照目录（配合 ocs 命令恢复）
3. 🚫 跳过备份（配置将丢失！）

请选择 (1/2/3): 1
保存路径 [/home/user/Desktop]: /mnt/backup

✅ 快照已保存!
  📦 文件: /mnt/backup/openclaw_backup_20250115_143022.tar.gz
  💾 大小: 12.5 MB

...（卸载过程）...

================================================================
🦞 OpenClaw 已完全卸载
================================================================

💾 快照已保存，以后可以恢复：
  📦 文件: /mnt/backup/openclaw_backup_20250115_143022.tar.gz

恢复方法：
  1. 重新安装 OpenClaw
  2. 安装快照工具: pip install openclaw-snapshot
  3. 导入快照: ocs import /mnt/backup/openclaw_backup_xxx.tar.gz
  4. 恢复快照: ocs restore <快照ID>

         🦞
        /  \
       │ 👋 │   ← 挥手告别
        \  /
         🦞
    
    ✨ 感谢陪伴 ✨
    有缘再会！
```

## 🧹 清理内容

| 位置 | 内容 | 是否备份 |
|------|------|----------|
| `~/.openclaw` | 主配置目录 | ✅ 是 |
| `~/.config/openclaw` | 配置缓存 | ✅ 是 |
| `/usr/local/bin/openclaw*` | 全局命令 | ❌ 否 |
| `~/.npm-global/` | npm 安装 | ❌ 否 |
| Shell 配置 | PATH、别名 | ❌ 否 |

## 🔄 与其他工具配合使用

```bash
# 1. 部署工具安装
openclaw-feishu deploy

# 2. 快照工具备份
ocs create  # 创建当前状态快照

# 3. 卸载工具（带快照）
openclaw-uninstall  # 卸载前自动备份

# 4. 重装后恢复
ocs import xxx.tar.gz
ocs restore xxx
```

## 📦 快照文件结构

```
openclaw_backup_20250115_143022/
├── snapshot.json           # 元数据（时间、大小、校验和）
└── openclaw_data/          # 完整的 ~/.openclaw 目录
    ├── openclaw.json
    ├── config/
    ├── credentials/
    ├── identity/
    └── ...
```

## 🐛 常见问题

### Q: 恢复快照后身份验证失败？
```bash
# 检查恢复后的文件权限
ls -la ~/.openclaw/credentials/

# 可能需要重新授权某些服务
openclaw config
```

### Q: 快照文件太大？
```bash
# 快照已自动排除日志和缓存
# 如果还是很大，可以手动清理后再卸载：
rm -rf ~/.openclaw/logs/
rm -rf ~/.openclaw/media/
```

### Q: 跨系统恢复（如 Linux → macOS）？
```bash
# 完全支持！快照是跨平台的
# 注意：绝对路径配置可能需要手动调整
```

## 📄 许可证

MIT License © 2025 Duka Works

---

<p align="center">
  🦞💥 <strong>Made with love by 卸载虾</strong> 🦞💥
  <br>
  <a href="https://github.com/dukaworks/openclaw-uninstaller">GitHub</a> •
  <a href="https://pypi.org/project/openclaw-uninstaller">PyPI</a>
</p>
