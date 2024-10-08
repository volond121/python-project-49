#!/usr/bin/env python3

from brain_games.games.gcd import get_round_params_gcd
import brain_games.game_engine as game_engine


def main():
    game_engine.play_game(get_round_params_gcd, "Find the"
                          " greatest common divisor of given numbers.")


if __name__ == '__main__':
    main()
