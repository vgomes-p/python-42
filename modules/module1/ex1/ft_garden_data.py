# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 16:26:15 by vgomes-p          #+#    #+#              #
#    Updated: 2026/05/15 14:27:53 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:1f}cm, ", end='')
        print(self.age if self.age >= 1 else "",
              ("days old" if self.age > 1 else "day old")
              if self.age >= 1 else "just planted")


list_of_plants = {
    0: {"name": "Rose", "height": 25, "age": 30},
    1: {"name": "Sunflower", "height": 80, "age": 45},
    2: {"name": "Cactus", "height": 15, "age": 120},
    3: {"name": "Olive", "height": 150, "age": 365},
    4: {"name": "Venus", "height": 9, "age": 1},
    5: {"name": "whatever", "height": 0, "age": 0},
}


def main():
    print("=== Garden Plant Registry ===")
    for p in list_of_plants:
        plant = list_of_plants[p]
        plants = Plant(plant["name"], plant["height"], plant["age"])
        plants.show()


if __name__ == "__main__":
    main()
