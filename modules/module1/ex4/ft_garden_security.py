# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/15 14:59:01 by vigomes-          #+#    #+#              #
#    Updated: 2026/05/15 17:01:30 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str = "", height: float = 0.0,
                 plant_age: int = 0, grow_level: float = 0.0):
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.grow_level = grow_level

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height:.1f}cm, ", end='')
        if self.plant_age > 0:
            print(self.plant_age,
                  ("days old" if self.plant_age > 1 else "day old"))
        else:
            print("just planted")

    def get_info(self, name: str, height: float,
                 plant_age: int, grow_level: float) -> None:
        self.name = name
        self.height = self.set_heigth(height, name)
        self.plant_age = self.set_age(plant_age, name)
        self.grow_level = grow_level
        pass

    def grow(self, days: int) -> float:
        grew = 0
        for _ in range(0, days):
            self.height += self.grow_level
            grew += self.grow_level
            self.age()
        return (grew)

    def age(self) -> None:
        self.plant_age += 1

    def set_heigth(self, heigth_to_set: float,
                   name: str, update: bool = False) -> float:
        if heigth_to_set < 0:
            print(f"{name}: Error, height can't be negative")
            print(f"{name}: Height" 'update'
                  if update else 'setting', "height rejected and",
                  'updated to' if update else 'setted as', '0.0')
            return 0
        else:
            print(f"{name}: Height", "updated" if update else "setted")
            return heigth_to_set

    def set_age(self, age_to_set: int, name: str, update: bool = False) -> int:
        if age_to_set < 0:
            print(f"{name}: Error, age can't be negative")
            print(f"{name}: Age" 'update'
                  if update else 'setting', "age rejected and",
                  'updated to' if update else 'setted as', '0')
            return 0
        else:
            print(f"{name}: Age", "updated" if update else "setted")
            return age_to_set

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.plant_age


list_of_plants = {
    0: {"name": "Rose", "height": 25, "age": 30, "grpd": 0.86},
    1: {"name": "Sunflower", "height": 80, "age": 45, "grpd": 0.9},
    2: {"name": "Cactus", "height": -15, "age": 120, "grpd": 0.15},
    3: {"name": "Olive", "height": 150, "age": -365, "grpd": 0.02},
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
        plants.grow(7)
        height = plants.get_height()
        age = plants.get_age()
        print(f"Current state: {plant['name']}: {height:.1f}cm, {age} days old")
        print("\n-----------------------------------------------\n")


if __name__ == "__main__":
    main()
