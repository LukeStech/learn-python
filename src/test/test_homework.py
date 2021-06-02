from unittest import TestCase
from src.main.homework import *


# DO NOT MODIFY
class Test(TestCase):
    def test_1(self):
        result = problem_1()

        # PRINT THE RESULTS
        for team in result.teams:
            print("\n" + team.location + " " + team.name + " Schedule:")
            for opponent in team.schedule:
                print(opponent.location + " " + opponent.name)

        self.assertTrue(len(result.teams) == 8)
        self.assertEqual(result.teams[4].name, "Jaguars")
        self.assertEqual(result.teams[4].schedule[1].name, "Packers")
        print("\n###########################\nNICE JOB! PROBLEM 1 PASSED!!\n")

    def test_2(self):
        result = problem_2()

        week = 1
        for team in result:
            print("Week " + str(week) + ": " + str(team.name))
            week = week + 1

        self.assertEqual(result[0].name, "Dolphins")
        self.assertEqual(result[1].name, "Bears")
        self.assertEqual(result[2].name, "Browns")
        print("\n###########################\nNICE JOB! PROBLEM 2 PASSED!!")
        print("You can now push your code to GitHub")
