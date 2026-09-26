import sys


def parser() -> dict[str, int]:
    av = sys.argv[1:]
    ret: dict[str, int] = dict()
    for item in av:
        try:
            key, value = item.split(':')
            if key in ret:
                print(f"Redundant item '{key}' - discarting")
                continue
            if key == '':
                print(f"Item missing for quantity {value}")
            elif int(value) < 0:
                print(f"Item {key} quantity cannot be negative!")
            else:
                ret[str(key)] = int(value)
        except ValueError as e:
            if "for int()" in e.args[0]:
                print(f"Quantity error for '{key if key else item}': {e}")
            else:
                print(f"Error - invalid parameter '{item}'")
    return ret


def display_inventory(inventory: dict[str, int]) -> int:
    i = 1
    total = len(inventory)
    print("Inventory: ", end='')
    for item in inventory:
        print(f"{item}: {inventory[item]}",
              end=" | " if i < total else ".\n")
        i += 1
    return total


def display_itens(inventory: dict[str, int], total: int) -> list[str]:
    list_of_itens: list[str] = []
    i = 1
    print("Item list: ", end='')
    for item in inventory:
        print(item, end=", " if i < total else ".\n")
        list_of_itens += [item]
        i += 1
    return list_of_itens


def display_quantity_of_itens(inventory: dict[str, int], total: int) -> int:
    quantity = 0
    for item in inventory:
        quantity += inventory[item]
    print(f"Total quantity of the {total} items: {quantity}")
    return quantity


def display_itens_percentage(inventory: dict[str, int], quantity: int) -> None:
    for item in inventory:
        item_quantity = inventory[item]
        percentage = (item_quantity * 100) / quantity
        print(f"Item {item} represents {percentage:.1f}%")


def display_abundance(inventory: dict[str, int]) -> None:
    item_most: str | None = None
    item_least: str | None = None
    imi = 0
    ili = 0
    for item in inventory:
        ii = inventory[item]
        if item_most is None or item_least is None:
            item_most = item
            item_least = item
            imi = ii
            ili = ii
        elif ii > imi:
            item_most = item
            imi = ii
        elif ii < ili:
            item_least = item
            ili = ii
    print(f"Item most abundant: {item_most} with quantity {imi}")
    print(f"Item least abundant: {item_least} with quantity {ili}")


def add_item(inventory: dict[str, int],
             item: str, quantity: int) -> None:
    inventory[item] = quantity


def main() -> None:
    inventory = parser()
    total = display_inventory(inventory)
    display_itens(inventory, total)
    quantity = display_quantity_of_itens(inventory, total)
    display_itens_percentage(inventory, quantity)
    display_abundance(inventory)
    add_item(inventory, "magic_item", 1)
    print("UPDATE: ", end='')
    display_inventory(inventory)


if __name__ == "__main__":
    main()
