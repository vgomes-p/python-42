# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_alchemist.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:46:00 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:46:01 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random as rdm


init_players = ["Liam", "sophia", "Noah", "olivia", "Ethan", "ava",
                "mason", "Isabella", "Lucas", "mia"]


def make_cap(players: list[str]) -> list[str]:
    return [name.capitalize() for name in players]


def get_cap(players: list[str]) -> list[str]:
    return [name for name in players if name == name.capitalize()]


def gen_score() -> int:
    return rdm.randint(0, 1000)


def mk_scores(players: list[str]) -> dict[str, int]:
    return {name: gen_score() for name in players}


def get_average(scores: dict[str, int]) -> float:
    i = 0
    total = 0
    for key in scores:
        total += scores[key]
        i += 1
    return total / i


def get_above_average(average: float,
                      scores: dict[str, int]) -> dict[str, int]:
    return {name: scores[name] for name in scores if scores[name] > average}


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {init_players}")
    players = make_cap(init_players)
    print(f"New list with all names capitalized: {players}")
    just_cap_players = get_cap(init_players)
    print(f"New list of capitalized names only: {just_cap_players}")
    scores = mk_scores(players)
    print(f"Score dict: {scores}")
    average = get_average(scores)
    print(f"Score average is {average}")
    above_average = get_above_average(average, scores)
    print(f"High scores: {above_average}")


if __name__ == "__main__":
    main()
