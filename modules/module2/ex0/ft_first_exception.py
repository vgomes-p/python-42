# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:14 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:15 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(entry: str) -> int:
    try:
        temperature = int(entry)
    except ValueError:
        raise ValueError(f"entry '{entry}' is not valid for int() convertion")
    return temperature


def test_temperature() -> None:
    inputs = ["25", "abc", "42", "-51", '42sp']

    for inp in inputs:
        print(f"Input data is '{inp}'")
        try:
            temp = input_temperature(inp)
            print(f"Temperature is now {temp}°C", end="\n\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}", end="\n\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
