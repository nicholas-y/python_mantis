class SessionHelper:

    def __init__(self, app):
        self.app = app

    def do_login(self, usertype):
        wd = self.app.wd
        username = self.app.get_jsontarget()[usertype]["username"]
        password = self.app.get_jsontarget()[usertype]["password"]
        self.app.open_login_page()
        # enter username
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        # enter password
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        # click login button
        wd.find_element_by_css_selector("input[type='submit']").click()

    def do_logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.do_logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout"))

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def ensure_login(self, usertype):
        username = self.app.get_jsontarget()[usertype]["username"]
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.do_logout()
        self.do_login(usertype)