class Team:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.schedule = None

    def create_schedule(self, schedule):
        self.schedule = schedule
