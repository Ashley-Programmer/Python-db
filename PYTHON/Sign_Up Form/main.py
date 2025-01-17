from customtkinter import *


def signup_page():
    loginFrame.grid_forget()
    signup_window.title("Sign Up Window")
    signup_window.geometry('440x500+500+100')
    signupFrame.grid(row=0, column=0, pady=40, padx=60)


# function section: Login Page
def login_page():
    global loginFrame
    
    signupFrame.grid_forget()
    signup_window.title('Login Window')
    
    signup_window.geometry('450x370+500+100')
    
    loginFrame = CTkFrame(signup_window)
    loginFrame.grid(row=0, column=0, pady=40, padx=25)
    loginFrame.configure(fg_color='#fff')
    
    Heading_label = CTkLabel(loginFrame, text='Welcome back Login Now!',
                             font=('bookman old style', 30, 'bold'), text_color='green')

    Sub_Heading_label = CTkLabel(loginFrame, text='Login as a member!.',
                                 font=('bookman old style', 18), text_color='black')
    Heading_label.grid(row=0, column=0)
    Sub_Heading_label.grid(row=1, column=0, pady=(0, 40))
    
    EmailEntry = CTkEntry(loginFrame, placeholder_text='Enter email here...',
                          font=('bookman old style', 15), text_color='black', height=40, width=350)
    PassEntry = CTkEntry(loginFrame, placeholder_text='Enter password here...',
                         font=('bookman old style', 15), text_color='black', height=40, width=350)
    
    EmailEntry.grid(row=3, column=0, pady=(0, 20))
    EmailEntry.configure(fg_color='#f5f5f5', bg_color='#000', border_color='#000')

    PassEntry.grid(row=4, column=0, pady=(0, 20))
    PassEntry.configure(fg_color='#f5f5f5', bg_color='#000', border_color='#000')
    
    btnLogin = CTkButton(loginFrame, text='LOGIN', 
                      font=('bookman old style', 15, 'bold'), 
                      text_color='white', hover_color='darkgreen', height=40 ,width=350, cursor='hand2')
    btnLogin.grid(row=6, column=0, pady=(0, 20))
    btnLogin.configure(fg_color='green')
    
    Frame = CTkFrame(loginFrame, fg_color='#fff')
    Frame.grid(row=7, column=0)
    
    label = CTkLabel(Frame, text="Not a member yet?", font=('bookman old style', 13), text_color='#000')
    label.grid(row=0, column=0)
    label.configure(fg_color='white')
    
    Login_here = CTkButton(Frame, text='SignUp here',
                           font=('bookman old style', 15, 'underline'),
                           text_color='darkgreen', hover_color='#fff', cursor='hand2', command=signup_page)
    Login_here.grid(row=0, column=1)
    Login_here.configure(fg_color='#fff')
    
    

# GUI Section: signUp Page

signup_window = CTk()

# set the title
signup_window.title('Sign Up Window')

# change background color of window
signup_window.configure(fg_color='white')

# width and height of the window and the distance of x:500, y-axis:100
signup_window.geometry('440x500+500+100') # width = 440, height = 500

#disable the maximise button
signup_window.resizable(False,False)

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
                      text_color='white', hover_color='darkgreen', height=40 ,width=320, cursor='hand2')
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