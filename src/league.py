class League:
    def __init__(self, teams):
        self.teams = teams

    def add_team(self, team):
        self.teams.append(team)

    def remove_team(self, team):
        self.teams.remove(team)

    def view_teams(self):
        for team in self.teams:
            print(team)
