# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:29 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:30 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class WaterError(Exception):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise WaterError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print("[OK]")


def test_watering_system() -> str:
    to_test = ["Tomato", "Lettuce", "Carrots"]
    print("Opening watering system")
    try:
        for i in to_test:
            print(f"Watering {i}: ", end="")
            water_plant(i)
    except Exception as e:
        error_type = e.__class__.__name__
        print(f"Caught {error_type}: {e}")
        print("... ending tests and returing to main")
    finally:
        print("Closing watering system...")
        return "clear"


def main() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    ret = test_watering_system()
    if ret == "clear":
        print("\nCleanup always happens, even with errors!")
    else:
        print("\nCleanup failed!")


if __name__ == "__main__":
    main()
