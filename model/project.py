class Project:

    def __init__(self, name=None, status=None, enabled=None, view_status=None, description=None):
        self.name = name
        self.status = status
        self.enabled = enabled
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return "%s:%s" % (self.name, self.description)