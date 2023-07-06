from selene import browser, have, command


class TextBoxPage:
    def __init__(self):
        self.output_container = browser.element("#output")
        self.output_data = self.output_container.all("p")

    def fill_form(self, full_name, email, current_address, permanent_address):
        browser.element("#userName").type(full_name)
        browser.element("#userEmail").type(email)
        browser.element("#currentAddress").type(current_address)
        browser.element("#permanentAddress").type(permanent_address)
        browser.element("#submit").perform(command.js.click)
        return self

    def should_have_submitted(self):
        expected_result = [
            "Name:full_name",
            "Email:email@hotmail.com",
            "Current Address :current_address",
            "Permananet Address :permanent_address",
        ]
        self.output_container.perform(command.js.scroll_into_view)
        self.output_data.should(have.texts(expected_result))
        return self
