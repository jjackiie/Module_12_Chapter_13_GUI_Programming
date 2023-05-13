# ====================================
# Attached: m14 Homework #14
# ====================================
# File: Project #1
# ====================================
# Name: The Average GUI App
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program uses a GUI to get three test scores and display their average

import tkinter


class TestAvg:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        # create the five frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # create and pack the widgets for test 1
        self.test1_label = tkinter.Label(self.test1_frame, text="Enter the score for the test 1:")
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)

        self.test1_label.pack(side="left")
        self.test1_entry.pack(side="left")

        # create and pack the widgets for test 2
        self.test2_label = tkinter.Label(self.test2_frame, text="Enter the score for the test 2:")
        self.test2_entry = tkinter.Entry(self.test2_frame, width=10)

        self.test2_label.pack(side="left")
        self.test2_entry.pack(side="left")

        # create and pack the widgets for test 3
        self.test3_label = tkinter.Label(self.test3_frame, text="Enter the score for the test 3:")
        self.test3_entry = tkinter.Entry(self.test3_frame, width=10)

        self.test3_label.pack(side="left")
        self.test3_entry.pack(side="left")

        # create and pack the widgets for the average
        self.result_label = tkinter.Label(self.avg_frame, text="average:")
        self.avg = tkinter.StringVar()  # to update avg_label
        self.avg_label = tkinter.Label(self.avg_frame, textvariable=self.avg)

        self.result_label.pack(side="left")
        self.avg_label.pack(side="left")

        # create and pack the button widgets
        self.calc_button = tkinter.Button(self.button_frame, text="Average", command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame, text="quit", command=self.main_window.destroy)

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        # pack the frames
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # start the main loop
        tkinter.mainloop()

    # the calc_avg method is the callback function for the calc_button widget

    def calc_avg(self):
        # get the three test scores and store them in variables
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # calculate the average
        self.average = (self.test1 + self.test2 + self.test3) / 3.0

        # update the avg_label widget by storing the value of self average in the StringVar object referenced by avg
        self.avg.set(self.average)


# create an instance of the TestAvg class
if __name__ == "__main__":
    test_avg = TestAvg()

''''
===============Output=================
Screen Shot 2023-05-13 at 3.16.36 PM

'''


# ====================================
# Attached: m14 Homework #14
# ====================================
# File: Project #2
# ====================================
# Name: The Average and Total
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program uses a GUI to get three test scores and display their average


class TestAvg:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        # create the five frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.test4_frame = tkinter.Frame(self.main_window)
        self.test5_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # create and pack the widgets for test 1
        self.test1_label = tkinter.Label(self.test1_frame, text="Enter the score for the test 1:")
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)

        self.test1_label.pack(side="left")
        self.test1_entry.pack(side="left")

        # create and pack the widgets for test 2
        self.test2_label = tkinter.Label(self.test2_frame, text="Enter the score for the test 2:")
        self.test2_entry = tkinter.Entry(self.test2_frame, width=10)

        self.test2_label.pack(side="left")
        self.test2_entry.pack(side="left")

        # create and pack the widgets for test 3
        self.test3_label = tkinter.Label(self.test3_frame, text="Enter the score for the test 3:")
        self.test3_entry = tkinter.Entry(self.test3_frame, width=10)

        self.test3_label.pack(side="left")
        self.test3_entry.pack(side="left")

        # create and pack the widgets for test 4
        self.test4_label = tkinter.Label(self.test4_frame, text="Enter the score for the test 4:")
        self.test4_entry = tkinter.Entry(self.test4_frame, width=10)

        self.test4_label.pack(side="left")
        self.test4_entry.pack(side="left")

        # create and pack the widgets for test 5
        self.test5_label = tkinter.Label(self.test5_frame, text="Enter the score for the test 5:")
        self.test5_entry = tkinter.Entry(self.test5_frame, width=10)

        self.test5_label.pack(side="left")
        self.test5_entry.pack(side="left")

        # create and pack the widgets for the average
        self.result_label = tkinter.Label(self.avg_frame, text="average:")
        self.avg = tkinter.StringVar()  # to update avg_label
        self.avg_label = tkinter.Label(self.avg_frame, textvariable=self.avg)

        self.result_label.pack(side="left")
        self.avg_label.pack(side="left")

        # create and pack the widgets for the total
        self.result_label = tkinter.Label(self.total_frame, text="total:")
        self.total = tkinter.StringVar()  # to update total_label
        self.total_label = tkinter.Label(self.total_frame, textvariable=self.total)

        self.result_label.pack(side="left")
        self.total_label.pack(side="left")

        # create and pack the button widgets
        self.calc_button = tkinter.Button(self.button_frame, text="Average", command=self.calc_avg)
        self.total_button = tkinter.Button(self.button_frame, text="Total", command=self.calc_total)
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy)

        self.calc_button.pack(side="left")
        self.total_button.pack(side="left")
        self.quit_button.pack(side="left")

        # pack the frames
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.test4_frame.pack()
        self.test5_frame.pack()
        self.avg_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack()

        # start the main loop
        tkinter.mainloop()

    # the calc_avg method is the callback function for the calc_button widget

    def calc_avg(self):
        # get the five test scores and store them in variables
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())
        self.test4 = float(self.test4_entry.get())
        self.test5 = float(self.test5_entry.get())

        # calculate the average
        self.average = (self.test1 + self.test2 + self.test3 + self.test4 + self.test5) / 5.0

        # update the avg_label widget by storing the value of self average in the StringVar object referenced by avg
        self.avg.set(self.average)

    def calc_total(self):
        # get the five test scores and store them in variables
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())
        self.test4 = float(self.test4_entry.get())
        self.test5 = float(self.test5_entry.get())

        # calculate the total
        self.total = self.test1 + self.test2 + self.test3 + self.test4 + self.test5

        # update the total_label widget by storing the value of self total in the StringVar object referenced by total
        self.total.set(self.total)


