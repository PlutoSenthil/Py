try:
    import tkinter as tk  # python 3
except ImportError:
    import Tkinter as tk  # python 2
import tkinter.messagebox
import TableFn
import TreeView

dbname='books.db'
table_name='library'
create=TableFn.create()
if create==1:
    tk.messagebox.showerror(title='Db', message='Fail to Create Table')

window = tk.Tk()

w = 1300  # width for the Tk root
h = 650  # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth()  # width of the screen
hs = window.winfo_screenheight()  # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
# set the dimensions of the screen
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

id=tk.StringVar()
name=tk.StringVar()
title=tk.StringVar()
year=tk.StringVar()
status=tk.StringVar()

frame_top = tk.Frame(window, highlightbackground="MediumSeaGreen", highlightthickness=10, width=800, height=50,
                     borderwidth=1, relief=tk.RIDGE,bg='#E9F7F8')
frame_top.pack(side=tk.TOP, fill=tk.BOTH)



frame_right = tk.Frame(window, highlightbackground="MediumSeaGreen", highlightthickness=10, width=700, height=360, bd=0
                       ,bg='#E9F7F8')
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

frame_right_container=tk.Frame(frame_right)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
# view_container_label = tk.Label(frame_right_container, text='WELCOME1',
#                       relief=tk.RIDGE, height=1, width=25,
#                       bg='#FF9A98', bd=7, font=(None, 24))
# view_container_label.pack(side=tk.TOP, fill=tk.BOTH)

def get_container_right_for_delete():
    global frame_right_container
    frame_right_container = tk.Frame(frame_right)


def general1():
    global frame_right_container
    frame_right_container.destroy()
    get_container_right_for_delete()
    frame_right_container.pack(side=tk.TOP, fill=tk.BOTH)
    frame_inside_container = tk.Frame(frame_right_container,bg='#E9F7F8')
    frame_inside_container.pack(side=tk.TOP, fill=tk.BOTH)
    return frame_inside_container

frame_left = tk.Frame(window, width=100, height=510, borderwidth=1, relief=tk.RIDGE,bg='#E9F7F8')
frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

frame_left1 = tk.Frame(frame_left, highlightbackground="MediumSeaGreen", highlightthickness=5, width=80, height=100,
                       borderwidth=1, relief=tk.RIDGE,bg='#E9F7F8')
frame_left1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
frame_right1 = tk.Frame(frame_left, highlightbackground="MediumSeaGreen", highlightthickness=10, width=350, height=360,
                        bd=0,bg='#E9F7F8')
frame_right1.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

frame_right1_container = tk.Frame(frame_right1)
frame_right1_container.pack(side=tk.TOP, fill=tk.BOTH)
frame_inside_container = tk.Frame(frame_right1_container)
frame_inside_container.pack(side=tk.TOP, fill=tk.BOTH)
welcome_label = tk.Label(frame_inside_container, text='WELCOME',
                      relief=tk.RIDGE, height=1, width=25,
                      bg='#FF9A98', bd=7, font=(None, 24))
welcome_label.pack(side=tk.TOP, fill=tk.BOTH)


def get_container_right1_for_delete():
    global frame_right1_container
    frame_right1_container = tk.Frame(frame_right1)


def general():
    global frame_right1_container
    frame_right1_container.destroy()
    get_container_right1_for_delete()
    frame_right1_container.pack(side=tk.TOP, fill=tk.BOTH)
    frame_inside_container = tk.Frame(frame_right1_container,bg='#E9F7F8')
    frame_inside_container.pack(side=tk.TOP, fill=tk.BOTH)
    return frame_inside_container


def view_action():
    view=TableFn.view(table_name=table_name)
    if not view:
        tk.messagebox.showerror(title='Db', message='Empty Table Add Book First')
    elif view==1:
        tk.messagebox.showerror(title='Db', message='Fail to View')
    else:
        frame_inside_container=general1()
        my_tree=TreeView.tree_view(frame_inside_container,view)
