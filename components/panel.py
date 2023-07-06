import time

from selene import browser, by

from common_methods import delete_ads
from src.pages.text_box_page import TextBoxPage


class Panel:
    def __init__(self):
        self.container = browser.element(by.css(".left-pannel"))

    def open_text_box(self):
        self.container.element(by.text("Elements")).s("..").click()
        self.container.element(by.text("Text Box")).click()
        return TextBoxPage()
