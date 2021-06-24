import tkinter
from tkinter import font
from tkinter.constants import END 

#defining window
root = tkinter.Tk()
root.title('Tick Things')
root.iconbitmap('check.ico')
root.geometry('500x400')
root.resizable(0,0)

# defining fonts and colors
my_root = ('Times New Roman', 14)
root_color ='#842cd4'
button_color='#e4d2f7'

root.config(bg=root_color)

# define functions
def add_item():
  """ add individual iems to list box """
  my_list_box.insert(END, list_entry.get())
  list_entry.delete(0,END)


# defining layout
#creating frames
input_frame = tkinter.Frame(root, bg=root_color)
output_frame = tkinter.Frame(root, bg=root_color)
button_frame = tkinter.Frame(root, bg=root_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

# input frame layout
list_entry = tkinter.Entry(input_frame, width=35, borderwidth=3, font=my_root)
list_add_button = tkinter.Button(input_frame, text='Add', borderwidth=2, font=my_root, bg=button_color, command=add_item)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=2)

# output frame layout
my_scrollbar = tkinter.Scrollbar(output_frame)
my_list_box = tkinter.Listbox(output_frame, height=13, width=40, borderwidth=3, font=my_root)
my_list_box.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky='NS')

# Button frame layout
list_remove_button=tkinter.Button(button_frame, text='Remove Thing', borderwidth=2, font=my_root, bg=button_color)
list_clear_button = tkinter.Button(button_frame, text='Clear All', borderwidth=2, font=my_root, bg=button_color)
save_button = tkinter.Button(button_frame, text='Save Things', borderwidth=2, font=my_root, bg=button_color)
quit_button = tkinter.Button(button_frame, text='Quit', borderwidth=2, font=my_root, bg=button_color, command=root.destroy)

list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=10, padx=2, pady=10, ipadx=17)
save_button.grid(row=0, column=20, padx=2, pady=10, ipadx=13)
quit_button.grid(row=0, column=30, padx=2, pady=10, ipadx=28)


# run the main window loop
root.mainloop()