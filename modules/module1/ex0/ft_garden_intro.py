# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 16:06:14 by vgomes-p          #+#    #+#              #
#    Updated: 2026/05/15 14:35:15 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_my_garden(name: str, height: float, age: int) -> None:
    print("Plant:", name)
    print(f"Height: {height}cm")
    print("Age:", age, "days" if age > 1 else "day")


def main():
    print("=== Welcome to My Garden ===")
    ft_my_garden("Rose", 25, 30)
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
