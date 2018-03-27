import json


def test_add_project(app, data_project):
    project = data_project
    old_projects = app.soap.get_project_list(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    app.session.ensure_login("webadmin")
    app.project.add(project)
    new_projects = app.soap.get_project_list(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=lambda proj: proj.name.lower().replace(' ', '')) == new_projects

