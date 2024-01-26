import tkinter as tk

def validate_card():
    card_no = card_entry.get()
    odd_sum = 0
    even_sum = 0
    double_num = []
    number = list(card_no)

    for (idx, val) in enumerate(number):
        if idx % 2 != 0:
            odd_sum += int(val)
        else:
            double_num.append(int(val) * 2)

    double_string = ""
    for x in double_num:
        double_string += str(x)

    double_num = list(double_string)
    for x in double_num:
        even_sum += int(x)

    net_sum = odd_sum + even_sum
    if net_sum % 10 == 0:
        result_label.config(text="Valid card", font=("Arial", 16))  # Increase font size
    else:
        result_label.config(text="Invalid card", font=("Arial", 16))  # Increase font size

# Create a GUI window
window = tk.Tk()
window.title("Credit Card Validator")

# Set the window size
window.geometry("400x200")  # Width x Height

# Create and place input label and entry with a larger width and font size><
card_label = tk.Label(window, text="Enter credit card details:", font=("Times New Roman", 20))  # Increase font size
card_label.pack(pady=10)

card_entry = tk.Entry(window, width=30, font=("Times New Roman", 14))  # Increased wid++th and font size
card_entry.pack(pady=10)

# Create and place validate button with a larger font size
validate_button = tk.Button(window, text="Validate", command=validate_card, font=("Arial", 16))  # Increase font size
validate_button.pack(pady=10)

# Create and place result label with a larger font size
result_label = tk.Label(window, text="", font=("Times New Roman", 16))  # Increase font size
result_label.pack()

# Start the GUI event loop
window.mainloop()



#5610591081018250
#4137894711755904