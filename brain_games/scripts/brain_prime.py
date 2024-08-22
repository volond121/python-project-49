#!/usr/bin/env python3

from brain_games.games.prime import get_round_params_prime
import brain_games.game_engine as game_engine


def main():
    game_engine.play_game(get_round_params_prime, 'Answer "yes" if given number'
                          ' is prime. Otherwise answer "no".')


if __name__ == '__main__':
    main()
