# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:25 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:26 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


# def ft_isalnum(target: str) -> bool:
#     an = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
#     for char in target:
#         if char not in an:
#             return False
#     return True


# def ft_isnumeric(target: str) -> bool:
#     an = "1234567890"
#     for char in target:
#         if char not in an:
#             return False
#     return True


# def validate_garden(garden_name: str) -> bool:
#     if ft_isalnum(garden_name):
#         raise GardenError("Garden name can only contain")
#     elif ft_isnumeric(garden_name):
#         raise GardenError("Garden name cannot be integer")
#     else:
#         return True


# def validate_plant(plant_name: str, plant_age: int) -> bool:
#     if ft_isalnum(plant_name):
#         raise PlantError(f"'{plant_name}' is invalid!" +
#                          " Plant name can only be alphabetic")
#     elif ft_isnumeric(plant_name):
#         raise PlantError(f"'{plant_name}' is invalid!" +
#                          " Plant name cannot be integer")
#     elif plant_age < 0:
#         raise PlantError(f"Age for plant {plant_name} is invalid!" +
#                          " Plant age cannot be negative")
#     else:
#         return True


# def validate_watering(last_time_watered: int) -> bool:
#     if last_time_watered < 0:
#         raise WaterError("Last time watered cannot be negative!")
#     if last_time_watered > 3:
#         return True
#     else:
#         return False


def test_personal_errors_type() -> None:
    to_test = [0, 1, 2]
    for i in to_test:
        print(f"test {i}...")
        try:
            if i == 0:
                raise GardenError("Garden error can be used for " +
                                  "garden creation errors")
            if i == 1:
                raise PlantError("Plant error can be used for " +
                                 "plant creation errors")
            if i == 2:
                raise WaterError("Water error can be used for " +
                                 "watering plant errors")
        except Exception as e:
            error_type = e.__class__.__name__
            print(f">> Caught {error_type}: {e}")


# def test_personal_errors_type_pp() -> None:
#     to_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     tests = {
#         0: {"function": "validate_garden", "params": ["My Litte garden"]},
#         1: {"function": "validate_garden", "params": ["4 b1g gard3n"]},
#         2: {"function": "validate_garden", "params": ["42"]},
#         3: {"function": "validate_plant", "params": ["Cactus", 42]},
#         4: {"function": "validate_plant", "params": ["5unFl0ower", 4]},
#         5: {"function": "validate_plant", "params": ["42", 52]},
#         6: {"function": "validate_plant", "params": ["Cactus", 0]},
#         7: {"function": "validate_plant", "params": ["Cactus", -365]},
#         8: {"function": "validate_watering", "params": [42]},
#         9: {"function": "validate_watering", "params": [-42]}
#     }
#     for i in to_test:
#         print(f"Testing {i}...")
#         testing = tests.get(i)
#         func = testing.get("function")
#         params = testing.get("params")
#         try:
#             match func:
#                 case "validate_garden":
#                     validate_garden(params[0])
#                 case "validate_plant":
#                     validate_plant(params[0], params[1])
#                 case "validate_watering":
#                     validate_watering(params[0])
#             print(">> done")
#         except Exception as e:
#             error_type = e.__class__.__name__
#             print(f">> Caught {error_type}: {e}")
#     print("All custom error types work correctly!")


if __name__ == "__main__":
    test_personal_errors_type()
