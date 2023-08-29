import tkinter as tk

def is_entry_filled(entry_widget):
    content = entry_widget.get()
    return len(content.strip()) > 0

def main():
    root = tk.Tk()
    root.title("Entry Filled Check Example")

    entry = tk.Entry(root)
    entry.pack(padx=20, pady=20)

    def check_filled_entry():
        if is_entry_filled(entry):
            result_label.config(text="Entry is filled!")
        else:
            result_label.config(text="Entry is empty!")

    check_button = tk.Button(root, text="Check Entry", command=check_filled_entry)
    check_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
