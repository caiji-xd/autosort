import os
import json
import shutil

def load_keywords_from_json(file_path):
    with open(file_path, 'rb') as file:  # 以二进制模式读取文件
        keywords = json.loads(file.read().decode('utf-8'))  # 使用 UTF-8 编码解析
    return keywords

def contains_keyword_in_list(keyword_list, filename):
    for keyword in keyword_list:
        if keyword in filename.lower():
            return True
    return False

def move_files_to_folder(extension_list, source_folder, destination_folder, keyword_data):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for item in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, item)):
            if any(item.endswith(ext) for ext in extension_list):
                for category, keywords in keyword_data.items():
                    if contains_keyword_in_list(keywords, item):
                        folder_name = category
                        break
                else:
                    folder_name = ''

                if folder_name:
                    target_folder = os.path.join(destination_folder, folder_name)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                else:
                    target_folder = destination_folder

                shutil.move(os.path.join(source_folder, item), os.path.join(target_folder, item))
                print(f"Moved: {item} to {target_folder}")

if __name__ == "__main__":
    # 定义要移动的文件扩展名
    file_extensions = ['.pdf', '.pptx', '.ppt', '.doc', '.docx', '.xlsx', '.xls', '.hhtx']

    # 桌面路径
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')

    # 目标文件夹
    target_folder = os.path.join(desktop_path, '学习资料')

    # 从 JSON 文件中加载关键词
    keyword_file_path = 'keywords.json'
    keyword_data = load_keywords_from_json(keyword_file_path)

    # 运行函数
    move_files_to_folder(file_extensions, desktop_path, target_folder, keyword_data)