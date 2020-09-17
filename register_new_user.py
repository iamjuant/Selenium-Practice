import unittest
from selenium import webdriver
import time
class NewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\\Users\\jtruj\\OneDrive\\Desktop\\Selenium-Practice\\Selenium-Practice\\chromedriver_win32\\chromedriver.exe')
        driver=self.driver  
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        firstName = driver.find_element_by_id('firstname')
        middleName = driver.find_element_by_id('middlename')
        lastName =driver.find_element_by_id('lastname')
        email = driver.find_element_by_id('email_address')
        news_letter_button = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')
        #To simplify create a list of the elements in the form to manipulate them easily using a loop   
        form_fields=[firstName,middleName,lastName,email,password,confirm_password]

        #Check if everything that we need is enabled
        self.assertTrue(submit_button.is_enabled())
        self.assertTrue(news_letter_button.is_enabled())

        for item in form_fields:
            self.assertTrue(item.is_enabled())
        
        #this is what we are going to fill in the form fields
        whatToSend = iter(['test', 'test', 'test', 'test@myemail.com', 'testPassword', 'testPassword'])

        for item in form_fields:
            item.send_keys(next(whatToSend))
        submit_button.click()


    def tearDown(self):
        time.sleep(10.0)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)