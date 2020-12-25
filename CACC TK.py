from tkinter import *

mainColor = bg = 'navajo white'
secondColor = fg = 'black'


def login():
    # Whatever you want to change
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    empty_label2.config(text='* Your username or password is incorrect', fg='red')


root_window = Tk()
root_window.title('College Admission Chance Calculator')
root_window.geometry('450x450')
root_window.config(bg=mainColor)


def open_register_window():
    root_window.withdraw()
    register_window = Toplevel()
    register_window.title('Register')
    register_window.geometry('550x550')
    register_window.config(bg=mainColor)

    font = 13
    empty_label3 = Label(register_window, text='', bg=mainColor)
    empty_label3.grid(row=1, column=3)
    empty_label4 = Label(register_window, text='', bg=mainColor)
    empty_label4.grid(row=2, column=3)
    empty_label5 = Label(register_window, text='', bg=mainColor)
    empty_label5.grid(row=3, column=3)
    empty_label6 = Label(register_window, text='', bg=mainColor)
    empty_label6.grid(row=4, column=5)

    # LABELS

    name_label = Label(register_window, text='First Name: ', bg=mainColor, fg=secondColor, font=('Arial', font, 'bold'))
    name_label.grid(row=5, column=2)
    empty_label7 = Label(register_window, text='', bg=mainColor)
    empty_label7.grid(row=6, column=1)
    last_name_label = Label(register_window, text='Last Name: ', bg=mainColor, fg=secondColor, font=('Arial', font,
                                                                                                     'bold'))
    last_name_label.grid(row=7, column=2)
    empty_label8 = Label(register_window, text='', bg=mainColor)
    empty_label8.grid(row=8, column=1)
    email_label = Label(register_window, text='Email: ', bg=mainColor, fg=secondColor, font=('Arial', font, 'bold'))
    email_label.grid(row=9, column=2)
    empty_label9 = Label(register_window, text='', bg=mainColor)
    empty_label9.grid(row=10, column=1)
    username_label = Label(register_window, text='Username: ', bg=mainColor, fg=secondColor,
                           font=('Arial', font, 'bold'))
    username_label.grid(row=11, column=2)
    empty_label9 = Label(register_window, text='', bg=mainColor)
    empty_label9.grid(row=12, column=1)
    password_label = Label(register_window, text='Password: ', bg=mainColor, fg=secondColor,
                           font=('Arial', font, 'bold'))
    password_label.grid(row=13, column=2)
    empty_label10 = Label(register_window, text='', bg=mainColor)
    empty_label10.grid(row=14, column=1)
    password_again_label = Label(register_window, text='Enter your password again: ', bg=mainColor, fg=secondColor,
                                 font=('Arial', font, 'bold'))
    password_again_label.grid(row=15, column=2)
    sat_score_label = \
        Label(register_window, text='SAT Score: ', bg=mainColor, fg=secondColor, font=('Arial', font, 'bold'))
    sat_score_label.place(x=77, y=360)
    empty_label11 = Label(register_window, text=' ', bg=mainColor, fg='red', font=('Arial', 7, 'italic'))
    empty_label11.place(x=220, y=380)
    gpa_label = \
        Label(register_window, text='Weighted GPA: ', bg=mainColor, fg=secondColor, font=('Arial', font, 'bold'))
    gpa_label.place(x=66, y=400)
    empty_label13 = Label(register_window, text='', bg=mainColor, fg='red', font=('Arial', 7, 'italic'))
    empty_label13.place(x=223, y=420)

    # ENTRIES

    first_name_entry = Entry(register_window, width=25, bg=secondColor, fg=mainColor)
    first_name_entry.grid(row=5, column=5)
    last_name_entry = Entry(register_window, width=25, bg=secondColor, fg=mainColor)
    last_name_entry.grid(row=7, column=5)
    email_entry = Entry(register_window, width=25, bg=secondColor, fg=mainColor)
    email_entry.grid(row=9, column=5)
    username_create_entry = Entry(register_window, width=25, bg=secondColor, fg=mainColor)
    username_create_entry.grid(row=11, column=5)
    password_create_entry = Entry(register_window, width=25, bg=secondColor, fg=mainColor)
    password_create_entry.grid(row=13, column=5)
    password_again_entry = Entry(register_window, width=25, bg=secondColor, fg=mainColor)
    password_again_entry.grid(row=15, column=5)
    sat_score_entry = Entry(register_window, width=25, bg=secondColor, fg=mainColor)
    sat_score_entry.place(x=242, y=360)
    gpa_entry = Entry(register_window, width=25, bg=secondColor, fg=mainColor)
    gpa_entry.place(x=242, y=400)

    empty_label12 = Label(register_window, text='', bg=mainColor)
    empty_label12.grid(row=16, column=5)

    def open_main_window():
        if password_create_entry.get() != password_again_entry.get():
            empty_label12.config(text="Your passwords don't match", bg=mainColor, fg='red', font=('Arial', 9, 'italic'))
        else:
            if float(sat_score_entry.get()) > 1600 or float(sat_score_entry.get()) < 400:
                empty_label11.config(text="*Make sure you entered your SAT score right")
            else:
                if float(gpa_entry.get()) > 5:
                    empty_label13.config(text='**Make sure you entered your GPA right')

                else:
                    register_window.withdraw()
                    empty_label12.config(text='')
                    main_window = Toplevel()
                    main_window.title('Main Page')
                    main_window.geometry('550x570')
                    main_window.config(bg=mainColor)
                    welcome_label = Label(main_window, text='Welcome!', bg=mainColor, fg=secondColor,
                                          font=('Arial', 20, 'bold'))
                    welcome_label.place(x=200, y=10)
                    choose_uni_label = Label(main_window,
                                             text='Choose the university you want to calculate your admission chance.',
                                             bg=mainColor, fg=secondColor, font=('Arial', 11, 'bold'))
                    choose_uni_label.place(x=20, y=50)

                    # LABELS

                    your_place_label = Label(main_window, text='Your place in percentile based on your ', bg=mainColor,
                                             fg=secondColor,
                                             font=('Arial', 15, 'bold'))
                    your_place_label.place(x=80, y=330)
                    your_place_label.place_forget()

                    sat_result_label = Label(main_window, text='SAT: ', bg=mainColor, fg=secondColor,
                                             font=('Arial', 15, 'bold'))
                    sat_result_label.place(x=100, y=400)
                    sat_result_label.place_forget()
                    gpa_result_label = Label(main_window, text='GPA: ', bg=mainColor, fg=secondColor,
                                             font=('Arial', 15, 'bold'))
                    gpa_result_label.place(x=100, y=450)
                    gpa_result_label.place_forget()

                    sat_result_number_label = \
                        Label(main_window, text=' ', bg=mainColor, fg=secondColor, font=('Arial', 15, 'bold'))
                    sat_result_number_label.place(x=300, y=380)
                    sat_result_number_label.place_forget()

                    gpa_result_number_label = \
                        Label(main_window, text=' ', bg=mainColor, fg=secondColor, font=('Arial', 15, 'bold'))
                    gpa_result_number_label.place(x=300, y=40)
                    gpa_result_number_label.place_forget()

                    sat_score = sat_score_entry.get()
                    gpa_score = gpa_entry.get()

                    def uptade():
                        sat_score = scala.get()
                        gpa_score = scala2.get()

                    def show_label():
                        your_place_label.place(x=80, y=330)
                        sat_result_label.place(x=50, y=410)
                        gpa_result_label.place(x=50, y=460)
                        sat_result_number_label.place(x=120, y=410)
                        gpa_result_number_label.place(x=120, y=460)

                    def show_scales():
                        scala.place(x=250, y=375)
                        scala2.place(x=250, y=430)
                        uptade_button.place(x=180, y=520)

                    def calculate_harvard():
                        show_scales()
                        show_label()
                        sat_result_number_label.config(text='{:.3f} %'.format(float(sat_score) * 50 / 1520))
                        gpa_result_number_label.config(text='{:.3f} %'.format(float(gpa_score) * 50 / 4.18))

                    def calculate_yale():
                        show_scales()
                        show_label()
                        sat_result_number_label.config(text='{:.3f} %'.format(float(sat_score) * 50 / 1515))
                        gpa_result_number_label.config(text='{:.3f} %'.format(float(gpa_score) * 50 / 4.14))

                    def calculate_princeton():
                        show_scales()
                        show_label()
                        sat_result_number_label.config(text='{:.3f} %'.format(float(sat_score) * 50 / 1505))
                        gpa_result_number_label.config(text='{:.3f} %'.format(float(gpa_score) * 50 / 3.9))

                    def calculate_columbia():
                        show_scales()
                        show_label()
                        sat_result_number_label.config(text='{:.3f} %'.format(float(sat_score) * 50 / 1505))
                        gpa_result_number_label.config(text='{:.3f} %'.format(float(gpa_score) * 50 / 4.12))

                    def calculate_brown():
                        show_scales()
                        show_label()
                        sat_result_number_label.config(text='{:.3f} %'.format(float(sat_score) * 50 / 1485))
                        gpa_result_number_label.config(text='{:.3f} %'.format(float(gpa_score) * 50 / 4.08))

                    def calculate_dartmouth():
                        show_scales()
                        show_label()
                        sat_result_number_label.config(text='{:.3f} %'.format(float(sat_score) * 50 / 1500))
                        gpa_result_number_label.config(text='{:.3f} %'.format(float(gpa_score) * 50 / 4.11))

                    def calculate_upenn():
                        show_scales()
                        show_label()
                        sat_result_number_label.config(text='{:.3f} %'.format(float(sat_score) * 50 / 1500))
                        gpa_result_number_label.config(text='{:.3f} %'.format(float(gpa_score) * 50 / 3.9))

                    def calculate_cornell():
                        show_scales()
                        show_label()
                        sat_result_number_label.config(text='{:.3f} %'.format(float(sat_score) * 50 / 1480))
                        gpa_result_number_label.config(text='{:.3f} %'.format(float(gpa_score) * 50 / 4.07))

                    # UNI BUTTONS
                    harvard_button = \
                        Button(main_window, text='Harvard University', padx=40, pady=5, bg=secondColor, fg=mainColor)
                    harvard_button.config(command=calculate_harvard)
                    harvard_button.place(x=20, y=90)
                    yale_button = \
                        Button(main_window, text='Yale University', padx=51, pady=5, bg=secondColor, fg=mainColor)
                    yale_button.config(command=calculate_yale)
                    yale_button.place(x=20, y=150)
                    princeton_button = \
                        Button(main_window, text='Princeton University', padx=37, pady=5, bg=secondColor, fg=mainColor)
                    princeton_button.config(command=calculate_princeton)
                    princeton_button.place(x=20, y=210)
                    columbia_button = \
                        Button(main_window, text='Columbia University', padx=37, pady=5, bg=secondColor, fg=mainColor)
                    columbia_button.config(command=calculate_columbia)
                    columbia_button.place(x=20, y=270)
                    brown_button = \
                        Button(main_window, text='Brown University', padx=40, pady=5, bg=secondColor, fg=mainColor)
                    brown_button.config(command=calculate_brown)
                    brown_button.place(x=300, y=90)
                    dartmouth_button = \
                        Button(main_window, text='Dartmouth University', padx=28, pady=5, bg=secondColor, fg=mainColor)
                    dartmouth_button.config(command=calculate_dartmouth)
                    dartmouth_button.place(x=300, y=150)
                    pennsylvania_button = \
                        Button(main_window, text=' University of Pennsylvania', padx=15, pady=5, bg=secondColor,
                               fg=mainColor)
                    pennsylvania_button.config(command=calculate_upenn)
                    pennsylvania_button.place(x=300, y=210)
                    cornell_button = \
                        Button(main_window, text='Cornell University', padx=40, pady=5, bg=secondColor, fg=mainColor)
                    cornell_button.config(command=calculate_cornell)
                    cornell_button.place(x=300, y=270)

                    scala = Scale(main_window, from_=1200, to=1600, orient=HORIZONTAL, bg=mainColor, fg=secondColor,
                                  troughcolor='black', sliderlength=10, highlightbackground=mainColor, length=210,
                                  label='         Want to try another score?', resolution=10)
                    scala.place(x=250, y=375)
                    scala.place_forget()

                    scala2 = Scale(main_window, from_=0, to=5, orient=HORIZONTAL, bg=mainColor, fg=secondColor,
                                   troughcolor='black', sliderlength=10, highlightbackground=mainColor, length=210,
                                   label='         Want to try another score?', resolution=0.05)
                    scala2.place(x=250, y=430)
                    scala2.place_forget()

                    uptade_button = Button(main_window, text='Uptade', padx=40, pady=5, bg=secondColor, fg=mainColor)
                    uptade_button.config(command=uptade)
                    uptade_button.place(x=180, y=520)
                    uptade_button.place_forget()

    register_button_2nd = Button(register_window, text='Register', padx=40, pady=5, bg=secondColor, fg=mainColor)
    register_button_2nd.config(command=open_main_window)
    register_button_2nd.place(x=200, y=460)

    register_window.mainloop()


