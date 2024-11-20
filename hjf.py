import mysql.connector

import customtkinter as ctk

from tkinter import messagebox

from tkcalendar import Calendar

from PIL import Image, ImageTk

import math

import subprocess

import sys


# Database connection setup
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='divya123',
        database='nitin'
    )
userdata={'name' :''}

k = '';


def latestmovies():
    o = connect_db()
    k = o.cursor()
    k.execute('select movie_title from movies order by release_date asc')
    l = k.fetchmany(4)
    return l

def popularmovies():
    o = connect_db()
    k = o.cursor()
    k.execute('select movie_title from movies order by viewers asc')
    l = k.fetchmany(4)
    return l

def bill(movie_name, price, seatnumber,food):
    ticket_content = f"Movie Ticket\n"
    ticket_content += f"-----------------------------\n"
    ticket_content += f"Movie Name: {movie_name}\n"
    ticket_content += f"Seats Selected: {', '.join(seatnumber)}\n"
    ticket_content += f"Food: {food}\n"
    ticket_content += f"Total Price: ${price}\n"
    ticket_content += f"-----------------------------\n"
    ticket_content += f"Thank you for your purchase!\n"

    # Write the ticket content to the file
    with open(f'{userdata["name"]}{movie_name}.txt', 'a') as file:
        file.write(ticket_content)
        file_path = f'{userdata["name"]}{movie_name}.txt'

        if sys.platform == "win32":
            subprocess.run(["start", file_path], shell=True)  # Windows
        elif sys.platform == "darwin":
            subprocess.run(["open", file_path])  # macOS
        else:
            subprocess.run(["xdg-open", file_path])  # Linux
    mainpageing()


def payment(movie, seatnumber , food):
    def payed():
        if len(cardid.get()) == 16 and len(pin.get())==4:
            payment_form.pack_forget()
            bill(movie, price,seatnumber,food)

    name = userdata['name']
    price = 0
    for i in seatnumber:
        price += 94
        if "A" in i or "B" in i:
            price += price * 0.05

    if food == 'Popcorn':
        price += 20
    elif food == 'Nachos':
        price += 30
    if "A" in seatnumber or "B" in seatnumber:
        price += price*0.05
    payment_form = ctk.CTkFrame(root , fg_color='#ffca00')
    payment_form.pack(fill='both', padx=20, pady=20, anchor='center')
    image = Image.open("logo.png")
    image = image.resize((135, 105))
    logo = ImageTk.PhotoImage(image)
    label = ctk.CTkLabel(payment_form, image=logo, text="", anchor="w", font=("Arial", 36, 'bold'))
    label.pack(anchor='center', padx=50, pady=5)
    header = ctk.CTkLabel(payment_form, text='Payment',text_color='black', font=('Helvetica', 36, 'bold'))
    header.pack(anchor='center', padx=10)
    Price = ctk.CTkLabel(payment_form, text=f'₹{ math.trunc(price * 100) / 100}', text_color='black', font=('Helvetica', 36, 'bold'))
    Price.pack(anchor='center', padx=10)
    cardid_label = ctk.CTkLabel(payment_form, text_color='black',text='Card Number')
    cardid_label.pack(anchor='center')
    cardid = ctk.CTkEntry(payment_form,fg_color='black')
    cardid.pack(anchor='center')
    pin_label = ctk.CTkLabel(payment_form, text_color='black', text='PIN Number')
    pin_label.pack(anchor='center')
    pin = ctk.CTkEntry(payment_form, fg_color='black')
    pin.pack(anchor='center')
    paybutton = ctk.CTkButton(payment_form , fg_color='black' , text='Pay', command=lambda: payed())
    paybutton.pack(anchor='center', pady=20)



