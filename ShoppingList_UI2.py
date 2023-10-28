import tkinter as tk

class Item():
    def __init__(self, item_id, name, price, count):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.count = count

    def get_item_info(self):
        return self.item_id, self.name, f'£{self.price:.2f}', self.count

    def add_n(self, n):
        self.count += n

    def remove_n(self, n):
        if self.count >= n:
            self.count -= n
            return True
        else:
            self.count = 0
            return False

#Tkinter window
root = tk.Tk()
root.title("Item Management")

FONTS = ["Arial", 
                "Times New Roman", 
                "Courier New", 
                "Verdana", 
                "Comic Sans MS", 
                "Impact"]

# Initialize your items
ids_list = ["apl001", "mil001", "ck001"]
prices = [2.45, 1, 8]
names = ["apple", "milk", "cake"]

items_map = {
    ids_list[i]: Item(f"{ids_list[i]}", f"{names[i]}", prices[i], 0) for i in range(len(ids_list))
}

item_count = 0

# Listbox to display items and quantities
item_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
item_listbox.pack()

# frame within which buttons will be placed
display_frame = tk.Frame(root, bg="white")
display_frame.columnconfigure(0, weight=1) # nth column fills available x-axis space 
display_frame.columnconfigure(1, weight=10) # nth column fills available x-axis space 
display_frame.columnconfigure(2, weight=1) # nth column fills available x-axis space 
display_frame.columnconfigure(3, weight=1) # nth column fills available x-axis space 

# buttons and place them in the frame
def item_button_click(item_id, increment=True):
    item = items_map[item_id]
    if increment:
        if item_count >= 15:
            message_label.config(text="Maximum quantity reached (15 items)", fg="red")
        else:
            item.add_n(1)
    else:
        item.remove_n(1)
    update_item_listbox()
    update_total()
    message_label.config(text="")

def create_item_buttons():
    row_num = 0
    for item_id in items_map:
        item = items_map[item_id]
        item_frame = tk.Frame(display_frame)
        item_frame.grid(row=row_num, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        item_frame.columnconfigure(0, weight=1)
        item_frame.columnconfigure(1, weight=10)
        item_frame.columnconfigure(2, weight=1)
        item_frame.columnconfigure(3, weight=1)
        
        item_name_label = tk.Label(item_frame, text=f"{item.name} - Quantity: {item.count}")
        item_name_label.grid(row=row_num, column=0, sticky="w")

        add_button = tk.Button(item_frame, text="+", font=(FONTS[0], 12), command=lambda i=item_id: item_button_click(i, increment=True))
        add_button.grid(row=row_num, column=1)

        remove_button = tk.Button(item_frame, text="-", font=(FONTS[0], 12), command=lambda i=item_id: item_button_click(i, increment=False))
        remove_button.grid(row=row_num, column=2)

        row_num += 1

create_item_buttons()

display_frame.pack(fill="x")

#  label to display item information
info_label = tk.Label(root, text="Select an item to see details.")
info_label.pack()

#   frame for the message
message_frame = tk.Frame(root)
message_frame.pack()

# label to show the message in the message frame
message_label = tk.Label(message_frame, text="", fg="red")
message_label.pack()

#label to display the total cost
total_cost_label = tk.Label(root, text="Total Cost: £0.00")
total_cost_label.pack()

# entry field for user input
entry = tk.Entry(root)
entry.pack()

def update_item_listbox():
    item_listbox.delete(0, tk.END)
    for item_id, item in items_map.items():
        item_listbox.insert(tk.END, f"{item.name} - Quantity: {item.count}")

update_item_listbox()

# button to remove items from the cart
def remove_item(item_id):
    item = items_map[item_id]
    if item.remove_n(1):
        update_item_listbox()
        update_total()

# button to update item information
def update_info():
    selected_index = item_listbox.curselection()
    if selected_index:
        item_id = list(items_map.keys())[selected_index[0]]
        item = items_map[item_id]
        info = f"Item ID: {item.item_id}, Name: {item.name}, Price: {item.price:.2f}, Count: {item.count}"
        info_label.config(text=info)

update_button = tk.Button(root, text="Get Item Info", command=update_info)
update_button.pack()

# Function to update the total amount
def update_total():
    global item_count
    item_count = sum(item.count for item in items_map.values())
    if item_count > 15:
        message_label.config(text="Maximum quantity reached (15 items)", fg="red")
    else:
        message_label.config(text="", fg="red")
    total = sum(item.price * item.count for item in items_map.values())
    total_cost_label.config(text=f"Total Cost: £{total:.2f}")

# button to show the total
def show_total():
    update_total()

total_button = tk.Button(root, text="Show Total", command=show_total)
total_button.pack()

# button to exit the program
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
