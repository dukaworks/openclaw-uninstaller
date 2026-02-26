#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞💥 OpenClaw 完全卸载工具 - 联动快照版
     卸载虾出品 - 先存档，再告别
"""

import os
import sys
import shutil
import subprocess
import json
import tarfile
import hashlib
from pathlib import Path
from datetime import datetime
from typing import List, Optional

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

# ASCII 艺术
LOGO = f"""
{Colors.PINK}
    💥 ╔═══════════════════════════════════════╗
      ║     OpenClaw 完全卸载工具             ║
      ║      💾 先存档，再告别 👋             ║
      ╚═══════════════════════════════════════╝
{Colors.END}
"""

SNAPSHOT_ART = f"""
{Colors.CYAN}
       📸 ✨
      ╱    ╲
     │  💾  │   ← 快照已保存
      ╲    ╱
       ────
   你的身份已安全存档
   重装后可随时恢复！
{Colors.END}
"""

GOODBYE_ART = f"""
{Colors.GREEN}
         🦞
        /  \
       │ 👋 │   ← 挥手告别
        \\  /
         🦞
    
    ✨ 感谢陪伴 ✨
    有缘再会！
    
    💡 重装后恢复命令：
       ocs import <快照文件>
       ocs restore <快照ID>
{Colors.END}
"""

def print_logo():
    print(LOGO)

def print_step(step_num: int, total: int, message: str, icon: str = "📋"):
    progress = "█" * step_num + "░" * (total - step_num)
    print(f"\n{Colors.CYAN}[{progress}] 步骤 {step_num}/{total}{Colors.END}")
    print(f"{Colors.BOLD}{icon} {message}{Colors.END}\n")

def print_success(msg: str):
    print(f"{Colors.GREEN}✅ {msg}{Colors.END}")

def print_error(msg: str):
    print(f"{Colors.RED}❌ {msg}{Colors.END}")

def print_info(msg: str):
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.END}")

def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.END}")

def print_goodbye(msg: str):
    print(f"{Colors.PINK}🦞 {msg}{Colors.END}")

def loading_animation(msg: str = "处理中", duration: float = 1.0):
    import itertools
    import time
    frames = ["🦐", "🦞", "🦐", "🦞", "💾"]
    start = time.time()
    for frame in itertools.cycle(frames):
        if time.time() - start > duration:
            break
        print(f"\r{frame} {msg}...", end="", flush=True)
        time.sleep(0.2)
    print("\r" + " " * 50 + "\r", end="")

def get_openclaw_paths() -> List[Path]:
    """获取所有 OpenClaw 路径"""
    home = Path.home()
    paths = []
    
    main_dir = home / ".openclaw"
    if main_dir.exists():
        paths.append(main_dir)
    
    # 其他可能位置
    other_paths = [
        home / ".config" / "openclaw",
        Path("/usr/local/bin/openclaw"),
        home / ".npm-global" / "bin" / "openclaw",
    ]
    
    for p in other_paths:
        if p.exists():
            paths.append(p)
    
    return paths

def calculate_checksum(path: Path) -> str:
    """计算校验和"""
    if path.is_file():
        return hashlib.md5(path.read_bytes()).hexdigest()[:8]
    
    hashes = []
    for f in sorted(path.rglob("*")):
        if f.is_file():
            try:
                hashes.append(hashlib.md5(f.read_bytes()).hexdigest())
            except:
                pass
    
    return hashlib.md5("".join(hashes).encode()).hexdigest()[:8] if hashes else "empty"

def get_directory_size(path: Path) -> int:
    """获取目录大小"""
    total = 0
    for f in path.rglob("*"):
        if f.is_file():
            total += f.stat().st_size
    return total

def format_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"

def create_snapshot(export_dir: Optional[Path] = None) -> Optional[Path]:
    """创建快照（内置快照功能，不依赖 ocs）"""
    home = Path.home()
    openclaw_dir = home / ".openclaw"
    
    if not openclaw_dir.exists():
        print_info("没有找到 OpenClaw 配置，跳过快照")
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_name = f"openclaw_backup_{timestamp}"
    
    # 确定保存位置
    if export_dir:
        snapshot_dir = export_dir / snapshot_name
    else:
        snapshot_dir = home / ".openclaw_snapshots" / snapshot_name
    
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    
    print_info(f"正在创建快照: {snapshot_name}")
    
    # 复制配置
    loading_animation("正在备份配置", 1.5)
    
    # 备份整个 .openclaw 目录
    backup_target = snapshot_dir / "openclaw_data"
    shutil.copytree(openclaw_dir, backup_target, dirs_exist_ok=True)
    
    # 创建元数据
    metadata = {
        "id": snapshot_name,
        "name": "pre_uninstall_backup",
        "description": "卸载前自动备份",
        "type": "auto",
        "timestamp": timestamp,
        "created_at": datetime.now().isoformat(),
        "size": get_directory_size(backup_target),
        "checksum": calculate_checksum(backup_target),
        "version": "1.0"
    }
    
    meta_file = snapshot_dir / "snapshot.json"
    with open(meta_file, "w") as f:
        json.dump(metadata, f, indent=2)
    
    # 打包为 tar.gz
    tar_path = snapshot_dir.parent / f"{snapshot_name}.tar.gz"
    with tarfile.open(tar_path, "w:gz") as tar:
        tar.add(snapshot_dir, arcname=snapshot_name)
    
    # 如果指定了导出目录，保留 tar.gz，删除临时目录
    if export_dir:
        shutil.rmtree(snapshot_dir)
        final_path = tar_path
    else:
        final_path = tar_path
        # 也保留解压版本方便直接恢复
    
    print(SNAPSHOT_ART)
    print_success(f"快照已保存!")
    print(f"  📦 文件: {final_path}")
    print(f"  💾 大小: {format_size(metadata['size'])}")
    print(f"  🔖 校验: {metadata['checksum']}")
    
    return final_path

def find_openclaw_processes() -> List[str]:
    try:
        result = subprocess.run(
            ["pgrep", "-f", "openclaw"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return result.stdout.strip().split("\n")
    except:
        pass
    return []

def stop_services():
    print_step(1, 4, "停止 OpenClaw 服务", "🛑")
    
    pids = find_openclaw_processes()
    if not pids:
        print_info("没有运行中的服务")
        return True
    
    print_warning(f"发现 {len(pids)} 个进程")
    
    for pid in pids:
        try:
            loading_animation(f"停止进程 {pid}", 0.5)
            subprocess.run(["kill", "-TERM", pid], check=False)
            print_success(f"进程 {pid} 已停止")
        except Exception as e:
            print_error(f"停止失败: {e}")
    
    import time
    time.sleep(2)
    
    # 强制终止残留
    remaining = find_openclaw_processes()
    for pid in remaining:
        subprocess.run(["kill", "-KILL", pid], check=False)
    
    print_success("所有服务已停止")
    return True

def backup_and_snapshot():
    print_step(2, 4, "创建卸载前快照", "💾")
    
    print(f"{Colors.CYAN}卸载会删除 ~/.openclaw 目录{Colors.END}")
    print(f"{Colors.CYAN}建议先创建快照，方便以后恢复身份{Colors.END}\n")
    
    print("选项:")
    print("1. 📦 保存为 tar.gz 文件（推荐，可导出到其他机器）")
    print("2. 📁 保存到快照目录（配合 ocs 命令恢复）")
    print("3. 🚫 跳过备份（配置将丢失！）")
    print()
    
    choice = input(f"{Colors.BOLD}请选择 (1/2/3): {Colors.END}").strip()
    
    if choice == "1":
        # 保存为 tar.gz
        default_path = Path.home() / "Desktop"
        custom_path = input(f"保存路径 [{default_path}]: ").strip()
        export_dir = Path(custom_path) if custom_path else default_path
        
        if not export_dir.exists():
            print_info(f"创建目录: {export_dir}")
            export_dir.mkdir(parents=True, exist_ok=True)
        
        snapshot_path = create_snapshot(export_dir)
        return snapshot_path
        
    elif choice == "2":
        # 保存到默认快照目录
        snapshot_path = create_snapshot()
        return snapshot_path
        
    elif choice == "3":
        print_warning("⚠️  已跳过备份！配置将永久丢失！")
        confirm = input("输入 'SKIP' 确认跳过: ").strip()
        if confirm != "SKIP":
            print_info("已取消，返回备份选项")
            return backup_and_snapshot()
        return None
    else:
        print_info("默认选择选项 1")
        return create_snapshot(Path.home() / "Desktop")

def uninstall_packages():
    print_step(3, 4, "卸载 npm 包", "📦")
    
    packages = ["openclaw", "clawhub"]
    for pkg in packages:
        try:
            loading_animation(f"卸载 {pkg}", 0.8)
            result = subprocess.run(
                ["npm", "uninstall", "-g", pkg],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                print_success(f"{pkg} 已卸载")
            else:
                print_info(f"{pkg} 未安装")
        except Exception as e:
            print_warning(f"卸载 {pkg} 出错: {e}")
    
    return True

def remove_all_files():
    print_step(4, 4, "删除所有文件", "🗑️")
    
    paths = get_openclaw_paths()
    
    if not paths:
        print_info("没有找到文件")
        return True
    
    print_warning(f"即将删除 {len(paths)} 个项目:")
    for p in paths:
        print(f"  {Colors.YELLOW}- {p}{Colors.END}")
    
    print()
    confirm = input(f"{Colors.BOLD}输入 'DELETE' 确认删除: {Colors.END}").strip()
    
    if confirm != "DELETE":
        print_info("已取消")
        return False
    
    for path in paths:
        try:
            loading_animation(f"删除 {path.name}", 0.3)
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            print_success(f"已删除: {path}")
        except Exception as e:
            print_error(f"删除失败 {path}: {e}")
    
    return True

def cleanup_shell():
    print_info("清理环境变量...")
    
    home = Path.home()
    configs = [home / ".bashrc", home / ".zshrc", home / ".bash_profile"]
    
    for config in configs:
        if not config.exists():
            continue
        try:
            content = config.read_text()
            original = content
            import re
            content = re.sub(r".*# OpenClaw.*\n?", "", content)
            content = re.sub(r".*export PATH.*openclaw.*\n?", "", content)
            if content != original:
                config.write_text(content)
                print_success(f"已清理: {config.name}")
        except:
            pass

def show_restore_guide(snapshot_path: Optional[Path]):
    print()
    print("=" * 60)
    print_goodbye("OpenClaw 已完全卸载")
    print("=" * 60)
    
    if snapshot_path:
        print()
        print(f"{Colors.GREEN}💾 快照已保存，以后可以恢复：{Colors.END}")
        print(f"  📦 文件: {snapshot_path}")
        print()
        print(f"{Colors.CYAN}恢复方法：{Colors.END}")
        print("  1. 重新安装 OpenClaw")
        print("  2. 安装快照工具: pip install openclaw-snapshot")
        print(f"  3. 导入快照: ocs import {snapshot_path}")
        print("  4. 恢复快照: ocs restore <快照ID>")
        print()
        print(f"{Colors.DIM}或直接复制文件:{Colors.END}")
        print(f"  tar -xzf {snapshot_path} -C ~")
        print(f"  mv ~/openclaw_backup_*/openclaw_data ~/.openclaw")
    
    print()
    print(GOODBYE_ART)

def main():
    print_logo()
    
    print(f"{Colors.CYAN}你好！我是卸载虾 🦞{Colors.END}")
    print(f"{Colors.CYAN}我会帮你安全卸载 OpenClaw{Colors.END}")
    print(f"{Colors.CYAN}先存档，再告别，随时可以回来~{Colors.END}\n")
    
    paths = get_openclaw_paths()
    if not paths:
        print_info("没有找到 OpenClaw")
        return
    
    # 1. 停止服务
    if not stop_services():
        print_error("停止服务失败")
    
    # 2. 创建快照
    snapshot_path = backup_and_snapshot()
    
    # 3. 卸载 npm
    uninstall_packages()
    
    # 4. 删除文件
    if not remove_all_files():
        print_error("删除未完成")
        return
    
    # 5. 清理 shell
    cleanup_shell()
    
    # 6. 显示恢复指南
    show_restore_guide(snapshot_path)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.PINK}🦞 取消卸载，我们还在一起！{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}💥 错误: {e}{Colors.END}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
