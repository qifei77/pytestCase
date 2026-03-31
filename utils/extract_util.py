import re
from utils.tools import *
from utils.context import context

def replace_var(s):
    if not isinstance(s, str):
        return s

    pattern = re.compile(r'\$\{(\w+)\}')
    keys = pattern.findall(s)

    for key in keys:
        if key in context:
            value = str(context[key])
        elif key in globals():
            func = globals()[key]
            value = str(func())
        else:
            continue

        s = s.replace(f"${{{key}}}", value)
    return s

def replace_data(data):
    if isinstance(data, dict):
        new_dict = {}
        for k, v in data.items():
            new_dict[k] = replace_data(v)
        return new_dict
    elif isinstance(data, list):
        return [replace_data(item) for item in data]
    elif isinstance(data, str):
        return replace_var(data)
    else:
        return data