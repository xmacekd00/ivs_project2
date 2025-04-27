Built for:
-----------

Windows 10 64bit

Authors:
-----------

- xmacekd00 David Macek
- xcapkad00 Daniel Čapka
- xkrystm00 Miroslav Krystyn
- xperuta00 Adam Perutka

-----------
License:
TBA

# About our project
This Desktop Calculator is a simple yet powerful application designed for everyday calculations on your PC. With a clean and intuitive interface, it supports both basic arithmetic and more advanced mathematical functions, making it suitable for users of all levels. Whether you're working, studying, or managing personal tasks, this calculator offers a reliable and user-friendly solution to help you get the job done efficiently.

## Development
The calculator was implemented in Python, with the GUI built using the Tkinter library. 

## GitHub
You can obtain our Desktop Calculator using this command:

`git clone  https://github.com/xmacekd00/ivs_project2.git`

## Instalation

Ubuntu: 1. Make sure you have python3 installed
            "python3 --version"
        1.2.If not, install it
            "sudo apt install python3"
        2. Go into src directory 
            e.g."cd .../ivs_project2/src"
        3. Use Makefile made ready for you
            "make"
        3.1 If tkinter is missing, install it 
            "sudo apt install python3-tk"

Windows:1. Make sure you have Python 3 installed
            "python --version"
        1.2 If not, install it
            "Download the 64-bit installer from https://www.python.org, 
            run it, and tick Add Python to  PATH.
            Tkinter is included automatically."
        2. Go into src directory
            e.g. "cd C:\path\to\ivs_project2\src"
        3. Install GNU Make (one-time)
            "choco install make"  ← requires Chocolatey
        3.1 Run the prepared Makefile
            "make"
        3.2 If Tkinter not found, reinstall Python with the tcl/tk feature enabled.