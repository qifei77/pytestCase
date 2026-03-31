import allure
import pytest
from utils.yaml_util import read_yaml
from api.base_api import BaseApi
from utils.log_util import log
from utils.assert_util import assert_response

# 读取所有YAML用例
test_cases = read_yaml("./data/test_post.yaml")

@allure.epic("接口自动化测试")
@allure.feature("文章模块")
class TestPost:

    @allure.story("批量获取文章")
    @pytest.mark.parametrize("case", test_cases, ids=[case["name"] for case in test_cases])
    def test_batch_get_post(self, base_url, case):
        with allure.step(f"执行用例：{case['name']}"):
            # 发送请求
            api = BaseApi(base_url)
            resp = api.send(
                method=case["method"],
                url=case["url"]
            )
            res = resp.json()

            # 断言
            with allure.step("断言结果"):
                assert_response(res,case["assert"],resp.status_code)