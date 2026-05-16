# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/15 13:09:47 by vigomes-          #+#    #+#              #
#    Updated: 2026/05/15 13:20:53 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    d1 = int(input("Day 1 harvest: "))
    d2 = int(input("Day 2 harvest: "))
    d3 = int(input("Day 3 harvest: "))

    final = d1 + d2 + d3
    print(f"Total harvest: {final}")
