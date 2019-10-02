from tkinter import *
from tkinter import font ,filedialog , messagebox , colorchooser
from tkinter.ttk import Combobox
 


root = Tk()
root.geometry("1300x700")

root.title("Text Editor")



################### main menu functionality #####################################


def select_color():
    clr = colorchooser.askcolor(title = "select color")
    cl  = clr[1]
    text_editor.config(bg = cl)

def select_color1():
    clr = colorchooser.askcolor(title = "Select Color")
    cl = clr[1]
    text_editor.config(fg = cl)

def bold_text():
    text_editor.configure(font = (current_font_family , current_font_size , 'bold'))

def italic_text():
    text_editor.configure(font = (current_font_family , current_font_size , 'italic'))

def under_line():
    text_editor.configure(font = (current_font_family , current_font_size  , 'underline'))

def normal():
    text_editor.configure(font = (current_font_family , current_font_size))

def apply():
    text_editor.configure(font = (current_font_family , current_font_size , 'bold' , 'italic' , 'underline'))

def left_align():
    text_content =text_editor.get(1.0 , 'end')

    text_editor.tag_config('left' , justify = LEFT)
    text_editor.delete(1.0, 'end')
    text_editor.insert(INSERT , text_content , 'left')


def center_align():
    text_content = text_editor.get(1.0, 'end')

    text_editor.tag_config('center', justify=CENTER)
    text_editor.delete(1.0, 'end')
    text_editor.insert(INSERT, text_content, 'center')

def right_align():
    text_content = text_editor.get(1.0, 'end')

    text_editor.tag_config('right', justify=RIGHT)
    text_editor.delete(1.0, 'end')
    text_editor.insert(INSERT, text_content, 'right')

def new_file(e):
    text_editor.delete(1.0 , 'end')

def open_file(e):
    file_open = filedialog.askopenfile(title ="Select File" , filetype=(("Text files", ".txt"), ("All files", "*.*")))
    text_editor.delete(1.0 , 'end')
    for i in file_open:
        text_editor.insert(INSERT , i)

def save_file(e):
    text_content =text_editor.get(1.0 , 'end')

    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    file.write(text_content)
    file.close()
    messagebox.showinfo("information", "file saved")

def save_as(e):
    file1 = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file1 is None:
        return
    write_text = text_editor.get(1.0, END)
    file1.write(write_text)
    file1.close()

    messagebox.showinfo("information", "file saved")

def exit(e):
    answer = messagebox.askquestion("Exit", "Do you  want to exit")
    if answer == "yes":
        root.destroy()

def cut_text(e):
    copy_text()
    text_editor.delete("sel.first", "sel.last")


def paste_text(e):
    text_editor.insert(INSERT, text_editor.clipboard_get())


def copy_text(e):
    text_editor.clipboard_clear()
    text_editor.clipboard_append(text_editor.selection_get())

def clear_all(e):
    text_editor.delete(1.0 , 'end')

def  hide_tool_bar():
   global show_tool_bar
   if show_tool_bar:
       tool_bar.pack_forget()
       show_tool_bar = False

   else:
       text_editor.pack_forget()
       status_bar.pack_forget()
       tool_bar.pack(side  = TOP , fill= X)
       text_editor.pack(fill = BOTH , expand = True)
       status_bar.pack(side = BOTTOM)
       show_tool_bar = True

def hide_status_bar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar = False
    else:
        status_bar.pack(side = BOTTOM)
        show_status_bar = True


################### end main menu functionality ###################################


#################### main menu #######################################################################################

main_menu = Menu()

file_menu = Menu(main_menu ,tearoff = False)
#file icons
new_icon = PhotoImage(file = "icons2/new.png")
open_icon = PhotoImage(file = "icons2/open.png")
save_icon = PhotoImage(file = "icons2/save.png")
save_as_icon = PhotoImage(file = "icons2/save_as.png")
exit_icon = PhotoImage(file = "icons2/exit.png")

#Add file command
file_menu.add_command(label = "New " , image = new_icon , compound = LEFT ,accelerator = 'Ctrl + N' , command = new_file)
file_menu.add_command(label = "Open" , image = open_icon , compound = LEFT ,accelerator = 'Ctrl + O' , command = open_file)
file_menu.add_command(label = "Save" , image = save_icon , compound = LEFT ,accelerator = 'Ctrl + S' , command = save_file)
file_menu.add_command(label = "Save as" , image = save_as_icon , compound = LEFT,accelerator = 'Ctrl +Alt+ S' , command = save_as)
file_menu.add_command(label = "Exit" , image = exit_icon , compound = LEFT ,accelerator = 'Ctrl + Q' , command = exit)

#############################################

edit_menu = Menu(main_menu , tearoff = False)
#edit icons
copy_icon = PhotoImage(file = "icons2/copy.png")
paste_icon = PhotoImage(file = "icons2/paste.png")
cut_icon = PhotoImage(file = "icons2/cut.png")
clearall_icon = PhotoImage(file = "icons2/clear_all.png")
find_icon = PhotoImage(file = "icons2/find.png")

