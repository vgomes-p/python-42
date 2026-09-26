# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ancient_text.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:46:05 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:46:09 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv as av
from typing import IO


class ContentError(Exception):
    pass


def ft_handle_reading(stream: IO[str]) -> None:
    content = stream.read()
    if content:
        print(content, end="")
    else:
        raise ContentError("file is empty")


def ft_ancient_text(file_path: str) -> None:
    print('=== Cyber Archives Recovery ===')
    print(f"Accessing file '{file_path}'")
    content: IO[str] | None = None
    try:
        content = open(file_path, "r")
        print("-" * 62)
        ft_handle_reading(content)
        print("-" * 62)
    except Exception as e:
        error_type = e.__class__.__name__
        print(f"Error on handling file '{file_path}': {error_type}: {e}")
    finally:
        if content is not None:
            content.close()
            print(f"File '{file_path}' closed.")


def main() -> None:
    if len(av) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    ft_ancient_text(av[1])


if __name__ == "__main__":
    main()
