from tkinter import *
import random
import datetime
from twilio.rest import Client

class Bill_App:
    def __init__(self,root):
        
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1400,height = 700)
        self.root.minsize(width = 1400,height = 700)
        self.root.title("Restaurant Billing System")
        
        #==Variables
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        self.bill =StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.bread = IntVar()
        self.egg = IntVar()
        self.tea = IntVar()
        self.dosa = IntVar()
        self.sandwich = IntVar()
        self.rice = IntVar()
        self.soup = IntVar()
        self.fruit_salad = IntVar()
        self.mashroomrice = IntVar()
        self.shawarma = IntVar()
        self.gatorade = IntVar()
        self.coke = IntVar()
        self.juice = IntVar()
        self.waffer = IntVar()
        self.biscuits = IntVar()
        self.total_food = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()


        #===================================
        bg_color = "skyblue"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Restaurant Billing System",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "Yellow",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #==================Item-1=====================#
        F2 = LabelFrame(self.root,text = 'Item-1',bd = 10,relief = GROOVE,bg = bg_color,fg = "Yellow",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bread")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.bread)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Egg")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.egg)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Tea")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.tea)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Dosa")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.dosa)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sandwich")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sandwich)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Item-2=====================#
        F2 = LabelFrame(self.root,text = 'Item-2',bd = 10,relief = GROOVE,bg = bg_color,fg = "Yellow",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 380)

        #===========Frame Content
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.rice)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Fruit Salad")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.fruit_salad)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Soup")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.soup)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Mashroom Rice")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.mashroomrice)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Shawarma")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.shawarma)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Item-3=====================#

        F2 = LabelFrame(self.root,text = 'Item-3',bd = 10,relief = GROOVE,bg = bg_color,fg = "Yellow",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 380)

        #===========Frame Content
        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Gatorade")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.gatorade)
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        coke_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        coke_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        coke_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.coke)
        coke_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "FreshJuice")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.juice)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Waffer")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.waffer)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.biscuits)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 358,height = 380)
        #===========
        bill_title = Label(F3,text = "Bill List",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "Yellow",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Item-1")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_food)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Item-2")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_grocery)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Item-3")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_other)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Restaurant Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_other)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

        exit_btn = Button(F4,text = "Send",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.send)
        exit_btn.grid(row = 1,column = 8,ipadx = 20, padx =30)

#Function to get total prices
    def total(self):
        #=================Total Food Prices
        self.total_food_prices = (
            (self.bread.get() * 10)+
            (self.egg.get() * 3)+
            (self.tea.get() * 8)+
            (self.dosa.get() * 26)+
            (self.sandwich.get() * 14)
        )
        self.total_food.set("Rs."+str(self.total_food_prices))
        self.tax_cos.set("Rs."+str(round(self.total_food_prices*0.05)))
        #====================Total Grocery Prices
        self.total_grocery_prices = (
            (self.mashroomrice.get()*100)+
            (self.fruit_salad.get() * 15)+
            (self.soup.get() * 10)+
            (self.rice.get() *30)+
            (self.shawarma.get() * 90)

        )
        self.total_grocery.set("Rs."+str(self.total_grocery_prices))
        self.tax_groc.set("Rs."+str(round(self.total_grocery_prices*0.05)))
        #======================Total Other Prices
        self.total_other_prices = (
            (self.gatorade.get() * 4)+
            (self.juice.get() * 2)+
            (self.coke.get() * 2)+
            (self.waffer.get() * 2)+
            (self.biscuits.get() * 2)
        )
        self.total_other.set("Rs."+str(self.total_other_prices))
        self.tax_other.set("Rs."+str(round(self.total_other_prices*0.05)))


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,f"\n   {str(datetime.datetime.now())}   \n")
        self.txt.insert(END,"       Your Food Details  \n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n=======================================")
        self.txt.insert(END,"\nProduct            Qty            Price")
        self.txt.insert(END,"\n=======================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.bread.get() != 0:
            self.txt.insert(END,f"\nBread             {self.bread.get()}           {self.bread.get() * 10}")
        if self.egg.get() != 0:
            self.txt.insert(END,f"\nEgg             {self.egg.get()}           {self.egg.get() * 3}")
        if self.tea.get() != 0:
            self.txt.insert(END,f"\nTea         {self.tea.get()}           {self.tea.get() * 8}")
        if self.dosa.get() != 0:
            self.txt.insert(END,f"\nDosa           {self.dosa.get()}           {self.dosa.get() * 26}")
        if self.sandwich.get() != 0 :
            self.txt.insert(END,f"\nSandwich           {self.sandwich.get()}           {self.sandwich.get() * 14}")
        if self.mashroomrice.get() != 0:
            self.txt.insert(END,f"\nMashroomRice           {self.mashroomrice.get()}           {self.mashroomrice.get() * 100}")
        if self.fruit_salad.get() != 0:
            self.txt.insert(END,f"\nFruit Salad          {self.fruit_salad.get()}           {self.fruit_salad.get() * 15}")
        if self.soup.get() != 0:
            self.txt.insert(END,f"\nSalt              {self.soup.get()}           {self.soup.get() * 10}")
        if self.rice.get() != 0:
            self.txt.insert(END,f"\nRice              {self.rice.get()}           {self.rice.get() * 30}")
        if self.shawarma.get() != 0:
            self.txt.insert(END,f"\nShawarma             {self.shawarma.get()}           {self.shawarma.get() * 90}")
        if self.gatorade.get() != 0:
            self.txt.insert(END,f"\nGatorade          {self.gatorade.get()}           {self.gatorade.get() * 4}")
        if self.juice.get() != 0:
            self.txt.insert(END,f"\nFreshJuice             {self.juice.get()}           {self.juice.get() * 2}")
        if self.coke.get() != 0:
            self.txt.insert(END,f"\nCoke              {self.coke.get()}           {self.coke.get() * 2}")
        if self.waffer.get() != 0:
            self.txt.insert(END,f"\nWaffer            {self.waffer.get()}           {self.waffer.get() * 2}")
        if self.biscuits.get() != 0:
            self.txt.insert(END,f"\nBiscuits          {self.biscuits.get()}           {self.biscuits.get() * 2}")
        self.txt.insert(END,"\n======================================")
        self.txt.insert(END,f"\n                      Total : Rs.{self.total_food_prices+self.total_grocery_prices+self.total_other_prices+self.total_food_prices * 0.05+self.total_grocery_prices * 0.05+self.total_other_prices * 0.05}")


    def exit(self):
        self.root.destroy()
    def send(self):
        
        account_sid = "AC3148e4f4dd7d0e2ba842bd94a5d1c9d5"
        auth_token = "3ddb89bd0803c4d2e6d66daf17e47916"
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                 body='We are from India',
         from_='+19205474999',
         to=self.c_phone.get(), 
             )

        print(message.sid)

        
root = Tk()
object = Bill_App(root)
root.mainloop()


