# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:18 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:19 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(entry: str) -> int:
    min_temp = "(min 0°C)"
    max_temp = "(max 40°C)"
    try:
        temp = int(entry)
    except ValueError:
        raise ValueError(f"entry '{entry}' is not valid for int() convertion")
    if temp < 0:
        to_raise = f"temperature warning: {temp}°C is too cold for plant"
        raise Exception(to_raise + min_temp)
    elif temp > 40:
        to_raise = f"temperature warning: {temp}°C is too hot for plant"
        raise Exception(to_raise + max_temp)
    return temp


def test_temperature() -> None:
    inputs = ["25", "abc", "42", "-51", '42sp']

    for inp in inputs:
        print(f"Input data is '{inp}'")
        try:
            temp = input_temperature(inp)
            print(f"Temperature is now {temp}°C", end="\n\n")
        except ValueError as e:
            print(f"Caught input_temperature value error: {e}", end="\n\n")
        except Exception as e:
            print(f"Caught input_temperature warning: {e}", end="\n\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
