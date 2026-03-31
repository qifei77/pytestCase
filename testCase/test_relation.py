import allure
import pytest

from utils.assert_util import assert_response
from utils.yaml_util import read_yaml
from api.base_api import BaseApi
from utils.log_util import log
from utils.tools import timestamp
from utils.tools import random_str
from utils.context import context
from utils.jsonpath_util import extract_by_jsonpath

case = read_yaml("data/test_create_post.yaml")

@allure.epic("接口自动化测试项目")
@allure.feature("文章关联场景")
class TestPostRelation:

    @allure.story("步骤1：创建文章")
    def test_create_post(self, base_url):
        api = BaseApi(base_url)

        # 发送请求（随机值已经替换好了）
        resp = api.send(
            method=case["method"],
            url=case["url"],
            json=case["json"]
        )
        res = resp.json()
        log.info(f"状态码：{resp.status_code}")
        context["post_id"] = extract_by_jsonpath(res,"$.id")
        # 断言
        assert_response(res, case["assert"], resp.status_code)

    @allure.story("步骤2：查询刚创建的文章")
    def test_select_post(self,base_url,context):
        post_id = context["post_id"]
        api = BaseApi(base_url)

        resp = api.send(
            method="GET",
            url=f"/posts/{post_id}"
        )
        res = resp.json()

        assert_response(res,{"id":post_id},resp.status_code)
        log.info("查询创建的文章成功")
