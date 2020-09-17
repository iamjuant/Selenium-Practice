import unittest
from selenium import webdriver
#we need Select from this library to manipulate dropdown menus
from selenium.webdriver.support.ui import Select
class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\\Users\\jtruj\\OneDrive\\Desktop\\Selenium-Practice\\Selenium-Practice\\chromedriver_win32\\chromedriver.exe')
        driver=self.driver  
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()


    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

        x=driver.find_elements_by_class_name('link-compare')

        for i in range(len(x)):
            driver.find_elements_by_class_name('link-compare')[i].click()

        driver.find_element_by_link_text('Clear All').click()
        alert = driver.switch_to.alert()
        alert_text = alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        alert.accept()



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)