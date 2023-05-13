# ====================================
# Attached: Class Exercise #11
# ====================================
# File: Challenge Exercise #1
# ====================================
# Name: Title Bar
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

import tkinter


class MyGUI:

    def __init__(self):
        # create the main window widget
        self.main_window = tkinter.Tk()

        # Enter the tkinter main loop
        tkinter.mainloop()

        # display a title
        self.main_window.title("My first GUI")

        # Enter the tkinter main loop
        tkinter.mainloop()


# create an instance of the MyGUI class
if __name__ == "__main__":
    my_gui = MyGUI()

''''
===============Output=================



'''


# ====================================
# Attached: Class Exercise #11
# ====================================
# File: Challenge Exercise #2
# ====================================
# Name: Label
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program displays a label with text


class MyGUI:
    def __init__(self):
        # create the main window widget
        self.main_window = tkinter.Tk()

        # create three labels widget with values of last name, first name, and age
        self.label = tkinter.Label(self.main_window, text="Last Name")
        self.label2 = tkinter.Label(self.main_window, text="First Name")
        self.label3 = tkinter.Label(self.main_window, text="Age")

        # call the label widget's pack method
        self.label.pack()
        self.label2.pack()
        self.label3.pack()

        # enter the tkinter main loop
        tkinter.mainloop()


# create an instance of the MyGUI class
if __name__ == "__main__":
    my_gui = MyGUI()

''''
===============Output=================



'''


# ====================================
# Attached: Class Exercise #11
# ====================================
# File: Challenge Exercise #3
# ====================================
# Name: Internal Padding
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program demonstrates internal padding


class MyGUI:

    def __init__(self):
        # create the main window widget
        self.main_window = tkinter.Tk()

        # create four label widget with solid borders
        self.label1 = tkinter.Label(self.main_window, text="Hello World!", borderwidth=1, relief="solid")
        self.label2 = tkinter.Label(self.main_window, text="This is my GUI program.", borderwidth=1, relief="solid")
        self.label3 = tkinter.Label(self.main_window, text="Eventually everything connects.", borderwidth=1,
                                    relief="solid")
        self.label4 = tkinter.Label(self.main_window, text="Be the change.", borderwidth=1, relief="solid")

        # display the Labels with 20 pixels of horizontal and vertical internal padding
        self.label1.pack(ipadx=20, ipady=20)
        self.label2.pack(ipadx=20, ipady=20)
        self.label3.pack(ipadx=20, ipady=20)
        self.label4.pack(ipadx=20, ipady=20)

        # enter the tkinter main loop
        tkinter.mainloop()


# create an instance of the MyGUI class
if __name__ == "__main__":
    my_gui = MyGUI()

''''
===============Output=================



'''

# ====================================
# Attached: Class Exercise #11
# ====================================
# File: Challenge Exercise #4
# ====================================
# Name: Buttons
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program has a Quit button that class the Tk class's destroy method when clicked
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # create the main window widget
        self.main_window = tkinter.Tk()

        # create a button widget. The text "Click Me!" should appear on the face of the button. The do_something
        # method should be executed when the user clicks the button.
        self.my_button = tkinter.Button(self.main_window, text="Click me!", command=self.do_something)

        # create a button widget. The text "Positive Button" should appear on the face of the button. The do_something2
        # should be executed when the user clicks the button.
        self.positive_button = tkinter.Button(self.main_window, text="Positive Button", command=self.do_something2)

        # create a Quit button. When is button is clicked the root widget's destroy method is class (The main_window
        # variable reference the root widget. so the callback function is self.main_window.destroy)
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        # pack the buttons
        self.my_button.pack()
        self.positive_button.pack()
        self.quit_button.pack()

        # enter the tkinter main loo[
        tkinter.mainloop()

    # this do_something method is a callback function for the Button widget
    def do_something(self):
        tkinter.messagebox.showinfo("POSITIVE QUOTE", "Thanks for clicking the button")

    def do_something2(self):
        tkinter.messagebox.showinfo("POSITIVE QUOTE")


# create an instance of the MyGUI class
if __name__ == "__main__":
    my_gui = MyGUI()

''''
===============Output=================



'''

# ====================================
# Attached: Class Exercise #11
# ====================================
# File: Challenge Exercise #5
# ====================================
# Name: Kilo to Miles
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

class KiloConverterGUI:
    def __init__(self):

        # create the main window
        self.main_window = tkinter.Tk()

        # create two frames go group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a distance in kilometers:")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # pack the top frame's widgets
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        # create the button widget for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # pack the buttons
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

# the convert method is a callback function for the Calculate button
    def convert(self):
        # get the value entered by the user into the kilo_entry widget
        kilo = float(self.kilo_entry.get())

        # convert kilometers to miles
        miles = kilo * 0.6214

        # display the results in an info dialog box
        tkinter.messagebox.showinfo("Results", str(kilo) + "kilometers is equal to" + str(miles) + "miles.")


# create an instance of the KiloConverterGUI class
if __name__ == "__main__":
    kilo_conv = KiloConverterGUI

''''
===============Output=================



'''

# ====================================
# Attached: Class Exercise #11
# ====================================
# File: Challenge Exercise #6
# ====================================
# Name: Kilo App
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program converts distance in kilometers to miles. The result is displayed in a label on the main window

class KiloConverterGUI:
    def __init__(self):

        # create the main window
        self.main_window = tkinter.Tk()

        # crete three frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a distance in kilometers:")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # pack the top frame's widgets
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        # create the widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame, text="Converted to miles:")

        # we need a stringVar object to associate with an output label. Use the object's set method to store a string
        # of blank characters
        self.value = tkinter.stringVar()

        # create a label and associate it with the stringVar object. Any value stored in the stringVar object with
        # automatically be displayed in the label
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # pack the middle frame's widgets
        self.descr_label.pack(side="left")
        self.miles_label.pack(side="left")

        # create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # pack the buttons
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        # pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    # the convert method is a callback function for the calculate button
    def convert(self):
        # get the value entered by the user info the kilo_entry widget
        kilo = float(self.kilo_entry.get())

        # convert the kilometer to miles
        miles = kilo * 0.6214

        # convert miles ot a string and store it in the stringVar object. This will automatically update the
        # miles_label widget.
        self.value.set(miles)


# create an instance of the KiloConverterGUI class
if __name__ == "__main__":
    kilo_conv = KiloConverterGUI()

''''
===============Output=================



'''