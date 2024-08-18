#!/usr/bin/env python3

from brain_games.games.progression import get_res_progression
import brain_games.game_engine as game_engine


def main():
    game_engine.play_game(get_res_progression, "What number"
                          " is missing in the progression?")


if __name__ == '__main__':
    main()
