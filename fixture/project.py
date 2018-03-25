from model.project import Project

class ProjectHelper():

    project_cache = None

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
        self.project_cache = None

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

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cache = []
            row_list = wd.find_elements_by_xpath("((//table[@class='width100'])[2])//tr")
            for element in row_list[2:]:
                cells = element.find_elements_by_css_selector("td")
                name = cells[0].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)