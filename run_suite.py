# 导包
import unittest
from tool.HTMLTestReportCN import HTMLTestRunner
# 定义测试套件
suite = unittest.defaultTestLoader.discover("./")
# 获取文件流 并 实例化HTMLTestRunner调用run方法
with open("../report/report.html","wb")as f:
    HTMLTestRunner(stream=f, title="tpshop登录模块接口测试测试报告").run(suite)