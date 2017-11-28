from tkinter import *
from operator import add
from tkinter import messagebox

fields1 = ('Channel 1 Data','Channel 2 Data','Channel 3 Data','Channel 4 Data','Sender','Receiver')

c1=[1,1,1,1]
c2=[1,-1,1,-1]
c3=[1,1,-1,-1]
c4=[1,-1,-1,1]
a=[]
l=[]

def final1(entries):
    m=entries['Channel 1 Data'].get()
    if(m=='0'):
        a.append(-1)
    elif(m=='1'):
        a.append(1)
    else:
        a.append(0)

    m=entries['Channel 2 Data'].get()
    if(m=='0'):
        a.append(-1)
    elif(m=='1'):
        a.append(1)
    else:
        a.append(0)
    m=entries['Channel 3 Data'].get()
    if(m=='0'):
        a.append(-1)
    elif(m=='1'):
        a.append(1)
    else:
        a.append(0)
    m=entries['Channel 4 Data'].get()
    if(m=='0'):
        a.append(-1)
    elif(m=='1'):
        a.append(1)
    else:
        a.append(0)
    print("the data for each channel is:",a)
    messagebox.showinfo("Channel wise Data",a)


    l1=[a[0]*x for x in c1]
    l2=[a[1]*x for x in c2]
    l3=[a[2]*x for x in c3]
    l4=[a[3]*x for x in c4]
    l5=list(map(add,l1,l2))
    l6=list(map(add,l3,l4))
    l=list(map(add,l5,l6))
    print("the data in channel is:",l)
    messagebox.showinfo("Data in Link",l)

    ch=int(entries['Sender'].get())
    #dummy rec
    rec=int(entries['Receiver'].get())
    if(ch==1):
        func1(l,c1)
    elif(ch==2):
        func1(l,c2)
    elif(ch==3):
        func1(l,c3)
    elif(ch==4):
        func1(l,c4)

def func1(l,c):
    ans=[]
    p=0
    for i in range(4):
        p=p+(l[i]*c[i])
    ans=p//4
    if(ans==1):
        messagebox.showinfo("Answer","The data sent was 1")
    elif(ans==-1):
        messagebox.showinfo("Answer","The data sent was 0")
    else:
        messagebox.showinfo("Answer","Silent i.e no data sent")

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        #ent.insert(0,"0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries



root = Tk()
root.title("Code Multiple Division Access")

ents = makeform(root, fields1)
b1 = Button(root, text='OK',command=(lambda e=ents: final1(e)))
b1.pack(side=LEFT, padx=5, pady=5)

b3 = Button(root, text='Quit', command=root.quit)
b3.pack(side=LEFT, padx=5, pady=5)
root.mainloop()
