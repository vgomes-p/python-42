# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_stream_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:46:14 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:46:19 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv as av, stdin, stdout, stderr
from typing import IO


class ContentError(Exception):
    pass


class UntrackedError(Exception):
    pass


def ft_input(prompt: str = "") -> str:
    stdout.write(prompt)
    stdout.flush()
    return stdin.readline().rstrip("\n")


def ft_handle_reading(stream: IO[str]) -> str:
    content = stream.read()
    if content:
        print(content, end="")
        return content
    raise ContentError("file is empty")


def ft_handle_convert(l_content: list[str], eol_char: str = "#") -> str:
    size = len(l_content)
    n_content = ""
    i = 1
    for line in l_content:
        if line:
            n_content += line + eol_char + '\n'
        else:
            if i == size:
                continue
            n_content += '\n'
        i += 1
    return n_content


def ft_handle_writing(content: str, file: IO[str]) -> None:
    try:
        if content:
            file.write(content)
        else:
            raise ContentError("Content is empty")
    except Exception as e:
        error_type = e.__class__.__name__
        raise UntrackedError(f"Untracked error for {error_type} type: {e}")


def ft_ancient_text(file_path: str) -> str:
    print(f"Accessing file '{file_path}'")
    fcontent: str | None = None
    content: IO[str] | None = None
    try:
        content = open(file_path, "r")
        print("-" * 62)
        fcontent = ft_handle_reading(content)
        print("-" * 62)
    except Exception as e:
        error_type = e.__class__.__name__
        print(f"Error on handling file '{file_path}': {error_type}: {e}",
              file=stderr)
    finally:
        if content is not None:
            content.close()
            print(f"File '{file_path}' closed.")
    return fcontent if fcontent else ""


def ft_archive_creation(content: str) -> None:
    l_content = content.split('\n')
    n_content = ft_handle_convert(l_content)
    print(f"\nTransform data:\n{'-' * 63}\n{n_content}{'-' * 63}")
    file_name = str(ft_input("Enter new file name (or empty): ").strip())
    if not file_name:
        print("Not saving data.")
        return
    file: IO[str] | None = None
    try:
        file = open(file_name, 'w')
        print(f"Saving data to '{file_name}'")
        ft_handle_writing(n_content, file)
    except Exception as e:
        error_type = e.__class__.__name__
        print(f"Error on handling archive creation: {error_type}: {e}",
              file=stderr)
    finally:
        if file is not None:
            file.close()
        print(f"Data saved in file '{file_name}'")


def main() -> None:
    if len(av) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = ft_ancient_text(av[1])
    ft_archive_creation(content)


if __name__ == "__main__":
    main()
