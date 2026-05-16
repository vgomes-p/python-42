# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/16 08:59:25 by vigomes-          #+#    #+#              #
#    Updated: 2026/05/16 14:01:12 by vigomes-         ###   ########.fr        #
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
        print(f"{self.name}: {self.height:.1f}cm, ", end='')
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


class Flower(Plant):
    def __init__(self, name: str = "", height: float = 0.0,
                 plant_age: int = 0, grow_level: float = 0.0,
                 color: str = "", blooming: bool = False):
        super().__init__(name, height, plant_age, grow_level)
        self.color = color
        self.blooming = blooming

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        print(f" {self.name} has not bloomed yet" if not self.blooming
              else f" {self.name} is blooming beautifully!")

    def get_info(self, name: str, height: float, plant_age: int,
                 grow_level: float, color: str, blooming: bool = False) -> None:
        super().get_info(name, height, plant_age, grow_level)
        self.color = color
        self.blooming = blooming


class Tree(Plant):
    def __init__(self, name: str = "", height: float = 0.0,
                 plant_age: int = 0, grow_level: float = 0.0,
                 trunk_diameter: float = 0.0, prod_shade: bool = False):
        super().__init__(name, height, plant_age, grow_level)
        self.trunk_diameter = trunk_diameter
        self.prod_shade = prod_shade

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        self.prod_shade = True
        print(f"Tree {self.name} now produce a shade of",
              f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}")

    def get_info(self, name: str, height: float, plant_age: int,
                 grow_level: float, trunk_diameter: float,
                 prod_shade: bool = False) -> None:
        super().get_info(name, height, plant_age, grow_level)
        self.trunk_diameter = trunk_diameter
        self.prod_shade = prod_shade


class Vegetables(Plant):
    def __init__(self, name: str = "", height: float = 0.0, plant_age: int = 0,
                 grow_level: float = 0.0, harvest_season: str = "June",
                 nutritional_grow: float = 0.0, nutritional_value: int = 0):
        super().__init__(name, height, plant_age, grow_level)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.nutritional_grow = nutritional_grow

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def get_info(self, name: str, height: float, plant_age: int,
                 grow_level: float, harvest_season: str,
                 nutritional_grow: float, nutritional_value: int) -> None:
        super().get_info(name, height, plant_age, grow_level)
        self.harvest_season = harvest_season
        self.nutritional_grow = nutritional_grow
        self.nutritional_value = nutritional_value

    def make_nutri(self, days) -> None:
        for _ in range(0, days):
            self.nutritional_value += self.nutritional_grow

    def grow(self, days: int) -> float:
        ret = super().grow(days)
        print(f"[make {self.name} grow and age for {days}",
              "days]" if days > 1 else "day]")
        self.make_nutri(days)
        return ret


list_of_plants = {
    0: {"name": "Rose", "height": 25.0, "age": 30, "grpd": 0.86},
}

list_of_flowers = {
    0: {"name": "Rose", "height": 25.0, "age": 30,
        "grpd": 0.86, "color": "White"}
}

list_of_tree = {
    0: {"name": "Oak", "height": 200.0, "age": 1095,
        "grpd": 10.0, "trunk_diameter": 5.0}
}

list_of_veg = {
    0: {"name": "Tomato", "height": 5.0, "age": 10,
        "grpd": 2.1, "season": "April", "nutri": 1}
}


def main():
    flower = Flower()
    fl = list_of_flowers[0]
    flower.get_info(name=fl["name"], height=fl["height"], plant_age=fl["age"],
                    grow_level=fl["grpd"], color=fl["color"])
    flower.show()
    flower.bloom()
    flower.show()
    print("\n-----------------------------------------------\n")
    tree = Tree()
    tr = list_of_tree[0]
    tree.get_info(name=tr["name"], height=tr["height"], plant_age=tr["age"],
                  grow_level=tr["grpd"], trunk_diameter=tr["trunk_diameter"])
    tree.show()
    tree.produce_shade()
    print("\n-----------------------------------------------\n")
    veg = Vegetables()
    vg = list_of_veg[0]
    veg.get_info(name=vg["name"], height=vg["height"], plant_age=vg["age"],
                 grow_level=vg["grpd"], harvest_season=vg["season"],
                 nutritional_grow=vg["nutri"], nutritional_value=0)
    veg.show()
    veg.grow(20)
    veg.show()
    print("\n-----------------------------------------------\n")


if __name__ == "__main__":
    main()
