import os
import shutil

# 配置路径
root_dir = "."
docs_dir = "docs"
marker_start = ""
marker_end = ""

def update_docs():
    # 1. 获取根目录下所有的 html 文件 (排除 index.html 和 docs 目录)
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html') and f != 'index.html']
    html_files.sort(reverse=True) # 按文件名排序（通常按日期命名的话，最新的在前）

    # 2. 确保文件已同步到 docs 文件夹
    # 我们把它们放在 docs/previews/ 目录下以保持整洁
    preview_dir = os.path.join(docs_dir, "previews")
    if not os.path.exists(preview_dir):
        os.makedirs(preview_dir)

    list_items = []
    for f in html_files:
        shutil.copy2(f, os.path.join(preview_dir, f))
        # 生成 HTML 列表项（可以带预览链接）
        list_items.append(f'<li><a href=" " target="_blank">{f}</a > - <small>已同步</small></li>')

    # 3. 更新 docs/index.html
    index_path = os.path.join(docs_dir, "index.html")
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if marker_start in content and marker_end in content:
        new_list_content = f"{marker_start}\n    <ul>\n        {''.join(['        ' + item + '\n' for item in list_items])}    </ul>\n    {marker_end}"
        
        # 替换旧内容
        start_idx = content.find(marker_start)
        end_idx = content.find(marker_end) + len(marker_end)
        updated_content = content[:start_idx] + new_list_content + content[end_idx:]

        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Index updated successfully.")
    else:
        print("Markers not found in index.html")

if __name__ == "__main__":
    update_docs()
