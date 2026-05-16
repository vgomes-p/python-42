# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/15 13:09:59 by vigomes-          #+#    #+#              #
#    Updated: 2026/05/15 13:10:01 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    entry = int(input("Enter plant age in days: "))
    if entry > 60:
        print("Plant is ready to harvest!")
        return 0
    print("Plant needs more time to grow.")


ft_plant_age()
