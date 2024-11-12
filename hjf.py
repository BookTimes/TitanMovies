import mysql.connector
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk



# Database connection setup
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='divya123',
        database='nitin'
    )
userdata={'name' :''}




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

def bookTicket(movie):
    form = ctk.CTkFrame(root , fg_color='transparent')
    form.pack(fill='both' , padx = 20 , pady=20)
    image = Image.open("logo.png")
    image = image.resize((135, 105))
    logo = ImageTk.PhotoImage(image)
    label = ctk.CTkLabel(form, image=logo, text="", anchor="w", font=("Arial", 36, 'bold'))
    label.pack(anchor='center', padx=10, pady=5)
    header = ctk.CTkLabel(form , text='Book Ticket' , font=('Helvetica' , 36 , 'bold'))
    header.pack(anchor='center',padx=10)
    personal = ctk.CTkFrame(form ,fg_color='transparent')
    personal.pack(side='left' , padx=10)
    name_label = ctk.CTkLabel(personal, text="Personal Information", anchor="w", font=("Arial", 15))
    name_label.pack(fill="x", padx=2, pady=5)
    name_input = ctk.CTkEntry(personal)
    name_input.pack(pady=5)
    mail = ctk.CTkFrame(form, fg_color='transparent')
    mail.pack(side='left', padx=20)
    mail_label = ctk.CTkLabel(mail, text="Mail id", anchor="w", font=("Arial", 15))
    mail_label.pack(fill="x", padx=2, pady=5)
    mail_input = ctk.CTkEntry(mail)
    mail_input.pack(pady=5)





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
    # Load image for the main page
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
    # Create the text box (Entry widget) for entering movie name
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
        button1 = ctk.CTkButton(newfilm, text=f"{i[0]}")
        button1.pack(side="left", padx=10, pady=10)


    popularfilm = ctk.CTkFrame(main_page, fg_color='transparent')
    popularfilm.pack(fill="x", padx=20, pady=20)
    label = ctk.CTkLabel(popularfilm, text="Popular Movies", anchor="w", font=("Arial", 36, 'bold'))
    label.pack(fill="x", padx=10, pady=5)
    # Create Buttons and pack them horizontally
    for i in popularmovies():
        button1 = ctk.CTkButton(popularfilm, text=f"{i[0]}")
        button1.pack(side="left", padx=10, pady=10)




# Run the application
root.mainloop()