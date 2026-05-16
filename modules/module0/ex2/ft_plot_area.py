# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/15 13:09:29 by vigomes-          #+#    #+#              #
#    Updated: 2026/05/16 14:10:03 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> str:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))

    print(f"Plot area: {length * width}")
