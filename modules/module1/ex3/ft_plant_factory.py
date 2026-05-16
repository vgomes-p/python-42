# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/28 18:33:50 by vgomes-p          #+#    #+#              #
#    Updated: 2026/05/16 14:04:26 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str = "", heigh: float = 0.0,
                 plant_age: int = 0, grow_level: float = 0.0):
        self.name = name
        self.height = heigh
        self.plant_age = plant_age
        self.grow_level = grow_level

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height:.1f}cm, ", end='')
        print(self.plant_age, ("days old" if self.plant_age > 1 else "day old")
              if self.plant_age >= 0 else "not planted")

    def get_info(self, name: str, height: float,
                 plant_age: int, grow_level: float) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.grow_level = grow_level

    def grow(self, days: int) -> float:
        grew = 0
        for _ in range(0, days):
            self.height += self.grow_level
            grew += self.grow_level
            self.age()
        return (grew)

    def age(self) -> None:
        self.plant_age += 1


list_of_plants = {
    0: {"name": "Rose", "height": 25, "age": 30, "grpd": 0.86},
    1: {"name": "Sunflower", "height": 80, "age": 45, "grpd": 0.9},
    2: {"name": "Cactus", "height": 15, "age": 120, "grpd": 0.15},
    3: {"name": "Olive", "height": 150, "age": 365, "grpd": 0.02},
    4: {"name": "Venus", "height": 9, "age": 1, "grpd": 0.5},
    5: {"name": "whatever", "height": 0, "age": 1, "grpd": 2.0},
}


def main():
    plants = Plant()
    for p in list_of_plants:
        plant = list_of_plants[p]
        plants.get_info(plant["name"], plant["height"],
                        plant["age"], plant["grpd"])
        plants.show()


if __name__ == "__main__":
    main()