def view_available_action():
    view,para=TableFn.search(table_name=table_name,status='Available')
    if not view:
        frame_inside_container = general1()
        tk.messagebox.showerror(title='Db', message='No Available Book Found')
    elif view==1:
        frame_inside_container = general1()
        tk.messagebox.showerror(title='Db', message='fail Available Book view')
    else:
        result_page(result_text='Available Book')
        frame_inside_container=general1()
        my_tree=TreeView.tree_view(frame_inside_container,view)
def view_issue_action():
    view,para = TableFn.search(table_name=table_name, status='Issued')
    if not view:
        frame_inside_container = general1()
        tk.messagebox.showerror(title='Db', message='No Issued Book Found')
    elif view == 1:
        frame_inside_container = general1()
        tk.messagebox.showerror(title='Db', message='fail Issued Book view')
    else:
        result_page(result_text='Issued Book')
        frame_inside_container = general1()
        my_tree = TreeView.tree_view(frame_inside_container, view)
def search_action(id1, name1, title1, year1):
    id1=id1.get()
    name1=name1.get()
    title1=title1.get()
    year1=year1.get()
    search,parameter_value = TableFn.search(table_name=table_name, id=id1, name=name1, title=title1, year=year1)
    print(parameter_value)
    if search == 1:
        result_page(result_text='fail to search')
    if not search:
        result_page(result_text='No Record Found')
    else:
        result_page(result_text='Record Found')
        frame_inside_container = general1()
        my_tree = TreeView.tree_view(frame_inside_container, search)
def add_action(name,title,year):
    name=name.get();title=title.get();year=year.get()
    insert=TableFn.insert(table_name=table_name,name=name,title=title,year=year,status='Available')
    if create == 1:
        result_page(result_text='fail to add')
    else:
        result_page(result_text=[name,title,year])
def issue_action(id):
    id = id.get();
    issue = TableFn.issue(table_name=table_name,id=id)
    if issue == 1:
        result_page(result_text='Fail to Issue')
    elif issue:
        result_page(result_text='Book Id '+str(id)+' is Issued')
    else:
        result_page(result_text='Book Not Available')
def return_action(id):
    id = id.get();
    return_result= TableFn.return_table(table_name=table_name,id=id)
    if return_result==1:
        result_page(result_text='Fail to Return')
    elif return_result:
        result_page(result_text='Book Id '+str(id)+' is Returned')
    else:
        result_page(result_text='Check Book Id for return')
def delete_action(id):
    id = id.get();
    delete = TableFn.delete(table_name=table_name,id=id)
    if not delete:
        result_page(result_text='Check Book Id for delete')
    elif delete == 1:
        result_page(result_text='Fail to Return')
    else:
        result_page(result_text=delete[0][0]+' '+str(id)+' deleted')
def delete_all_action():
    delete = TableFn.delete_all(table_name=table_name)
    if delete==0:
        result_page(result_text='All data Deleted')
        frame_inside_container = general1()
    elif delete == 1:
        result_page(result_text='Fail to Delete All')
def drop_action():
    drop = TableFn.drop(table_name=table_name)
    if drop==0:
        result_page(result_text='Reseted Successfully')
        frame_inside_container = general1()
    elif drop == 1:
        result_page(result_text='Fail to Reset')
def display():
    frame_inside_container = general()
    name_label = tk.Label(frame_inside_container, text='Display Book',
                          relief=tk.RIDGE, height=1, width=25,
                          bg='#FF9A98', bd=7, font=(None, 24))
    name_label.pack(side=tk.TOP, fill=tk.BOTH)
    view_confirm_button = tk.Button(frame_inside_container, text="View All",
                               relief=tk.RIDGE, height=1, width=20,
                               bg='#9DDAD2', bd=1, font=(None, 17),
                               command=lambda: view_action())
    view_confirm_button.pack(side=tk.TOP, pady=20)
    avail_confirm_button = tk.Button(frame_inside_container, text="Available Book",
                                     relief=tk.RIDGE, height=1, width=20,
                                     bg='#9DDAD2', bd=1, font=(None, 17),
                                     command=lambda: view_available_action())
    avail_confirm_button.pack(side=tk.TOP, pady=20)
    issue_confirm_button = tk.Button(frame_inside_container, text="Issued Book",
                                     relief=tk.RIDGE, height=1, width=20,
                                     bg='#9DDAD2', bd=1, font=(None, 17),
                                     command=lambda: view_issue_action())
    issue_confirm_button.pack(side=tk.TOP, pady=20)

