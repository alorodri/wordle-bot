from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager

from constants import Constants

class Explorer():

    __driver = None
    __body = None

    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--lang=es")
        self.__driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    def __find_cookies_button(self):
        return self.__body.find_element_by_xpath('//button[@aria-label="Close"]')

    def navigate(self):
        self.__driver.get('https://wordle.danielfrg.com/')
        self.__body = self.__driver.find_element_by_tag_name('body')
        attempts = 0
        while attempts < 5 and self.__find_cookies_button() is None:
            time.sleep(0.5)
            attempts += 1
        if self.__find_cookies_button() is None:
            self.__body.send_keys(Keys.ESCAPE)
        else:
            self.__find_cookies_button().click()

    def attempt(self, word, n):
        word = word.lower()
        for letter in word:
            if letter == 'ñ':
                self.__body.find_element_by_xpath('//button[@aria-label="ñ"]').click()
            else:
                self.__body.send_keys(letter)
            time.sleep(0.3)

        self.__body.send_keys(Keys.ENTER)
        time.sleep(1.5)

        cards_row = self.__driver.find_element_by_xpath(f'//div[@class=" css-ceoe56"][{n}]')
        cards = cards_row.find_elements_by_xpath('div/div/div[2]/div')
        colors = []
        for card in cards:
            card_class = card.get_attribute('class')
            if card_class == 'css-1jtxyvl':
                colors.append(Constants.GREEN)
            elif card_class == 'css-140kyip':
                colors.append(Constants.YELLOW)
            elif card_class == 'css-1hwd5vh':
                colors.append(Constants.GRAY)
                
        return colors
