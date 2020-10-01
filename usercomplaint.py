from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
db=mysql.connector.connect(host="localhost", database="cgrsdb", user="root", password="")
class complaint:
    def submit(self):
        cur=db.cursor()
        roll=self.roll_entry.get()
        name=self.name_entry.get()
        category=self.cb.get()
        date=self.date_entry.get()
        desc=self.desc_entry.get("1.0",END)
        cur.execute("select * from complaintdb where RollNo='"+roll+"' AND category='"+category+"'")
        rec =cur.fetchall()
        totrec=len(rec)
        if totrec==1 or totrec>1:
            messagebox.showinfo(title="Info",message="Complaint already made for "+category)
        else:
            if(date=="Year-Month-Date" or category=="Select Complaint Category" or len(desc)==1):
                messagebox.showinfo(title="Info",message="Please Enter All The Fields And make Entry correctly!")
            else:
                cur.execute("insert into complaintdb (RollNo,Name,Date,Complaint,category) values('"+roll+"','"+name+"','"+date+"','"+desc+"','"+category+"')")
            db.commit()
        self.complaint_root.destroy()
    def __init__(self,rec):
        self.complaint_root=Tk()
        self.complaint_root.title("Complaint Section")
        self.complaint_root.geometry("500x600+60+50")
        
        categories=["Select Complaint Category","Academic (Lectures)","Training & Placement cell","Hostel","Transport","Accounts","library","Canteen","others"]
        self.canvas3=Canvas(self.complaint_root,width=500,height=600)
        self.canvas3.create_rectangle(0,0,500,100,fill="#ff8566")
        self.canvas3.create_text(60,10,text="Complaint & Grievance Section",font="Times 20 bold underline",anchor="nw")
        self.canvas3.create_text(50,50,text="Panipat Institute Of Engineering & Technology,\n\t\tSamalkha",font="Times 15 bold",fill="green",anchor="nw")

        self.student_name=Label(self.complaint_root,text="Name of Student",font="Helvetica 15 bold")
        self.student_name.place(x=20,y=150)
        self.var1=StringVar(self.complaint_root)
        self.var1.set(rec[1])
        self.name_entry=Entry(self.complaint_root,textvariable=self.var1,font="Helvetica 12")
        self.name_entry.place(x=250,y=150,height=30,width=240)
        self.name_entry.config(state="readonly")

        self.student_roll=Label(self.complaint_root,text="Student's RollNumber",font="Helvetica 15 bold")
        self.student_roll.place(x=20,y=190)
        self.var2=StringVar(self.complaint_root)
        self.var2.set(rec[0])
        self.roll_entry=Entry(self.complaint_root,textvariable=self.var2,font="Helvetica 12")
        self.roll_entry.place(x=250,y=190,height=30,width=240)
        self.roll_entry.config(state="readonly")
        
        self.comp_catg=Label(self.complaint_root,text="Complaint Category",font="Helvetica 15 bold")
        self.comp_catg.place(x=20,y=230)
        self.cb=ttk.Combobox(self.complaint_root,text="Enter complaint Category",values=categories)
        self.cb.place(x=250,y=230,height=30,width=240)
        self.cb.current(0)
        
        self.datevar=StringVar(self.complaint_root)
        self.datevar.set("Year-Month-Date")
        self.date=Label(self.complaint_root,text="Date of Complaint",font="Helvetica 15 bold")
        self.date.place(x=20,y=270)
        self.date_entry=Entry(self.complaint_root,textvariable=self.datevar,font="Helvetica 12")
        self.date_entry.place(x=250,y=270,height=30,width=240)
        self.date_entry.bind('<FocusIn>', self.focusIn)
        self.date_entry.bind('<FocusOut>', self.focusOut)

        self.desc=Label(self.complaint_root,text="Complaint Description",font="Helvetica 15 bold")
        self.desc.place(x=20,y=365)
        self.desc_entry=Text(self.complaint_root,font="Helvetica 12")
        self.desc_entry.place(x=250,y=310,height=140,width=240)
        self.scrb = Scrollbar(self.desc_entry)
        self.scrb.pack(side=RIGHT, fill=Y)
        self.scrb.config(command=self.desc_entry.yview)
        self.desc_entry.config(yscrollcommand=self.scrb.set)

        self.submit_button=Button(self.complaint_root,text="Submit",width=20,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.submit)
        self.submit_button.place(x=20,y=500)
        self.submit_button.bind("<Enter>", self.on_ucenter1)
        self.submit_button.bind("<Leave>", self.on_ucleave1)

        self.cancel_button=Button(self.complaint_root,text="Cancel",width=20,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.complaint_root.destroy)
        self.cancel_button.place(x=260,y=500)
        self.cancel_button.bind("<Enter>", self.on_ucenter2)
        self.cancel_button.bind("<Leave>", self.on_ucleave2)
        
        self.canvas3.pack()
        self.complaint_root.resizable(0,0)
        self.complaint_root.mainloop()
    def focusIn(self, event):
        s=self.datevar.get()

        if(s=="Year-Month-Date"):
            self.datevar.set("")
    def focusOut(self, event):
        s=self.datevar.get()
        if(s==""):
            self.datevar.set("Year-Month-Date")

    def on_ucenter1(self, e):
        self.submit_button['background'] = 'white'

    def on_ucleave1(self, e):
        self.submit_button['background'] = '#ff8566'

    def on_ucenter2(self, e):
        self.cancel_button['background'] = 'white'

    def on_ucleave2(self, e):
        self.cancel_button['background'] = '#ff8566'