def search():
    frame_inside_container = general()
    global id,name,title,year
    id,name,title,year = tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
    view_action()
    name_label = tk.Label(frame_inside_container, text='Search Book',
                          relief=tk.RIDGE, height=1, width=25,
                          bg='#FF9A98', bd=7, font=(None, 24))
    name_label.pack(side=tk.TOP, fill=tk.BOTH)
    search_id_label = tk.Label(frame_inside_container, text='Book Id',
                        relief=tk.RIDGE, height=1, width=15,
                        bg='#FFDEDF', bd=7, font=(None, 24))
    search_id_label.pack(side=tk.TOP, pady=9)
    search_id_entry = tk.Entry(frame_inside_container, textvariable=id, relief=tk.SUNKEN, justify=tk.CENTER,
                               width=15, font=("Helvetica", 18, "bold"))
    search_id_entry.pack(side=tk.TOP, ipady=4)
    search_name_label = tk.Label(frame_inside_container, text='Author Name',
                                 relief=tk.RIDGE, height=1, width=15,
                                 bg='#FFDEDF', bd=7, font=(None, 24))
    search_name_label.pack(side=tk.TOP, pady=9)
    search_name_entry = tk.Entry(frame_inside_container, textvariable=name, relief=tk.SUNKEN, justify=tk.CENTER,
                                 width=30, font=("Helvetica", 18, "bold"))
    search_name_entry.pack(side=tk.TOP, ipady=4)
    search_title_label = tk.Label(frame_inside_container, text='Book Title',
                                  relief=tk.RIDGE, height=1, width=15,
                                  bg='#FFDEDF', bd=7, font=(None, 24))
    search_title_label.pack(side=tk.TOP, pady=9)
    search_title_entry = tk.Entry(frame_inside_container, textvariable=title, relief=tk.SUNKEN, justify=tk.CENTER,
                                  width=30, font=("Helvetica", 18, "bold"))
    search_title_entry.pack(side=tk.TOP, ipady=4)
    search_year_label = tk.Label(frame_inside_container, text='Book Year',
                                 relief=tk.RIDGE, height=1, width=15,
                                 bg='#FFDEDF', bd=7, font=(None, 24))
    search_year_label.pack(side=tk.TOP, pady=9)
    search_year_entry = tk.Entry(frame_inside_container, textvariable=year, relief=tk.SUNKEN, justify=tk.CENTER,
                                 width=15, font=("Helvetica", 18, "bold"))
    search_year_entry.pack(side=tk.TOP, ipady=4)
    search_confirm_button = tk.Button(frame_inside_container, text="Find",
                               relief=tk.RIDGE, height=1, width=10,
                               bg='#9DDAD2', bd=1, font=(None, 17),
                               command=lambda: search_action(id,name,title,year))
    search_confirm_button.pack(side=tk.TOP, pady=9)
def add():
    frame_inside_container = general()
    global name,title,year
    name,title,year=tk.StringVar(),tk.StringVar(),tk.StringVar()
    view_action()
    add_label = tk.Label(frame_inside_container, text='Add Book',
                          relief=tk.RIDGE, height=1, width=25,
                          bg='#FF9A98', bd=7, font=(None, 24))
    add_label.pack(side=tk.TOP, fill=tk.BOTH)
    add_name_label = tk.Label(frame_inside_container, text='Author Name',
                        relief=tk.RIDGE, height=1, width=15,
                        bg='#FFDEDF', bd=7, font=(None, 24))
    add_name_label.pack(side=tk.TOP, pady=20)
    add_name_entry = tk.Entry(frame_inside_container,textvariable=name,relief=tk.SUNKEN, justify=tk.CENTER,
                              width=35, font=("Helvetica", 18, "bold"))
    add_name_entry.pack(side=tk.TOP, ipady=5)
    add_title_label = tk.Label(frame_inside_container, text='Book Title',
                              relief=tk.RIDGE, height=1, width=15,
                              bg='#FFDEDF', bd=7, font=(None, 24))
    add_title_label.pack(side=tk.TOP, pady=20)
    add_title_entry = tk.Entry(frame_inside_container,textvariable=title, relief=tk.SUNKEN, justify=tk.CENTER,
                              width=35, font=("Helvetica", 18, "bold"))
    add_title_entry.pack(side=tk.TOP, ipady=5)
    add_year_label = tk.Label(frame_inside_container, text='Book Year',
                              relief=tk.RIDGE, height=1, width=15,
                              bg='#FFDEDF', bd=7, font=(None, 24))
    add_year_label.pack(side=tk.TOP, pady=20)
    add_year_entry = tk.Entry(frame_inside_container,textvariable=year, relief=tk.SUNKEN, justify=tk.CENTER,
                              width=15, font=("Helvetica", 18, "bold"))
    add_year_entry.pack(side=tk.TOP, ipady=5)
    add_confirm_button = tk.Button(frame_inside_container, text="Append",
                               relief=tk.RIDGE, height=1, width=10,
                               bg='#9DDAD2', bd=1, font=(None, 17),
                               command=lambda: add_action(name,title,year))
    add_confirm_button.pack(side=tk.TOP, pady=20)
