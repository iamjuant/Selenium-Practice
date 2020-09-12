import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
#This class is for "Testing" how to use selenium webdriver by passing a unittest test case
class SeleniumPractice(unittest.TestCase):
    #This method is for the initial setup for the tests
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\\Users\\jtruj\\OneDrive\\Desktop\\Selenium-Practice\\Selenium-Practice\\chromedriver_win32\\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10) 

    #This is one of the test, We can have a lot of test to do 
    def test_Google(self):
        driver = self.driver
        driver.get('https://www.google.com')
    
    #This methos just stop the webdriver, and closes the window
    def tearDown(self):
        self.driver.quit()

#We call main by passing unittest with vervosity as 2, and a HTML testrunner where we can see the report in a new folder called reports/report
if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output='report', report_name='Selenium-Practice-report'))

