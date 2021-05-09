'''
code file: tkeys.py
date: Mar 2021
commants:
    tkinter reference utility
    written in python3 + tkinter ttk
'''
from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
import os
from tkinter.font import Font
import webbrowser
from tkinter.colorchooser import askcolor
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets

initext = '''
W E L C O M E
Pick a Widget
  Click "List" to view option keys
  Select a key
  Click "Search" | "Reference"

    ctrl-q | Esc  QUIT
    ctrl-k        Color Chooser
'''

urlpath = "https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/"

lookup = {
"Button":       "ttk-Button.html",
"Checkbutton":  "ttk-Checkbutton.html",
"Combobox":     "ttk-Combobox.html",
"Entry":        "ttk-Entry.html",
"Frame":        "ttk-Frame.html",
"LabelFrame":   "ttk-LabelFrame.html",
"Label":        "ttk-Label.html",
"Listbox":      "listbox.html",
"Menu":         "menu.html",
"Message":      "message.html",
"Notebook":     "ttk-Notebook.html",
"OptionMenu":   "optionmenu.html",
"PanedWindow":  "ttk-PanedWindow.html",
"Progressbar":  "ttk-Progressbar.html",
"Radiobutton":  "ttk-Radiobutton.html",
"Scale":        "ttk-Scale.html",
"Scrollbar":    "scrollbar.html",
"Separator":    "ttk-Separator.html",
"Spinbox":      "spinbox.html",
"Text":         "text.html",
"Toplevel":     "toplevel.html",
"Treeview":     "ttk-Treeview.html"}

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True)
        self.configure(relief=FLAT)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # customize widget style when using ttk...
        style = Style()
        style.configure("TButton",      width=10)
        style.configure('TFrame',       background='burlywood1')
        style.configure('TButton',      background='burlywood1')
        style.configure("TCombobox",    background="burlywood1")
        style.configure("TLabel",       background="burlywood1")

        self.vcmbo = StringVar()
        self.cmbo = Combobox(self, textvariable=self.vcmbo, width=32)
        self.cmbo['values'] = ("Select a Widget",
                               "Button",
                               "Checkbutton",
                               "Colors",
                               "Combobox",
                               "Entry",
                               "Frame",
                               "Label",
                               "LabelFrame",
                               "Layout Managers",
                               "Listbox",
                               "Message",
                               "Notebook",
                               "OptionMenu",
                               "PanedWindow",
                               "Progressbar",
                               "Radiobutton",
                               "Separator",
                               "Scale",
                               "Scrollbar",
                               "Spinbox",
                               "Text",
                               "Toplevel",
                               "Treeview")
        self.cmbo.current(0)  # set start cmbo to display
        self.cmbo.grid(row=1, column=1, padx=10)
        self.cmbo['state'] = 'readonly'
        self.cmbo.bind("<<ComboboxSelected>>", self.cmbo_selected)
        self.cmbo.focus()

        btn_get = Button(self, text='Reference', command=self.btn_reference_click)
        btn_get.grid(row=1, column=2, sticky="e", pady=10, padx=10)

        self.txt = Text(self, padx=10)
        self.txt.grid(row=2, column=1, columnspan=2,
                      padx=5, sticky='nsew')
        efont = Font(family="Monospace", size=10)
        self.txt.configure(font=efont)
        self.txt.config(wrap="word", # wrap=NONE
               undo=True, # Tk 8.4
               width=50,
               height=14)
        self.txt.insert("1.0", initext)  # literal opening help instruction

        self.lbl = Label(self, text='Internal Class Name')
        self.lbl.grid(row=3, column=1, pady=10, padx=10)

        btn_search = Button(self, text='Search', command=self.btn_search_click)
        btn_search.grid(row=3, column=2, sticky="ew", pady=10, padx=10)

        root.bind("<Escape>",       self.exit_keyed)
        root.bind("<Control-q>",    self.exit_keyed)
        root.bind("<Control-k>",    self.colorchooser)

    def btn_search_click(self, e=None):
        ''' docstring '''
        widget = self.vcmbo.get()
        try:
            opt = self.txt.selection_get()
        except:
            opt = ""
        webbrowser.open("https://www.google.com/search?q=tkinter " +
                        widget + " " + opt)

    def btn_reference_click(self):
        ''' Open Reference Help For Widget in Browser '''
        widget = self.vcmbo.get()
        wtxt = lookup[widget]
        url = urlpath + wtxt
        webbrowser.open(url)

    def exit_keyed(self, e=None):
        ''' docstring '''
        root.destroy()

    def colorchooser(self, e=None):
        colors = askcolor(title="Tkeys Color Chooser")
        root.clipboard_clear()
        root.clipboard_append(colors[1])  #999999 color now in clipboard

    def cmbo_selected(self, e=None):
        '''
            instantiate selected widget object
            and insert it's option keys
            into the text widget (txt)
        '''
        widget = self.vcmbo.get()

        if widget == "Button":
            w = Button(root)
        elif widget == "Label":
            w = Label(root)
        elif widget == "Frame":
            w = Frame(root)
        elif widget == "LabelFrame":
            w = LabelFrame(root)
        elif widget == "OptionMenu":
            var = StringVar()
            w = OptionMenu(root, var)
        elif widget == "Entry":
            w = Entry(root)
        elif widget == "Radiobutton":
            w = Radiobutton(root)
        elif widget == "Spinbox":
            w = Spinbox(root)
        elif widget == "Text":
            w = Text(root)
        elif widget == "Checkbutton":
            w = Checkbutton(root)
        elif widget == "Listbox":
            w = Listbox(root)
        elif widget == "Scrollbar":
            w = Scrollbar(root)
        elif widget == "Combobox":
            w = Combobox(root)
        elif widget == "Message":
            w = Message(root)
        elif widget == "Notebook":
            w = Notebook(root)
        elif widget == "Menu":
            w = Menu(root)
        elif widget == "PanedWindow":
            w = PanedWindow(root)
        elif widget == "Progressbar":
            w = Progressbar(root)
        elif widget == "Separator":
            w = Separator(root)
        elif widget == "Scale":
            w = Scale(root)
        elif widget == "Toplevel":
            w = Toplevel(root)
        elif widget == "Treeview":
            w = Treeview(root)
        elif widget == "Colors":
            os.system("xdg-open TkInterColorCharts.png")
            return
        elif widget == "Layout Managers":
            os.system("xdg-open layouts.pdf")
            return
        else:
            self.txt.delete("1.0", END)
            self.txt.insert("1.0", "No Widget")
            return

        sout = ""
        for key in w.keys():
            sout += key + " : "
        self.txt.delete("1.0", END)
        self.txt.insert("1.0", sout)
        self.lbl['text'] = w.winfo_class()  # widget internal class name

root = ThemedTk(theme="radiance")

# change working directory to path for this file
# so it can use files in this directory
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))

Sizegrip(root).place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

root.tk_bisque()
root.title("Tkinter Widget Options")
app = Application(root)
app.mainloop()
