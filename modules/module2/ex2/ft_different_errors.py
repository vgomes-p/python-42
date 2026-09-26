# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:21 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:22 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations(op_nbr: int) -> None:
    if op_nbr == 0:
        int("abc")
    elif op_nbr == 1:
        42 / 0
    elif op_nbr == 2:
        open("/non/existent/file")
    elif op_nbr == 3:
        "40" + 2
    else:
        return


def test_error_types() -> None:
    ops = [0, 1, 2, 3, 4]
    for op in ops:
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except Exception as e:
            exception_type = e.__class__.__name__
            print(f"Caught {exception_type}: {e}")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
