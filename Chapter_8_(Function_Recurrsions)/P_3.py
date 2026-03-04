# Function 1: Keep print on same line
def same_line_print():
    print("Hello", end="")  # no new line
    print("World")          # prints right after Hello
    print()                 # line break for clarity

# Function 2: Print numbers on same line with spaces
def numbers_with_spaces():
    for i in range(5):
        print(i, end=" ")   # space instead of new line
    print()                 # line break

# Function 3: Custom text at the end
def custom_text_end():
    print("Loading", end="...")  # adds "..." instead of new line
    print("Done")                # prints after "..."
    print()                      # line break

# Function 4: Table style using tabs
def table_with_tabs():
    for i in range(1, 6):
        print(i, end="\t")       # tab instead of new line
    print()                      # line break

# Function 5: Items separated by comma
def items_with_comma():
    for i in range(1, 6):
        print(f"Item{i}", end=", ")  # comma instead of new line
    print()                          # line break

# ===============================
# Call each function one by one
# ===============================
same_line_print()
numbers_with_spaces()
custom_text_end()
table_with_tabs()
items_with_comma()
