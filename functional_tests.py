"""
功能测试

"""
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        # self.fail('Finish the test')
        # header_text = self.browser.find_element_by_tag_name('h1').text
        header_text = self.browser.find_element(by='tag name', value='h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        input_box = self.browser.find_element(by='id', value='id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在文本框中输入"Buy peacock features"
        input_box.send_keys('Buy peacock features')

        # 她按回车键后，页面更新了
        # 待办事项表格中显示"1. Buy peacock features"
        input_box.send_keys(Keys.ENTER)
        time.sleep(4)

        table = self.browser.find_element(by='id', value='id_list_table')
        rows = table.find_elements(by='tag name', value='tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock features' for row in rows)
        )

        # 页面又显示了一个文本框，可以输入其他待办事项
        # 她输入了"Use peacock features to make a fly"

        # 页面再次更新，她的清单中显示了这两个待办事项

        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 她访问那个URL，发现她的待办事项列表还在

        # 她很满意，去睡觉了


if __name__ == '__main__':
    unittest.main(warnings='ignore')
