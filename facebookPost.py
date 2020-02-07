from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

class FacebookPost():
    def __init__(self):
        #Use your Firefox Profile to prevent everytime login
        self.profile = webdriver.FirefoxProfile('')
        self.options = Options()
        self.options.add_argument('--headless')
        self.driver = webdriver.Firefox(self.profile, options=self.options)
    
    def upload(self):
        URL = ''
        self.driver.get(URL)
        print('Facebook Page Opened!\n')
        self.driver.find_element_by_xpath("//*[starts-with(@data-testid, 'photo-video-button')]").click()
        print('Uploading Picture!\n')
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[starts-with(@data-testid, 'media-attachment-add-photo')]").send_keys('')
        print('Picture Uploaded Successfully!\n')
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[starts-with(@data-testid, 'status-attachment-mentions-input')]").send_keys('Automation of Facebook Post without GRAPHAPI Token')
        print('Writing Caption!\n')
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[starts-with(@data-testid, 'react-composer-post-button')]").click()
        print('Post have been successfully posted!')

bot = FacebookPost()
bot.upload()