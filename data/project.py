from model.project import Project
from generators.random_data import RandomData


generator = RandomData()

testdata = [
    Project(name=generator.random_string("Project", 10), description=generator.random_string("Decription", 20)),
    Project(name=generator.random_string("Project", 10), description=generator.random_string("Decription", 20))
]