def bookTicket(movie,l =0):
    form = ctk.CTkFrame(root , fg_color='transparent')
    form.pack(fill='both' , padx = 20 , pady=20)



    image = Image.open("logo.png")
    image = image.resize((135, 105))
    logo = ImageTk.PhotoImage(image)



    label = ctk.CTkLabel(form, image=logo, text="", anchor="w", font=("Arial", 36, 'bold'))
    label.pack(anchor='center', padx=10, pady=5)
    header = ctk.CTkLabel(form , text='Book Ticket' , font=('Helvetica' , 36 , 'bold'))
    header.pack(anchor='center',padx=10)
    personalinfo = ctk.CTkFrame(form, fg_color='black')
    personalinfo.pack(fill='both', padx=20, pady=20)
    personal = ctk.CTkFrame(personalinfo ,fg_color='transparent')


    # personal.pack(side='left' , padx=10)
    name_label = ctk.CTkLabel(personal, text="Personal Information", anchor="w", font=("Arial", 15))
    name_label.pack(fill="x", padx=2, pady=5)
    name_input = ctk.CTkEntry(personal)
    name_input.pack(pady=5)


    mail = ctk.CTkFrame(personalinfo, fg_color='transparent')
    mail.pack(side='left', padx=20)
    mail_label = ctk.CTkLabel(mail, text="Mail id", anchor="w", font=("Arial", 15))
    mail_label.pack(fill="x", padx=2, pady=5)


    mail_input = ctk.CTkEntry(mail)
    mail_input.pack(pady=5)
    kl = ctk.CTkFrame(form,fg_color='black')
    kl.pack(fill='both' ,padx = 10 , pady=10)
    standard = ctk.CTkFrame(kl, fg_color='transparent')
    standard.pack(side='left', padx=20)
    standard_label = ctk.CTkLabel(standard, text="Food Choice", anchor="w", font=("Arial", 15))
    standard_label.pack(fill="x", padx=2, pady=5)
    combobox = ctk.CTkComboBox(master=standard,
                                         values=['None',"Popcorn", "Nachos"],
                                   )
    combobox.pack(padx=2, pady=10)
    seat_frame = ctk.CTkFrame(form,fg_color='black')
    seat_frame.pack(padx=10, pady = 20)



    rows = 5
    cols = 6
    seatid = []



    def select_seat(seat_id,p):
        seatid.append(seat_id)
        p.configure(fg_color='black')





    # Create a grid of buttons representing the seats
    seat_buttons = []
    for row in range(rows):
        row_buttons = []
        for col in range(cols):
            seat_id = f"{chr(65 + row)}{col + 1}"  # e.g., A1, B2, C3
            seat_button = ctk.CTkButton(seat_frame, text=seat_id, width=50, height=40,
                                       )
            seat_button.configure( command=lambda seat=seat_id, button=seat_button: select_seat(seat, button))
            seat_button.grid(row=row, column=col, padx=5, pady=5)
            row_buttons.append(seat_button)
        seat_buttons.append(row_buttons)
    pay_button_form = ctk.CTkFrame(form, fg_color='#ffca00')
    pay_button_form.pack(fill='both')
    def payproceed():
        if seatid and mail_input.get():
            form.pack_forget()
            payment(movie, seatid, combobox.get())
            print(movie , seatid , combobox.get())
    paybutton = ctk.CTkButton(pay_button_form,text='Pay',fg_color='black' , text_color='white' , command=lambda:payproceed())
    paybutton.pack(pady = 10)









def login():
    username = entry_username.get()

    # Simple login validation (replace with your own logic)
    if username:
        userdata['name'] = username
        # Hide login page
        login_frame.pack_forget()

        # Show the main page
        mainpageing()
    else:
        pass


# Create the main window
root = ctk.CTk(fg_color='black')

# Set window title and size
root.title("Login Page")
root.geometry("1080x800")

# Create a frame for the login page
login_frame = ctk.CTkFrame(root,fg_color='black')
login_frame.pack(fill="both", expand=True)
image = Image.open("logo.png")
image = image.resize((270, 205))

