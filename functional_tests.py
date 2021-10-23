"""
功能测试

"""
import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # 应用邀请她输入一个待办事项

        # 她在文本框中输入"Buy peacock features"

        # 她按回车键后，页面更新了
        # 待办事项表格中显示"1. Buy peacock features"

        # 页面又显示了一个文本框，可以输入其他待办事项
        # 她输入了"Use peacock features to make a fly"

        # 页面再次更新，她的清单中显示了这两个待办事项

        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 她访问那个URL，发现她的待办事项列表还在

        # 她很满意，去睡觉了


if __name__ == '__main__':
    unittest.main(warnings='ignore')
