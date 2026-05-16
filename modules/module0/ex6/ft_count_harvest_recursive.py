# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 17:23:47 by vgomes-p          #+#    #+#              #
#    Updated: 2026/05/16 14:09:40 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_day(day: int, final_day: int) -> int:
    print(f"Day {day}")
    return final_day - 1


def ft_recursive(day: int, final: int):
    if day == final + 1:
        return 0
    print("Day ", day)
    ft_recursive(day + 1, final)


def ft_count_harvest_recursive():
    entry = int(input("Days until harvest: "))
    ft_recursive(1, entry)
    print("Harvest time!")
