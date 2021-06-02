from src.main.league import League
from src.main.team import Team


def problem_1():
    # Create Teams in League
    bears = Team("Bears", "Chicago")
    browns = Team("Browns", "Cleveland")
    bengals = Team("Bengals", "Cincinnati")
    dolphins = Team("Dolphins", "Miami")

    # TODO: (1) Add New NFL Teams

    # Set Schedules
    bears.create_schedule([browns, bengals, dolphins])
    browns.create_schedule([bears, dolphins, bengals])
    bengals.create_schedule([dolphins, bears, browns])
    dolphins.create_schedule([bengals, browns, bears])

    # TODO: (2) Set New Team's Schedule

    # Initialize League
    nfl = League([bears, browns, bengals, dolphins])

    # We will learn about lambda later. For now know that this sorts the teams by name (A-Z)
    nfl.teams.sort(key=lambda x: x.name, reverse=False)

    return nfl


def problem_2():
    # Use the results from problem 1
    nfl = problem_1()

    # TODO: (3) return just the Bengals schedule
    # for team in nfl.teams:
    # some code here to filter the teams
    # return a list containing the teams in the bengals schedule
