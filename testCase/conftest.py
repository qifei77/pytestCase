import pytest
from utils.yaml_util import read_yaml
import allure

# 读取环境 URL
@pytest.fixture(scope="session")
def base_url():
    config = read_yaml("config/config.yaml")
    return config["env"][config["current_env"]]

@pytest.fixture(scope = "session")
def log_info():
    config = read_yaml("config/config.yaml")
    return config["login"]

@pytest.fixture(scope = "session")
def context():
    return{}


def pytest_collection_modifyitems(items):
    for item in items:
        # 所有用例都打上标签
        item.add_marker(allure.epic("接口自动化测试平台"))
        item.add_marker(allure.feature(item.parent.name))

# 全局登录获取 token
# @pytest.fixture(scope="session")
# def token(base_url):
#     from api.base_api import BaseApi
#     api = BaseApi(base_url)
#
#     # 登录接口（按你们公司修改）
#     res = api.send(
#         method="post",
#         url="/api/login",
#         json={"username": "test", "password": "123456"}
#     )
#     return res.json()["data"]["token"]