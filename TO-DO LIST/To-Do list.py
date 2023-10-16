class ToDoItem:
    def __init__(self, task, due_date=None):
        self.task = task
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_list(self):
        for item in self.items:
            print(f"{item.task} - due: {item.due_date}")

    def mark_item_complete(self, item):
        item.completed = True

    def get_incomplete_items(self):
        return [item for item in self.items if not item.completed]


def main():
    to_do_list = ToDoList()

    # Add some items to the list
    to_do_list.add_item(ToDoItem("Finish this program"))
    to_do_list.add_item(ToDoItem("Go to the grocery store"))
    to_do_list.add_item(ToDoItem("Call my mom"))

    # Print the list
    to_do_list.print_list()

    # Mark an item complete
    to_do_list.mark_item_complete(to_do_list.items[0])

    # Print the list again
    print("Incomplete items:")
    to_do_list.print_list()


if __name__ == "__main__":
    main()
