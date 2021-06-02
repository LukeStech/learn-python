from src.main.league import League
from src.main.team import Team


def problem_1():
    # Create Teams in League
    bears = Team("Bears", "Chicago")
    browns = Team("Browns", "Cleveland")
    bengals = Team("Bengals", "Cincinnati")
    dolphins = Team("Dolphins", "Miami")

    # TODO: Add New NFL Teams
    jets = Team("Jets", "New York")
    jaguars = Team("Jaguars", "Jacksonville")
    seahawks = Team("Seahawks", "Seattle")
    packers = Team("Packers", "Green Bay")

    # Set Schedules
    bears.create_schedule([browns, bengals, dolphins])
    browns.create_schedule([bears, dolphins, bengals])
    bengals.create_schedule([dolphins, bears, browns])
    dolphins.create_schedule([bengals, browns, bears])

    # TODO: Set New Team's Schedule
    jets.create_schedule([jaguars, seahawks, packers])
    jaguars.create_schedule([jets, packers, seahawks])
    seahawks.create_schedule([packers, jets, jaguars])
    packers.create_schedule([seahawks, jaguars, jets])

    # Initialize League
    nfl = League([bears, browns, bengals, dolphins, jets, jaguars, seahawks, packers])

    # We will learn about lambda later. For now know that this sorts the teams by name (A-Z)
    nfl.teams.sort(key=lambda x: x.name, reverse=False)

    # returns the new list of nfl teams
    return nfl


def problem_2():
    # Use the results from problem 1
    nfl = problem_1()

    # TODO: return just the Bengals schedule
    for team in nfl.teams:
        if team.name == "Bengals":
            return team.schedule
