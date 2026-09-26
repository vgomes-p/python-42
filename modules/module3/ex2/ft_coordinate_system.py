# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:42 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:43 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math as m


class GetDataError(Exception):
    def __init__(self, message: str = "Unknown error"):
        super().__init__(message)


def get_player_pos() -> tuple[float, float, float]:
    entry = input("Enter new coordinates as floats in format 'x,y,z': ")
    splited = entry.split(',')
    if len(splited) < 3:
        raise GetDataError("Less than 3 coordinate values passed.")
    elif len(splited) > 3:
        raise GetDataError("More than 3 coordinate values passed.")
    try:
        x = float(str(splited[0]).strip())
        y = float(str(splited[1]).strip())
        z = float(str(splited[2]).strip())
    except Exception as e:
        raise GetDataError(f"Error: {e}")
    return x, y, z


def main() -> None:
    first_entry = False
    print("Get a first set of coordinates")
    while not first_entry:
        try:
            x1, y1, z1 = get_player_pos()
            first_entry = True
        except GetDataError:
            print("Invalid syntax")
            continue
    print(f"Got a first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_1 = m.sqrt(((x1)**2) + ((y1)**2) + ((z1)**2))
    print(f"Distance to center: {distance_1:.4f}")

    print("Get a second set of coordinates")
    second_entry = False
    while not second_entry:
        try:
            x2, y2, z2 = get_player_pos()
            second_entry = True
        except GetDataError as e:
            print(e)
            continue
    distance = m.sqrt(((x1 - x2)**2) + ((y1 - y2)**2) + ((z1 - z2)**2))
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    main()
