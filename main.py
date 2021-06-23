import tkinter
from tkinter import font 

#defining window
root = tkinter.Tk()
root.title('Tick Things')
root.iconbitmap('check.ico')
root.geometry('450x400')
root.resizable(0,0)

# defining fonts and colors
my_root = ('Times New Roman', 14)
root_color ='#842cd4'
button_color='#e4d2f7'

root.config(bg=root_color)

# define functions

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
list_add_button = tkinter.Button(input_frame, text='Add', borderwidth=2, font=my_root, bg=button_color)
list_entry.grid(row=0, column=0)
list_add_button.grid(row=0, column=1)

# output frame layout
my_list_box = tkinter.Listbox(output_frame, height=13, width=40, borderwidth=3, font=my_root)
my_list_box.grid(row=0, column=0)

# Button frame layout
list_remove_button=tkinter.Button(button_frame, text='Remove Thing', borderwidth=2, font=my_root, bg=button_color)
list_clear_button = tkinter.Button(button_frame, text='Clear All', borderwidth=2, font=my_root, bg=button_color)
save_button = tkinter.Button(button_frame, text='Save Things', borderwidth=2, font=my_root, bg=button_color)
quit_button = tkinter.Button(button_frame, text='Quit', borderwidth=2, font=my_root, bg=button_color, command=root.destroy)

list_remove_button.grid(row=0, column=0)
list_clear_button.grid(row=0, column=1)
save_button.grid(row=0, column=2)
quit_button.grid(row=0, column=3)


# run the main window loop
root.mainloop()