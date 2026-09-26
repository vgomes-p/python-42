# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:47 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:54 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random as rdm


achivements = [
    "Boss Slayer", "Collector Supreme", "Crafting Genius", "First Steps",
    "Hidden Path Finder", "Master Explorer", "Sharp Mind", "Speed Runner",
    "Strategist", "Survivor", "Treasure Hunter", "Untouchable", "World Savior"]


def get_player_achivements() -> set[str]:
    player_achivements: list[str] = []
    a_max = rdm.randint(4, 13)
    while len(player_achivements) < a_max:
        achivement = rdm.sample(achivements, 1)[0]
        if achivement in player_achivements:
            continue
        player_achivements += [achivement]
    return set(player_achivements)


def create_players(players_names: list[str]) -> dict[str, set[str]]:
    if not players_names:
        return {"None": set()}
    players = {}
    for player in players_names:
        players[player] = get_player_achivements()
    return players


def print_players_achivements(players: dict[str, set[str]]) -> None:
    print("PLAYERS ACHIVEMENTS:")
    for player in players:
        i = 1
        player_achivements = players[player]
        a_nbr = len(player_achivements)
        print(f"Player {player}: ", end="")
        for achieve in player_achivements:
            print(achieve, end=', ' if i < a_nbr else "")
            i += 1
        print(f" | total of {a_nbr} achivements.")
    print('\n')


def print_unique_achivements(players: dict[str, set[str]]) -> None:
    print("UNSHARED ACHIVEMENTS:")
    for player in players:
        others_union: set[str] = set()
        for others in players:
            if others == player:
                pass
            else:
                others_union = set.union(others_union, players[others])
        player_unique = []
        for achieve in players[player]:
            if achieve not in others_union:
                player_unique += [achieve]
        i = 1
        if len(player_unique) == 0:
            print(f"{player} has no unshared achivement!")
        else:
            print(f"Only {player} has: ", end='')
            for item in player_unique:
                print(item, end=', ' if i < len(player_unique) else ".\n")
                i += 1
    print('\n')


def print_common_achivements(players: dict[str, set[str]]) -> None:
    print("SHARED ACHIVEMENTS:")
    common: set[str] | None = None
    for achieve in players.values():
        if common is None:
            common = achieve
        else:
            common = common.intersection(achieve)
    if common is None or len(common) == 0:
        print("There is no common achivements!\n\n")
        return
    print("Common achivements: ", end='')
    i = 1
    for item in common:
        print(item, end=", " if i < len(common) else '.\n')
        i += 1
    print('\n')


def print_missing_achivements(players: dict[str, set[str]]) -> None:
    print("MISSING ACHIVEMENTS:")
    for player in players:
        achieves = players[player]
        all = set(achivements)
        missing = set.difference(all, achieves)
        i = 1
        if len(missing) == 0:
            print(f"{player} is missing no achivements")
            continue
        print(f"{player} is missing: ", end='')
        for item in missing:
            print(item, end=", " if i < len(missing) else '.\n')
            i += 1


def main() -> None:
    print("=== Achievement Tracker System ===")
    players_names = ["Alice", "Bob", "Charlie", "Dylan"]
    players = create_players(players_names)
    print_players_achivements(players)
    print_common_achivements(players)
    print_unique_achivements(players)
    print_missing_achivements(players)


if __name__ == "__main__":
    main()
