from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find.element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows ])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Sam heard about a new online to-do app. He logs on to checkout its homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-d- lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
    
        # He is invited to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                  inputbox.get_attribute('placeholder'),
                  'Enter a to-do item'
        )

        # He types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When he hits enter, the page updates and now the page lists "#1: Buy peacock feathers"
        # as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #import time
        #time.sleep(10)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])


        # There is still a text box inviting her to add another item.
        # He enters "Use peacock feathers to make a fly."
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)


        # The page updates again, and now shows both items on her list
        self.check_for_row_list_table('1: Buy peacock feathers')
        self.check_for_row_list_table('2: Use peacock feathers to make a fly')


        # Sam wonders whether the site will remember the list. Then, he sees
        # that he has generated a unique URL for him --- there is some explanatory text
        # to that effect.

        self.fail("finish the test")

        # He visits the URL -- his to-do list is still there

        # Happy, he goes to sleep

if __name__ == '__main__':
    unittest.main()