def issue():
    frame_inside_container = general()
    global id
    id=tk.StringVar()
    view_action()
    issue_label = tk.Label(frame_inside_container, text='Issue Book',
                         relief=tk.RIDGE, height=1, width=25,
                         bg='#FF9A98', bd=7, font=(None, 24))
    issue_label.pack(side=tk.TOP, fill=tk.BOTH)
    issue_id_label = tk.Label(frame_inside_container, text='Book Id',
                        relief=tk.RIDGE, height=1, width=15,
                        bg='#FFDEDF', bd=7, font=(None, 24))
    issue_id_label.pack(side=tk.TOP, pady=20)
    issue_id_entry = tk.Entry(frame_inside_container,textvariable=id, relief=tk.SUNKEN, justify=tk.CENTER,
                               width=15, font=("Helvetica", 18, "bold"))
    issue_id_entry.pack(side=tk.TOP, ipady=10)
    issue_confirm_button = tk.Button(frame_inside_container, text="Supply",
                               relief=tk.RIDGE, height=1, width=10,
                               bg='#9DDAD2', bd=1, font=(None, 17),
                               command=lambda: issue_action(id))
    issue_confirm_button.pack(side=tk.TOP, pady=20)
def return_():
    frame_inside_container = general()
    global id
    id=tk.StringVar()
    view_action()
    return_label = tk.Label(frame_inside_container, text='Return Book',
                         relief=tk.RIDGE, height=1, width=25,
                         bg='#FF9A98', bd=7, font=(None, 24))
    return_label.pack(side=tk.TOP, fill=tk.BOTH)
    return_id_label = tk.Label(frame_inside_container, text='Book Id',
                        relief=tk.RIDGE, height=1, width=15,
                        bg='#FFDEDF', bd=7, font=(None, 24))
    return_id_label.pack(side=tk.TOP, pady=20)
    return_id_entry = tk.Entry(frame_inside_container,textvariable=id, relief=tk.SUNKEN, justify=tk.CENTER,
                               width=15, font=("Helvetica", 18, "bold"))
    return_id_entry.pack(side=tk.TOP, ipady=10)
    return_confirm_button = tk.Button(frame_inside_container, text="Return",
                               relief=tk.RIDGE, height=1, width=10,
                               bg='#9DDAD2', bd=1, font=(None, 17),
                               command=lambda: return_action(id))
    return_confirm_button.pack(side=tk.TOP, pady=20)
