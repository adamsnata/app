from src.application import app


def test_text_box():
    app.registration_page.open()

    (
        app.panel.open_text_box()
        .fill_form(
            full_name="full_name",
            email="email@hotmail.com",
            current_address="current_address",
            permanent_address="permanent_address",
        )
        .should_have_submitted()
    )
