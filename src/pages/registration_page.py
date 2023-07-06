from selene.support.shared import browser

from common_methods import delete_ads


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")
        delete_ads()
        return self
