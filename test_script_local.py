"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os

# python -m unittest test_script_local.TestTemplate.test_case_1
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
        # import ipdb
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

    def test_case_1(self):
        """Find and click top-left logo button"""
        assert 1 == 1
        import ipdb
        # ipdb.sset_trace()

        SAVE_FILE = "fake_prev_close.txt"
        ##make a fake svaed prev_close
        file = open(SAVE_FILE,"w")
        file.write("0.35")
        file.close()

        ## fetch prev_closed_data

        OTC_QUOTES_URL = os.environ.get("OTC_QUOTES_URL")
        self.driver.get(OTC_QUOTES_URL)

        from selenium.webdriver.common.by import By
        driver = self.driver

        #sibling html element of label "prev close" has actual number
        new_prev_close = driver.find_elements(By.XPATH,
                  '//label[contains(text(),"Prev Close")]/../p')[0]
        
        new_prev_close = new_prev_close.text

        ## get prev close
        file = open(SAVE_FILE,"r")
        old_prev_close = file.read()
        file.close()

        print("=== prev close from file: {}".format(old_prev_close))
        print("=== new prev close: {}".format(new_prev_close))

        
        ipdb.sset_trace()

        print('done')
        
       


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
