
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Sam heard about a new online to-do app. He logs on to checkout its homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-d- lists
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

        # He is invited to enter a to-do item right away

        # He types "Buy peacock feathers" into a text box

        # When he hits enter, the page updates and now the page lists "#1: Buy peacock feathers"
        # as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # He enters "Use peacock feathers to make a fly."

        # The page updates again, and now shows both items on her list

        # Sam wonders whether the site will remember the list. Then, he sees
        # that he has generated a unique URL for him --- there is some explanatory text
        # to that effect.

        # He visits the URL -- his to-do list is still there

        # Happy, he goes to sleep

if __name__ == '__main__':
    unittest.main()
