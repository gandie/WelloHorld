from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.binary_location = "node_modules/.bin/electron"
opts.add_argument("app=/home/lars/Dev/Node/WelloHorld/")

driver = webdriver.Remote(command_executor="http://localhost:9515", options=opts)

elem = driver.find_elements_by_id("el_eier")[0]

assert elem.text == "Eier!"

driver.close()
print("Done")
