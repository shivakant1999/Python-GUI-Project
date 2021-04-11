from random import randint
from tkinter import*
from tkinter import font
from typing import Collection
from tkinter import messagebox
import math, random, os
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#82E0AA"
        G_font = ("times new roman", 16, "bold")
        title = Label(self.root, text="Billing Software", bd=8, relief=RIDGE, bg=bg_color , fg="#1A5276", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

# ========================= Variables ======================================================== #
        # ====== cosmetics variables =================#
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash  = IntVar()
        self.hair_spray = IntVar()
        self.hair_gel = IntVar()
        self.lotion = IntVar()
        self.perfume = IntVar()

        # ====== grocery variables =================#
        self.sugar = IntVar()
        self.rice = IntVar()
        self.flour  = IntVar()
        self.tea = IntVar()
        self.pulses = IntVar()
        self.spices = IntVar()
        self.butter = IntVar()

        # ====== cold drinks variables =================#
        self.maza = IntVar()
        self.fruiti = IntVar()
        self.appy  = IntVar()
        self.thumps = IntVar()
        self.coca = IntVar()
        self.lemon = IntVar()
        self.marinda = IntVar()

        # ====== Total product price and tax variables =================#
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

 # ====== Customer detail variables =================#
        self.c_name = StringVar()
        self.c_phn = StringVar()
        self.bill_no = StringVar()
        x = randint(10000, 99999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


# ========================== CUSTOMER DETAILS SECTIONS STARTS ================================= #
        f1 = LabelFrame(self.root, bd=8, relief=GROOVE, text="Customer Details", font=("times new roman", 14, "bold"), fg="#C70039", bg=bg_color)
        f1.place(x=0, y=66, relwidth=1)

        cname_label = Label(f1, text="Customer Name",bg=bg_color, fg="#4A235A" , font=G_font).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(f1, width=15, textvariable=self.c_name,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)
        cphn_label = Label(f1, text="Phone No.",bg=bg_color, fg="#4A235A" , font=G_font).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(f1, width=15,textvariable=self.c_phn,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_label = Label(f1, text="Bill Number",bg=bg_color, fg="#4A235A" , font=G_font).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(f1, width=15,textvariable=self.search_bill,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(f1, text="Search", command=self.find_bill, font="arial 12 bold").grid(row=0, column=6, pady=10, padx= 20)

# ========================= COSMETICS FRAME ================================================= #

        f2 = LabelFrame(self.root, bd=8, relief=GROOVE, text="Cosmetics", font=("times new roman", 14, "bold"), fg="#C70039", bg=bg_color)
        f2.place(x=5, y=152, width=280, height=420)

        bath_lbl = Label(f2, text="Bath Soap", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(f2, width=10,textvariable=self.soap, font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lbl = Label(f2, text="Face Cream", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(f2, width=10, textvariable=self.face_cream, font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        face_w_lbl = Label(f2, text="Face Wash", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(f2, width=10,textvariable=self.face_wash, font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        hair_s_lbl = Label(f2, text="Hair Spray", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(f2, width=10,textvariable=self.hair_spray, font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        hair_g_lbl = Label(f2, text="Hair Gel", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(f2, width=10, textvariable=self.hair_gel ,font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        body_lbl = Label(f2, text="Body Lotion", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(f2, width=10, textvariable=self.lotion ,font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        perf_lbl = Label(f2, text="Perfume", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        perf_txt = Entry(f2, width=10, textvariable=self.perfume , font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

# ========================= GROCERY FRAME ================================================= #

        f3 = LabelFrame(self.root, bd=8, relief=GROOVE, text="Grocery", font=("times new roman", 14, "bold"), fg="#C70039", bg=bg_color)
        f3.place(x=300, y=152, width=280, height=420)

        p1_lbl = Label(f3, text="Sugar", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        p1_txt = Entry(f3, width=10, textvariable=self.sugar ,font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        p2_lbl = Label(f3, text="Rice", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        p2_txt = Entry(f3, width=10, textvariable=self.rice ,font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        p3_lbl = Label(f3, text="Flour", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        p3_txt = Entry(f3, width=10,textvariable=self.flour, font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        p4_lbl = Label(f3, text="Tea", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        p4_txt = Entry(f3, width=10,textvariable=self.tea, font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        p5_lbl = Label(f3, text="Pulses", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        p5_txt = Entry(f3, width=10, textvariable=self.pulses , font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        p6_lbl = Label(f3, text="Spices", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        p6_txt = Entry(f3, width=10, textvariable=self.spices ,font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        p7_lbl = Label(f3, text="Butter", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        p7_txt = Entry(f3, width=10, textvariable=self.butter ,font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

# ========================= Cold Drinks FRAME ================================================= #

        f4 = LabelFrame(self.root, bd=8, relief=GROOVE, text="Cold Drinks", font=("times new roman", 14, "bold"), fg="#C70039", bg=bg_color)
        f4.place(x=595, y=152, width=280, height=420)

        g1_lbl = Label(f4, text="Maazaa", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(f4, width=10,textvariable=self.maza, font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_cream_lbl = Label(f4, text="Fruiti", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_cream_txt = Entry(f4, width=10, textvariable=self.fruiti ,font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(f4, text="Appy Fiz", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(f4, width=10, textvariable=self.appy ,font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(f4, text="Thumps Up", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(f4, width=10, textvariable=self.thumps ,font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(f4, text="Coca Cola", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(f4, width=10, textvariable=self.coca , font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(f4, text="Lemonade", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(f4, width=10, textvariable=self.lemon, font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        g7_lbl = Label(f4, text="Marinda", font=("times new roman", 14, "bold"), bg=bg_color,fg="#17202A").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        g7_txt = Entry(f4, width=10, textvariable=self.marinda , font=("times new roman", 14, "bold"), bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

# ========================= Bill Area FRAME ================================================= #

        f5 = Frame(self.root, bd=8, relief=GROOVE)
        f5.place(x=890, y=152, width=455, height=420)

        bill_title = Label(f5, text="Bill Area", fg="#1A5276", font="arial 18 bold", bd=8, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(f5, orient=VERTICAL)
        self.textarea = Text(f5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill="both", expand=1)

# ======================= Button frame ======================================================= #

        f6 = LabelFrame(self.root, bd=8, relief=GROOVE, text="Bill Menu", font=("times new roman", 14, "bold"), fg="#C70039", bg=bg_color)
        f6.place(x=0, y=567, relwidth=1, height=136)

        m1_lbl = Label(f6, text="Total Cosmetics Price", font=("times new roman", 13, "bold"), bg=bg_color,fg="Red").grid(row=0, column=0, padx=8, pady=1, sticky="w")
        m1_txt = Entry(f6, width=10, textvariable=self.cosmetic_price, font=("times new roman", 13, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=8, pady=1)

        m2_lbl = Label(f6, text="Total Grocery Price", font=("times new roman", 13, "bold"), bg=bg_color,fg="Red").grid(row=1, column=0, padx=8, pady=1, sticky="w")
        m2_txt = Entry(f6, width=10, textvariable=self.grocery_price , font=("times new roman", 13, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=8, pady=1)

        m3_lbl = Label(f6, text="Total Cold Drinks Price", font=("times new roman", 13, "bold"), bg=bg_color,fg="Red").grid(row=2, column=0, padx=8, pady=1, sticky="w")
        m3_txt = Entry(f6, width=10, textvariable=self.cold_drink_price, font=("times new roman", 13, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=8, pady=1)

        n1_lbl = Label(f6, text="Tax on Cosmetics", font=("times new roman", 13, "bold"), bg=bg_color,fg="Red").grid(row=0, column=3, padx=8, pady=1, sticky="w")
        n1_txt = Entry(f6, width=10, textvariable=self.cosmetic_tax , font=("times new roman", 13, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=4, padx=8, pady=1)

        n2_lbl = Label(f6, text="Tax on Grocery", font=("times new roman", 13, "bold"), bg=bg_color,fg="Red").grid(row=1, column=3, padx=8, pady=1, sticky="w")
        n2_txt = Entry(f6, width=10, textvariable=self.grocery_tax , font=("times new roman", 13, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=4, padx=8, pady=1)

        n3_lbl = Label(f6, text="Tax on Cold Drinks", font=("times new roman", 13, "bold"), bg=bg_color,fg="Red").grid(row=2, column=3, padx=8, pady=1, sticky="w")
        n3_txt = Entry(f6, width=10, textvariable=self.cold_drink_tax , font=("times new roman", 13, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=4, padx=8, pady=1)

        btn_f = Frame(f6, bd=7, relief=GROOVE)
        btn_f.place(x=610, width=720, height=100)

        total_btn = Button(btn_f, command=self.total, text="Total", font=("times new roman", 15, "bold") , bg="cadetblue", fg="yellow", pady=17, width=12, bd=5).grid(row=0,column=0, padx=8, pady=3)
        gbill_btn = Button(btn_f, text="Generate Bill", command=self.bill_area , font=("times new roman", 15, "bold") , bg="cadetblue", fg="yellow", pady=17, width=12, bd=5).grid(row=0,column=1, padx=8, pady=3)
        clear_btn = Button(btn_f, text="Clear", command=self.clear_data , font=("times new roman", 15, "bold") , bg="cadetblue", fg="yellow", pady=17, width=12, bd=5).grid(row=0,column=2, padx=8, pady=3)
        exit_btn = Button(btn_f, text="EXIT", command=self.Exit_app , font=("times new roman", 15, "bold") , bg="cadetblue", fg="yellow", pady=17, width=12, bd=5).grid(row=0,column=3, padx=8, pady=3)
        self.welcome_bill()

# ============================= Calculation ============================= #
    def total(self):
        """
        calculates the price and tax of all cosemtic items 
        """
        self.bs_price = round((self.soap.get()*35),2)
        self.fc_price = round((self.face_cream.get()*60.6),2)
        self.fw_price = round((self.face_wash.get()*55),2)
        self.hs_price = round((self.hair_spray.get()*95),2)
        self.hg_price = round((self.hair_gel.get()*78),2)
        self.l_price = round((self.lotion.get()*120),2)
        self.perfume_price = round((self.perfume.get()*195),2)
        self.total_cosmetic_price=float(
                                        self.bs_price+
                                        self.fc_price+
                                        self.fw_price+
                                        self.hs_price+
                                        self.hg_price+
                                        self.l_price+
                                        self.perfume_price
                                    )

        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.cos_tax = round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.cos_tax))


        """
        calculates the price and tax of all grocery items 
        """

        self.s_price = round((self.sugar.get()*42),2)
        self.r_price = round((self.rice.get()*67),2)
        self.f_price = round((self.flour.get()*35.8),2)
        self.t_price = round((self.tea.get()*65),2)
        self.p_price = round((self.pulses.get()*80),2)
        self.sp_price = round((self.spices.get()*120),2)
        self.b_price = round((self.butter.get()*30),2)

        self.total_grocery_price=float(
                                        self.s_price+
                                        self.r_price+
                                        self.f_price+
                                        self.t_price+
                                        self.p_price+
                                        self.sp_price+
                                        self.b_price
                                    )

        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        """
        calculates the price and tax of all cold drink items 
        """

        self.cd_mz_price = round((self.maza.get()*25),2)
        self.cd_ma_price = round((self.marinda.get()*22),2)
        self.cd_l_price = round((self.lemon.get()*30),2)
        self.cd_c_price = round((self.coca.get()*35),2)
        self.cd_f_price = round((self.fruiti.get()*70),2)
        self.cd_ap_price = round((self.appy.get()*35),2)
        self.cd_t_price = round((self.thumps.get()*20),2)

        self.total_cold_price=float(
                                        self.cd_ap_price+
                                        self.cd_c_price+
                                        self.cd_ma_price+
                                        self.cd_mz_price+
                                        self.cd_l_price+
                                        self.cd_f_price+
                                        self.cd_t_price
                                    )

        self.cold_drink_price.set("Rs. "+str(self.total_cold_price))
        self.cd_tax = round((self.total_cold_price*0.18),2)
        self.cold_drink_tax.set("Rs. "+ str(self.cd_tax))

        # ================= Total Bill ================= #
        self.total_bill = float(
                                self.total_cosmetic_price + 
                                self.total_grocery_price + 
                                self.total_cold_price + 
                                self.cos_tax + 
                                self.g_tax + 
                                self.cd_tax
                                )
        self.grand_total = round((self.total_bill),2)

    def welcome_bill(self):
        """
        docstring
        """
        self.textarea.delete("1.0", END)
        self.textarea.insert(END, "\tWelcome to Shiva's Super Market")
        self.textarea.insert(END, "\n----------------------------------------------------")
        self.textarea.insert(END, "\n")
        self.textarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phn.get()}")
        self.textarea.insert(END, "\n")
        self.textarea.insert(END, "\n====================================================")
        self.textarea.insert(END, "\nProduct\t\tQTY\t\t\tPrice")
        self.textarea.insert(END, "\n====================================================")
        

    def bill_area(self):
        """
        This function displays all the information in the bill area
        """

        if self.c_name.get() == "" or self.c_phn.get() == "":
                messagebox.showerror("Error", "All Customer Detail Fields are neccessary !")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
                messagebox.showerror("Error", "No Product Selected, Please Select atleast 1 product.")
        else:
                self.welcome_bill()

                #========== Displaying Cosmetic Items =============== #
                if self.soap.get()!=0:
                        self.textarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t\t{self.bs_price}")
                if self.face_cream.get()!=0:
                        self.textarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t\t{self.fc_price}")
                if self.face_wash.get()!=0:
                        self.textarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t\t{self.fw_price}")
                if self.hair_gel.get()!=0:
                        self.textarea.insert(END, f"\n Hair Gel\t\t{self.hair_gel.get()}\t\t\t{self.hg_price}")
                if self.hair_spray.get()!=0:
                        self.textarea.insert(END, f"\n Hair Spray\t\t{self.hair_spray.get()}\t\t\t{self.hs_price}")
                if self.perfume.get()!=0:
                        self.textarea.insert(END, f"\n Perfume\t\t{self.perfume.get()}\t\t\t{self.perfume_price}")
                if self.lotion.get()!=0:
                        self.textarea.insert(END, f"\n Body Lotion\t\t{self.lotion.get()}\t\t\t{self.l_price}")
                
                #========== Displaying Grocery Items =============== #
                if self.sugar.get()!=0:
                        self.textarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t\t{self.s_price}")
                if self.rice.get()!=0:
                        self.textarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t\t{self.r_price}")
                if self.flour.get()!=0:
                        self.textarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t\t{self.f_price}")
                if self.tea.get()!=0:
                        self.textarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t\t{self.t_price}")
                if self.pulses.get()!=0:
                        self.textarea.insert(END, f"\n Pulses\t\t{self.pulses.get()}\t\t\t{self.p_price}")
                if self.spices.get()!=0:
                        self.textarea.insert(END, f"\n Spice\t\t{self.spices.get()}\t\t\t{self.sp_price}")
                if self.butter.get()!=0:
                        self.textarea.insert(END, f"\n Butter\t\t{self.butter.get()}\t\t\t{self.b_price}")

                #========== Displaying Cold Drinks Items =============== #
                if self.maza.get()!=0:
                        self.textarea.insert(END, f"\n Maazaa\t\t{self.maza.get()}\t\t\t{self.cd_mz_price}")
                if self.fruiti.get()!=0:
                        self.textarea.insert(END, f"\n Fruiti\t\t{self.fruiti.get()}\t\t\t{self.cd_f_price}")
                if self.appy.get()!=0:
                        self.textarea.insert(END, f"\n Appy Fiz\t\t{self.appy.get()}\t\t\t{self.cd_ap_price}")
                if self.thumps.get()!=0:
                        self.textarea.insert(END, f"\n Thumps Up\t\t{self.thumps.get()}\t\t\t{self.cd_t_price}")
                if self.coca.get()!=0:
                        self.textarea.insert(END, f"\n Coca Cola\t\t{self.coca.get()}\t\t\t{self.cd_c_price}")
                if self.lemon.get()!=0:
                        self.textarea.insert(END, f"\n Lemonade\t\t{self.lemon.get()}\t\t\t{self.cd_l_price}")
                if self.marinda.get()!=0:
                        self.textarea.insert(END, f"\n Marinda\t\t{self.marinda.get()}\t\t\t{self.cd_ma_price}")
                
                self.textarea.insert(END, "\n")
                self.textarea.insert(END, "\n****************************************************")
                if self.cosmetic_tax.get()!="Rs. 0.0":
                        self.textarea.insert(END, f"\n Cosmetics Tax : \t\t\t\t{self.cosmetic_tax.get()}")
                if self.grocery_tax.get()!="Rs. 0.0":
                        self.textarea.insert(END, f"\n Grocery Tax : \t\t\t\t{self.grocery_tax.get()}")
                if self.cold_drink_tax.get()!="Rs. 0.0":
                        self.textarea.insert(END, f"\n Cold Drink Tax : \t\t\t\t{self.cold_drink_tax.get()}")
                self.textarea.insert(END, "\n")
                self.textarea.insert(END, "\n----------------------------------------------------")
                self.textarea.insert(END, "\n")
                self.textarea.insert(END, f"\n Total Bill Amount : \t\t\t\t Rs. {self.grand_total}")
                self.textarea.insert(END, "\n")
                self.textarea.insert(END, "\n****************************************************")
                self.save_bill()
                
    def save_bill(self):
        mess = messagebox.askyesno("Save Bill", "Do you want to save bill ?")
        if mess > 0:
            self.bill_data = self.textarea.get("1.0", END)
            file1 = open('Bills/'+str(self.bill_no.get())+".txt", "w")
            file1.write(self.bill_data)
            file1.close()
            messagebox.showinfo("Saved", f"Bill No : {self.bill_no.get()} saved successfully")
        else:
           return

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split(".")[0] == self.search_bill.get():
                file2 = open(f"Bills/{i}", "r")
                self.textarea.delete("1.0", END)
                for d in file2:
                    self.textarea.insert(END, d)
                file2.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill Number !")
    
    def clear_data(self):
        """
        This function clears the data of all variables.
        """
        mess = messagebox.askyesno("Clear Bill", "Do you Really Want to Clear the Bill data ?")
        
        if mess > 0:
            # ====== cosmetics variables =================#
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.hair_gel.set(0)
            self.lotion.set(0)
            self.perfume.set(0)

            # ====== grocery variables =================#
            self.sugar.set(0)
            self.rice.set(0)
            self.flour.set(0)
            self.tea.set(0)
            self.pulses.set(0)
            self.spices.set(0)
            self.butter.set(0)

            # ====== cold drinks variables =================#
            self.maza.set(0)
            self.fruiti.set(0)
            self.appy.set(0)
            self.thumps.set(0)
            self.coca.set(0)
            self.lemon.set(0)
            self.marinda.set(0)

            # ====== Total product price and tax variables =================#
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

    # ====== Customer detail variables =================#
            self.c_name.set("")
            self.c_phn.set("")
            self.bill_no.set("")
            x = randint(10000, 99999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    
    def Exit_app(self):
        """
        This function will destroy Bill App and close the application
        """
        mess = messagebox.askyesno("Exit", "Do You Really Want to Exit ?")
        if mess > 0:
            self.root.destroy()
        

                
root = Tk()
obj = Bill_App(root)
root.mainloop()