from utils.log_util import log

def assert_response(actual, expect,stuats_code):
    """
        通用断言
        :param actual: 实际返回 dict
        :param expect: 期望断言 dict
        """
    log.info(f"实际返回结果：{actual}")
    log.info(f"期望返回结果：{expect}")
    assert 200<=stuats_code<300,f"状态码错误"
    for key , expect_value in expect.items():
        # 判断实际结果中是否包含期望字段
        assert key in actual , f"返回结果中不存在 {key} 字段"
        actual_value = actual[key]

        # 特殊标记：存在即可，不判断值
        if expect_value == "存在":
            log.info(f"{key} 存在，校验通过")
            continue

        # 相等断言
        assert actual_value == expect_value, \
            f"{key} 断言失败：期望={expect_value}，实际={actual_value}"

    log.info("判断全部通过")