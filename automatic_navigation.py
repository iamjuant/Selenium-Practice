import unittest
from selenium import webdriver
from time import sleep

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\\Users\\jtruj\\OneDrive\\Desktop\\Selenium-Practice\\Selenium-Practice\\chromedriver_win32\\chromedriver.exe')
        driver=self.driver  
        driver.get('http://google.com')
        driver.maximize_window()


    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('funny cats')
        search_field.submit()

        driver.back()
        sleep(2)
        driver.forward()
        sleep(2)
        driver.refresh()
        sleep(2)    

        


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)