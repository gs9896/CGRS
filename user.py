from tkinter import*
from PIL import ImageTk
from usercomplaint import *
class user_l:
    def __init__(self,recd):
        self.userroot=Toplevel()
        self.userroot.title(recd[1]+"'s Complaint Window")

        self.userroot.geometry("1200x600+100+50")
        self.canvas2=Canvas(self.userroot,width=1200,height=600)
        self.canvas2.pack()
        imagepath1 = r'F:\Projects\python\cgrs\projimg2.jpg'
        image1 = ImageTk.PhotoImage(file = imagepath1)
        self.canvas2.create_image(0,0, image = image1,anchor="nw")
        self.canvas2.create_text(80,50,font="Times 20 bold underline",text="Categories Of Grievance",anchor="nw")
        self.canvas2.create_text(80,100,font="Times 15 bold ",text="\n\n* Acadameic(Lectures)\n\n* Training & Placement Cell\n\n* Hostel\n\n* Transport\n\n* Accounts\n\n* Library\n\n* Canteen\n\n* Others",anchor="nw")
        
        self.canvas2.create_text(660,50,font="Times 20 bold underline",text=str(recd[0])+"'s   Profile",anchor="nw")
        self.canvas2.create_text(650,70,font="Times 15 bold",text="\n\nName                     :   "+recd[1]+"\n\nDepartment           :   "+recd[3]+"\n\nEmail                      :   "+recd[4],anchor="nw")
        self.comp_button=Button(self.userroot,text="Make Complaint",width=30,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=lambda :complaint(recd))
        self.canvas2.create_window(450,300,window=self.comp_button,anchor="nw")
        self.comp_button.bind("<Enter>", self.on_userenter1)
        self.comp_button.bind("<Leave>", self.on_userleave1)

        self.status_button=Button(self.userroot,text="Status Of Complaint",width=30,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=lambda :complaintstatus(recd))
        self.canvas2.create_window(800,300,window=self.status_button,anchor="nw")
        self.status_button.bind("<Enter>", self.on_userenter2)
        self.status_button.bind("<Leave>", self.on_userleave2)

        self.log_out=Button(self.userroot,text="LogOut",width=30,font="Calibri 15 bold",bg="#ff8566",relief='ridge',command=self.userroot.destroy)
        self.canvas2.create_window(650,400,window=self.log_out,anchor="nw")
        self.log_out.bind("<Enter>", self.on_userenter3)
        self.log_out.bind("<Leave>", self.on_userleave3)

        self.canvas2.create_line(400,0,400,600,width=5)
        self.userroot.resizable(0,0)
        self.userroot.mainloop()

    def on_userenter1(self, e):
        self.comp_button['background'] = 'white'

    def on_userleave1(self, e):
        self.comp_button['background'] = '#ff8566'

    def on_userenter2(self, e):
        self.status_button['background'] = 'white'

    def on_userleave2(self, e):
        self.status_button['background'] = '#ff8566'

    def on_userenter3(self, e):
        self.log_out['background'] = 'white'

    def on_userleave3(self, e):
        self.log_out['background'] = '#ff8566'

