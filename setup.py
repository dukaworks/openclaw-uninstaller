#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞💥 OpenClaw Uninstaller
一键彻底卸载 OpenClaw - 卸载虾出品
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="openclaw-uninstaller",
    version="1.0.0",
    author="Duka Works",
    author_email="chenzhy.bj@gmail.com",
    description="🦞💥 一键彻底卸载 OpenClaw - 温柔地说再见",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dukaworks/openclaw-uninstaller",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Installation/Setup",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "openclaw-uninstall=openclaw_uninstaller.uninstaller:main",
            "ocu=openclaw_uninstaller.uninstaller:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
