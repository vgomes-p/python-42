# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_score_analytics.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:36 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:37 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys as s


class ConversionError(Exception):
    def __init__(self, message: str = "Unknown convertion error"):
        super().__init__(message)


def ft_score_analytics() -> None:
    usage_text = "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
    print("=== Player Score Analytics ===")
    args = s.argv[1:]
    scores = [int(score) for score in args]
    total_players = len(scores)
    if total_players == 0:
        print("No parameter passed.", usage_text)
        return
    invalids = False
    # negative_score = False
    total_score = 0
    until = 1
    for arg in scores:
        # if arg < 0:
        #     negative_score = True
        #     break
        try:
            total_score = sum(scores)
        except Exception:
            invalids = True
            print(f"Invalid parameter: '{arg}'")
        finally:
            until += 1
    if invalids:
        if total_score == 0:
            print("No scores provided.", usage_text)
        return
    # if total_score < 0 or negative_score:
    #     print("Negative scores are not valid.", usage_text)
    #     return
    biggest = max(scores)
    lowest = min(scores)
    avarage = total_score / total_players
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Avarage score: {avarage}")
    print(f"High score: {biggest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {biggest - lowest}")


def main() -> None:
    ft_score_analytics()


if __name__ == "__main__":
    main()
