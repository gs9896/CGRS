from tkinter import*   
from PIL import ImageTk
from admin import admin_l
import mysql.connector
from tkinter import messagebox
from user import user_l
from employee import emp_l
rootmain= Tk()
rootmain.title("CGRS")
rootmain.geometry("1200x600+100+50")

canvas1 = Canvas(rootmain, width = 1200, height = 600)
canvas1.pack()
         
class main:    
    def  __init__(self):
        self.db=mysql.connector.connect(host="localhost", database="cgrsdb", user="root", password="")
        imagepath1 = r'F:\Projects\python\cgrs\projimg2.jpg'
        image1 = ImageTk.PhotoImage(file = imagepath1)
        canvas1.create_image(0,0, image = image1,anchor="nw")
        imagepath2 = r'F:\Projects\python\cgrs\pietlogo.jpg'
        image2 = ImageTk.PhotoImage(file = imagepath2)
        canvas1.create_image(310,10, image = image2,anchor="nw")

        canvas1.create_text(430,10,font= "Times 20 bold",text="PANIPAT INSTITUTE OF \nENGINEERING & TECHNOLOGY",anchor="nw")
        canvas1.create_text(430,80,font= "Times 10 bold",text="(Approved by AICTE, New Delhi & Affiliated to Kurukshetra University, Kurukshetra)",anchor="nw")
        canvas1.create_text(350,200,tag="t1",font= "Times 20 bold underline",text="P.I.E.T Grievance & Redressal Mechanism",anchor="nw")

        self.user_login=Button(rootmain,text="User Login",width=30,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.user)
        canvas1.create_window(450,300,window=self.user_login,anchor="nw")
        self.user_login.bind("<Enter>", self.on_enter1)
        self.user_login.bind("<Leave>", self.on_leave1)

        self.ad_login=Button(rootmain,text="Admin Login",width=30,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.admin)
        canvas1.create_window(250,380,window=self.ad_login,anchor="nw")
        self.ad_login.bind("<Enter>", self.on_enter2)
        self.ad_login.bind("<Leave>", self.on_leave2)

        self.emp_login = Button(rootmain, text="Employee Login", width=30, font="Calibri 15 bold", bg="#ff8566",relief='ridge',command=self.employ)
        canvas1.create_window(650, 380, window=self.emp_login, anchor="nw")
        self.emp_login.bind("<Enter>", self.on_enter6)
        self.emp_login.bind("<Leave>", self.on_leave6)

        self.exitbutton=Button(rootmain,text="EXIT",width=30,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=exit)
        canvas1.create_window(450,460,window=self.exitbutton,anchor="nw")
        self.exitbutton.bind("<Enter>", self.on_enter3)
        self.exitbutton.bind("<Leave>", self.on_leave3)

        rootmain.resizable(0,0)
        rootmain.mainloop()
    def on_enter1(self, e):
        self.user_login['background'] = 'white'

    def on_leave1(self, e):
        self.user_login['background'] = '#ff8566'

    def on_enter2(self, e):
        self.ad_login['background'] = 'white'

    def on_leave2(self, e):
        self.ad_login['background'] = '#ff8566'

    def on_enter3(self, e):
        self.exitbutton['background'] = 'white'

    def on_leave3(self, e):
        self.exitbutton['background'] = '#ff8566'

    def on_enter4(self, e):
        self.sub_button['background'] = 'white'

    def on_leave4(self, e):
        self.sub_button['background'] = '#ff8566'

    def on_enter5(self, e):
        self.home_button['background'] = 'white'

    def on_leave5(self, e):
        self.home_button['background'] = '#ff8566'

    def on_enter6(self, e):
        self.emp_login['background'] = 'white'

    def on_leave6(self, e):
        self.emp_login['background'] = '#ff8566'

    def subuser(self):
        roll=self.id_entry.get()
        cur=self.db.cursor(buffered=True)
        cur.execute("select * from userdetails")
        dbu=cur.fetchone()
        try:
            while  dbu!="NULL" :
                r=dbu[0]
                pu=dbu[2]
                if int(roll)==r:
                    passw=self.pass_entry.get()
                    if int(passw)==pu:
                        user_l(dbu)
                        break
                    else:
                        messagebox.showinfo(title="info",message="Wrong UserName or Password")
                        break
                else:
                    dbu=cur.fetchone()
        except Exception:
            messagebox.showinfo(title="info",message="Please Enter Valid UserName & Password")

    def subadm(self):
        adid=self.id_entry.get()
        cur=self.db.cursor(buffered=True)
        cur.execute("select * from admindetail")
        dba=cur.fetchone()
        try:
            while  dba!="NULL" :
                i=dba[0]
                pa=dba[2]
                if int(adid)==i:
                    passw=self.pass_entry.get()
                    if int(passw)==pa:
                        admin_l()
                        break
                    else:
                        messagebox.showinfo(title="info",message="Wrong UserName or Password")
                        break
                else:
                    dba=cur.fetchone()
        except Exception:
            messagebox.showinfo(title="info",message="Please Enter Valid UserName & Password")

    def subemp(self):
        empid = self.id_entry.get()
        cur = self.db.cursor(buffered=True)
        cur.execute("select * from empdetails")
        dba = cur.fetchone()
        try:
            while dba != "NULL":
                i = dba[0]
                pa = dba[2]
                emp_name=dba[1]
                if int(empid) == i:
                    passw = self.pass_entry.get()
                    if int(passw) == pa:
                        emp_l(emp_name)
                        break
                    else:
                        messagebox.showinfo(title="info", message="Wrong UserName or Password")
                        break
                else:
                    dba = cur.fetchone()
        except Exception:
            messagebox.showinfo(title="info", message="Please Enter Valid UserName & Password")

    def user(self):
        canvas1.delete("t1")
        self.user_login.destroy()
        self.ad_login.destroy()
        self.emp_login.destroy()
        self.exitbutton.destroy()
        self.sv1=StringVar()
        self.sv2=StringVar()

        canvas1.create_text(500,200,font= "Times 20 bold ",text="User Login",anchor="nw",tag="t2")

        canvas1.create_text(450,300,text="Roll Number",font="Times 20 bold")

        canvas1.create_text(450,350,text="Password",font="Times 20 bold")


        self.id_entry=Entry(canvas1,font="calibri 15 ",textvariable=self.sv1)
        canvas1.create_window(700,300,window=self.id_entry)

        self.pass_entry=Entry(canvas1,font="calibri 15 ",textvariable=self.sv2,show="*")
        canvas1.create_window(700,350,window=self.pass_entry)

        self.sub_button=Button(rootmain,text="Submit",width=20,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.subuser)
        canvas1.create_window(370,450,window=self.sub_button,anchor="nw")
        self.sub_button.bind("<Enter>", self.on_enter4)
        self.sub_button.bind("<Leave>", self.on_leave4)
        self.home_button=Button(rootmain,text="Home",width=20,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.home)
        canvas1.create_window(620,450,window=self.home_button,anchor="nw")
        self.home_button.bind("<Enter>", self.on_enter5)
        self.home_button.bind("<Leave>", self.on_leave5)
    def admin(self):
        canvas1.delete("t1")
        self.user_login.destroy()
        self.ad_login.destroy()
        self.emp_login.destroy()
        self.exitbutton.destroy()

        canvas1.create_text(500,200,font= "Times 20 bold",text="Admin Login",anchor="nw",tag="t2")
        canvas1.create_text(450,300,text="Admin-Id",font="Times 20 bold")

        canvas1.create_text(450,350,text="Password",font="Times 20 bold")

        self.id_entry=Entry(canvas1,font="calibri 15 ")
        canvas1.create_window(700,300,window=self.id_entry)

        self.pass_entry=Entry(canvas1,font="calibri 15 ",show="*")
        canvas1.create_window(700,350,window=self.pass_entry)

        self.sub_button=Button(rootmain,text="Submit",width=20,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.subadm)
        canvas1.create_window(370,450,window=self.sub_button,anchor="nw")
        self.sub_button.bind("<Enter>", self.on_enter4)
        self.sub_button.bind("<Leave>", self.on_leave4)

        self.home_button=Button(rootmain,text="Home",width=20,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.home)
        canvas1.create_window(620,450,window=self.home_button,anchor="nw")
        self.home_button.bind("<Enter>", self.on_enter5)
        self.home_button.bind("<Leave>", self.on_leave5)

    def employ(self):
        canvas1.delete("t1")
        self.user_login.destroy()
        self.ad_login.destroy()
        self.emp_login.destroy()
        self.exitbutton.destroy()

        canvas1.create_text(500,200,font= "Times 20 bold",text="Employee Login",anchor="nw",tag="t2")
        canvas1.create_text(450,300,text="Employee-Id",font="Times 20 bold")

        canvas1.create_text(450,350,text="Password",font="Times 20 bold")

        self.id_entry=Entry(canvas1,font="calibri 15 ")
        canvas1.create_window(700,300,window=self.id_entry)

        self.pass_entry=Entry(canvas1,font="calibri 15 ",show="*")
        canvas1.create_window(700,350,window=self.pass_entry)

        self.sub_button=Button(rootmain,text="Submit",width=20,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.subemp)
        canvas1.create_window(370,450,window=self.sub_button,anchor="nw")
        self.sub_button.bind("<Enter>", self.on_enter4)
        self.sub_button.bind("<Leave>", self.on_leave4)

        self.home_button=Button(rootmain,text="Home",width=20,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.home)
        canvas1.create_window(620,450,window=self.home_button,anchor="nw")
        self.home_button.bind("<Enter>", self.on_enter5)
        self.home_button.bind("<Leave>", self.on_leave5)

    def home(self):
        canvas1.delete("t2")
        self.id_entry.destroy()
        self.pass_entry.destroy()
        self.sub_button.destroy()
        self.home_button.destroy()
        self.__init__()

ob=main()



