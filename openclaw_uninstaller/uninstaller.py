#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞💥 OpenClaw 完全卸载工具
     卸载虾出品 - 温柔地说再见
"""

import os
import sys
import shutil
import subprocess
import json
from pathlib import Path
from datetime import datetime
from typing import List, Tuple

# 颜色代码 🎨
class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

# 可爱的 ASCII 艺术 🦞
LOGO = f"""
{Colors.PINK}
    💥 ╔═══════════════════════════════════════╗
      ║     OpenClaw 完全卸载工具             ║
      ║        温柔地说再见 👋                ║
      ╚═══════════════════════════════════════╝
{Colors.END}
"""

GOODBYE_ART = f"""
{Colors.CYAN}
         🦞
        /  \
       │ 👋 │   ← 挥手告别
        \\  /
         🦞
    
    ✨ 感谢陪伴 ✨
    有缘再会！
    
    {Colors.DIM}OpenClaw 已完全移除{Colors.END}
{Colors.END}
"

BACKUP_ART = f"""
{Colors.GREEN}
    📦 💾 📦
    
    配置文件已安全备份
    随时欢迎回来！
    
    🦞 "记得想我哦~"
{Colors.END}
"

WARNING_ART = f"""
{Colors.YELLOW}
    ⚠️  (╯°□°)╯ 等等！
    
    你真的要删除我吗？
    我还可以帮你做很多事情呢...
    
    {Colors.DIM}（反正我拦不住你）{Colors.END}
{Colors.END}
"

def print_logo():
    """打印Logo"""
    print(LOGO)

def print_step(step_num: int, total: int, message: str, icon: str = "📋"):
    """打印步骤进度"""
    progress = "█" * step_num + "░" * (total - step_num)
    print(f"\n{Colors.CYAN}[{progress}] 步骤 {step_num}/{total}{Colors.END}")
    print(f"{Colors.BOLD}{icon} {message}{Colors.END}\n")

def print_success(message: str):
    """打印成功信息"""
    print(f"{Colors.GREEN}✅ {message}{Colors.END}")

def print_error(message: str):
    """打印错误信息"""
    print(f"{Colors.RED}❌ {message}{Colors.END}")

def print_info(message: str):
    """打印信息"""
    print(f"{Colors.BLUE}ℹ️  {message}{Colors.END}")

def print_warning(message: str):
    """打印警告"""
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.END}")

def print_goodbye(message: str):
    """打印告别信息"""
    print(f"{Colors.PINK}🦞 {message}{Colors.END}")

def loading_animation(message: str = "正在处理", duration: float = 1.0):
    """加载动画"""
    import itertools
    import time
    
    frames = ["🦐", "🦞", "🦐", "🦞", "✨"]
    start_time = time.time()
    
    for frame in itertools.cycle(frames):
        if time.time() - start_time > duration:
            break
        print(f"\r{frame} {message}...", end="", flush=True)
        time.sleep(0.2)
    
    print("\r" + " " * 50 + "\r", end="")

def get_openclaw_paths() -> List[Path]:
    """获取所有 OpenClaw 相关路径"""
    home = Path.home()
    
    paths = [
        # 主目录
        home / ".openclaw",
        # 全局安装
        Path("/usr/local/bin/openclaw"),
        Path("/usr/local/bin/openclaw-gateway"),
        # npm 全局
        home / ".npm-global" / "bin" / "openclaw",
        home / ".npm-global" / "lib" / "node_modules" / "openclaw",
        # npx 缓存
        home / ".npm" / "_npx",
        # 配置目录（各种可能的位置）
        home / ".config" / "openclaw",
        home / "Library" / "Application Support" / "openclaw",  # macOS
        home / "AppData" / "Roaming" / "openclaw",  # Windows
        home / "AppData" / "Local" / "openclaw",
    ]
    
    # 过滤存在的路径
    existing = [p for p in paths if p.exists()]
    return existing

