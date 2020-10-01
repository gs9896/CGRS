from tkinter import*
from PIL import ImageTk
from adminsection import*
class admin_l:
    def __init__(self):
        self.admin_root=Toplevel()
        self.admin_root.title("Admin Page")-
        self.admin_root.geometry("1200x600+100+50")
        self.canvas4=Canvas(self.admin_root,width=1200,height=600)
        self.canvas4.pack()
        imagepath1 = r'F:\Projects\python\cgrs\projimg2.jpg'
        image1 = ImageTk.PhotoImage(file = imagepath1)
        self.canvas4.create_image(0,0, image = image1,anchor="nw")
        self.canvas4.create_text(210,20,text="Panipat Institute Of Engineering & Technology - Admin",font="Times 25 bold ",anchor="nw")
        self.canvas4.create_line(0,80,1200,80,width=5)
        self.canvas4.create_text(140,140,font="calibri 15 bold",text="P.I.E.T college , the Grievance Redressal Cell attempts to address genuine problems and complaints of students\nwhatever be the nature of the problem.\n\nStudents are encouraged to use the suggestion boxes placed on different sections of the campus to express\nconstructive suggestions and grievances.\n\nThe Grievance Cell is also empowered to look into matters of harassment.",anchor="nw")
        self.canvas4.create_text(140,330,font="calibri 15 bold",fill="red",text="The Objective of the Grievance Cell",anchor="nw")
        self.canvas4.create_text(440,330,font="calibri 15 bold",text="is to develop a responsive and accountable attitude among all the",anchor="nw")
        self.canvas4.create_text(140,350,font="calibri 15 bold",text="stakeholders in order to maintain a harmonious educational atmosphere in the institute.",anchor="nw")
        self.canvas4.create_line(0,390,1200,390,width=5)
        self.view_button=Button(self.admin_root,text="View Complaints",width=30,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=complaint_sec)
        self.view_button.place(x=250,y=480)
        self.view_button.bind("<Enter>", self.on_adminenter1)
        self.view_button.bind("<Leave>", self.on_adminleave1)

        self.logout_button=Button(self.admin_root,text="Log Out",width=30,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.admin_root.destroy)
        self.logout_button.place(x=650,y=480)
        self.logout_button.bind("<Enter>", self.on_adminenter2)
        self.logout_button.bind("<Leave>", self.on_adminleave2)

        self.admin_root.resizable(0,0)
        self.admin_root.mainloop()

    def on_adminenter1(self, e):
        self.view_button['background'] = 'white'

    def on_adminleave1(self, e):
        self.view_button['background'] = '#ff8566'

    def on_adminenter2(self, e):
        self.logout_button['background'] = 'white'

    def on_adminleave2(self, e):
        self.logout_button['background'] = '#ff8566'
#ob=admin_l()

