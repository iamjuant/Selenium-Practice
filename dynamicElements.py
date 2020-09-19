import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
#How to manipulate explicit waits
class DynamicElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\\Users\\jtruj\\OneDrive\\Desktop\\Selenium-Practice\\Selenium-Practice\\chromedriver_win32\\chromedriver.exe')
        driver=self.driver  
        driver.get('http://the-internet.herokuapp.com')
        driver.maximize_window()
        driver.find_element_by_link_text('Disappearing Elements').click()
    #This method shows how to select an element when that element appears and disappears
    # by a random refresh
    def test_new_user(self):
        driver = self.driver
        options = []
        menu = 5
        tries = 1 
        while(len(options) <5):
            options.clear()
            for i in range(menu):
                try:
                    options_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(options_name.text)
                    print(options)
                except:
                    print(f'Option number {i + 1} is NOT FOUND')
                    tries +=1
                    driver.refresh()
        print(f'Finished in {tries} tries')
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)