logo = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(login_frame, image=logo, text="", anchor="w", font=("Arial", 36, 'bold') )
label.pack(anchor='center', padx=10, pady=5)

# Username label and entry
label_username = ctk.CTkLabel(login_frame, text="Username:")
label_username.pack(pady=(40, 5))

entry_username = ctk.CTkEntry(login_frame, placeholder_text="Enter Username")
entry_username.pack(pady=5)


# Login button
login_button = ctk.CTkButton(login_frame, text="Login", command=login)
login_button.pack(pady=20)

# Label to show result message

# Create the second frame (Main Page)


def mainpageing():
    def on_button_click( ticket_id):
        main_page.pack_forget()
        bookTicket(ticket_id)



    def srch():
        c = search_entry.get()
        o = connect_db()
        h = o.cursor()
        h.execute(f'select movie_title from movies where movie_title="{c}"')
        l = h.fetchone()




        if l:
            re = messagebox.askyesno('Found', 'Movie is available \n Would you like to book')
            if re:
                bookTicket(search_entry.get())
                main_page.pack_forget()
        else:
            messagebox.showinfo('Not found' , "Your movie is not found")




    root.title("TitanCinema")
    main_page = ctk.CTkFrame(root,fg_color='black')
    main_page.pack(fill="x", expand=False)
    image = Image.open("logo.png")
    image = image.resize((135, 105))
    logo = ImageTk.PhotoImage(image)
    label = ctk.CTkLabel(main_page, image=logo, text="", anchor="w", font=("Arial", 36, 'bold') )
    label.pack(anchor='center', padx=10, pady=5)



    image = Image.open("bg.jpg")
    image = image.resize((1080, 200))
    photo = ImageTk.PhotoImage(image)

    # Image label
    label_image = ctk.CTkLabel(main_page, image=photo, text=f'Welcome to TitanCinemas {userdata["name"]}',font=("Arial", 20, "bold"))
    label_image.pack(pady=(0,0))
    search_movie_frame = ctk.CTkFrame(main_page, fg_color='black')
    search_movie_frame.pack(fill="x", padx=20, pady=10)  # Adjust padding around the frame
    search_label = ctk.CTkLabel(search_movie_frame, text="Search Movies", anchor="w", font=("Arial", 36, 'bold'))
    search_label.pack(fill="x", padx=10, pady=5)



    search_entry = ctk.CTkEntry(search_movie_frame, width=180, placeholder_text="Enter movie name")
    search_entry.pack(side='left' , padx=10,pady=10)  # Positioning the text box closer to the top left corner

    # Create the button for search
    search_button = ctk.CTkButton(search_movie_frame, text="Search", command=srch)
    search_button.pack(side = 'left', padx=10 , pady=10)
    newfilm = ctk.CTkFrame(main_page, fg_color='transparent')
    newfilm.pack(fill="x", padx=20)
    label = ctk.CTkLabel(newfilm, text="New Movies", anchor="w", font=("Arial", 36, 'bold'))
    label.pack(fill="x", padx=10, pady=5)
    for i in latestmovies():
        button1 = ctk.CTkButton(newfilm, text=f"{i[0]}",command=lambda jk=i[0]: on_button_click(jk))
        button1.pack(side="left", padx=10, pady=10)





    popularfilm = ctk.CTkFrame(main_page, fg_color='transparent')
    popularfilm.pack(fill="x", padx=20, pady=20)
    label = ctk.CTkLabel(popularfilm, text="Popular Movies", anchor="w", font=("Arial", 36, 'bold'))
    label.pack(fill="x", padx=10, pady=5)
    # Create Buttons and pack them horizontally


    
    for i in popularmovies():
        button1 = ctk.CTkButton(popularfilm, text=f"{i[0]}",command=lambda jk=i[0]: on_button_click(jk))
        button1.pack(side="left", padx=10, pady=10)




# Run the application
root.mainloop()