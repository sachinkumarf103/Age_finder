from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from datetime import *
from tkcalendar import *

class App(Tk):
    def __init__(self,):
        super().__init__()
        self.title("Calculate Age")
        self.geometry("700x500+400+125")
        self.resizable(0,0)

    def user_interface(self):
        self.lbl = Label(self, text="Calculate Age", font=('Arial', 35, BOLD),)
        self.lbl.pack()
        #frame 01
        self.frm1 = Frame(self,)
        self.frm1.pack(fill=BOTH)
        self.lbl1 = Label(self.frm1, text="Current Date :", font=('Arial', 25, BOLD))
        self.lbl1.pack(side=LEFT, pady=25, padx=5)

        #for date
        self.today = date.today()
        self.td = self.today.strftime("%d/%m/%Y")
        # self.curr_date = int(self.today.strftime("%d"))
        # self.curr_mont = int(self.today.strftime("%m"))
        # self.curr_yer = int(self.today.strftime("%Y"))
        ######
        

        # print(type(self.curr_date))
        
        self.lbl2 = Label(self.frm1,text = self.td, font=('Arial', 25, BOLD))
        self.lbl2.pack(side=RIGHT, pady=25, padx=5)

        #Frame 02
        self.frm2 = Frame(self,)
        self.frm2.pack(fill=BOTH)
        self.lbl3 = Label(self.frm2, text="Select DOB :", font=('Arial', 20, BOLD))
        self.lbl3.pack(side=LEFT, padx=50)

        def find(*arg):
            find.birth_date = self.sel.get()
            self.lbl5.config(text=find.birth_date)
             
        self.sel = StringVar()
        self.cal = DateEntry(self.frm2, selectmode = "day", font=('Arial', 15, BOLD), year=2000, month=1, day=1, date_pattern='dd/MM/yyyy', state="readonly", textvariable =self.sel)
        self.cal.pack(side=RIGHT, padx=10)
        
        
        #Frame 03
        self.frm3 = Frame(self, )
        self.frm3.pack(fill=BOTH)
        
        self.lbl4 = Label(self.frm3,text="Your DOB :", font=('Arial', 25, BOLD))
        self.lbl4.pack(side=LEFT,padx=40, pady=15)

        self.lbl5 = Label(self.frm3,text="DOB", font=('Arial', 25, BOLD))
        self.lbl5.pack(side=RIGHT,padx=10,)

        self.sel.trace('w',find)
        
        def date_cal():
            ################
            self.curr_time = datetime.now()
            self.curr_date = int(self.curr_time.strftime("%d"))
            self.curr_mont = int(self.curr_time.strftime("%m"))
            self.curr_yer = int(self.curr_time.strftime("%Y"))
            ###############
            find()
            d = find.birth_date
            y = d.split("/")
            b_date = int(y[0])
            b_mont = int(y[1])
            b_yer = int(y[2])
            # print(self.curr_yer)

            #Logic for calculation
            if b_date > self.curr_date:
                self.curr_date += 30
                self.curr_date -= b_date
                #for month
                self.curr_mont -= 1
                if b_mont > self.curr_mont:
                    self.curr_mont += 12
                    self.curr_mont -= b_mont
                    #for year
                    self.curr_yer -= 1
                    self.curr_yer -= b_yer
                elif b_mont < self.curr_mont:
                    self.curr_mont -= b_mont
                    self.curr_yer -= b_yer
                else:
                    self.curr_mont -= b_mont
                    self.curr_yer -= b_yer

            elif b_date < self.curr_date or b_date == self.curr_date:
                self.curr_date -= b_date
                if b_mont > self.curr_mont:
                    self.curr_mont += 12
                    self.curr_mont -= b_mont
                    self.curr_yer -= 1
                    self.curr_yer -= b_yer
                elif b_mont < self.curr_mont:
                    self.curr_mont -= b_mont
                    self.curr_yer -= b_yer
                else:
                    self.curr_mont -= b_mont
                    self.curr_yer -= b_yer

            if self.curr_date == 0 and self.curr_mont == 0:
                self.lbl6['text'] = self.curr_yer,"Years"
                #print(self.curr_yer,"Years")
            elif self.curr_date == 0:
                self.lbl6['text'] = self.curr_yer,"Years",self.curr_mont,"Months"
                #print(self.curr_yer,"Years",self.curr_mont,"Months")
            else:
                self.lbl6['text'] = self.curr_yer,"Years",self.curr_mont,"Months", self.curr_date,"Days"
                #print(self.curr_yer,"Years",self.curr_mont,"Months", self.curr_date,"Days")

            # print(self.curr_date)
            # print(self.curr_mont)
            # print(self.curr_yer)



        #Button
        self.btn = Button(self, text="Find",width=10, font=("Arial", 18), relief=GROOVE, command=date_cal)
        self.btn.pack()
        
        self.lbl6 = Label(self, text="Result", font= ('Ariel', 20, "bold"), fg="green")
        self.lbl6.pack(pady=40,)

        
if __name__ == '__main__':
    win = App()
    win.user_interface()
    win.mainloop()
