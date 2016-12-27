from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

username = sys.argv[1]
password = sys.argv[2]

class Facebook:
    
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.birthdayPeople = []

    def login(self):
        self.browser.get("https://www.facebook.com/login")
        emailInpt = self.browser.find_element_by_id("email")
        emailInpt.send_keys(self.username)
        passInpt = self.browser.find_element_by_id("pass")
        passInpt.send_keys(self.password)
        passInpt.submit()

    def wishBirthday(self, person):
        name = person.text.split(" ")[0]
        name = str(name)
        area = person.find_element_by_css_selector("textarea")
        message = "Happy Birthday " + name + "! I hope you have a fantastic day!"
        area.send_keys(message)
        area.submit()

    def checkBirthdays(self):
        self.browser.get("https://www.facebook.com/birthdays")
        tableDay = self.browser.find_elements_by_xpath("//table")[0]
        birthdayPeople = tableDay.find_elements_by_css_selector(".clearfix")
        for person in birthdayPeople:
            self.wishBirthday(person)

    def run(self):
        self.login()
        self.checkBirthdays()



x = Facebook(username, password)
x.run()
