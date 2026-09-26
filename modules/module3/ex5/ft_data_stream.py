# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vigomes- <vigomes-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/26 15:45:57 by vigomes-          #+#    #+#              #
#    Updated: 2026/09/26 15:45:58 by vigomes-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import typing as tp
import random as rdm

names = ["Liam", "Sophia", "Noah", "Olivia", "Ethan", "Ava",
         "Mason", "Isabella", "Lucas", "Mia"]
actions = ["run", "jump", "swim", "climb", "dance", "sing", "write",
           "read", "cook", "drive", "build", "paint", "code", "hike",
           "bike", "ski", "surf", "meditate", "stretch", "lift",
           "throw", "catch", "kick", "punch", "stretch"]


def gen_event() -> tp.Generator[tuple[str, str], None, None]:
    while True:
        yield (rdm.choice(names), rdm.choice(actions))


def gen_index(target: list[tuple[str, str]]) -> int:
    return rdm.randint(0, len(target) - 1)


def consume_event(events: list[tuple[str, str]]
                  ) -> tp.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        i = gen_index(events)
        event = events[i]
        del events[i]
        yield event


def main() -> None:
    generator = gen_event()
    ten_events = []
    for n in range(1000):
        name, action = next(generator)
        print(f"Event {n}: Player {name} did action {action}")
        if n < 10:
            ten_events += [(name, action)]
    print("Ten events generated:", ten_events)
    generator = consume_event(ten_events)
    for n in range(10):
        event = next(generator)
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
