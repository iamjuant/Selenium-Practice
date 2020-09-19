import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
#How to manipulate explicit waits
class ExplicitWaitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\\Users\\jtruj\\OneDrive\\Desktop\\Selenium-Practice\\Selenium-Practice\\chromedriver_win32\\chromedriver.exe')
        driver=self.driver  
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test_new_user(self):
        #We use Webdriverwait passing the driver and the time, then we specify until when it will wait
        #in this case, it will wait until it find the element select-language, and then check if the number of languages are equal to 3
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        #We can assign an element to a variable just like find_element_by_class etc.
        #in this example it will wait up to 10 seconds to find if an element that it's
        # Link text is equal to ACCOUNT and once it finds it it will beassigned to the variable account
        account = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        #we can use the element account to click it
        account.click()
    def test_create_new_customer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()

        #Remember that the methods from expected conditions only accept one parameter, we send a tuple
        # using (By.'how', 'What'
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        create_account_button = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.LINK_TEXT,'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver,10).until(EC.title_contains('Create New Customer Account'))
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)