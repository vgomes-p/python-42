# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/27 19:33:34 by vgomes-p          #+#    #+#              #
#    Updated: 2026/05/16 14:04:32 by vigomes-         ###   ########.fr        #
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
        print(f"{self.name}: {self.height:1f}cm, ", end='')
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
    0: {"name": "Rose", "height": 25, "age": 30, "grow_level": 0.86},
    1: {"name": "Sunflower", "height": 80, "age": 45, "grow_level": 0.9},
    2: {"name": "Cactus", "height": 15, "age": 120, "grow_level": 0.15},
    3: {"name": "Olive", "height": 150, "age": 365, "grow_level": 0.02},
    4: {"name": "Venus", "height": 9, "age": 1, "grow_level": 0.5},
    5: {"name": "whatever", "height": 0, "age": 1, "grow_level": 2.0},
}


def main():
    print("=== Day 1 ===")
    pl = list_of_plants[0]
    plants = Plant()
    plants.get_info(pl["name"], pl["height"], pl["age"], pl["grow_level"])
    plants.show()
    grow_progress = plants.grow(7)
    print("=== Day 7 ===")
    plants.show()
    print(f"Growth this week: +{grow_progress}cm")


if __name__ == "__main__":
    main()
