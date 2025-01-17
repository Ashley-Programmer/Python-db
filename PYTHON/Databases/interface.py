import database1
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


app = customtkinter.CTk()
app.title("Employee Management System")
app.geometry('860x420+250+100')
app.config(bg='#000')
app.resizable(False, False)

# frstFont = ('Arial', 20, 'bold')
scndFont = ('Arial', 12, 'bold')

id_label = customtkinter.CTkLabel(app, text='Identity Number:', text_color='#fff', font=('Arial', 20, 'bold'), bg_color='#000')
id_label.place(x = 20, y = 20)
id_entry = customtkinter.CTkEntry(app, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
id_entry.place(x = 200, y = 20)

name_label = customtkinter.CTkLabel(app, text='Name(s):', text_color='#fff', font=('Arial', 20, 'bold'), bg_color='#000')
name_label.place(x= 20, y =80)
name_entry = customtkinter.CTkEntry(app, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
name_entry.place(x = 200, y = 80)

role_label = customtkinter.CTkLabel(app, text='Role:', text_color='#fff', font=('Arial', 20, 'bold'), bg_color='#000')
role_label.place(x = 20, y = 140)
role_entry = customtkinter.CTkEntry(app, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
role_entry.place(x = 200, y = 140)

gender_label = customtkinter.CTkLabel(app, text='Gender:', text_color='#fff', font=('Arial', 20, 'bold'), bg_color='#000')
gender_label.place(x = 20, y = 200)

#ComboBox for gender
options = ['Male', 'Female']
var1 = StringVar()
gender_option = customtkinter.CTkComboBox(app, font=('Arial', 20, 'bold'), text_color='#000', fg_color='#fff', dropdown_hover_color='#0C9295',
                                          button_color='#0C9295', button_hover_color='#0C9295', border_color='#0C9295', width=180, 
                                          variable=var1, values=options, state='readonly')
gender_option.set('Select Gender')
gender_option.place(x = 200, y = 200)


status_label = customtkinter.CTkLabel(app, text='Status:', text_color='#fff', font=('Arial', 20, 'bold'), bg_color='#000')
status_label.place(x = 20, y = 260)
status_entry = customtkinter.CTkEntry(app, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
status_entry.place(x = 200, y = 260)

add_button = customtkinter.CTkButton(app, text='Add Employee', font=('arial', 20, 'bold'), text_color='#fff', fg_color='transparent', 
                                    hover_color='#161C25',bg_color='#00f', cursor='hand2', border_color='orange',
                                    corner_radius=2, width=260, border_width=2)
add_button.place(x = 20, y = 310)

clear_button = customtkinter.CTkButton(app, text='New Employee', font=('arial', 20, 'bold'), text_color='#fff', fg_color='transparent', 
                                    hover_color='#161C25',bg_color='#000', cursor='hand2', border_color='orange',
                                    corner_radius=2, width=260, border_width=2)
clear_button.place(x = 20, y = 360)

update_button = customtkinter.CTkButton(app, text='Update Employee', font=('arial', 20, 'bold'), text_color='#fff', fg_color='transparent', 
                                    hover_color='#161C25',bg_color='#000', cursor='hand2', border_color='orange',
                                    corner_radius=2, width=260, border_width=2)
update_button.place(x = 300, y = 360)

delete_button = customtkinter.CTkButton(app, text='Delete Employee', font=('arial', 20, 'bold'), text_color='#fff', fg_color='transparent', 
                                    hover_color='#161C25',bg_color='#f00', cursor='hand2', border_color='orange',
                                    corner_radius=2, width=260, border_width=2)
delete_button.place(x = 580, y = 360)

style = ttk.Style(app)
style.theme_use('clam')
style.configure('TreeView', font=scndFont, foreground='#fff', background='#000', fieldbackground='#313837')
style.map('Treeview', background=[('Selected', '#1A8F20')])

tree = ttk.Treeview(app, height=15)
tree['columns'] = ('Identity number', 'Name', 'Role', 'Gender', 'Status')

tree.column("#0", width=0, stretch=tk.NO)
tree.column("ID", anchor=tk.CENTER, width=120)
tree.column("Name", anchor=tk.CENTER, width=120)
tree.column("Role", anchor=tk.CENTER, width=120)
tree.column("Gender", anchor=tk.CENTER, width=120)
tree.column("Status", anchor=tk.CENTER, width=120)

tree.heading('ID', text='Identity No')
tree.heading('Name', text='Name')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Status', text='Status')

app.mainloop()
