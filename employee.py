from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
newrec=""
class emp_l:
    def __init__(self, rec):
        global newrec
        newrec=rec
        self.db = mysql.connector.connect(host="localhost", database="cgrsdb", user="root", password="")
        self.status_root = Tk()
        self.status_root.title(rec+" Window")
        self.status_root.geometry("1350x660+0+30")
        self.frame_canvas = Canvas(self.status_root)
        self.frame_canvas.grid(row=0, column=0, sticky="news")
        self.canvas5 = Canvas(self.frame_canvas, width=1350, height=200)
        self.canvas5.grid(row=0, column=0)
        self.canvas5.create_rectangle(0, 0, 1350, 150, fill="gray")
        self.canvas5.create_text(420, 15, text="Complaint & Grievance Section", font="Times 25 bold underline",
                                 anchor="nw")
        self.canvas5.create_text(370, 70, text="Panipat Institute Of Engineering & Technology,\n\t\tSamalkha",
                                 font="Times 20 bold", fill="green", anchor="nw")

        self.complaint_id = Label(self.canvas5, text="Complaint Id", font="Times 15 bold", fg="green")
        self.canvas5.create_window(80, 170, window=self.complaint_id)
        self.date = Label(self.canvas5, text="Date", font="Times 15 bold", fg="green")
        self.canvas5.create_window(280, 170, window=self.date)
        self.complaint = Label(self.canvas5, text="Complaint", font="Times 15 bold", fg="green")
        self.canvas5.create_window(520, 170, window=self.complaint)
        self.category = Label(self.canvas5, text="Category", font="Times 15 bold", fg="green")
        self.canvas5.create_window(760, 170, window=self.category)
        self.action = Label(self.canvas5, text="Action", font="Times 15 bold", fg="green")
        self.canvas5.create_window(990, 170, window=self.action)
        self.status = Label(self.canvas5, text="Status", font="Times 15 bold", fg="green")
        self.canvas5.create_window(1240, 170, window=self.status)

        self.Exit = Button(self.status_root, text="Exit", width=15, font="Times 15 bold", bg="#ff8566", relief='ridge',command=self.status_root.destroy)
        self.canvas5.create_window(1125,110, window=self.Exit)
        self.Exit.bind("<Enter>", self.on_senter1)
        self.Exit.bind("<Leave>", self.on_sleave1)

        self.take_action = Button(self.status_root, text="Change Status", width=15, font="Times 15 bold",bg="#ff8566", relief='ridge',command=self.stat)
        self.canvas5.create_window(1025, 50, window=self.take_action)
        self.take_action.bind("<Enter>", self.on_senter2)
        self.take_action.bind("<Leave>", self.on_sleave2)

        self.Refresh_button = Button(self.status_root, font="Times 15 bold", width=15, text="Refresh", bg="#ff8566",relief="ridge", command=self.refresh)
        self.canvas5.create_window(1225, 50, window=self.Refresh_button)
        self.Refresh_button.bind("<Enter>", self.on_senter3)
        self.Refresh_button.bind("<Leave>", self.on_sleave3)

        self.canvas5.create_line(0, 190, 1350, 190, width=5)
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
        self.cur.execute("select * from complaintdb where empname='" + str(rec) + "'")
        db = self.cur.fetchall()
        rows = len(db)
        columns = 6
        i = 0
        try:
            comp_label = [[Label() for j in range(columns)] for i in range(rows)]
            for r in db:
                for j in range(0, columns):
                    comp_label[i][0] = Label(self.frame, width=15, font="Times 15 ", text=r[4])
                    comp_label[i][0].grid(row=i, column=0, sticky='news')
                    comp_label[i][1] = Label(self.frame, width=20, font="Times 15 ", text=r[3])
                    comp_label[i][1].grid(row=i, column=1, sticky='news')
                    comp_label[i][2] = Text(self.frame, height=4, width=25, bg="#f0f0f0", font="Times 15 ")
                    comp_label[i][2].grid(row=i, column=2, sticky='news')
                    comp_label[i][2].insert("1.0", r[5])
                    comp_label[i][2].config(state=DISABLED)
                    comp_label[i][3] = Label(self.frame, width=20, font="Times 15 ", text=r[6])
                    comp_label[i][3].grid(row=i, column=3, sticky='news')
                    comp_label[i][4] = Text(self.frame, height=4, width=25, bg="#f0f0f0", font="Times 15")
                    comp_label[i][4].grid(row=i, column=4, sticky='news')
                    comp_label[i][4].insert("1.0", r[8])
                    comp_label[i][4].config(state=DISABLED)
                    comp_label[i][5] = Label(self.frame, width=20, font="Times 15", text=r[7])
                    comp_label[i][5].grid(row=i, column=5, sticky='news')

                i = i + 1
        except Exception:
            pass
        if rows == 0:
            a = 0
        elif rows == 1:
            a = 1
        elif rows == 2:
            a = 2
        elif rows == 3:
            a = 3
        elif rows == 4:
            a = 4
        else:
            a = 5
        self.frame.update_idletasks()
        c_width = sum([comp_label[0][j].winfo_width() for j in range(0, a)])
        r_height = sum([comp_label[i][0].winfo_height() for i in range(0, a)])
        self.frame_comp.config(width=c_width + vsb.winfo_width(),
                               height=r_height)
        self.canvas_frame.config(scrollregion=self.canvas_frame.bbox("all"))
        self.status_root.resizable(0, 0)
        self.status_root.mainloop()

    def stat(self):
        self.action_root=Tk()
        self.action_root.geometry("350x320+400+200")
        self.action_root.title("Action")
        self.main_label=Label(self.action_root,text="* All the fields are mandatory to fill ",font="Times 10 bold",fg="#ff8566")
        self.main_label.place(x=50,y=10,height=30,width=250)

        self.strvar=StringVar(self.action_root)
        self.comp_aintid=Label(self.action_root,text="Complaint Id",font="Helvetica 10 bold")
        self.comp_aintid.place(x=10,y=40,height=20,width=100)
        self.comp_aintide=Entry(self.action_root,textvariable=self.strvar,width=23,font="Helvetica 10")
        self.comp_aintide.place(x=140,y=40,height=20,width=200)

        categories = ["Select Complaint Category", "Academic (Lectures)", "Training & Placement cell", "Hostel","Transport", "Accounts", "library", "Canteen", "others"]
        self.category_l = Label(self.action_root, text="Category", font="Helvetica 10 bold")
        self.category_l.place(x=10,y=70,height=20,width=100)
        self.category_e = ttk.Combobox(self.action_root,values=categories, font="Helvetica 10")
        self.category_e.place(x=140,y=70,height=20,width=200)
        self.category_e.current(0)

        st=["Select Status","Processing","Closed"]
        self.status_label = Label(self.action_root, text="Status", font="Helvetica 10 bold")
        self.status_label.place(x=10,y=100,height=20,width=100)
        self.st_box = ttk.Combobox(self.action_root, values=st, font="Helvetica 10")
        self.st_box.place(x=140,y=100,height=20,width=200)
        self.st_box.current(0)

        self.action_label = Label(self.action_root, text="Action", font="Helvetica 10 bold")
        self.action_label.place(x=10,y=150,height=20,width=100)
        self.action_entry = Text(self.action_root, font="Helvetica 10")
        self.action_entry.place(x=140,y=140,height=100,width=200)
        self.scrb = Scrollbar(self.action_entry)
        self.scrb.pack(side=RIGHT, fill=Y)
        self.scrb.config(command=self.action_entry.yview)
        self.action_entry.config(yscrollcommand=self.scrb.set)

        self.update_button=Button(self.action_root,font="Helvetica 10 bold",text="Assign",bg="#ff8566",relief="ridge",command=self.Ac_tion)
        self.update_button.place(x=40,y=260,height=30,width=100)
        self.update_button.bind("<Enter>", self.on_empenter1)
        self.update_button.bind("<Leave>", self.on_empleave1)

        self.cancel_button = Button(self.action_root, font="Helvetica 10 bold", text="Cancel", bg="#ff8566",relief="ridge", command=self.action_root.destroy)
        self.cancel_button.place(x=190,y=260,height=30,width=100)
        self.cancel_button.bind("<Enter>", self.on_empenter2)
        self.cancel_button.bind("<Leave>", self.on_empleave2)

        self.action_root.resizable(0,0)
        self.action_root.mainloop()

    def refresh(self):
        global newrec
        self.status_root.destroy()
        self.__init__(newrec)

    def on_senter1(self, e):
        self.Exit['background'] = 'white'

    def on_sleave1(self, e):
        self.Exit['background'] = '#ff8566'

    def on_senter2(self, e):
        self.take_action['background'] = 'white'

    def on_sleave2(self, e):
        self.take_action['background'] = '#ff8566'

    def on_senter3(self, e):
        self.Refresh_button['background'] = 'white'

    def on_sleave3(self, e):
        self.Refresh_button['background'] = '#ff8566'

    def on_empenter1(self, e):
        self.update_button['background'] = 'white'

    def on_empleave1(self, e):
        self.update_button['background'] = '#ff8566'

    def on_empenter2(self, e):
        self.cancel_button['background'] = 'white'

    def on_empleave2(self, e):
        self.cancel_button['background'] = '#ff8566'

    def Ac_tion(self):
        comp=self.comp_aintide.get()
        cat_gory=self.category_e.get()
        stat_s=self.st_box.get()
        actio_n=self.action_entry.get("1.0",END)
        if(comp=="" or cat_gory=="Select Complaint Category"):
            messagebox.showinfo(title="Info",message="Please fill all the fields first")
        else:
            self.cur.execute("select * from complaintdb where complaintId='"+comp+"' AND category='"+cat_gory+"'")
            db1=self.cur.fetchone()
            self.cur.execute("update complaintdb set Status='"+stat_s+"',Action='"+db1[8]+actio_n+"' where complaintId='"+comp+"' and category='"+cat_gory+"'")
            self.db.commit()
            self.action_root.destroy()