# PLEASE SIGN IN FIRST

signInLabel = Label(text='Please, sign in first.', bg=mainColor, fg=secondColor, font=('Arial', 16, 'bold'))
signInLabel.pack()

empty_label1 = Label(text='', font=2, bg=mainColor)
empty_label1.pack()

# ENTRY
username_entry = Entry(width=35, bg=secondColor, fg=mainColor)
username_entry.pack()
username_entry.insert(0, 'Enter your username')

password_entry = Entry(width=35, bg=secondColor, fg=mainColor)
password_entry.pack()
password_entry.insert(0, 'Enter your password')

empty_label2 = Label(text='', bg=mainColor, fg=secondColor, font=('Arial', 8, 'italic'))
empty_label2.pack()

# LOGIN

login_button = Button(text='Log in', padx=20, pady=5, bg=secondColor, fg=mainColor)
login_button.config(command=login)  # Whe THIS is clicked, what you want to happen.
login_button.pack()

labelDontHaveAcc = Label(text="Don't have an account?", bg=mainColor, fg=secondColor, font=('Arial', 11, 'italic',))
labelDontHaveAcc.pack()

register_button = Button(text='Register', padx=20, pady=5, bg=secondColor, fg=mainColor)
register_button.config(command=open_register_window)
register_button.pack()

root_window.mainloop()
