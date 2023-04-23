from tkinter import *
from tkinter import messagebox
import pymysql
import time

class EmployeeSytsem:
    def __init__(self,root):
        self.root = root
        self.root.title("Employee Payroll Management System | Developed by Oswin Lopes and Seon Tuscano")
        self.root.geometry("1350x680+0+0")
        self.root.config(bg="lightgray")
        main_title = Label(self.root,text="Employee Payroll Management System",font=("times new roman",25,"bold"),bg="darkblue",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)


        #================Frame1====================
        #================Variables=================
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hired_loc = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_experience = StringVar()
        self.var_proof_id = StringVar()     #===Adhaar Card======
        self.var_contact = StringVar()
        self.var_status = StringVar()


        Frame1 = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=720,height=580)
        title1 = Label(Frame1, text="Employee Details", font=("helvetica", 20), bg="darkblue",fg="white", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        #=======Row1======
        lbl_code = Label(Frame1,text="Employee Code",font=("helvetica",15),bg="alice blue",fg="black",relief=SUNKEN).place(x=10,y=60)
        txt_code = Entry(Frame1,font=("helvetica",15), textvariable=self.var_emp_code,bg="lightyellow",fg="black",relief=SUNKEN,width=20).place(x=180,y=60)
        btn_search = Button(Frame1,text=" Search \U0001F50D ",command=self.search,font=("helvetica",15),bg="lightgray",fg="black",relief=RAISED).place(x=450,y=60)

        # =======Row2======
        lbl_designation = Label(Frame1,text=" Designation ",font=("helvetica",15),bg="alice blue",fg="black",relief=SUNKEN).place(x=10,y=120)
        txt_designation = Entry(Frame1,font=("helvetica",15),textvariable=self.var_designation,bg="lightyellow",fg="black",relief=SUNKEN,width=20).place(x=160,y=120)
        lbl_DOJ = Label(Frame1, text=" D.O.J  ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=400,y=120)
        txt_DOJ = Entry(Frame1, font=("helvetica", 15),textvariable=self.var_doj, bg="lightyellow", fg="black", relief=SUNKEN, width=15).place(x=530,y=120)

        # =======Row3======
        lbl_name = Label(Frame1, text=" Name ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=10, y=170)
        txt_name = Entry(Frame1,font=("helvetica",15),textvariable=self.var_name,bg="lightyellow",fg="black",relief=SUNKEN,width=20).place(x=160,y=170)
        lbl_DOB = Label(Frame1, text=" D.O.B ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=400,y=170)
        txt_DOB = Entry(Frame1, font=("helvetica", 15),textvariable=self.var_dob, bg="lightyellow", fg="black", relief=SUNKEN, width=15).place(x=530,y=170)

        #=======Row4======
        lbl_age = Label(Frame1, text=" Age ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=10, y=220)
        txt_age = Entry(Frame1,font=("helvetica",15),textvariable=self.var_age,bg="lightyellow",fg="black",relief=SUNKEN,width=20).place(x=160,y=220)
        lbl_experience = Label(Frame1, text=" Experience ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=400,y=220)
        txt_experience = Entry(Frame1,textvariable=self.var_experience, font=("helvetica", 15), bg="lightyellow", fg="black", relief=SUNKEN, width=15).place(x=530,y=220)

        # =======Row5======
        lbl_gender = Label(Frame1, text=" Gender ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=10, y=270)
        txt_gender = Entry(Frame1,font=("helvetica",15),textvariable=self.var_gender,bg="lightyellow",fg="black",relief=SUNKEN,width=20).place(x=160,y=270)
        lbl_proofId = Label(Frame1, text=" Proof ID ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=400,y=270)
        txt_proofId = Entry(Frame1, font=("helvetica", 15),textvariable=self.var_proof_id, bg="lightyellow", fg="black", relief=SUNKEN, width=15).place(x=530,y=270)

        # =======Row6======
        lbl_email = Label(Frame1, text=" Email ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=10, y=330)
        txt_email = Entry(Frame1,font=("helvetica",15),textvariable=self.var_email,bg="lightyellow",fg="black",relief=SUNKEN,width=20).place(x=160,y=330)
        lbl_contact = Label(Frame1, text=" Contact No. ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=400,y=330)
        txt_contact = Entry(Frame1, font=("helvetica", 15),textvariable=self.var_contact, bg="lightyellow", fg="black", relief=SUNKEN, width=15).place(x=530,y=330)

        # =======Row7======
        lbl_hiredLoc = Label(Frame1, text=" Hired Location ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=10, y=400)
        txt_hiredLoc = Entry(Frame1,font=("helvetica",15),textvariable=self.var_hired_loc,bg="lightyellow",fg="black",relief=SUNKEN,width=20).place(x=160,y=400)
        lbl_status = Label(Frame1, text=" Status ", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=400, y=400)
        txt_status = Entry(Frame1, font=("helvetica", 15),textvariable=self.var_status, bg="lightyellow", fg="black", relief=SUNKEN,width=15).place(x=530, y=400)

        # =======Row8======
        lbl_address = Label(Frame1, text=" Address ", font=("helvetica", 15), bg="alice blue", fg="black",relief=SUNKEN).place(x=10, y=450)
        self.txt_address = Text(Frame1, font=("helvetica", 15),bg="lightyellow", fg="black", relief=SUNKEN, width=20)
        self.txt_address.place(x=160, y=450, width= 500, height=100)

        # ================Frame2====================
        # ================Variables=================
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_bas_sal = StringVar()
        self.var_t_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_PF = StringVar()
        self.var_convenience = StringVar()
        self.var_net_sal = StringVar()

        Frame2 = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Frame2.place(x=740, y=70, width=600, height=280)
        title1 = Label(Frame2, text="Employee Salary Details", font=("helvetica", 20), bg="darkblue", fg="white", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        # =======Row1======
        lbl_month = Label(Frame2, text=" Month ", font=("helvetica", 15), bg="alice blue", fg="black",relief=SUNKEN).place(x=20, y=50)
        txt_month = Entry(Frame2, font=("helvetica", 15),textvariable=self.var_month, bg="lightyellow", fg="black", relief=SUNKEN, width=5).place(x=100, y=50)
        lbl_year = Label(Frame2, text=" Year ", font=("helvetica", 15), bg="alice blue", fg="black",relief=SUNKEN).place(x=170, y=50)
        txt_year = Entry(Frame2, font=("helvetica", 15),textvariable=self.var_year, bg="lightyellow", fg="black", relief=SUNKEN, width=7).place(x=240, y=50)
        lbl_basicSal = Label(Frame2, text=" Basic Salary ", font=("helvetica", 15), bg="alice blue", fg="black",relief=SUNKEN).place(x=330, y=50)
        txt_basicSal = Entry(Frame2, font=("helvetica", 15),textvariable=self.var_bas_sal, bg="lightyellow", fg="black", relief=SUNKEN,width=10).place(x=470, y=50)

        # =======Row2======
        lbl_totalDays = Label(Frame2, text=" Total Days ", font=("helvetica", 15), bg="alice blue", fg="black",relief=SUNKEN).place(x=10, y=90)
        txt_totalDays = Entry(Frame2, font=("helvetica", 15),textvariable=self.var_t_days, bg="lightyellow", fg="black", relief=SUNKEN,width=10).place(x=140, y=90)
        lbl_absents = Label(Frame2, text=" Absents  ", font=("helvetica", 15), bg="alice blue", fg="black",relief=SUNKEN).place(x=320, y=90)
        txt_absents = Entry(Frame2, font=("helvetica", 15),textvariable=self.var_absent, bg="lightyellow", fg="black", relief=SUNKEN, width=12).place(x=430, y=90)

        # =======Row3======
        lbl_medical = Label(Frame2, text=" Medical ", font=("helvetica", 15), bg="alice blue", fg="black",relief=SUNKEN).place(x=10, y=130)
        txt_medical = Entry(Frame2, font=("helvetica", 15),textvariable=self.var_medical, bg="lightyellow", fg="black", relief=SUNKEN, width=10).place(x=140, y=130)
        lbl_provFund = Label(Frame2, text=" Provident Fund ", font=("helvetica", 15), bg="alice blue", fg="black",relief=SUNKEN).place(x=270, y=130)
        txt_provFund = Entry(Frame2, font=("helvetica", 15),textvariable=self.var_PF, bg="lightyellow", fg="black", relief=SUNKEN, width=12).place(x=430, y=130)

        # =======Row4======
        lbl_convenience = Label(Frame2, text=" Convenience", font=("helvetica", 15), bg="alice blue", fg="black", relief=SUNKEN).place(x=10, y=170)
        txt_convenience = Entry(Frame2, font=("helvetica", 15),textvariable=self.var_convenience, bg="lightyellow", fg="black", relief=SUNKEN, width=10).place(x=140, y=170)
        lbl_netSal = Label(Frame2, text=" Net Salary ", font=("helvetica", 15), bg="alice blue", fg="black",relief=SUNKEN).place(x=300, y=170)
        txt_netSal = Entry(Frame2, font=("helvetica", 15),textvariable=self.var_net_sal, bg="lightyellow", fg="black", relief=SUNKEN,width=12).place(x=430, y=170)

        #=======Row5======
        btn_Calculate = Button(Frame2, text="Calculate ", command=self.calculate, font=("helvetica", 14), bg="yellow", fg="black",relief=RAISED,height=1).place(x=200, y=230)
        btn_save = Button(Frame2, text="Save",command=self.add, font=("helvetica", 15), bg="green", fg="white",relief=RAISED,height=1).place(x=320, y=230)
        btn_clear = Button(Frame2, text="Clear",command=self.clear, font=("helvetica", 15), bg="lightgrey", fg="black",relief=RAISED,height=1).place(x=400, y=230)

        # ================Frame3====================
        Frame3 = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Frame3.place(x=740, y=360, width=600, height=290)

        #=============Calculator Frame=========

        Cal_frame = Frame(Frame3, bd=2, relief=RIDGE, bg="black")
        Cal_frame.place(x=12, y=12, width=262, height=255)

        self.var_txt = StringVar()
        self.var_operator = ''
        def btn_click(num):
            if num == 'clr':
                self.var_txt.set('')
                self.var_operator = ''
            elif num == 'del':
                oper_on_scr = self.var_txt.get()
                self.var_txt.set('')
                self.var_operator = oper_on_scr[:len(oper_on_scr)-1]
                self.var_txt.set(oper_on_scr[:len(oper_on_scr)-1])
            elif num == 'result':
                res = eval(self.var_operator)
                self.var_txt.set(res)
                self.var_operator = ''
            else :
                self.var_operator += str(num)
                self.var_txt.set(self.var_operator)

        txt_result = Entry(Cal_frame,font=("helvetica",15,"bold"),textvariable=self.var_txt,bg="light slate gray",fg="white",justify=RIGHT).place(x=2,y=2,w=252,h=40)

        #=======Row1=======
        btn_7 = Button(Cal_frame,text=" 7 ",font=("sans serif",15,"bold"),command=lambda : btn_click(7),bg="dim gray",fg="white",relief=RAISED).place(x=5,y=45,w=50,h=50)
        btn_8 = Button(Cal_frame, text=" 8 ", font=("sans serif", 15, "bold"),command=lambda : btn_click(8), bg="dim gray", fg="white",relief=RAISED).place(x=55, y=45,w=50,h=50)
        btn_9 = Button(Cal_frame, text=" 9 ", font=("sans serif", 15, "bold"),command=lambda : btn_click(9), bg="dim gray", fg="white",relief=RAISED).place(x=105, y=45,w=50,h=50)
        btn_div = Button(Cal_frame, text=" \u2797 ", font=("sans serif", 15, "bold"),command=lambda : btn_click('/'), bg="dim gray", fg="white",relief=RAISED).place(x=155, y=45,w=50,h=50)

        # =======Row2=======
        btn_4 = Button(Cal_frame, text=" 4 ", font=("sans serif", 15, "bold"),command=lambda : btn_click(4), bg="dim gray", fg="white",relief=RAISED).place(x=5, y=96, w=50, h=50)
        btn_5 = Button(Cal_frame, text=" 5 ", font=("sans serif", 15, "bold"),command=lambda : btn_click(5), bg="dim gray", fg="white",relief=RAISED).place(x=55, y=96, w=50, h=50)
        btn_6 = Button(Cal_frame, text=" 6 ", font=("sans serif", 15, "bold"),command=lambda : btn_click(6), bg="dim gray", fg="white",relief=RAISED).place(x=105, y=96, w=50, h=50)
        btn_mul = Button(Cal_frame, text=" \u2716 ", font=("sans serif", 15, "bold"),command=lambda : btn_click('*'), bg="dim gray", fg="white", relief=RAISED).place(x=155,y=96,w=50,h=50)

        # =======Row3=======
        btn_1 = Button(Cal_frame, text=" 1 ", font=("sans serif", 15, "bold"),command=lambda : btn_click(1), bg="dim gray", fg="white",relief=RAISED).place(x=5, y=147, w=50, h=50)
        btn_2 = Button(Cal_frame, text=" 2 ", font=("sans serif", 15, "bold"),command=lambda : btn_click(2), bg="dim gray", fg="white",relief=RAISED).place(x=55, y=147, w=50, h=50)
        btn_3 = Button(Cal_frame, text=" 3 ", font=("sans serif", 15, "bold"),command=lambda : btn_click(3), bg="dim gray", fg="white",relief=RAISED).place(x=105, y=147, w=50, h=50)
        btn_sub = Button(Cal_frame, text=" \u2796 ", font=("sans serif", 15, "bold"),command=lambda : btn_click('-'), bg="dim gray", fg="white",relief=RAISED).place(x=155, y=147, w=50, h=50)
        btn_del = Button(Cal_frame, text=" del ", font=("sans serif", 15, "bold"), command=lambda: btn_click('del'), bg="dim gray", fg="white", relief=RAISED).place(x=205, y=147, w=50, h=50)

        # =======Row4=======
        btn_0 = Button(Cal_frame, text=" 0 ", font=("sans serif", 15, "bold"),command=lambda : btn_click(0), bg="dim gray", fg="white",relief=RAISED,anchor="w").place(x=5, y=198, w=100, h=50)
        btn_equal = Button(Cal_frame, text=" = ", font=("sans serif", 15, "bold"),command=lambda : btn_click('result'), bg="dim gray", fg="white",relief=RAISED).place(x=105, y=198, w=50, h=50)
        btn_add = Button(Cal_frame, text=" \u2795 ", font=("sans serif", 15, "bold"),command=lambda : btn_click('+'), bg="dim gray", fg="white",relief=RAISED).place(x=155, y=198, w=50, h=50)
        btn_point = Button(Cal_frame, text=" . ", font=("sans serif", 15, "bold"), command=lambda: btn_click('.'),bg="dim gray", fg="white", relief=RAISED).place(x=205, y=198, w=50, h=50)

        btn_clr = Button(Cal_frame, text=" clr ", font=("sans serif", 15, "bold"), command=lambda: btn_click('clr'),bg="dim gray", fg="white", relief=RAISED).place(x=205, y=45, w=50, h=100)

        #=========SalaryFrame===========
        sal_Frame = Frame(Frame3, bd=2, relief=RIDGE, bg="white")
        sal_Frame.place(x=282, y=12, width=302, height=255)

        sal_title = Label(sal_Frame, text="Salary Reciept", font=("helvetica", 15), bg="lavenderblush3", fg="black", anchor="w",padx=10).place(x=0, y=0, relwidth=1)

        #=======SalaryFrame2=======
        sal_Frame2 = Frame(sal_Frame,bg='black',bd=2,relief=GROOVE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=190)
        self.sample = f'''         Company Name ,XYZ\n         Address: XYZ, ****
------------------------------------------------------
Employee ID\t\t:XYZ
Salary of\t\t: ****
Generated On\t\t: DD-MM-YYYY
------------------------------------------------------
Total Days\t\t: Days
Total Present \t\t: Presents
Total Absent\t\t: Absents
Convenience\t\t: Rs.----
Medical\t\t: Rs.----
PF\t\t: Rs.----
Gross Payment\t\t: Rs.----
Net Salary\t\t: Rs.----
------------------------------------------------------
This is a computer generated slip, not
required any signature
'''

        scroll_y = Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_reciept = Text(sal_Frame2,font=('sans serif',12),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.insert(END,self.sample)
        btn_print = Button(sal_Frame, text="Print", font=("sans serif", 15), bg="lightblue", fg="black",relief=RAISED).place(x=195, y=223,w=90,h=25)


    #===============All Functions=====================

    def search(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='ems')
            cur = con.cursor()
            cur.execute('select * from emp_salary where e_id=%s', (self.var_emp_code.get()))
            row = cur.fetchone()
            # print(rows)
            if row == None:
                messagebox.showerror("Error",'Invalid Employee ID, PLease try with another ID',
                                     parent=self.root)
            else:
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hired_loc.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_proof_id.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert(END,row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_bas_sal.set(row[16])
                self.var_t_days.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_PF.set(row[20])
                self.var_convenience.set(row[21])
                self.var_net_sal.set(row[22])
                file = open('Salary_Reciept/' + str(row[23]) , 'r')
                self.txt_salary_reciept.delete('1.0',END)
                for i in file:
                    self.txt_salary_reciept.insert(END,i)
                file.close()
        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')


    def clear(self):
        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hired_loc.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof_id.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,'')
        self.var_month.set('')
        self.var_year.set('')
        self.var_bas_sal.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_PF.set('')
        self.var_convenience.set('')
        self.var_net_sal.set('')
        self.txt_salary_reciept.delete('1.0',END)
        self.txt_salary_reciept.insert(END,self.sample)

    def add(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee deatails must be required")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur = con.cursor()
                cur.execute('select * from emp_salary where e_id=%s',(self.var_emp_code.get()))
                row = cur.fetchone()
                #print(rows)
                if row!=None:
                    messagebox.showerror("Error",'This employee ID is already available in our record,try again with another ID',parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                self.var_emp_code.get(),
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_hired_loc.get(),
                                self.var_doj.get(),
                                self.var_dob.get(),
                                self.var_experience.get(),
                                self.var_proof_id.get(),
                                self.var_contact.get(),
                                self.var_status.get(),
                                self.txt_address.get('1.0', END),
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_bas_sal.get(),
                                self.var_t_days.get(),
                                self.var_absent.get(),
                                self.var_medical.get(),
                                self.var_PF.get(),
                                self.var_convenience.get(),
                                self.var_net_sal.get(),
                                self.var_emp_code.get()+".txt"
                                )
                    )
                    con.commit()
                    con.close()
                    file=open('Salary_Reciept/'+str(self.var_emp_code.get())+'.txt','w')
                    file.write(self.txt_salary_reciept.get('1.0',END))
                    file.close()
                    messagebox.showinfo("Success","Record added successfully")
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to : {str(ex)}')


    def calculate(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_bas_sal.get()=='' or self.var_PF=='' or self.var_medical.get()=='' or self.var_absent.get()=='' or self.var_convenience.get()=='':
          messagebox.showerror('Error','All fields are required')
        else:
            per_day = int(self.var_bas_sal.get()) / int(self.var_t_days.get())
            work_day = int(self.var_t_days.get()) - int(self.var_absent.get())
            sal = per_day * work_day
            deduct = int(self.var_medical.get())+int(self.var_PF.get())
            addition = int(self.var_convenience.get())
            net_sal = sal-deduct+addition
            self.var_net_sal.set(str(round(net_sal, 2)))
            #===========Receipt===============
            new_sample=f'''        Company Name ,XYZ\n         Address: XYZ, Floor4
------------------------------------------------------
Employee ID\t\t:{self.var_emp_code.get()}
Salary of\t\t: {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t: {str(time.strftime('%d-%m-%Y'))}
------------------------------------------------------
Total Days\t\t: {self.var_t_days.get()}
Total Present \t\t: {str(int(self.var_t_days.get())-int(self.var_absent.get()))}
Total Absent\t\t: {self.var_absent.get()}
Convenience\t\t: Rs.{self.var_convenience.get()}
Medical\t\t: Rs.{self.var_medical.get()}
PF\t\t: Rs.{self.var_PF.get()}
Gross Payment\t\t: Rs.{self.var_bas_sal.get()}
Net Salary\t\t: Rs.{self.var_net_sal.get()}
------------------------------------------------------
This is a computer generated slip, not
required any signature
'''
            self.txt_salary_reciept.delete('1.0',END)
            self.txt_salary_reciept.insert(END,new_sample)


root = Tk()
obj = EmployeeSytsem(root)
root.mainloop() #puts the window in an infinite loop until the window is not closed