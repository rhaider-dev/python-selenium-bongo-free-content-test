from selenium import webdriver
import unittest, time

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'..\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_bongo_test_case(self):
        driver = self.driver
        driver.get("https://bongobd.com/")

        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/header/div/div/div[2]/div/a[2]/div/span").click()
        driver.find_element_by_xpath("(//img[@alt='img'])[3]").click()
    
    def tearDown(self):
        time.sleep(10)
        self.driver.close()
        self.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()
