#!/usr/bin/env python3

from brain_games.games.even import get_round_params_even
import brain_games.game_engine as game_engine


def main():
    game_engine.play_game(
        get_round_params_even, 'Answer "yes" if the number is even, '
        'otherwise answer "no".')


if __name__ == '__main__':
    main()
