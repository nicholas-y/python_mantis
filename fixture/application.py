from selenium import webdriver
from fixture.session import SessionHelper


target = None


class Application:

    def __init__(self, browser, base_url, jsontarget):
        global target
        target = jsontarget
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False},
                                        firefox_binary="c:/Program Files/Mozilla Firefox/firefox.exe")
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.base_url = base_url

    def get_jsontarget(self):
        global target
        return target

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_login_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_css_selector("input[type=\"submit\"]")) > 0):
            wd.get(self.base_url)

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()