#add edit command
edit_menu.add_command(label = "Copy" , image = copy_icon , compound = LEFT , accelerator = "Ctrl+C" , command = copy_text)
edit_menu.add_command(label = "Paste" , image = paste_icon , compound = LEFT , accelerator = "Ctrl+V" , command = paste_text)
edit_menu.add_command(label = "Cut" , image = cut_icon , compound = LEFT , accelerator = "Ctrl+X" , command = cut_text)
edit_menu.add_command(label = "Clear all" , image = clearall_icon , compound = LEFT , accelerator = "Ctrl+alt+C" , command = clear_all)
#edit_menu.add_command(label = "Find" , image = find_icon , compound = LEFT , accelerator = "Ctrl+F" , command = find_func)

######################################

view_menu = Menu(main_menu , tearoff = False)
#view icons
toolbar_icon = PhotoImage(file = "icons2/tool_bar.png")
statusbar_icon = PhotoImage(file = "icons2/status_bar.png")


show_tool_bar = BooleanVar()
show_tool_bar.set(True)
show_status_bar = BooleanVar()
show_status_bar.set(True)


view_menu.add_checkbutton(label = "Tool bar" ,onvalue = True  ,offvalue = False,variable = show_tool_bar, image = toolbar_icon , compound = LEFT , command = hide_tool_bar  )
view_menu.add_checkbutton(label = "Status bar" ,onvalue = True  , offvalue = False , variable = show_status_bar, image = statusbar_icon , compound = LEFT , command = hide_status_bar )

########################################

color_theme = Menu(main_menu , tearoff = False)
#add icons
red_icon = PhotoImage(file = "icons2/red.png")
color_theme.add_command(label = "Select window color" , image = red_icon ,compound = LEFT,   command = select_color)
color_theme.add_command(label = "Select Font color" , image = red_icon ,compound = LEFT, command = select_color1)






#cascade

main_menu.add_cascade(label = "File" , menu = file_menu)
main_menu.add_cascade(label = "Edit" , menu = edit_menu)
main_menu.add_cascade(label = "View" , menu = view_menu)
main_menu.add_cascade(label = "Color Theme" , menu = color_theme)


################### end main menu #################################################################################





#################### tool bar #####################################

tool_bar = Label(root)
tool_bar.pack(side  = TOP , fill = X)

font_tuple = font.families()
font_family = StringVar()
font_box = Combobox(tool_bar , width = 30 ,textvariable = font_family , state = 'readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0 , column = 0 , padx = 5)



select_size = IntVar()
size_box = Combobox(tool_bar , width =14 , textvariable = select_size , state = 'readonly')
size_box['values'] = tuple(range(8,80))
size_box.current(4)
size_box.grid(row = 0 , column = 1 , padx = 5)



bold_icon = PhotoImage(file = "icons2/bold.png")
italic_icon = PhotoImage(file = "icons2/italic.png")
underline_icon = PhotoImage(file = "icons2/underline.png")

bold_button = Button(tool_bar  , image = bold_icon , command = bold_text)
bold_button.grid(row=0 , column=2 , padx = 5)

italic_button = Button(tool_bar , image = italic_icon , command = italic_text)
italic_button.grid(row=0 , column=3 , padx = 5)

underline_button = Button(tool_bar , image = underline_icon , command = under_line)
underline_button.grid(row=0 , column=4 , padx=5)

align_left_icon = PhotoImage(file = "icons2/align_left.png")
align_right_icon = PhotoImage(file = "icons2/align_right.png")
align_center_icon = PhotoImage(file = "icons2/align_center.png")


left_align = Button(tool_bar , image = align_left_icon , command = left_align)
center_align = Button(tool_bar , image = align_center_icon , command = center_align)
right_align = Button(tool_bar ,image = align_right_icon , command = right_align)

left_align.grid(row=0 , column = 5 , padx=5)
center_align.grid(row =0 , column = 6 , padx = 5)
right_align.grid(row=0 , column = 7 , padx=5)

normal_text = Button(tool_bar , text = "Normal Text" , command = normal)
normal_text.grid(row=0 , column = 8 , padx=5)

apply_three = Button(tool_bar , text = "Apply B I U" , command = apply)
apply_three.grid(row = 0 , column = 9, padx =5)

################### end tool bar ###################################






#################### text editor #####################################


text_editor = Text(root)
text_editor.config(wrap= 'word')

scroll_bar = Scrollbar(root)
text_editor.focus_set()
scroll_bar.pack(side = RIGHT , fill = Y)

text_editor.pack(fill = BOTH , expand = True)

scroll_bar.config(command = text_editor.yview)

text_editor.config(yscrollcommand = scroll_bar.set)


current_font_family = 'Arial'
current_font_size = 12



def change_font(e):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font = (current_font_family , current_font_size))

def change_font_size(e):
    global current_font_size
    current_font_size = select_size.get()
    text_editor.configure(font = (current_font_family , current_font_size))



size_box.bind("<<ComboboxSelected>>" , change_font_size)


font_box.bind("<<ComboboxSelected>>" , change_font)

text_editor.configure(font = (current_font_family , current_font_size))



################### end text editor ###################################



#################### status bar #####################################


status_bar = Label(root , text = "@Creator Himanshu Verma ")
status_bar.pack(side = BOTTOM ,)

################### status bar ###################################


root.config(menu = main_menu)

root.bind("<Control-n>" , new_file)
root.bind("<Control-o>" , open_file)
root.bind("<Control-s>" , save_file)
root.bind("<Control-Alt-s>" , save_as)
root.bind("<Control-q>" , exit)
root.bind("<Control-c>" , copy_text)
root.bind("<Control-v>" , paste_text)
root.bind("<Control-Alt-c>" ,clear_all)
root.mainloop()