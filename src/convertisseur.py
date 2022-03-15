from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep


def Convertir(lien):
    chromeOptions = Options()
    chromeOptions.headless = True
    browser  = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
    browser.get("https://notube.io/fr/youtube-app-v8")
    sleep(1)
    browser.find_element_by_xpath('//*[@id="keyword"]').send_keys(lien)
    sleep(1)
    browser.find_element_by_xpath('//*[@id="submit-button"]').click()
    sleep(3)
    browser.switch_to.window(browser.window_handles[0])
    sleep(2)
    browser.find_element_by_xpath('//*[@id="downloadButton"]').click()
    sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    sleep(20)

if __name__ == "__main__":
    lien = "https://www.youtube.com/watch?v=LDU_Txk06tM"
    Convertir(lien)