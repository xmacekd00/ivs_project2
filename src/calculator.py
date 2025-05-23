##
# @file calculator.py
# @authors xcapkad00, xkrystm00
# @brief Calculator created using the tkinter library with 
#              the possibility of extending it with custom mathematical operations.
# @date 13.04.2025
# @version 1.2
# 
import math_lib
import tkinter as tk
from tkinter import font

##
#@class Calculator
#@brief Main class for the GUI
class Calculator:
    ##
    #@breif Constructor, initialization of window, fonts and all elements
    #@param master Main tkinter window
    def __init__(self, master):
        # Set up the main window
        self.master = master
        self.master.title("Calculator")  # Set the title of the window
        self.master.geometry("300x500")  # Set the size of the window
        self.master.resizable(True, True)  # Allow resizing of the window
        self.master.configure(bg="#0c1520")  # Set the background color of the window
        self.master.minsize(300, 500)  # Minimum width: 300, Minimum height: 500
        
        # Fonts for different UI elements
        self.display_font = font.Font(family="Arial", size=28, weight="bold")  # Font for the result display
        self.equation_font = font.Font(family="Arial", size=14)  # Font for the equation display
        self.button_font = font.Font(family="Arial", size=18, weight="bold")  # Font for the main buttons
        self.small_button_font = font.Font(family="Arial", size=14)  # Font for smaller buttons
        
        # Equation state tracking
        self.equation = ""  # Initialize the equation as an empty string
        self.display_equation = ""  # Initialize the display equation as an empty string
        self.last_operation = None  # Track the last operation
        
        # Label to display the equation
        self.equation_display = tk.Label(
            master, 
            text="",  # Initially empty
            font=self.equation_font,  # Use the equation font
            bg="#0c1520",  # Background color
            fg="#6d737a",  # Text color
            anchor="e"  # Align text to the right
        )
        self.equation_display.pack(fill=tk.X, padx=20, pady=(40, 0))  # Add padding and fill horizontally
        
        # Label to display the result
        self.result_display = tk.Label(
            master, 
            text="0",  # Default result is 0
            font=self.display_font,  # Use the display font
            bg="#0c1520",  # Background color
            fg="white",  # Text color
            anchor="e"  # Align text to the right
        )
        self.result_display.pack(fill=tk.X, padx=20, pady=(0, 20))  # Add padding and fill horizontally
        
        # Add a help button in the top-left corner
        help_button = tk.Button(
            master,
            text="?",  # Text for the button
            font=self.small_button_font,  # Use the smaller font
            bg="#0059cc",  # Blue background
            fg="white",  # White text color
            command=self.show_help,  # Call the show_help method when clicked
            relief=tk.FLAT,  # Flat button style
            activebackground="#003d99",  # Darker blue when hovered
            activeforeground="white"  # White text when hovered
        )
        help_button.place(x=10, y=10, width=30, height=30)  # Position the button in the top-left corner
        
        # Frame for buttons
        button_frame = tk.Frame(master, bg="#0c1520")  # Create a frame for the buttons
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Add padding and allow expansion
        
        # Configure the grid inside button_frame
        for i in range(6):  # Create 6 rows for buttons
            button_frame.grid_rowconfigure(i, weight=1)  # Make rows equally spaced
        for i in range(4):  # Create 4 columns for buttons
            button_frame.grid_columnconfigure(i, weight=1)  # Make columns equally spaced
        
        # Scientific function buttons
        sci_buttons = [
            ("x²", 0, 0),  # Square function
            ("√", 0, 1),  # Square root function
            ("!", 0, 2),  # Factorial function
            ("MOD", 0, 3)  # Modulus function
        ]
        for (text, row, col) in sci_buttons:
            self.create_button(
                button_frame, 
                text=text,  # Button text
                font=self.small_button_font,  # Use smaller font for scientific buttons
                bg="#252e3b",  # Button background color
                fg="#3d88e0",  # Button text color
                command=lambda t=text: self.add_to_equation(t),  # Add button text to equation when clicked
                row=row,  # Row position in the grid
                column=col  # Column position in the grid
            )
        
        # Function buttons like clear and backspace
        func_buttons = [
            ("xⁿ", 1, 0),  # Exponentiation (shows as xⁿ but becomes ^ in display)
            ("ⁿ√", 1, 1),  # Nth root
            ("AC", 1, 2),  # Clear all
            ("DEL", 1, 3)  # Delete last character
        ]
        for (text, row, col) in func_buttons:
            if text in ["AC", "DEL"]:  # Special styling for AC and DEL buttons
                bg_color = "#0059cc"  # Blue background for these buttons
                fg_color = "white"  # White text color
            else:
                bg_color = "#252e3b"  # Default background color
                fg_color = "#3d88e0"  # Default text color
            
            if text == "AC":
                command = self.clear  # Clear the equation
            elif text == "DEL":
                command = self.backspace  # Remove the last character
            else:
                command = lambda t=text: self.add_to_equation(t)  # Add button text to equation
                
            self.create_button(
                button_frame, 
                text=text,  # Button text
                font=self.button_font if text in ["/", "*"] else self.small_button_font,  # Font size based on button type
                bg=bg_color,  # Background color
                fg=fg_color,  # Text color
                command=command,  # Command to execute when button is clicked
                row=row,  # Row position in the grid
                column=col  # Column position in the grid
            )
        
        # Number, dot and = buttons
        numbers = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),  # Row 2
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),  # Row 3
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),  # Row 4
            ("0", 5, 0), (",", 5, 1), ("=", 5, 2),  # Row 5
        ]
        for button in numbers:
            text, row, col = button
            self.create_button(
                button_frame, 
                text=text,  # Button text
                font=self.button_font,  # Font for numbers
                bg="#252e3b",  # Background color
                fg="white",  # Text color
                command=self.equals if text == "=" else lambda t=text: self.add_to_equation(t),  # "=" triggers equals or add to equation
                row=row,  # Row position
                column=col  # Column position
            )
        
        # Operator buttons: -, +, *, and /
        operators = [
            ("+", 2, 3),  # Addition
            ("-", 3, 3),  # Subtraction
            ("*", 4, 3),  # Multiplication
            ("/", 5, 3)   # Division
        ]
        for button in operators:
            text, row, col = button
            command = lambda t=text: self.add_to_equation(t)  # Add operator to equation
            self.create_button(
                button_frame, 
                text=text,  # Button text
                font=self.button_font,  # Font for operators
                bg="#0059cc",  # Blue background for operators
                fg="white",  # White text color
                command=command,  # Command to execute
                row=row,  # Row position
                column=col  # Column position
            )
        
        # Keyboard input binding
        self.master.bind("<Key>", self.key_press)  # Bind keyboard events to the calculator
        self.master.focus_set()  # Capture keyboard events

    ##
    #@brief Creates a styled button and places it into the grid layout.
    #@param parent Parent widget
    #@param text Button text
    #@param font Button font
    #@param bg Background hex color
    #@param fg Text hex color
    #@param command Function to call, when the button is pressed
    #@param row Row in grid
    #@param column Column in grid
    #@param rowspan Rowspan, default=1
    #@param columnspan Columnspan, default=1
    #@return Button widget
    def create_button(self, parent, text, font, bg, fg, command, row, column, rowspan=1, columnspan=1):
        frame = tk.Frame(parent, bg=parent["bg"])
        frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=4, pady=4, sticky="nsew")
        frame.grid_propagate(False)  # Prevent resizing of the frame
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        btn = tk.Button(
            frame, 
            text=text, 
            font=font,
            bg=bg, 
            fg=fg, 
            relief=tk.FLAT,
            activebackground=self.darken_color(bg),  # Darken color on hover
            activeforeground=fg,
            bd=0,
            padx=0, pady=0,
            highlightthickness=0,
            command=command
        )
        btn.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
        return btn
    ##
    #@brief Darkens a given HEX color by reducing its RGB values.
    #@param hex_color Color hex
    #@return Darkened color hex
    def darken_color(self, hex_color):
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        r = max(0, r - 30)  # Reduce red component
        g = max(0, g - 30)  # Reduce green component
        b = max(0, b - 30)  # Reduce blue component
        return f"#{r:02x}{g:02x}{b:02x}"


    ##
    #@brief Handles keyboard input.
    #@param event Tkinter key event
    def key_press(self, event):
        key = event.char
        if key in "0123456789.+-*/()^":  # Allow numeric and operator keys
            self.add_to_equation(key)
        elif event.keysym == "BackSpace":  # Handle backspace
            self.backspace()
        elif event.keysym == "Return":  # Handle Enter key
            self.equals()
        elif event.keysym == "Escape":  # Handle Escape key
            self.clear()


    ##
    #@brief Appends a character to the equation and updates the display.
    #@param value Symbol to add to equation string
    def add_to_equation(self, value):
        # Handle special operations for display
        if value == "x²":
            self.equation += "S"
            self.display_equation += "²"
        elif value == "xⁿ":
            self.equation += "N"
            self.display_equation += "^"
        elif value == "√":
            self.equation += "s"
            self.display_equation += "²√"
        elif value == "ⁿ√":
            self.equation += "n"
            self.display_equation += "√"
        elif value == "MOD":
            self.equation += "M"
            self.display_equation += "%"
        else:
            self.equation += value
            self.display_equation += value
        
        self.equation_display.config(text=self.display_equation)  # Update equation display
        self.last_operation = value

    ##
    #@brief Clears the equation and result displays.
    def clear(self):
        self.equation = ""
        self.display_equation = ""
        self.equation_display.config(text=self.display_equation)  # Clear equation display
        self.result_display.config(text="0")  # Reset result display

    ##
    #@brief Removes the last character or a special token from the equation.
    def backspace(self):
        # First handle the display equation
        special_display_tokens = ["²", "^", "√"]
        for token in special_display_tokens:
            if self.display_equation.endswith(token):
                self.display_equation = self.display_equation[:-len(token)]
                break
        else:
            self.display_equation = self.display_equation[:-1]
        
        # Then handle the actual equation
        special_tokens = ["S", "N", "s", "n"]  # Define special tokens
        for token in special_tokens:
            if self.equation.endswith(token):
                self.equation = self.equation[:-len(token)]
                break
        else:
            self.equation = self.equation[:-1]
            
        self.equation_display.config(text=self.display_equation)  # Update equation display
    ##
    #@brief Displays the result of an expression
    def equals(self):
        if self.equation:
            try:
                result = math_lib.truncate(math_lib.evaluate(self.equation),5)
                self.result_display.config(text=f"{result}")  # Display the result
                # Keep the display equation for reference
                self.equation_display.config(text=f"{self.display_equation}=")
                # Reset the actual equation but keep display equation for reference
                self.equation = str(result)
                self.display_equation = str(result)
            except Exception as e:
                self.result_display.config(text="Error")  # Display error if calculation fails
                self.equation = ""
                self.display_equation = ""
        else:
            self.result_display.config(text="0")  # Display 0 if equation is empty

    ##
    #@brief Displays a help window with usage instructions
    def show_help(self):
        help_window = tk.Toplevel(self.master)  # Create a new top-level window
        help_window.title("Help")  # Set the title of the help window
        help_window.geometry("700x730")  # Set the size of the help window
        help_window.configure(bg="#0c1520")  # Set the background color
    
        frame = tk.Frame(help_window)
        frame.pack(padx=0, pady=0, fill="both", expand=True)

        # Text widget for help content
        text_widget = tk.Text(
            frame,
            bg="#0c1520",
            fg="white",
            font=self.equation_font,
            wrap="word",
        )
        text_widget.pack(padx=0, pady=0, fill="both", expand=True)

    
        # Define styled tags
        text_widget.tag_configure("section", foreground="#0059cc", font=(self.equation_font.actual("family"), self.equation_font.actual("size"), "bold"))
        text_widget.tag_configure("title", foreground="#ffffff", font=(self.equation_font.actual("family"), self.equation_font.actual("size") + 2, "bold"), justify="center")

    
        # Insert the manual text with tagged sections
        text_widget.insert("end", "  Simple Calculator Help Manual\n\n", "title")
        
        text_widget.insert("end", "  Basic Operations:\n", "section")
        text_widget.insert("end",
            "    + : Addition\n"
            "    - : Subtraction\n"
            "    * : Multiplication\n"
            "    / : Division\n"
            "    MOD : Modulo (Remainder)\n\n"
        )
    
        text_widget.insert("end", "  Advanced Functions:\n", "section")
        text_widget.insert("end",
            "    x² : Square (5 and x² = 5²)\n"
            "    √ : Square root (√n = choose any number behind sqrt to be n)\n"
            "    ⁿ√ : Nth root (ⁿ√x = choose n before pressing the function, continue with x number)\n"
            "    xⁿ : Power (5 and xⁿ = 5 ^ : choose the next number to be ⁿ)\n"
            "    ! : Factorial (choose number before pressing ""!"")\n"
            "    see examples for more clarification\n\n"
        )
    
        text_widget.insert("end", "  Controls:\n", "section")
        text_widget.insert("end",
            "    AC : All Clear\n"
            "    DEL : Delete last digit\n"
            "    = : Evaluate expression\n\n"
        )
    
        text_widget.insert("end", "  How to Use:\n", "section")
        text_widget.insert("end",
            "    - Click buttons to build an expression.\n"
            "    - Use '=' to evaluate.\n"
            "    - Use 'AC' to reset everything.\n"
            "    - Use 'DEL' to delete the last character.\n\n"
        )
    
        text_widget.insert("end", "  For example:\n", "section")
        text_widget.insert("end",
            "    9 + 5 * 2 = 19\n"
            "    5 ! = 120\n"
            "    √ 9 = 3\n"
            "    4 x² = 4² = 16\n"
            "    3 ⁿ√ 27 = ³√27 = 3\n"
            "    5 MOD 5 = 5%5 = 0\n"
        )
    
        text_widget.config(state="disabled")
        text_widget.pack(padx=5, pady=5, fill="both", expand=True)

##
# @brief Entry point of the calculator application.
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

## End of the calculator code
# ================================================