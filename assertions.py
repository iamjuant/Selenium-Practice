import unittest
from selenium import webdriver

#needed to raise an exception in case an element is not find it
from selenium.common.exceptions import NoSuchElementException
#needed to pass how to find an element
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\\Users\\jtruj\\OneDrive\\Desktop\\Selenium-Practice\\Selenium-Practice\\chromedriver_win32\\chromedriver.exe')
        driver=self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    #create a function to check if an element is present, it passes how to check it, and what element
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value= what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == "__main__":
    unittest.main(verbosity=2)