from model.project import Project
import random


def test_del_project(app):
    app.session.ensure_login("webadmin")
    if len(app.project.get_project_list()) == 0:
        app.project.add(Project(name="Test1", description="Descr1"))
    old_projects = app.project.get_project_list()
    project_to_delete = random.choice(old_projects)
    app.project.delete(project_to_delete)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project_to_delete)
    assert sorted(old_projects, key=lambda proj: proj.name.lower().replace(' ', '')) == new_projects