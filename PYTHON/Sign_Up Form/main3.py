from customtkinter import *
import mysql.connector
from tkinter import messagebox

# Database connection function
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='python_register'
    )
# Test connection to the database
try:
    conn = connect_db()
    if conn.is_connected():
        print("Connected to database")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Register function
def register_user(username, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users_db (username, email, password) VALUES (%s, %s, %s)", 
                       (username, email, password))
        conn.commit() # save changes to the database
        messagebox.showinfo("Success", "User registered successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

# Login function
def login_user(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT password FROM users_db WHERE email=%s", (email,))
        result = cursor.fetchone()  # fetch first row (password for login)
        if result and result[0] == password:
            messagebox.showinfo("Success", "Logged in successfully!")
        elif not result:
            messagebox.showerror("Error", "Email not found!")
        elif result[0] != password:
            messagebox.showerror("Error", "Incorrect password!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

# Register form validation
def validate_form(username, email, password, confirm_password):
    if not username or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
        return False
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return False
    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 or more characters!")
        return False
    return True

# Login form validation
def validate_form2(email, password):
    if not email or not password:
        messagebox.showerror("Error", "All fields are required!")
        return False
    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 or more characters!")
        return False
    return True

# Register and redirect to login page
def register_and_redirect():
    if validate_form(nameEntry.get(), emailEntry.get(), passEntry.get(), cpassEntry.get()):
        register_user(nameEntry.get(), emailEntry.get(), passEntry.get())
        login_page()

# Display all users
def display_user_details():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT username, email FROM users_db")
        users = cursor.fetchall()
        user_details = "\n".join([f"Username: {user[0]}, Email: {user[1]}" for user in users])
        messagebox.showinfo("User Details", user_details)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

# Update user details
def update_user_details(email, new_username, new_password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users_db SET username=%s, password=%s WHERE email=%s", 
                       (new_username, new_password, email))
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "User details updated successfully!")
        else:
            messagebox.showerror("Error", "User not found!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

# Delete user
def delete_user(email):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users_db WHERE email=%s", (email,))
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "User deleted successfully!")
        else:
            messagebox.showerror("Error", "User not found!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error occurred: {err}")
    finally:
        cursor.close()
        conn.close()

# Manage user page
def manage_user_page():
    global manageFrame
    loginFrame.grid_forget()
    signupFrame.grid_forget()

    signup_window.title('Manage User Window')
    signup_window.geometry('450x370+500+100')

    manageFrame = CTkFrame(signup_window)
    manageFrame.grid(row=0, column=0, pady=40, padx=25)
    manageFrame.configure(fg_color='#fff')

    manage_label = CTkLabel(manageFrame, text='Manage User Details', 
                            font=('bookman old style', 30, 'bold'), text_color='green')
    manage_label.grid(row=0, column=0, pady=(0, 20))

    # Display all users
    btnDisplay = CTkButton(manageFrame, text='Display All Users', 
                           font=('bookman old style', 15, 'bold'), 
                           text_color='white', height=40, width=300, cursor='hand2',
                           command=display_user_details)
    btnDisplay.grid(row=1, column=0, pady=(10, 20))
    btnDisplay.configure(fg_color='blue')

    # Update section
    emailEntryUpdate = CTkEntry(manageFrame, placeholder_text='Enter email to update...', 
                                font=('bookman old style', 15), text_color='black', height=40, width=300)
    emailEntryUpdate.grid(row=2, column=0, pady=(0, 10))

    usernameEntryUpdate = CTkEntry(manageFrame, placeholder_text='Enter new username...', 
                                   font=('bookman old style', 15), text_color='black', height=40, width=300)
    usernameEntryUpdate.grid(row=3, column=0, pady=(0, 10))

    passEntryUpdate = CTkEntry(manageFrame, placeholder_text='Enter new password...', 
                               font=('bookman old style', 15), text_color='black', height=40, width=300, show="*")
    passEntryUpdate.grid(row=4, column=0, pady=(0, 20))

    # Update button
    btnUpdate = CTkButton(manageFrame, text='Update User', 
                          font=('bookman old style', 15, 'bold'), 
                          text_color='white', height=40, width=300, cursor='hand2',
                          command=lambda: update_user_details(emailEntryUpdate.get(), usernameEntryUpdate.get(), passEntryUpdate.get()))
    btnUpdate.grid(row=5, column=0, pady=(0, 20))
    btnUpdate.configure(fg_color='green')

    # Delete section
    emailEntryDelete = CTkEntry(manageFrame, placeholder_text='Enter email to delete...', 
                                font=('bookman old style', 15), text_color='black', height=40, width=300)
    emailEntryDelete.grid(row=6, column=0, pady=(0, 20))

    # Delete button
    btnDelete = CTkButton(manageFrame, text='Delete User', 
                          font=('bookman old style', 15, 'bold'), 
                          text_color='white', height=40, width=300, cursor='hand2',
                          command=lambda: delete_user(emailEntryDelete.get()))
    btnDelete.grid(row=7, column=0, pady=(0, 20))
    btnDelete.configure(fg_color='red')

# Signup page function
def signup_page():
    loginFrame.grid_forget()
    signup_window.title("Sign Up Window")
    signup_window.geometry('440x500+500+100')
    signupFrame.grid(row=0, column=0, pady=40, padx=60)

# Login page function
def login_page():
    global loginFrame
    signupFrame.grid_forget()
    signup_window.title('Login Window')
    signup_window.geometry('450x370+500+100')
    
    loginFrame = CTkFrame(signup_window)
    loginFrame.grid(row=0, column=0, pady=40, padx=25)
    loginFrame.configure(fg_color='#fff')

    heading_label = CTkLabel(loginFrame, text='Welcome back! Login Now!',
                             font=('bookman old style', 30, 'bold'), text_color='green')
    heading_label.grid(row=0, column=0)

    sub_heading_label = CTkLabel(loginFrame, text='Login as a member!',  
                                 font=('bookman old style', 18), text_color='black')
    sub_heading_label.grid(row=1, column=0, pady=(0, 40))

    emailEntry = CTkEntry(loginFrame, placeholder_text='Enter email here...', 
                          font=('bookman old style', 15), text_color='black', height=40, width=300)
    emailEntry.grid(row=2, column=0, pady=(0, 10))

    passEntry = CTkEntry(loginFrame, placeholder_text='Enter password here...', 
                         font=('bookman old style', 15), text_color='black', height=40, width=300, show="*")
    passEntry.grid(row=3, column=0, pady=(0, 20))

    # Login button
    btnLogin = CTkButton(loginFrame, text='Login Now', 
                         font=('bookman old style', 15, 'bold'), text_color='white', height=40, width=300, cursor='hand2',
                         command=lambda: login_user(emailEntry.get(), passEntry.get()))
    btnLogin.grid(row=4, column=0, pady=(0, 20))
    btnLogin.configure(fg_color='green')

    # Signup button
    sign_up_btn = CTkButton(loginFrame, text='New User? Sign Up', 
                            font=('bookman old style', 15, 'bold'), text_color='white', height=40, width=300, cursor='hand2', 
                            command=signup_page)
    sign_up_btn.grid(row=5, column=0)
    sign_up_btn.configure(fg_color='blue')

# Tkinter main window
signup_window = CTk()
signup_window.title('Sign Up Window')
signup_window.geometry('440x500+500+100')

signupFrame = CTkFrame(signup_window)
signupFrame.grid(row=0, column=0, pady=40, padx=60)

heading_label = CTkLabel(signupFrame, text='Sign Up', 
                         font=('bookman old style', 30, 'bold'), text_color='green')
heading_label.grid(row=0, column=0)

sub_heading_label = CTkLabel(signupFrame, text='Create a new member account!',  
                             font=('bookman old style', 18), text_color='black')
sub_heading_label.grid(row=1, column=0, pady=(0, 40))

nameEntry = CTkEntry(signupFrame, placeholder_text='Enter your name here...', 
                     font=('bookman old style', 15), text_color='black', height=40, width=300)
nameEntry.grid(row=2, column=0, pady=(0, 10))

emailEntry = CTkEntry(signupFrame, placeholder_text='Enter your email here...', 
                      font=('bookman old style', 15), text_color='black', height=40, width=300)
emailEntry.grid(row=3, column=0, pady=(0, 10))

passEntry = CTkEntry(signupFrame, placeholder_text='Enter password here...', 
                     font=('bookman old style', 15), text_color='black', height=40, width=300, show="*")
passEntry.grid(row=4, column=0, pady=(0, 10))

cpassEntry = CTkEntry(signupFrame, placeholder_text='Confirm password here...', 
                      font=('bookman old style', 15), text_color='black', height=40, width=300, show="*")
cpassEntry.grid(row=5, column=0, pady=(0, 20))

# Register button
btnRegister = CTkButton(signupFrame, text='Register Now', 
                        font=('bookman old style', 15, 'bold'), text_color='white', height=40, width=300, cursor='hand2', 
                        command=register_and_redirect)
btnRegister.grid(row=6, column=0)
btnRegister.configure(fg_color='green')

signup_window.mainloop()
