import mysql.connector
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar


# Database connection setup
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='divya123',
        database='nitin'
    )


# Login Function
def login():
    cn = connect_db()
    cursor = cn.cursor()

    username = u1.get()
    password = ''

    if username :
        show_main_menu(cursor, cn)
    else:
        messagebox.showerror("Login", "Invalid Username or Password")


# Main Menu after login
def show_main_menu(cursor, cn):
    for widget in root.winfo_children():
        widget.destroy()

    ctk.CTkLabel(root, text='WELCOME TO MOVIE TICKET BOOKING', font=('Arial', 18)).pack(pady=10)

    ctk.CTkButton(root, text='1. BOOKING COUNTER', command=lambda: booking_counter(cursor, cn)).pack(pady=5)
    db = connect_db()
    cu = db.cursor()
    cu.execute('select * from movies')
    k = cu.fetchall()
    for i, data in enumerate(k):
    # Add the first set of buttons with dynamic text from `data[0]`
        ctk.CTkButton(root, text=f'{data[0]}', command=lambda data=data: all_booking_details(data[0])).grid(row=0, column=i, padx=10, pady=10)

# Add the second and third buttons in the same row (row=0)
    ctk.CTkButton(root, text='2. ALL BOOKING DETAILS', command=lambda: all_booking_details(cursor)).grid(row=0, column=i+1, padx=10, pady=10)
    ctk.CTkButton(root, text='EXIT', command=root.quit).grid(row=0, column=i+2, padx=10, pady=10)



# Booking Counter for ticket booking
def booking_counter(cursor, cn):
    for widget in root.winfo_children():
        widget.destroy()

    def book_ticket():
        name_val = name.get()
        contact_val = contact.get()
        city_val = city.get()
        theater_val = theater.get()
        language_val = language.get()
        movie_val = movie.get()
        m_date_val = cal.get_date()
        seat_val = int(seat.get())
        price_val = 250 * seat_val

        booking_query = f"""
        INSERT INTO booking (name, contact, city, theater, language, movie, date, seats, price)
        VALUES ('{name_val}', '{contact_val}', '{city_val}', '{theater_val}', '{language_val}', 
                '{movie_val}', '{m_date_val}', {seat_val}, {price_val})
        """
        cursor.execute(booking_query)
        cn.commit()
        messagebox.showinfo("Booking", "Successfully Booked! Enjoy the Movie!")

    # Booking Entry UI
    ctk.CTkLabel(root, text='BOOKING COUNTER', font=('Arial', 16)).pack(pady=10)

    ctk.CTkLabel(root, text='Enter Your Name:').pack(pady=5)
    name = ctk.CTkEntry(root)
    name.pack(pady=5)

    ctk.CTkLabel(root, text='Enter Your Contact No.:').pack(pady=5)
    contact = ctk.CTkEntry(root)
    contact.pack(pady=5)

    ctk.CTkLabel(root, text='Enter Your City:').pack(pady=5)
    city = ctk.CTkEntry(root)
    city.pack(pady=5)

    ctk.CTkLabel(root, text='In Which Theater Do You Wish to See Movie:').pack(pady=5)
    theater = ctk.CTkEntry(root)
    theater.pack(pady=5)

    ctk.CTkLabel(root, text='In Which Language Do You Wish to See Movie:').pack(pady=5)
    language = ctk.CTkEntry(root)
    language.pack(pady=5)

    ctk.CTkLabel(root, text='Which Movie Do You Want to Watch:').pack(pady=5)
    movie = ctk.CTkEntry(root)
    movie.pack(pady=5)

    ctk.CTkLabel(root, text='When Do You Wish to Watch Movie:').pack(pady=5)
    cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.pack(pady=20)

    ctk.CTkLabel(root, text='How Many Tickets Do You Want to Book:').pack(pady=5)
    seat = ctk.CTkEntry(root)
    seat.pack(pady=5)

    ctk.CTkButton(root, text="Book Now", command=book_ticket).pack(pady=20)
    ctk.CTkButton(root, text="Back to Main Menu", command=lambda: show_main_menu(cursor, cn)).pack(pady=10)


# View All Booking Details
def all_booking_details(cursor):
    for widget in root.winfo_children():
        widget.destroy()

    cn = connect_db()
    cursor = cn.cursor()
    cursor.execute('SELECT * FROM booking')
    records = cursor.fetchall()

    ctk.CTkLabel(root, text='All Booking Details', font=('Arial', 16)).pack(pady=10)

    for record in records:
        ctk.CTkLabel(root, text=record).pack(pady=5)

    ctk.CTkButton(root, text="Back to Main Menu", command=lambda: show_main_menu(cursor, cn)).pack(pady=20)


# Setting up the login screen
root = ctk.CTk()
root.title('Movie Ticket Booking System')
root.geometry('400x300')  # Set the window size

# Create a frame to hold all the widgets and center them
frame = ctk.CTkFrame(root)
frame.pack(expand=True)  # Expand the frame to fill available space and center the content

# Title label
ctk.CTkLabel(frame, text='MOVIE TICKET BOOKING SYSTEM', font=('Arial', 18)).pack(pady=10)

# Sub-title label (LOGIN)
ctk.CTkLabel(frame, text='LOGIN', font=('Arial', 14)).pack(pady=5)

# Username input
ctk.CTkLabel(frame, text='Enter Name').pack(pady=5)
u1 = ctk.CTkEntry(frame)
u1.pack(pady=5)


# Buttons
ctk.CTkButton(frame, text='Login', command=login).pack(pady=20)
ctk.CTkButton(frame, text='Exit', command=root.quit).pack(pady=5)

# Start the GUI
root.mainloop()