class complaintstatus:
    
    def __init__(self,rec):
        self.status_root = Tk()
        self.status_root.title("Complaint Section")
        self.db = mysql.connector.connect(host="localhost", database="cgrsdb", user="root", password="")
        self.status_root.geometry("1350x660+0+30")
        self.frame_canvas = Canvas(self.status_root)
        self.frame_canvas.grid(row=0, column=0, sticky="news")
        self.canvas5 = Canvas(self.frame_canvas, width=1350, height=200)
        self.canvas5.grid(row=0, column=0)
        self.canvas5.create_rectangle(0, 0, 1350, 150, fill="gray")
        self.canvas5.create_text(420, 15, text="Complaint & Grievance Section", font="Times 25 bold underline", anchor="nw")
        self.canvas5.create_text(370, 70, text="Panipat Institute Of Engineering & Technology,\n\t\tSamalkha",font="Times 20 bold", fill="green", anchor="nw")

        self.roll_no = Label(self.canvas5, text="Roll No", font="Times 15 bold", fg="green")
        self.canvas5.create_window(80, 170, window=self.roll_no)
        self.name = Label(self.canvas5, text="Name", font="Times 15 bold", fg="green")
        self.canvas5.create_window(260, 170, window=self.name)
        self.date = Label(self.canvas5, text="Date", font="Times 15 bold", fg="green")
        self.canvas5.create_window(400, 170, window=self.date)
        self.complaint = Label(self.canvas5, text="Complaint", font="Times 15 bold", fg="green")
        self.canvas5.create_window(590, 170, window=self.complaint)
        self.category = Label(self.canvas5, text="Category", font="Times 15 bold", fg="green")
        self.canvas5.create_window(820, 170, window=self.category)
        self.action = Label(self.canvas5, text="Action", font="Times 15 bold", fg="green")
        self.canvas5.create_window(1050, 170, window=self.action)
        self.status = Label(self.canvas5, text="Status", font="Times 15 bold", fg="green")
        self.canvas5.create_window(1280, 170, window=self.status)

        self.Exit = Button(self.status_root, text="Exit", width=20, font="Times 15 bold", bg="#ff8566", relief='ridge', command=self.status_root.destroy)
        self.canvas5.create_window(1150, 90, window=self.Exit)
        self.Exit.bind("<Enter>", self.on_senter1)
        self.Exit.bind("<Leave>", self.on_sleave1)
        self.canvas5.create_line(0, 190, 1350, 190,width=5)
        self.frame_comp = Frame(self.status_root)
        self.frame_comp.grid(row=1, column=0, sticky="news")
        self.frame_comp.grid_rowconfigure(0, weight=1)
        self.frame_comp.grid_columnconfigure(0, weight=1)
        self.frame_comp.grid_propagate(False)

        self.canvas_frame = Canvas(self.frame_comp)
        self.canvas_frame.grid(row=0, column=0, sticky="news")

        vsb = Scrollbar(self.frame_comp, orient="vertical", command=self.canvas_frame.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        self.canvas_frame.configure(yscrollcommand=vsb.set)

        self.frame = Frame(self.canvas_frame)
        self.canvas_frame.create_window((0, 0), window=self.frame, anchor='nw')
        self.cur = self.db.cursor()
        self.cur.execute("select * from complaintdb where RollNo='"+str(rec[0])+"'")
        db = self.cur.fetchall()
        rows = len(db)
        columns = 7
        i=0
        try:
            comp_label = [[Label() for j in range(columns)] for i in range(rows)]
            for r in db:
                for j in range(0, columns):
                    comp_label[i][0] = Label(self.frame, width=15, font="Times 15 ", text=r[0])
                    comp_label[i][0].grid(row=i, column=0, sticky='news')
                    comp_label[i][1] = Label(self.frame, width=15, font="Times 15 ", text=r[1])
                    comp_label[i][1].grid(row=i, column=1, sticky='news')
                    comp_label[i][2] = Label(self.frame, width=10, font="Times 15 ", text=r[3])
                    comp_label[i][2].grid(row=i, column=2, sticky='news')
                    comp_label[i][3] = Text(self.frame, height=4, width=25, bg="#f0f0f0", font="Times 15 ")
                    comp_label[i][3].grid(row=i, column=3, sticky='news')
                    comp_label[i][3].insert("1.0", r[5])
                    comp_label[i][3].config(state=DISABLED)
                    comp_label[i][4] = Label(self.frame, width=20, font="Times 15 ", text=r[6])
                    comp_label[i][4].grid(row=i, column=4, sticky='news')
                    comp_label[i][5] = Text(self.frame,height=4,  width=25, bg="#f0f0f0", font="Times 15")
                    comp_label[i][5].grid(row=i, column=5, sticky='news')
                    comp_label[i][5].insert("1.0", r[8])
                    comp_label[i][5].config(state=DISABLED)
                    comp_label[i][6] = Label(self.frame, width=15, font="Times 15", text=r[7])
                    comp_label[i][6].grid(row=i, column=6, sticky='news')

                if r[7]=="Closed":
                    self.cur.execute("delete from complaintdb where Status='"+r[7]+"'")
                    self.db.commit()

                i=i+1
        except Exception:
            pass
        if rows==0:
            a=0
        elif rows==1:
            a=1
        elif rows==2:
            a=2
        elif rows==3:
            a=3
        elif rows==4:
            a=4
        else:
            a=5
        self.frame.update_idletasks()
        c_width = sum([comp_label[0][j].winfo_width() for j in range(0, a)])
        r_height = sum([comp_label[i][0].winfo_height() for i in range(0, a)])
        self.frame_comp.config(width=c_width + vsb.winfo_width(),
                               height=r_height)
        self.canvas_frame.config(scrollregion=self.canvas_frame.bbox("all"))
        self.status_root.resizable(0, 0)
        self.status_root.mainloop()

    def on_senter1(self, e):
        self.Exit['background'] = 'white'

    def on_sleave1(self, e):
        self.Exit['background'] = '#ff8566'
#ob=complaintstatus("gurdeep")

