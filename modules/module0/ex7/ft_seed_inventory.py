# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 19:24:59 by vgomes-p          #+#    #+#              #
#    Updated: 2026/05/15 13:27:00 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_seed_inventory(seed: str, quant: int, pac_type: str) -> None:
    if pac_type.lower() == "packets":
        print(f"{seed.capitalize()} seeds: {quant} packets available")
    if pac_type.lower() == "grams":
        print(f"{seed.capitalize()} seeds: {quant} grams total")
    if pac_type.lower() == "area":
        print(f"{seed.capitalize()} seeds: cover {quant} square meter")
