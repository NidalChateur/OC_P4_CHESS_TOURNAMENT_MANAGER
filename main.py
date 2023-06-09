""" main : run the chess tournament manager"""

from os import path

from src.models.common import folders_check
from src.models.player import Players
from src.models.tournament import Tournaments
from src.controllers.main import MainController


""" create 6 fake players for the demo """

Players.reboot()


""" create 2 fakes tournaments for the demo"""

Tournaments.reboot()


def main():
    if path.exists("./src/"):
        MainController().run()
    else:
        print("The 'src' folder is missing !")


if __name__ == "__main__":
    folders_check()
    main()
