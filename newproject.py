from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import sqlite3


#propriete de fenetre
root = Tk()
root.title("RDV MEDCINE")
root.geometry('1240x510')
root.resizable(False,False)
root.configure(bg='#2c3e50')

nom = StringVar()
prenom = StringVar()
genre = StringVar()
age = StringVar()
mobile = StringVar()
jour_Rdv = StringVar()



#=====ENTRIE_FRAME===== 
entries_frame = Frame(root,bg='#2c3e50')
entries_frame.place(x=1,y=1,width=360,height=510)
title = Label(entries_frame,text='RDV MEDCINE',font=('Calibri,18,bold'))
title.place(x=10,y=1)

lblName = Label(entries_frame,text="Nom",font=('Calibri',16,'bold'),bg='#2c3e50',fg='white')
lblName.place(x=10,y=50)

txtName = Entry(entries_frame,width=20,textvariable=nom,font=('Calibri',16))
txtName.place(x=120,y=50)

lblPrenom = Label(entries_frame,text="Prenom",font=('Calibri',16,'bold'),bg='#2c3e50',fg='white')
lblPrenom.place(x=10,y=90)

txtPrenom = Entry(entries_frame,textvariable=prenom,width=20,font=('Calibri',16))
txtPrenom.place(x=120,y=90)


lblGender = Label(entries_frame,text="Genre",font=('Calibri',16,'bold'),bg='#2c3e50',fg='white')
lblGender.place(x=10,y=130)
comboGender = ttk.Combobox(entries_frame,textvariable=genre,state='readonly',width=18,font=('Calibri',16))
comboGender['values'] = ("Homme","Femme")
comboGender.place(x=120,y=130)


lblAge = Label(entries_frame,text="Age",font=('Calibri',16,'bold'),bg='#2c3e50',fg='white')
lblAge.place(x=10,y=170)

txtAge = Entry(entries_frame,textvariable=age,width=20,font=('Calibri',16))
txtAge.place(x=120,y=170)

lblContact = Label(entries_frame,text="Mobile",font=('Calibri',16,'bold'),bg='#2c3e50',fg='white')
lblContact.place(x=10,y=210)

txtContact = Entry(entries_frame,textvariable=mobile,width=20,font=('Calibri',16))
txtContact.place(x=120,y=210)


lblAdress = Label(entries_frame,text="Adress :",font=('Calibri',16,'bold'),bg='#2c3e50',fg='white')
lblAdress.place(x=10,y=250)

txtAdress = Text(entries_frame,width=30,height=2,font=('Calibri',16))
txtAdress.place(x=120,y=250)


lblJour = Label(entries_frame,text="Jour RDV",font=('Calibri',16,'bold'),bg='#2c3e50',fg='white')
lblJour.place(x=10,y=330)

txtJour = Entry(entries_frame,textvariable=jour_Rdv,width=20,font=('Calibri',16))
txtJour.place(x=120,y=330)

#=====Defined======
def hide():
    root.geometry('365x515+0+0')
def show():
    root.geometry('1220x510+0+0')



btnhide = Button(entries_frame,text='HIDE',bg='white',bd=1,relief=SOLID,cursor='hand2',command=hide)
btnhide.place(x=270,y=10)

btnshow = Button(entries_frame,text='SHOW',bg='white',bd=1,relief=SOLID,cursor='hand2',command=show)
btnshow.place(x=310,y=10)




def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row 
    row = data["values"]
    nom.set(row[1])
    prenom.set(row[2])
    genre.set(row[3])
    age.set(row[4])
    mobile.set(row[5])
    txtAdress.delete(1.0,END)
    txtAdress.insert(END,row[6])
    jour_Rdv.set(row[7])


def clear():
    nom.set("")
    prenom.set("")
    genre.set("")
    age.set("")
    mobile.set("")
    txtAdress.delete("1.0",END)
    jour_Rdv.set("")

#ajouter
def add():
    if txtName.get() == "" or txtPrenom.get() == "" or comboGender.get() == "" or txtAge.get() == "" or txtContact.get() == "" or txtJour.get() == "":
        messagebox.showerror("Error","Please Fill all the Entry")
        return
    nom = txtName.get()
    prenom = txtPrenom.get()
    genre = comboGender.get()
    age = txtAge.get()
    mobile = txtContact.get()
    adress = txtAdress.get(1.0,END)
    jour_Rdv = txtJour.get()
    messagebox.showinfo("Success","Added Success")
    clear()
#Creeon la connexion
    con = sqlite3.connect('Medecine.db')
    cuser = con.cursor()
    cuser.execute("insert into patient values (NULL,?,?,?,?,?,?,?)",
                             (nom,prenom,genre,age,mobile,adress,jour_Rdv))
    con.commit()
    con.close()

 #afficher
    con = sqlite3.connect('Medecine.db')
    cuser = con.cursor()
    select = cuser.execute("select *from patient order by id desc")
    select = list(select)
    tv.insert('',END,values = select[0])
    con.close()


#delete
def supprimer():
    codeSelectionner = tv.item(tv.selection())['values'][0]
    con = sqlite3.connect("Medecine.db")
    cuser = con.cursor()
    delete  =cuser.execute("delete from patient where ID = {}".format(codeSelectionner))
    con.commit()
    tv.delete(tv.selection())




#=====ENTRIE_Button===== 
btn_frame = Frame(entries_frame,bg='#2c3e50',bd=1,relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=100)

btnAdd = Button(btn_frame,
                text='Ajouter',
                width=14,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg = '#16a085',
                bd = 0,
                command=add
                ).place(x=4,y=5)




btnDelete = Button(btn_frame,
                text='Supprimer',
                width=14,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg = '#c0392b',
                bd = 0,
                command=supprimer
                ).place(x=170,y=5)


btnClear = Button(btn_frame,
                text='Clear',
                width=14,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg = '#f39c12',
                bd = 0,
                command=clear
                ).place(x=90,y=50)



#=====ENTRIE_FRAME===== 
tree_frame = Frame(root,bg='white')
tree_frame.place(x=365,y=1,width=875,height=510)
style = ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',13))
tv = ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width="5")

tv.heading("2",text="Nom")
tv.column("2",width="25")

tv.heading("3",text="Prenom")
tv.column("3",width="25")

tv.heading("4",text="Genre")
tv.column("4",width="25")

tv.heading("5",text="Age")
tv.column("5",width="10")

tv.heading("6",text="Mobile")
tv.column("6",width="35")

tv.heading("7",text="Adress")
tv.column("7",width="40")

tv.heading("8",text="Jour RDV")
tv.column("8",width="50")
tv.bind("<ButtonRelease-1>",getData)
tv['show'] = 'headings'

tv.place(x=1,y=1,height=510,width=875)

# afficher les informations de la table
con =  sqlite3.connect('Medecine.db')
cuser = con.cursor()
select = cuser.execute("select * from patient")
for row in select:
    tv.insert('', END, value = row)
con.close()

mainloop()