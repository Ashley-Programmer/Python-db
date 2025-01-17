from customtkinter import *
import mysql.connector
from tkinter import messagebox

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='python_register'
    )
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='python_register'
    )
    if conn.is_connected():
        print("Connected to database")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Register function
def register_user(username, email, password):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users_db (username, email, password) VALUES (%s, %s, %s)", 
                       (username, email, password))
        connection.commit() # save changes to the database
        messagebox.showinfo("Success", "User registered successfully!")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error occurred: {error}")
    finally:
        cursor.close()
        connection.close()

# Login function
def login_user(email, password):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT password FROM users_db WHERE email=%s", (email,))
        result = cursor.fetchone()  # fetch first row (password for login)
        if result and result[0] == password:
            messagebox.showinfo("Success", "Logged in successfully!")
        elif  not result:
            messagebox.showerror("Error", "Email not found!")
        elif result[0]  != password:
            messagebox.showerror("Error", "Incorrect password!")
        elif len(password) < 8:
            messagebox.showerror("Error!", "Password must be at least 8 or more characters!")
        else:
            messagebox.showerror("Error", "Invalid email or password")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error occurred: {error}")
    finally:
        cursor.close()
        connection.close()

# register form validation
def validate_form(username, email, password, confirm_password):
    if not username or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
        return False
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return False
    elif len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 or more characters!")
        return False
    return True

# login form validation
def validate_form2(email, password):
    if not email or not password:
        messagebox.showerror("Error!", "All fields are required!")
        return False
    elif len(password) < 8:
        messagebox.showerror("Error!", "Password must be at least 8 or more characters!")
        return False
    return True

# def register_and_redirect
def register_and_redirect():
    if validate_form(nameEntry.get(), emailEntry.get(), passEntry.get(), cpassEntry.get()):
        register_user(nameEntry.get(), emailEntry.get(), passEntry.get())
        login_page()

def login_and_redirect():
    if validate_form2(emailEntry.get(), passEntry.get()):
        login_user(emailEntry.get(), passEntry.get())
        manage_user_page()


def signup_page():
    loginFrame.grid_forget()
    signup_window.title("Sign Up Window")
    signup_window.geometry('440x500+500+100')
    signupFrame.grid(row=0, column=0, pady=40, padx=60)


def manage_user_page():
    global  manage_user_frame

    loginFrame.grid_forget()
    signup_window.title("Manage User Window")
    signup_window.geometry('500x470+480+100')
    
    signupFrame.grid_forget()
    signup_window.title('Manage users Window')
    
    signup_window.geometry('550x300+500+100')
    
    manage_frame = CTkFrame(signup_window)
    manage_frame.grid(row=0, column=0, pady=40, padx=120)
    manage_frame.configure(fg_color='#fff')
    
    Heading_label = CTkLabel(manage_frame, text='Manage user data',
                             font=('algerian', 30, 'bold'), text_color='green')
    Heading_label.grid(row=0, column=0, pady=(0, 40))
    
    # Create a button to display user data
    display_button = CTkButton(manage_frame, text='Show/Pop up User Data',
                                command=display_user_data)
    display_button.grid(row=1, column=0, pady=20)
    
    manage_frame.grid_rowconfigure(1, weight=1)
    
def load_data_from_db():
    # Connect to the database
    connection = connect_db()
    cursor = connection.cursor()

    # Execute a query to fetch user data
    query = "SELECT id, username, email, password FROM users_db"  # Adjust the query as per your table structure
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the database connection
    cursor.close()
    connection.close()

    return rows

def display_user_data():
    # Load user data from the database
    user_data = load_data_from_db()
    
    if user_data:
        # Prepare message box content
        message = "User Data:\n"
        for row in user_data:
            message += f"ID Number: {row[0]}\n, Name: {row[1]}, Email: {row[2]}\n\n"
    else:
        message = "No user data found."

    # Display the message box with user data
    messagebox.showinfo("User Data:::::\n", message)


