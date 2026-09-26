# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:33 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:34 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys as s


def find_name(arg: str) -> int:
    arg_len = len(arg) - 1
    for i in arg:
        if arg[arg_len] == '/':
            return arg_len + 1
        arg_len -= 1
    return 0


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    args = s.argv
    total_args = len(args)
    pnip = find_name(args[0])
    program_name = args[0][pnip:]
    args = args[1:]
    nbr = 1
    print("Program name:", program_name)
    if len(args) > 0:
        print("Arguments received:", len(args))
    else:
        print("No argument provided!")
    for arg in args:
        print(f"Argument {nbr}: {arg}")
        nbr += 1
    print(f"Total arguments: {total_args}")


def main() -> None:
    ft_command_quest()


if __name__ == "__main__":
    main()
