from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
class complaint_sec:
    def __init__(self):
        self.adcomp_root=Tk()
        self.adcomp_root.title("Complaint Section")
        self.db=mysql.connector.connect(host="localhost", database="cgrsdb", user="root", password="")
        self.adcomp_root.geometry("1350x660+0+30")
        self.frame_canvas=Canvas(self.adcomp_root)
        self.frame_canvas.grid(row=0,column=0,sticky="news")
        self.canvas5=Canvas(self.frame_canvas,width=1350,height=200)
        self.canvas5.grid(row=0,column=0)
        self.canvas5.create_rectangle(0,0,1350,150,fill="gray")
        self.canvas5.create_text(380,15,text="Complaint & Grievance Section",font="Times 25 bold underline",anchor="nw")
        self.canvas5.create_text(330,70,text="Panipat Institute Of Engineering & Technology,\n\t\tSamalkha",font="Times 20 bold",fill="green",anchor="nw")
        self.Exit = Button(self.adcomp_root, text="Exit", width=15, font="Times 15 bold", bg="#ff8566", relief='ridge', command=self.adcomp_root.destroy)
        self.canvas5.create_window(1125, 110, window=self.Exit)
        self.Exit.bind("<Enter>", self.on_adenter1)
        self.Exit.bind("<Leave>", self.on_adleave1)

        self.take_action = Button(self.adcomp_root, text="Assign Employee", width=15, font="Times 15 bold", bg="#ff8566",relief='ridge',command=self.assign)
        self.canvas5.create_window(1025, 50, window=self.take_action)
        self.take_action.bind("<Enter>", self.on_adenter2)
        self.take_action.bind("<Leave>", self.on_adleave2)

        self.Refresh_button = Button(self.adcomp_root, font="Times 15 bold", width=15, text="Refresh", bg="#ff8566",relief="ridge", command=self.refresh)
        self.canvas5.create_window(1225, 50, window=self.Refresh_button)
        self.Refresh_button.bind("<Enter>", self.on_adenter3)
        self.Refresh_button.bind("<Leave>", self.on_adleave3)

        self.complaint_id = Label(self.canvas5, text="Complaint Id", font="Times 15 bold", fg="green")
        self.canvas5.create_window(80, 170, window=self.complaint_id)
        self.empname = Label(self.canvas5, text="Employee Assigned", font="Times 15 bold", fg="green")
        self.canvas5.create_window(260, 170, window=self.empname)
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
        self.canvas5.create_line(0,190,1350,190,width=5)

        self.frame_comp=Frame(self.adcomp_root)
        self.frame_comp.grid(row=1,column=0,sticky="news")
        self.frame_comp.grid_rowconfigure(0, weight=1)
        self.frame_comp.grid_columnconfigure(0, weight=1)
        self.frame_comp.grid_propagate(False)

        self.canvas_frame = Canvas(self.frame_comp)
        self.canvas_frame.grid(row=0, column=0, sticky="news")

        vsb = Scrollbar(self.frame_comp, orient="vertical", command=self.canvas_frame.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        self.canvas_frame.configure(yscrollcommand=vsb.set)
        self.frame=Frame(self.canvas_frame)
        self.canvas_frame.create_window((0,0),window=self.frame,anchor='nw')
        self.cur = self.db.cursor()
        self.cur.execute("select * from complaintdb")
        db=self.cur.fetchall()
        rows=len(db)
        columns = 7
        i=0
        try:
            comp_label = [[Label() for j in range(columns)] for i in range(rows)]
            for r in db:
                for j in range(0, columns):
                    comp_label[i][0] = Label(self.frame, width=15, font="Times 15 ", text=r[4])
                    comp_label[i][0].grid(row=i, column=0, sticky='news')
                    comp_label[i][1] = Label(self.frame, width=15, font="Times 15 ", text=r[2])
                    comp_label[i][1].grid(row=i, column=1, sticky='news')
                    comp_label[i][2] = Label(self.frame, width=10, font="Times 15 ", text=r[3])
                    comp_label[i][2].grid(row=i, column=2, sticky='news')
                    comp_label[i][3] = Text(self.frame,height=4, width=25,bg="#f0f0f0" ,font="Times 15 ")
                    comp_label[i][3].grid(row=i, column=3, sticky='news')
                    comp_label[i][3].insert("1.0",r[5])
                    comp_label[i][3].config(state=DISABLED)
                    comp_label[i][4] = Label(self.frame, width=20, font="Times 15 ", text=r[6])
                    comp_label[i][4].grid(row=i, column=4, sticky='news')
                    comp_label[i][5] = Text(self.frame, height=4, width=25, bg="#f0f0f0", font="Times 15")
                    comp_label[i][5].grid(row=i, column=5, sticky='news')
                    comp_label[i][5].insert("1.0", r[8])
                    comp_label[i][5].config(state=DISABLED)
                    comp_label[i][6] = Label(self.frame, width=15, font="Times 15", text=r[7])
                    comp_label[i][6].grid(row=i, column=6, sticky='news')

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
        self.adcomp_root.resizable(0,0)
        self.adcomp_root.mainloop()

    def refresh(self):
        self.adcomp_root.destroy()
        self.__init__()

    def on_adenter1(self, e):
        self.Exit['background'] = 'white'

    def on_adleave1(self, e):
        self.Exit['background'] = '#ff8566'

    def on_adenter2(self, e):
        self.take_action['background'] = 'white'

    def on_adleave2(self, e):
        self.take_action['background'] = '#ff8566'

    def on_adenter3(self, e):
        self.Refresh_button['background'] = 'white'

    def on_adleave3(self, e):
        self.Refresh_button['background'] = '#ff8566'

    def assign(self):
        self.action_root=Tk()
        self.action_root.geometry("370x200+400+200")
        self.action_root.title("Assigning")
        self.frame_head=Frame(self.action_root)
        self.frame_head.grid(row=0,column=0,sticky='news')
        self.main_label=Label(self.frame_head,text="* Fill the following fields to assign employee for Complaint",font="Times 10 bold",fg="#ff8566")
        self.main_label.grid(row=0,column=0,padx=20)

        self.frame_body=Frame(self.action_root)
        self.frame_body.grid(row=1,column=0,sticky='news')
        self.strvar=StringVar(self.frame_body)
        self.comp_aintid=Label(self.frame_body,text="Complaint Id",font="Helvetica 10 bold")
        self.comp_aintid.grid(row=0,column=0,sticky="nw",pady=10,padx=40)
        self.comp_aintide=Entry(self.frame_body,textvariable=self.strvar,width=23,font="Helvetica 10")
        self.comp_aintide.grid(row=0,column=1,sticky="nw",pady=10)

        categories = ["Select Complaint Category", "Academic (Lectures)", "Training & Placement cell", "Hostel","Transport", "Accounts", "library", "Canteen", "others"]
        self.category_l = Label(self.frame_body, text="Category", font="Helvetica 10 bold")
        self.category_l.grid(row=1, column=0,sticky="nw",pady=10,padx=40)
        self.category_e = ttk.Combobox(self.frame_body,values=categories, font="Helvetica 10")
        self.category_e.grid(row=1, column=1,sticky="nw",pady=10)
        self.category_e.current(0)

        employ=["Select Employee","Mr. Rupesh","Mr. Ajay","Mr. Vinesh","Mr. Prakash"]
        self.emp_label = Label(self.frame_body, text="Employee", font="Helvetica 10 bold")
        self.emp_label.grid(row=2, column=0,sticky="nw",pady=10,padx=40)
        self.emp = ttk.Combobox(self.frame_body, values=employ, font="Helvetica 10")
        self.emp.grid(row=2, column=1,sticky="nw",pady=10)
        self.emp.current(0)

        self.assign_button=Button(self.frame_body,font="Helvetica 15 bold",text="Assign",bg="#ff8566",relief="ridge",command=self.update)
        self.assign_button.grid(row=3,column=0,padx=40)
        self.assign_button.bind("<Enter>", self.on_adminenter3)
        self.assign_button.bind("<Leave>", self.on_adminleave3)

        self.cancel_button = Button(self.frame_body, font="Helvetica 15 bold", text="Cancel", bg="#ff8566",relief="ridge", command=self.action_root.destroy)
        self.cancel_button.grid(row=3, column=1, padx=70)
        self.cancel_button.bind("<Enter>", self.on_adminenter4)
        self.cancel_button.bind("<Leave>", self.on_adminleave4)

        self.action_root.resizable(0,0)
        self.action_root.mainloop()

    def on_adminenter3(self, e):
        self.assign_button['background'] = 'white'

    def on_adminleave3(self, e):
        self.assign_button['background'] = '#ff8566'

    def on_adminenter4(self, e):
        self.cancel_button['background'] = 'white'

    def on_adminleave4(self, e):
        self.cancel_button['background'] = '#ff8566'

    def update(self):
        comp=self.comp_aintide.get()
        cat_gory=self.category_e.get()
        emp1=self.emp.get()
        if(comp=="" or cat_gory=="Select Complaint Category"):
            messagebox.showinfo(title="Info",message="Please fill all the fields first")
        else:
            self.cur.execute("update complaintdb set empname='"+emp1+"' where complaintId='"+comp+"' and category='"+cat_gory+"'")
            self.db.commit()
            self.action_root.destroy()

#ob = complaint_sec()