# function section:
def login_page():
    global loginFrame
    
    signupFrame.grid_forget()
    signup_window.title('Login Window')
    
    signup_window.geometry('450x400+500+100')
    
    loginFrame = CTkFrame(signup_window)
    loginFrame.grid(row=0, column=0, pady=40, padx=25)
    loginFrame.configure(fg_color='#fff')
    
    Heading_label = CTkLabel(loginFrame, text='Welcome back Login Now!',
                             font=('bookman old style', 30, 'bold'), text_color='green')

    Sub_heading_label = CTkLabel(loginFrame, text='Login as a member!.',
                                 font=('bookman old style', 18), text_color='black')
    Heading_label.grid(row=0, column=0)
    Sub_heading_label.grid(row=1, column=0, pady=(0, 40))
    
    EmailEntry = CTkEntry(loginFrame, placeholder_text='Enter email here...',
                          font=('bookman old style', 15), text_color='black', height=40, width=350)
    PassEntry = CTkEntry(loginFrame, placeholder_text='Enter password here...',
                         font=('bookman old style', 15), text_color='black', height=40, width=350, show="*")
    
    EmailEntry.grid(row=3, column=0, pady=(0, 20))
    EmailEntry.configure(fg_color='#f5f5f5', bg_color='#000', border_color='#000')

    PassEntry.grid(row=4, column=0, pady=(0, 20))
    PassEntry.configure(fg_color='#f5f5f5', bg_color='#000', border_color='#000')
    
    btnLogin = CTkButton(loginFrame, text='LOGIN', 
                      font=('bookman old style', 15, 'bold'), 
                      text_color='white', hover_color='darkgreen', height=40 ,width=320, cursor='hand2', 
                      command=lambda: (
                              validate_form2(EmailEntry.get(), PassEntry.get()) and
                              login_user(EmailEntry.get(), PassEntry.get()) and
                              login_and_redirect()
                      )
)
    
    btnLogin.grid(row=6, column=0, pady=(0, 20))
    btnLogin.configure(fg_color='green')
    
    Frame = CTkFrame(loginFrame, fg_color='#fff')
    Frame.grid(row=7, column=0)
    
    label = CTkLabel(Frame, text="Not a member yet?", font=('bookman old style', 13), text_color='#000')
    label.grid(row=0, column=0)
    label.configure(fg_color='white')
    
    Login_here = CTkButton(Frame, text='SignUp here',
                           font=('bookman old style', 15, 'underline'),
                           text_color='darkgreen', hover_color='#fff', cursor='hand2',
                           command=signup_page)

    
    Login_here.grid(row=0, column=1)
    Login_here.configure(fg_color='#fff')
    
    frameOne = CTkFrame(loginFrame, fg_color='#fff')
    frameOne.grid(row=8, column=0)
    lblOne =  CTkLabel(frameOne, text='Main form', font=('arial', 12), text_color='#000')
    lblOne.grid(row=0, column=0)
    lblOne.configure(fg_color="#fff")
    main = CTkButton(frameOne, text='Main form', font=('arial', 14, 'underline'), text_color='darkgreen',
                     hover_color='#fff', cursor='hand2', command=manage_user_page)
    main.grid(row=0, column=1)
    main.configure(fg_color='#fff')
    
# sign up
# GUI Section:

signup_window = CTk()

# set the title
signup_window.title('Sign Up Window')

# change background color of window
signup_window.configure(fg_color='white')

# width and height of the window and the distance of x:500, y-axis:100
signup_window.geometry('440x500+500+100') # width = 440, height = 500

#disable the maximise button
signup_window.resizable(False, False)

# create a frame using frame class to place anything inside
# make its object (signupFrame)
signupFrame = CTkFrame(signup_window)

# frame color too
signupFrame.configure(fg_color='white')
signupFrame.grid(row=0, column=0, pady=40, padx=60)

# make a label inside the signupFrame
heading_label = CTkLabel(signupFrame, text='Join Us Today!',
                         font=('bookman old style', 40, 'bold'), text_color='green')

sub_heading_label = CTkLabel(signupFrame, text='Sign Up to be a member!.',
                         font=('bookman old style', 15), text_color='#000')

heading_label.grid(row=0, column=0)
sub_heading_label.grid(row=1, column=0, pady=(0, 40))

nameEntry = CTkEntry(signupFrame, placeholder_text='Enter username here...',
                     font=('bookman old style', 15), text_color='black', height=40, width=320)
emailEntry = CTkEntry(signupFrame, placeholder_text='Enter email here...',
                     font=('bookman old style', 15), text_color='black', height=40, width=320)
passEntry = CTkEntry(signupFrame, placeholder_text='Enter password here...',
                     font=('bookman old style', 15), text_color='black', height=40, width=320, show="*")
cpassEntry = CTkEntry(signupFrame, placeholder_text='Confirm password here...',
                      font=('bookman old style', 15), text_color='black', height=40, width=320, show="*")

                      
nameEntry.grid(row=2, column=0, pady=(0, 20))
nameEntry.configure(fg_color='#f5f5f5', bg_color='#000', border_color='#000')

emailEntry.grid(row=3, column=0, pady=(0, 20))
emailEntry.configure(fg_color='#f5f5f5', bg_color='#000', border_color='#000')

passEntry.grid(row=4, column=0, pady=(0, 20))
passEntry.configure(fg_color='#f5f5f5', bg_color='#000', border_color='#000')

cpassEntry.grid(row=5, column=0, pady=(0, 20))
cpassEntry.configure(fg_color='#f5f5f5', bg_color='#000', border_color='#000')

# create variable btnSignUp to make button
btnSignUp = CTkButton(signupFrame, text='SIGN UP', 
                      font=('bookman old style', 15, 'bold'), 
                      text_color='white', hover_color='darkgreen', height=40 ,width=320, cursor='hand2', 
                      command=lambda: (
                          register_and_redirect() and
                          validate_form(nameEntry.get(), emailEntry.get(), passEntry.get(), cpassEntry.get()) and
                          register_user(nameEntry.get(), emailEntry.get(), passEntry.get())
                      )
)



btnSignUp.grid(row=6, column=0, pady=(0, 20))
btnSignUp.configure(fg_color='green')

#create another frame
frame = CTkFrame(signupFrame, fg_color='#fff')
frame.grid(row=7, column=0)

# place a label inside it
lbl = CTkLabel(frame, text='Already have an account?', font=('bookman old style', 13), text_color='#000')
lbl.grid(row=0, column=0)
lbl.configure(fg_color='white')

login_here = CTkButton(frame, text='Login here', 
                       font=('bookman old style', 15, 'underline'),
                       text_color='darkgreen', hover_color='#fff', cursor='hand2', command=login_page)
login_here.grid(row=0, column=1)
login_here.configure(fg_color='#fff')

signup_window.mainloop()