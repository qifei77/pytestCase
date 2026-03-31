import logging
import os
import time

class LogUtil:
    def __init__(self):
        # 日志存放路径
        self.log_path = os.path.join(os.getcwd(),"logs")
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)
        # 日志文件名
        self.log_name = os.path.join(self.log_path, f"{time.strftime('%Y%m%d')}.log")

        # 日志配置
        self.logger = logging.getLogger("API_AUTO_TEST")
        self.logger.setLevel(logging.INFO)

        # 避免重复打印
        if self.logger.handlers:
            self.logger.handlers.clear()

        # 格式
        fmt = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")

        # 文件输出
        fh = logging.FileHandler(self.log_name, encoding="utf-8")
        fh.setFormatter(fmt)
        self.logger.addHandler(fh)

        # 控制台输出
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        self.logger.addHandler(sh)

        # 全局日志对象
log = LogUtil().logger