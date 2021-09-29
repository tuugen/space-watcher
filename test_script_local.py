"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        # options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/Applications/private/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = os.path.expanduser("~/bin/chromedriver")
        
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(chrome_driver_binary, options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_0(self):
        print("testing 0")
        import ipdb

        # ipdb.sset_trace()

        for i in range(2):
            print(i)


        self.driver.get('https://www.notams.faa.gov/dinsQueryWeb/')

        import time
        from selenium.webdriver.common.by import By
        driver = self.driver
        iagree = driver.find_elements(By.XPATH, '//div[@id="IAgree"]') 
        
        #popup to agree
        if iagree:
            agree_button = driver.find_elements(By.XPATH, '//button[text()="I Agree"]')

            assert(len(agree_button) == 1)
            agree_button = agree_button[0]
            agree_button.click()

        #input NOTAMs of interest
        notam_area = driver.find_elements(By.XPATH, '//textarea[@name="retrieveLocId"]')
        assert(len(notam_area) == 1)
        notam_area = notam_area[0]

        query = "NZZC"
        for c in query:
            time.sleep(0.250)
            notam_area.send_keys(c)

        report_type = driver.find_elements(By.XPATH, 
                        '//input[@name="reportType" and @value="Raw"]')
        report_type = report_type[0]
        report_type.click()
        

        # naively click first submit on page
        # submits = driver.find_elements(By.XPATH, '//input[@type="submit" and @name="submit"]')
        # s1 = submits[0]
        # s1.click()

        driver.find_elements(By.XPATH, 
        '//input[@type="submit" and @name="submit"]')[0].click()

        # new tab should be opened now
        assert(len(driver.window_handles) == 2)

        driver.switch_to.window(driver.window_handles[1])

        #ipdb.sset_trace()
        
        notams = driver.find_elements(By.XPATH, '//form[@name="NotamRetrievalForm"]/div/table/tbody/tr/td/table[3]/tbody')[0]
        

        notam_texts = notams.find_elements_by_xpath('tr/td[@class="textBlack12"]')

        file = open("result.txt","w")
        for t in notam_texts:
            print("\n\n========================\n\n")
            print(t.text)
            file.write(t.text)

        file.close()

    # def test_case_1(self):
    #     """Find and click top-left logo button"""
    #     try:
    #         self.driver.get('https://www.oursky.com/')
    #         el = self.driver.find_element_by_class_name('header__logo')
    #         el.click()
    #     except NoSuchElementException as ex:
    #         self.fail(ex.msg)

    # def test_case_2(self):
    #     """Find and click top-right Start your project button"""
    #     try:
    #         self.driver.get('https://www.oursky.com/')
    #         el = self.driver.find_element_by_class_name("header__cta")
    #         el.click()
    #     except NoSuchElementException as ex:
    #         self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
