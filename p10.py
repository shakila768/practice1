class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named '{name}'")
        del self.items[name]

    def total_value(self):
        return sum(qty * price for qty, price in self.items.values())

    def __len__(self):
        return len(self.items)


inventory = Inventory()

with open("stock.txt", "r") as file:
    for line in file:
        try:
            name, qty, price = line.strip().split(",")
            inventory.add_item(name, int(qty), int(price))
        except ValueError:
            print(f"Skipping {name}: bad number")

print(f"{len(inventory)} items, total value {inventory.total_value()}")

inventory.remove_item("pen")
print(f"{len(inventory)} items, total value {inventory.total_value()}")

try:
    inventory.remove_item("laptop")
except KeyError as error:
    print(f"Error: {error}")