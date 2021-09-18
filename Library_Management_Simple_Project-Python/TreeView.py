from tkinter import ttk
import tkinter as tk

Library_Management_System_header = ['Book Id', 'Author Name', 'Book Title', 'Book Year','Status']
def style():
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview.Heading', background="green3", font=(None,14),
                    foreground='black', rowheight=100, fieldbackground='NavajoWhite')
    style.configure('Treeview', background="PaleTurquoise",font=(None, 14),
                    foreground='black', rowheight=100, fieldbackground='NavajoWhite')
    style.map('Treeview', background=[('selected', 'orange')])
def tree_view(frame,display_detail):
    style()
    my_tree = ttk.Treeview(frame, selectmode='browse')
    scrollbarY = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=my_tree.yview)
    scrollbarY.pack(side=tk.RIGHT, fill=tk.Y)
    my_tree.configure(yscrollcommand=scrollbarY.set)
    my_tree.pack(side=tk.TOP, fill=tk.BOTH)

    my_tree['columns'] =Library_Management_System_header
    my_tree.column('#0', anchor=tk.W, width=0, stretch=False)
    my_tree.column('Book Id', anchor=tk.W, width=60)
    my_tree.column('Author Name', anchor=tk.W, width=150)
    my_tree.column('Book Title', anchor=tk.W, width=150)
    my_tree.column('Book Year', anchor=tk.W, width=150)
    my_tree.column('Status', anchor=tk.W, width=60)

    my_tree.heading('#0', text='Label', anchor=tk.W)
    my_tree.heading('Book Id', text='Id', anchor=tk.W)
    my_tree.heading('Author Name', text='Author Name', anchor=tk.W)
    my_tree.heading('Book Title', text='Book Title', anchor=tk.W)
    my_tree.heading('Book Year', text='Book Year', anchor=tk.W)
    my_tree.heading('Status', text='Status', anchor=tk.W)
    count = 0
    my_tree.tag_configure('odd_row', background='OldLace')
    my_tree.tag_configure('evenrow', background='MintCream')

    for row in display_detail:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='parent',
                           values=(row[0], row[1], row[2], row[3], row[4]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='parent',
                           values=(row[0], row[1], row[2], row[3], row[4]), tags=('odd_row',))

        count += 1
    return my_tree