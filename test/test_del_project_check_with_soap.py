from model.project import Project
import random


def test_del_project_check_with_soap(app):
    app.session.ensure_login("webadmin")
    if len(app.soap.get_project_list(app.config["webadmin"]["username"], app.config["webadmin"]["password"])) == 0:
        app.project.add(Project(name="Test1", description="Descr1"))
    old_projects = app.soap.get_project_list(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    project_to_delete = random.choice(old_projects)
    app.project.delete(project_to_delete)
    new_projects = app.soap.get_project_list(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project_to_delete)
    assert sorted(old_projects, key=lambda proj: proj.name.lower().replace(' ', '')) == new_projects