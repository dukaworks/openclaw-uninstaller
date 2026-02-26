#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞💥 OpenClaw Uninstaller - CLI 入口
"""

import sys
from .uninstaller import main

def cli():
    """CLI 入口点"""
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🦞 取消卸载，我们还在一起！")
        sys.exit(0)
    except Exception as e:
        print(f"\n💥 发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    cli()
