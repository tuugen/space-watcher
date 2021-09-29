from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome()
#driver = webdriver.Chrome(port=9515)

# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/private/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_driver_binary = "/Users/cody/bin/chromedriver"
# driver = webdriver.Chrome(chrome_driver_binary, options=options)


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
    command_executor='http://0.0.0.0:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://www.python.org")
assert "Python" in driver.title
print(driver.title)
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()