def delete():
    frame_inside_container = general()
    global id
    id=tk.StringVar()
    view_action()
    delete_label = tk.Label(frame_inside_container, text='Delete Book',
                           relief=tk.RIDGE, height=1, width=25,
                           bg='#FF9A98', bd=7, font=(None, 24))
    delete_label.pack(side=tk.TOP, fill=tk.BOTH)
    delete_id_label = tk.Label(frame_inside_container, text='Book Id',
                            relief=tk.RIDGE, height=1, width=15,
                            bg='#FFDEDF', bd=7, font=(None, 24))
    delete_id_label.pack(side=tk.TOP, pady=20)
    delete_id_entry = tk.Entry(frame_inside_container,textvariable=id, relief=tk.SUNKEN, justify=tk.CENTER,
                               width=15, font=("Helvetica", 18, "bold"))
    delete_id_entry.pack(side=tk.TOP, ipady=10)
    delete_confirm_button = tk.Button(frame_inside_container, text="Approve",
                              relief=tk.RIDGE, height=1, width=10,
                              bg='#9DDAD2', bd=1, font=(None, 17),
                              command=lambda: delete_action(id))
    delete_confirm_button.pack(side=tk.TOP, pady=20)

def result_page(result_text):
    frame_inside_container = general()
    view_action()
    result_label = tk.Label(frame_inside_container, text='Result',
                            relief=tk.RIDGE, height=1, width=25,
                            bg='#BFCAC4', bd=7, font=(None, 24))
    result_label.pack(side=tk.TOP, fill=tk.BOTH)
    result_text_label = tk.Label(frame_inside_container, text=result_text,
                               relief=tk.RIDGE, height=5, width=15,
                               bg='#CCBCA5', bd=7, font=(None, 24))
    result_text_label.pack(side=tk.TOP,fill=tk.BOTH,expand=1,pady=20)
def temp(): pass

def clear():
    window.destroy()

def main():
    label_header = tk.Label(frame_top, text='Library Management System',
                            relief=tk.RIDGE, height=1, width=55,
                            bg='#6EAD50', bd=7, font=(None, 18))
    label_header.pack(side=tk.LEFT, anchor=tk.W,expand=1,fill=tk.BOTH)
    clear_button = tk.Button(frame_top, text="X",
                             relief=tk.RIDGE, height=1, width=2,
                             bg='red', bd=1, font=(None, 24),
                             command=lambda: clear())
    clear_button.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.Y)
    delete_all_button = tk.Button(frame_top, text="Delete All",
                                  relief=tk.RIDGE, height=1, width=7,
                                  bg='#77B1AD', bd=1, font=(None, 24),
                                  command=lambda: delete_all_action())
    delete_all_button.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.Y)
    reset_button = tk.Button(frame_top, text="Reset",
                             relief=tk.RIDGE, height=1, width=5,
                             bg='#CDD6D5', bd=1, font=(None, 24),
                             command=lambda: drop_action())
    reset_button.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.Y)
    display_button = tk.Button(frame_left1, text="Display",
                               relief=tk.RIDGE, height=1, width=10,
                               bg='#048D79', bd=1, font=(None, 17),
                               command=lambda: display())
    display_button.pack(side=tk.TOP, expand=1, pady=3)
    search_button = tk.Button(frame_left1, text="Search",
                              relief=tk.RIDGE, height=1, width=10,
                              bg='#048D79', bd=1, font=(None, 17),
                              command=lambda: search())
    search_button.pack(side=tk.TOP, expand=1, pady=3)
    add_button = tk.Button(frame_left1, text="Add",
                           relief=tk.RIDGE, height=1, width=10,
                           bg='#048D79', bd=1, font=(None, 17),
                           command=lambda: add())
    add_button.pack(side=tk.TOP, expand=1, pady=3)
    issue_button = tk.Button(frame_left1, text="Issue",
                             relief=tk.RIDGE, height=1, width=10,
                             bg='#048D79', bd=1, font=(None, 17),
                             command=lambda: issue())
    issue_button.pack(side=tk.TOP, expand=1, pady=3)
    return_button = tk.Button(frame_left1, text="Return",
                             relief=tk.RIDGE, height=1, width=10,
                             bg='#048D79', bd=1, font=(None, 17),
                             command=lambda: return_())
    return_button.pack(side=tk.TOP, expand=1, pady=3)
    delete_button = tk.Button(frame_left1, text="Delete",
                              relief=tk.RIDGE, height=1, width=10,
                              bg='#048D79', bd=1, font=(None, 17),
                              command=lambda: delete())
    delete_button.pack(side=tk.TOP, expand=1, pady=3)

    window.mainloop()


if __name__ == "__main__":
    TableFn.create()
    TableFn.get_db()
    main()

