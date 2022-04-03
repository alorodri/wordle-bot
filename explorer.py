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
        self.__driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    def navigate(self):
        self.__driver.get('https://wordle.danielfrg.com/')
        self.__body = self.__driver.find_element_by_tag_name('body')
        self.__body.send_keys(Keys.ESCAPE)

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

        cards_row = self.__driver.find_element_by_xpath(f'//div[@class="grid grid-cols-5 gap-[5px] w-full "][{n}]')
        cards = cards_row.find_elements_by_xpath('div/div/div[2]/div')
        colors = []
        for card in cards:
            card_class = card.get_attribute('class')
            bg = card_class.split(' ')[-1]
            if bg == 'bg-correct':
                colors.append(Constants.GREEN)
            elif bg == 'bg-present':
                colors.append(Constants.YELLOW)
            elif bg == 'bg-absent':
                colors.append(Constants.GRAY)
                
        return colors
