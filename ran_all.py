import os
import pytest

if __name__ == '__main__':
    # 1. 执行所有用例
    pytest.main([
        "testCase/",
        "-vs",
        "--alluredir=reports",
        "--clean-alluredir"
    ])

    # 2. 自动打开报告
    os.system("allure serve reports")