import allure
from utils.yaml_util import read_yaml
from api.base_api import BaseApi
from utils.log_util import log

@allure.epic("接口自动化测试项目")
@allure.feature("文章模块")
class TestPost:
    @allure.story("获取单篇文章")
    @allure.title("测试获取ID=1的文章")
    def test_get_post(self, base_url):
        # 1. 读取用例
        case = read_yaml("./data/test_user.yaml")

        # 2. 发送请求
        api = BaseApi(base_url)
        res = api.send(
            method=case["method"],
            url=case["url"],
            headers=case["headers"]
        ).json()


        # 3. 断言
        try:
            assert res["id"] == case["assert"]["id"]
            assert res["userId"] == case["assert"]["userId"]
            assert "title1" in res
            log.info("用例执行成功")
        except AssertionError as e :
            log.error("用例执行失败")
            raise