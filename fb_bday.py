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
        name = person.find_element_by_css_selector("a")
        name = str(name.text).split(" ")[0]
        area = person.find_element_by_css_selector("textarea")
        message = "Happy Birthday " + name + "! I hope you have a fantastic day!"
        area.send_keys(message)
        area.submit()
        print(name)

    def checkBirthdays(self):
        self.browser.get("https://www.facebook.com/events/birthdays/")
        tableDay = self.browser.find_element_by_css_selector("#birthdays_content ._tzl")
        birthdayPeople = tableDay.find_elements_by_css_selector("._tzm")
        for person in birthdayPeople:
            try:
                self.wishBirthday(person)
            except:
                print("skipping")

    def run(self):
        self.login()
        self.checkBirthdays()
        self.browser.close()


x = Facebook(username, password)
x.run()
