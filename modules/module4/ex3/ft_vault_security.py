# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_vault_security.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:46:21 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:46:22 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def read_file(file_name: str) -> str:
    message: str | None = None
    with open(file_name, "r") as file:
        message = file.read()
    return message


def write_file(file_name: str, content: str) -> str:
    with open(file_name, "w") as file:
        file.write(content)
    return "Content successfully written to file "


def secure_archive(file_name: str, mode: str,
                   content: str = "") -> tuple[bool, str | None]:
    if mode not in ["w", "r"]:
        err = f"Mode error on secure_archive: '{mode}' is not a valid mode."
        md_usage = "Enter a valid mode ['r' for read and 'w' for write]."
        raise ValueError(err + md_usage)
    message: str | None = None
    access: bool = False
    try:
        match mode:
            case "r":
                message = read_file(file_name)
            case "w":
                message = write_file(file_name, content)
        access = True
    except Exception as e:
        message = str(e)
        access = False
    finally:
        return access, message


def main() -> None:
    msg0 = "Using 'secure_archive' to read from a nonexistent file:"
    msg1 = "Using 'secure_archive' to read from an inaccessible file:"
    msg2 = "Using 'secure_archive' to read from a regular file:"
    msg3 = "Using 'secure_archive' to write previous content to a new file:"
    files: dict[int, list[str]] = {
        0: [msg0, "/not/existing/file", "r", ""],
        1: [msg1, "/etc/master.passwd", "r", ""],
        2: [msg2, "ancient_fragment.txt", "r", ""],
        3: [msg3, "new_file.txt", "w", "message"],
    }
    print("=== Cyber Archives Security ===\n")
    for i in files:
        file = files[i]
        message = file[0]
        file_name = file[1]
        mode = file[2]
        content = file[3] if file[3] else ""
        print(message)
        print(secure_archive(file_name, mode, content),
              end="\n\n" if i < 3 else "\n")


if __name__ == "__main__":
    main()
