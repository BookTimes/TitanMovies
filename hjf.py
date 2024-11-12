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
root = ctk.CTk()

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
    search_movie_frame = ctk.CTkFrame(main_page , fg_color='black')
    search_movie_frame.pack(fill="x", padx=20)  # Center the frame in the window

    # Create the text box (Entry widget) for entering movie name
    search_entry = ctk.CTkEntry(search_movie_frame, width=200, placeholder_text="Enter movie name")
    search_entry.place(x=10, y=10)  # Positioning text box

    # Create the button for search
    search_button = ctk.CTkButton(search_movie_frame, text="Search")
    search_button.place(x=220, y=10)
    newfilm = ctk.CTkFrame(main_page, fg_color='transparent')
    newfilm.pack(fill="x", padx=20, pady=20)
    label = ctk.CTkLabel(newfilm, text="New Movies", anchor="w", font=("Arial", 36, 'bold'))
    label.pack(fill="x", padx=10, pady=5)
    # Create Buttons and pack them horizontally
    button1 = ctk.CTkButton(newfilm, text="ARM")
    button1.pack(side="left", padx=10, pady=10)

    button2 = ctk.CTkButton(newfilm, text="Venom")
    button2.pack(side="left", padx=10, pady=10)

    button3 = ctk.CTkButton(newfilm, text="Stree 2")
    button3.pack(side="left", padx=10, pady=10)

    popularfilm = ctk.CTkFrame(main_page, fg_color='transparent')
    popularfilm.pack(fill="x", padx=20, pady=20)
    label = ctk.CTkLabel(popularfilm, text="Popular Movies", anchor="w", font=("Arial", 36, 'bold'))
    label.pack(fill="x", padx=10, pady=5)
    # Create Buttons and pack them horizontally
    button1 = ctk.CTkButton(popularfilm, text="Pani")
    button1.pack(side="left", padx=10, pady=10)

    button2 = ctk.CTkButton(popularfilm, text="Lucky Bhaskar")
    button2.pack(side="left", padx=10, pady=10)

    button3 = ctk.CTkButton(popularfilm, text="Uljah")
    button3.pack(side="left", padx=10, pady=10)




# Run the application
root.mainloop()