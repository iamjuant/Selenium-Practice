import unittest
from selenium import webdriver
#we need Select from this library to manipulate dropdown menus
from selenium.webdriver.support.ui import Select
class LanguageOptions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\\Users\\jtruj\\OneDrive\\Desktop\\Selenium-Practice\\Selenium-Practice\\chromedriver_win32\\chromedriver.exe')
        driver=self.driver  
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()


    def test_select_language(self):
        #First we are going to verify that the webpage contain the following options
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element_by_id('select-language'))
        self.assertEqual(3,len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)
        self.assertListEqual(exp_options,act_options)

        #Then we are going to verify that english is the  first selected option
        self.assertEqual('English', select_language.first_selected_option.text)

        #We then select German, and it will change the url to the german page
        select_language.select_by_visible_text('German')

        #We can verify that  the german url is in display
        self.assertTrue('store=german' in self.driver.current_url)

        #Because we are on a different webpage, the select_language object is not longer
        #available, so we need to re-select it
        select_language = Select(self.driver.find_element_by_id('select-language'))
        print(select_language)
        #Then we can select again English to go back
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)