# create an instance of the TestAvg class
if __name__ == "__main__":
    test_avg = TestAvg()
    test_total = TestAvg()

''''
===============Output=================
Screen Shot 2023-05-13 at 3.35.05 PM

'''

# ====================================
# Attached: m14 Homework #14
# ====================================
# File: Project #3
# ====================================
# Name: Check Boxes
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program demonstrates group of Checkbutton widgets
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        # create two frames. One for the checkbuttons and another for the regular button widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create three IntVar objects to use with checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # set the intVar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        # create the checkbutton widgets in the top_frame
        self.cb1 = tkinter.CHECKBUTTON(self.top_frame, text="Option 1", variable=self.cb_var1)
        self.cb2 = tkinter.CHECKBUTTON(self.top_frame, text="Option 2", variable=self.cb_var2)
        self.cb3 = tkinter.CHECKBUTTON(self.top_frame, text="Option 3", variable=self.cb_var3)

        # pack the checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # create an OK button and a quit button
        self.ok_button = tkinter.Button(self.bottom_frame, text="OK", command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text="QUit", command=self.main_window.destroy)

        # pack the buttons
        self.ok_button.pack(side="left")
        self.quit_button.pack(side="left")

        # start the main loop
        tkinter.mainloop()

    # the show_choice method is the callback function for the OK button
    def show_choice(self):
        # create a message string
        self.message = "You selected: \n"

        # determine which Checkbuttons are selected and build the message string accordingly
        if self.cb_var1.get() == 1:
            self.message = self.message + "1\n"
        if self.cb_var2.get() == 2:
            self.message = self.message + "2\n"
        if self.cb_var3.get() == 3:
            self.message = self.message + "3\n"

        # display the message in an info dialog box
        tkinter.messagebox.showinfo("selection", self.message)


# create an instance of the MyGUI class
if __name__ == "__main__":
    my_gui = MyGUI

''''
===============Output=================
Screen Shot 2023-05-13 at 4.02.29 PM

'''


# ====================================
# Attached: m14 Homework #14
# ====================================
# File: Project #4
# ====================================
# Name: Check Boxes (Part 2)
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program demonstrates group of Checkbutton widgets


class MyGUI:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        # create two frames. One for the checkbuttons and another for the regular button widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create five IntVar objects to use with checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()

        # set the inVar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)

        # create the checkbutton widgets in the top frame
        self.cb1 = tkinter.CHECKBUTTON(self.top_frame, text="Option 1", variable=self.cb_var1)
        self.cb2 = tkinter.CHECKBUTTON(self.top_frame, text="Option 2", variable=self.cb_var2)
        self.cb3 = tkinter.CHECKBUTTON(self.top_frame, text="Option 3", variable=self.cb_var3)
        self.cb4 = tkinter.CHECKBUTTON(self.top_frame, text="Option 4", variable=self.cb_var4)
        self.cb5 = tkinter.CHECKBUTTON(self.top_frame, text="Option 5", variable=self.cb_var5)

        # pack the checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()

        # create an OK button and a quit button
        self.ok_button = tkinter.Button(self.bottom_frame, text="OK", command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text="QUit", command=self.main_window.destroy)

        # pack the buttons
        self.ok_button.pack(side="left")
        self.quit_button.pack(side="left")

        # start the main loop
        tkinter.mainloop()
        # the show_choice method is the callback function for the OK button

    def show_choice(self):
        # create a message string
        self.message = "You selected: \n"

        # determine which Checkbuttons are selected and build the message string accordingly
        if self.cb_var1.get() == 1:
            self.message = self.message + "1\n"
        if self.cb_var2.get() == 2:
            self.message = self.message + "2\n"
        if self.cb_var3.get() == 3:
            self.message = self.message + "3\n"
        if self.cb_var4.get() == 4:
            self.message = self.message + "4\n"
        if self.cb_var5.get() == 5:
            self.message = self.message + "5\n"

        # display the message in an info dialog box
        tkinter.messagebox.showinfo("selection", self.message)


# create an instance of the MyGUI class
if __name__ == "__main__":
    my_gui = MyGUI

''''
===============Output=================
Screen Shot 2023-05-13 at 4.15.21 PM

'''