def find_openclaw_processes() -> List[str]:
    """查找 OpenClaw 进程"""
    try:
        result = subprocess.run(
            ["pgrep", "-f", "openclaw"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip().split("\n")
    except:
        pass
    return []

def stop_openclaw_services() -> bool:
    """停止 OpenClaw 服务"""
    print_step(1, 5, "停止 OpenClaw 服务", "🛑")
    
    # 查找进程
    pids = find_openclaw_processes()
    
    if not pids:
        print_info("没有发现运行中的 OpenClaw 进程")
        return True
    
    print_warning(f"发现 {len(pids)} 个 OpenClaw 进程正在运行")
    
    for pid in pids:
        try:
            loading_animation(f"正在停止进程 {pid}", 0.5)
            subprocess.run(["kill", "-TERM", pid], check=False)
            print_success(f"进程 {pid} 已停止")
        except Exception as e:
            print_error(f"停止进程 {pid} 失败: {e}")
    
    # 等待进程完全退出
    import time
    time.sleep(2)
    
    # 检查是否还有残留
    remaining = find_openclaw_processes()
    if remaining:
        print_warning(f"还有 {len(remaining)} 个进程在运行，强制终止...")
        for pid in remaining:
            subprocess.run(["kill", "-KILL", pid], check=False)
    
    print_success("所有 OpenClaw 服务已停止")
    return True

def backup_config() -> bool:
    """备份配置"""
    print_step(2, 5, "备份配置文件", "💾")
    
    home = Path.home()
    openclaw_dir = home / ".openclaw"
    
    if not openclaw_dir.exists():
        print_info("没有找到配置文件，跳过备份")
        return True
    
    # 创建备份目录
    backup_dir = home / ".openclaw_backup"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"openclaw_backup_{timestamp}"
    
    try:
        backup_path.mkdir(parents=True, exist_ok=True)
        
        # 复制重要文件
        important_files = [
            "openclaw.json",
            "config.json",
            "credentials",
            "identity",
        ]
        
        for item in important_files:
            src = openclaw_dir / item
            if src.exists():
                if src.is_dir():
                    shutil.copytree(src, backup_path / item, dirs_exist_ok=True)
                else:
                    shutil.copy2(src, backup_path / item)
                print_info(f"已备份: {item}")
        
        # 保存备份信息
        backup_info = {
            "timestamp": timestamp,
            "path": str(backup_path),
            "reason": "Before uninstall"
        }
        
        info_file = backup_path / "backup_info.json"
        with open(info_file, "w") as f:
            json.dump(backup_info, f, indent=2)
        
        print_success(f"配置已备份到: {backup_path}")
        print(BACKUP_ART)
        
        return True
        
    except Exception as e:
        print_error(f"备份失败: {e}")
        return False

def uninstall_npm_package() -> bool:
    """卸载 npm 包"""
    print_step(3, 5, "卸载 npm 包", "📦")
    
    packages = ["openclaw", "clawhub"]
    
    for pkg in packages:
        try:
            loading_animation(f"正在卸载 {pkg}", 0.8)
            
            result = subprocess.run(
                ["npm", "uninstall", "-g", pkg],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print_success(f"{pkg} 已卸载")
            else:
                # 可能没安装
                print_info(f"{pkg} 未安装或已移除")
                
        except Exception as e:
            print_warning(f"卸载 {pkg} 时出错: {e}")
    
    return True

def remove_files_and_dirs() -> bool:
    """删除文件和目录"""
    print_step(4, 5, "清理文件和目录", "🗑️")
    
    paths = get_openclaw_paths()
    
    if not paths:
        print_info("没有找到 OpenClaw 相关文件")
        return True
    
    print_warning(f"即将删除以下 {len(paths)} 个项目：")
    for p in paths:
        print(f"  {Colors.YELLOW}- {p}{Colors.END}")
    
    print()
    confirm = input(f"{Colors.BOLD}确认删除以上所有文件？输入 'yes' 继续: {Colors.END}").strip()
    
    if confirm.lower() != "yes":
        print_info("已取消删除")
        return False
    
    for path in paths:
        try:
            loading_animation(f"正在删除 {path.name}", 0.3)
            
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            
            print_success(f"已删除: {path}")
            
        except Exception as e:
            print_error(f"删除失败 {path}: {e}")
    
    return True

def cleanup_shell_config() -> bool:
    """清理 shell 配置"""
    print_step(5, 5, "清理环境变量", "🧹")
    
    home = Path.home()
    shell_configs = [
        home / ".bashrc",
        home / ".zshrc",
        home / ".bash_profile",
        home / ".zprofile",
    ]
    
    patterns = [
        "# OpenClaw",
        "export PATH.*openclaw",
        "alias.*openclaw",
    ]
    
    found = False
    for config in shell_configs:
        if not config.exists():
            continue
        
        try:
            content = config.read_text()
            original = content
            
            # 移除 OpenClaw 相关配置
            for pattern in patterns:
                import re
                content = re.sub(f".*{pattern}.*\\n?", "", content)
            
            if content != original:
                config.write_text(content)
                print_success(f"已清理: {config}")
                found = True
                
        except Exception as e:
            print_warning(f"清理 {config} 时出错: {e}")
    
    if not found:
        print_info("没有发现需要清理的环境变量")
    
    return True

def final_cleanup():
    """最终清理"""
    print()
    print("=" * 50)
    print_goodbye("正在做最后的检查...")
    print("=" * 50)
    
    # 检查是否还有残留
    remaining = get_openclaw_paths()
    
    if remaining:
        print_warning(f"还有 {len(remaining)} 个项目可能需要手动删除:")
        for p in remaining:
            print(f"  {Colors.YELLOW}- {p}{Colors.END}")
        print()
        print_info("你可以手动删除以上文件，或使用 sudo 权限重试")
    else:
        print_success("清理完成！OpenClaw 已完全移除")
    
    print()
    print(GOODBYE_ART)
    
    print(f"{Colors.DIM}提示: 如果以后想重新安装，访问 https://openclaw.ai{Colors.END}")
    print()

def main():
    """主函数"""
    print_logo()
    
    print(f"{Colors.CYAN}你好！我是卸载虾 🦞{Colors.END}")
    print(f"{Colors.CYAN}我会帮你彻底移除 OpenClaw{Colors.END}\n")
    
    # 检查是否有 OpenClaw
    paths = get_openclaw_paths()
    
    if not paths:
        print_info("没有找到 OpenClaw 安装，可能已经被卸载了？")
        print()
        print(GOODBYE_ART)
        return
    
    print(f"{Colors.YELLOW}发现 OpenClaw 安装在以下位置：{Colors.END}")
    for p in paths[:5]:  # 只显示前5个
        print(f"  - {p}")
    
    if len(paths) > 5:
        print(f"  ... 还有 {len(paths) - 5} 个")
    
    print()
    print(WARNING_ART)
    
    # 确认
    print(f"{Colors.BOLD}卸载选项：{Colors.END}")
    print("1. 🗑️  完全删除（不保留配置）")
    print("2. 💾  备份后删除（推荐）")
    print("3. ❌  取消")
    print()
    
    choice = input(f"{Colors.BOLD}请选择 (1/2/3): {Colors.END}").strip()
    
    if choice == "3" or choice.lower() in ["cancel", "q", "quit"]:
        print_goodbye("好的，我会一直在这里等你~ 👋")
        return
    
    # 执行卸载流程
    if choice == "2":
        if not backup_config():
            print_error("备份失败，取消卸载")
            return
    else:
        print_warning("已选择不备份，配置将丢失！")
        confirm = input("确定不备份？输入 'DELETE' 继续: ").strip()
        if confirm != "DELETE":
            print_info("已取消")
            return
    
    # 停止服务
    if not stop_openclaw_services():
        print_error("停止服务失败，继续尝试卸载...")
    
    # 卸载 npm 包
    uninstall_npm_package()
    
    # 删除文件
    if not remove_files_and_dirs():
        print_error("文件删除未完成")
        return
    
    # 清理环境变量
    cleanup_shell_config()
    
    # 最终清理
    final_cleanup()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.PINK}🦞 取消卸载，我们还在一起！{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}💥 发生错误: {e}{Colors.END}")
        sys.exit(1)
