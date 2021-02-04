from tkinter import *

def addEntry(item,lst):
    global tasks
    task = item.get()
    tasks.append(task)
    lst.insert(END,task)
    item.delete(0,END)
    print(tasks)
def clearText(textbox):
    textbox.delete(0,END)
def deletetask(lstbox):
    task = lstbox.get(ANCHOR)
    tasks.remove(task)
    lstbox.delete(ANCHOR)
    



root = Tk()
width = 380
height = 600
tasks = []
root.geometry(f"{width}x{height}")
root.title("To do list maker")

lis = Listbox(root,font=('Cambria',10),width=40)
TaskEntry = Entry(root, text="Type task", width=40, bg="grey", fg="white", font=('Cambria',12))
AddTask = Button(root, text="Add", pady=5, padx=5, width=20, command = lambda:addEntry(TaskEntry,lis))
ClearText = Button(root, text="clear", pady=5, padx=5, width=20, command = lambda:clearText(TaskEntry))
DeleteTask = Button(root, text="Delete", pady=5, padx=5, width=20, command = lambda:deletetask(lis))




#render widgets
TaskEntry.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
AddTask.grid(row=1, column=0)
ClearText.grid(row=1, column=1)
lis.grid(row=2, column=0, columnspan=2, pady=10)
DeleteTask.grid(row=3, column=0, columnspan=2, pady=10)
root.mainloop()
