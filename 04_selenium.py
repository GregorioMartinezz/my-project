from selenium import webdriver  # hay que haber ejecutado `pip install selenium`

driver = webdriver.Chrome()
driver.get("http://www.python.org")
print(driver.title)
assert "Python" in driver.title