import yaml
import os
from utils.extract_util import replace_data

# 读取 YAML 文件
import yaml
from utils.extract_util import replace_data

def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return replace_data(data)

# 写入 YAML 文件
def write_yaml(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)