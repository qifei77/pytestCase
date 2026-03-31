from jsonpath_rw import parse

def extract_by_jsonpath(data:dict ,expr:str):
    """
        通过 jsonpath 表达式提取字段
        示例：extract_by_jsonpath(res, "$.id")
        """
    jsonpath_expr = parse(expr)
    result = [match.value for match in jsonpath_expr.find(data)]
    return result[0] if result else None