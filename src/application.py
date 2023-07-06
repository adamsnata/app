from components.panel import Panel
from src.pages.registration_page import RegistrationPage


class Application:
    def __init__(self):
        self.panel = Panel()
        self.registration_page = RegistrationPage()


app = Application()
