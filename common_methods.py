from selene import browser, have, command


def delete_ads():
    # workaround how to remove appearing ads
    if (
        browser.all("[id^=google_ads][id$=container__]")
        .with_(timeout=browser.config.timeout * 2)
        .wait.until(have.size_greater_than_or_equal(3))
    ):
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)
