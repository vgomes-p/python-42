# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/15 13:21:32 by vigomes-          #+#    #+#              #
#    Updated: 2026/05/15 13:21:58 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    entry = int(input("Days until harvest: "))
    i = 0
    while i <= entry:
        print("Day", i)
        i += 1
    print("Harvest time!")
