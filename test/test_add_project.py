from model.project import Project


def test_add_project(app, data_project):
    project = data_project
    app.session.ensure_login("webadmin")
    app.project.add(project)
