
def test_add_project(app, data_project):
    project = data_project
    app.session.ensure_login("webadmin")
    old_projects = app.project.get_project_list()
    app.project.add(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=lambda proj: proj.name.lower().replace(' ', '')) == new_projects

