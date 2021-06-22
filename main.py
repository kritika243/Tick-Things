import tkinter 

#defining window
root = tkinter.Tk()
root.title('Tick Things')
root.iconbitmap('check.ico')
root.geometry('400x400')
root.resizable(0,0)

# defining fonts and colors
my_root = ('Times New Roman', 14)
root_color ='#2596be'
button_color='#6c1cbc'

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


# run the main window loop
root.mainloop()