from main_menu_state import MainMenuState
from game_menu_state import GameMenuState
from game_state import GameState
from upgrade_menu_state import UpgradeMenuState

from state_manager import StateManager


def run():
    states = {
        "MAIN_MENU": MainMenuState(),
        "GAME_MENU": GameMenuState(),
        "UPGRADE_MENU": UpgradeMenuState(),
        "GAME": GameState(),
    }

    game_manager = StateManager(states, "MAIN_MENU")
    game_manager.run()


if __name__ == "__main__":
    run()
