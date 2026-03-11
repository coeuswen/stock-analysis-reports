#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
自动上传HTML报告到GitHub仓库
Automatically upload HTML reports to GitHub repository
"""

import subprocess
import os
import sys
from datetime import datetime

def run_command(cmd):
    """执行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def upload_report(html_file):
    """
    上传HTML报告到GitHub

    Args:
        html_file: HTML文件路径
    """
    # 切换到工作目录
    os.chdir('e:/WorkBuddy/openclaw')

    # 获取当前日期作为commit message
    today = datetime.now().strftime('%Y-%m-%d')
    commit_msg = f'Add_stock_analysis_report_{today.replace("-", "")}'

    # Git命令
    commands = [
        f'git add "{html_file}"',
        f'git commit -m {commit_msg}',
        'git push'
    ]

    print(f"[INFO] 开始上传报告: {html_file}")
    print("-" * 50)

    success = True
    for cmd in commands:
        print(f"[CMD] {cmd}")
        success, stdout, stderr = run_command(cmd)
        if success:
            print(f"[OK] 命令执行成功")
        else:
            print(f"[ERROR] 命令执行失败")
            if stderr:
                print(f"[STDERR] {stderr}")
            success = False
            break
        print()

    print("-" * 50)
    if success:
        print("[SUCCESS] 报告已成功上传到GitHub！")
        print("\n访问链接：")
        print("  GitHub仓库: https://github.com/Coeuswen/stock-analysis-reports")
        print("  直接访问: https://coeuswen.github.io/stock-analysis-reports/股票复盘分析报告_20260311_超级精美版.html")
    else:
        print("[FAILED] 上传失败，请检查错误信息")

    return success

def update_readme(html_file):
    """更新README.md文件"""
    try:
        # 获取文件名
        filename = os.path.basename(html_file)

        # 读取现有README
        readme_path = 'e:/WorkBuddy/openclaw/README.md'
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# Stock Analysis Reports\n\nThis repository contains daily stock market analysis reports.\n\n## Reports\n"

        # 检查是否已经存在这个链接
        if filename in content:
            print("[INFO] README.md中已存在此报告链接")
            return True

        # 添加新的报告链接
        today = datetime.now().strftime('%Y年%m月%d日')
        new_link = f"\n- [{today}]({filename})"

        # 在"## Reports"后添加
        if "## Reports" in content:
            content = content.replace("## Reports", f"## Reports{new_link}")
        else:
            content += f"\n## Reports{new_link}"

        # 保存README
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("[SUCCESS] README.md已更新")

        # 提交README
        os.chdir('e:/WorkBuddy/openclaw')
        run_command('git add README.md')
        run_command('git commit -m Update_READMD')
        run_command('git push')

        return True

    except Exception as e:
        print(f"[ERROR] 更新README失败: {str(e)}")
        return False

if __name__ == "__main__":
    # 获取HTML文件路径
    if len(sys.argv) > 1:
        html_file = sys.argv[1]
    else:
        # 默认使用今天的报告
        today = datetime.now().strftime('%Y%m%d')
        html_file = f'股票复盘分析报告_{today}_超级精美版.html'

    # 检查文件是否存在
    if not os.path.exists(html_file):
        print(f"[ERROR] 文件不存在: {html_file}")
        sys.exit(1)

    # 更新README
    update_readme(html_file)

    # 上传报告
    success = upload_report(html_file)

    sys.exit(0 if success else 1)
