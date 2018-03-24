

def test_login(app):
    app.session.do_login("webadmin")
    assert app.session.is_logged_in_as("administrator")