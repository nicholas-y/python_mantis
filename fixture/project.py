from model.project import Project

class ProjectHelper():

    def __init__(self, app):
        self.app = app

    def add(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form_field("name", project.name)
        self.fill_project_form_field("description", project.description)
        wd.find_element_by_css_selector("input.button").click()
        wd.find_element_by_link_text("Proceed").click()

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)