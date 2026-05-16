# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/15 13:10:07 by vigomes-          #+#    #+#              #
#    Updated: 2026/05/15 13:10:09 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    entry = int(input("Days since last watering: "))
    if entry > 2:
        print("Water the plant!")
        return 0
    print("Plant is fine.")


ft_water_reminder()
