from src import basic
from src.league import League
from src.team import Team

if __name__ == '__main__':
    # Create Teams in League
    bears = Team("Bears", "Chicago")
    browns = Team("Browns", "Cleveland")
    bengals = Team("Bengals", "Cincinnati")
    dolphins = Team("Dolphins", "Miami")

    # Set Schedules
    bears.create_schedule([browns, bengals, dolphins])
    browns.create_schedule([bears, dolphins, bengals])
    bengals.create_schedule([dolphins, bears, browns])
    dolphins.create_schedule([bengals, browns, bears])

    # Initialize League
    nfl = League([bears, browns, bengals, dolphins])

    # Print Week 1 Match-ups
    for team in nfl.teams:
        print("\n" + team.location + " " + team.name + " Schedule:")
        for opponent in team.schedule:
            print(opponent.location + " " + opponent.name)
