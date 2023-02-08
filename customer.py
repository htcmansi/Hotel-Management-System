from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        
        # ==========variables==========
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        
        
        
        # ============title==========
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        
        # =========Logo=============
        
        img2=Image.open(r"C:\Users\HP LAPTOP\Desktop\Hotel management system\images\logohotel.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        
        #============labelFrame==========
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
        # =========labels and entrys=======
        #custRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        enrty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        enrty_ref.grid(row=0,column=1)
        
        #custname
        cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)
        
        #mothername
        lbl_mname=Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_mname.grid(row=2,column=0,sticky=W)
        
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)
        
        #gender combobox
        lbl_gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",13,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        #post code
        lbl_postcode=Label(labelframeleft,text="Postcode",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_postcode.grid(row=4,column=0,sticky=W)
        txtpost=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13,"bold"))
        txtpost.grid(row=4,column=1)
        
        #mobile number
        lbl_mobile=Label(labelframeleft,text="Mobile",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_mobile.grid(row=5,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=5,column=1)
        
        #email
        lbl_email=Label(labelframeleft,text="E-mail",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_email.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
        txtemail.grid(row=6,column=1)
        
        #nationality
        lblNationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        
        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",13,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","Britist")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)
        
        # id proof type combobox
        lbl_idproof=Label(labelframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_idproof.grid(row=8,column=0,sticky=W)
        
        combo_Idproof=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",13,"bold"),width=27,state="readonly")
        combo_Idproof["value"]=("AdharCard","PanCard","Passport")
        combo_Idproof.current(0)
        combo_Idproof.grid(row=8,column=1)
        
        #id number
        lbl_idnumber=Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_idnumber.grid(row=9,column=0,sticky=W)
        txtidnumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
        txtidnumber.grid(row=9,column=1)
        
        #address
        lbl_address=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_address.grid(row=10,column=0,sticky=W)
        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        txtaddress.grid(row=10,column=1)
        
        #===========buttons============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)
        
        btndelet=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelet.grid(row=0,column=2,padx=1)
        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)
        
        # =========table frame search==============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Veiw Details And Search System",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)
        
        lbl_searchBy=Label(table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_searchBy.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(table_frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btShowAll=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btShowAll.grid(row=0,column=4,padx=1)
        
        #=======show data table========
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")
        
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
     
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mansic156918@",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mansic156918@",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
                conn.close()
                
    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
                    
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mansic156918@",database="hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,idnumber=%s,Address=%s where Ref=%s",(self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get(),self.var_ref.get()))            
         
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)
            
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mansic156918@",database="hotel")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    
    def reset(self):
         #self.var_ref.set(""),
         self.var_cust_name.set(""),
         self.var_mother.set(""),
         #self.var_gender.set(""),
         self.var_post.set(""),
         self.var_mobile.set(""),
         self.var_email.set(""),
         #self.var_nationality.set(""),
         #self.var_id_proof.set(""),
         self.var_id_number.set(""),
         self.var_address.set("")
         
         x=random.randint(1000,9999)
         self.var_ref.set(str(x))
         
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mansic156918@",database="hotel")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()    
                    
   
        
                
if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()