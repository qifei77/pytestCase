import requests
from utils.log_util import log
from utils.yaml_util import read_yaml


class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url

        #读取默认请求头
        config = read_yaml("./config/config.yaml")
        self.default_headers = config.get("default_headers",{})

    # 统一请求方法
    def send(self, method, url, **kwargs):
        full_url = self.base_url + url

        #合并headers
        headers = self.default_headers.copy()
        if "headers" in kwargs:
            headers.update(kwargs["headers"])
        kwargs["headers"] = headers

        log.info(f"请求地址：{full_url}")
        log.info(f"请求方式：{method}")
        log.info(f"请求参数：{kwargs}")

        try:
            # 发送请求
            response = requests.request(method=method, url=full_url, timeout=10, **kwargs)
            log.info(f"响应状态码：{response.status_code}")
            log.info(f"响应结果：{response.text}")
            return response

        except Exception as e:
            log.error(f"请求异常：{e}")
            raise e
