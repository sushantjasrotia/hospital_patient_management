from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Database System")
        self.root.geometry("1540x800+0+0")

        #================================variables===================================================

        # =================variables to fetch the data form text field=================

        self.hospital_card = StringVar()
        self.hospital_id = StringVar()
        self.patient_name = StringVar()
        self.age = StringVar()
        self.gardians_name = StringVar()
        self.address = StringVar()
        self.phone_no = StringVar()
        self.pincode = StringVar()
        self.id_card = StringVar()
        self.patient_id_no = StringVar()
        self.state = StringVar()
        self.city = StringVar()
        self.patient_info = StringVar()
        self.dept_name = StringVar()
        self.patient_care = StringVar()
        self.building = StringVar()

        #================================title========================================================

        lbl_title = Label(self.root, bd=20, relief=RIDGE, text="  PUBLIC HOSPITAL MANAGEMENT SYSTEM ", fg="pink",bg="pink",
                          font=("times new roman", 50, "bold"),background="#43210a")
        lbl_title.pack(side=TOP, fill=X)

        # ===================Patient_data_entry=========================
        Data_frame = Frame(self.root, bd=20, relief=RIDGE,background="grey",bg="black")
        Data_frame.place(x=0, y=130, width=1530, height=400)

        Data_frame_left = LabelFrame(Data_frame, bd=10, padx=20, relief=RIDGE,
                                     font=("arial", 12, "bold"), text="Patient Information")
        Data_frame_left.place(x=0, y=5, width=980, height=350)

        #======================Infomation_compilation=======================

        Data_frame_right = LabelFrame(Data_frame, bd=10, padx=20, relief=RIDGE,
                                      font=("arial", 12, "bold"), text="Information Compilation")
        Data_frame_right.place(x=990, y=5, width=460, height=350)

        #========================================== button - frame ==========================

        Button_frame = Frame(self.root, bd=20, relief=RIDGE,background="black")
        Button_frame.place(x=0, y=530, width=1530, height=70)

        # ====================== Details-db-Frame ============================

        Details_frame = Frame(self.root, bd=20,bg="grey",highlightcolor='red', relief=RIDGE, background="black")
        Details_frame.place(x=0, y=600, width=1530, height=190)

        ###=========================Patient-info-table===============================================
        # ====================Date_frame_left===============================
        #---------------------------------------------------------------------------------------------------------------

        lbl_hospital_card = Label(Data_frame_left, text="Hospital_Card", font=("times new roman", 12, "bold"), padx=2,
                                pady=6)
        lbl_hospital_card.grid(row=0, column=2, sticky=W)

        Com_card_type = ttk.Combobox(Data_frame_left, textvariable=self.hospital_card,state="readonly",
                                       font=("arial", 12, "bold"), width=33)
        Com_card_type['value'] = ("New","Renew")
        Com_card_type.current(0)
        Com_card_type.grid(row=0, column=3)

        #---------------------------------------------------------------------------------------------------------------

        lbl_name_tablet = Label(Data_frame_left, text="ID_CARD:", font=("times new roman", 12, "bold"), padx=2,
                                pady=6)
        lbl_name_tablet.grid(row=4, column=0, sticky=W)

        Com_ID_card = ttk.Combobox(Data_frame_left,textvariable=self.id_card, state="readonly",
                                       font=("arial", 12, "bold"), width=33)
        Com_ID_card['value'] = ("Aadhar Card", "Pan Card", "License", "Voter Card", "Electricity Consumer ID")
        Com_ID_card.current(0)
        Com_ID_card.grid(row=4, column=1)

        #---------------------------------------------------------------------------------------------------------------

        lbl_dept = Label(Data_frame_left, text="Dept_Name:", font=("times new roman", 12, "bold"), padx=2,
                                pady=6)
        lbl_dept.grid(row=6, column=2, sticky=W)

        Com_dept_name = ttk.Combobox(Data_frame_left, textvariable=self.dept_name, state="readonly",
                                       font=("arial", 12, "bold"), width=33)
        Com_dept_name['value'] = ("Cardiology", "Accident and emergency (A&E)", "Burn Center (Burn Unit or Burns Unit)",
                                  "Elderly Services", "Gynecology", "Infection Control","Maternity","Neonatal","Nutrition and Dietetics",
                                  "Urology","ENT")
        Com_dept_name.current(0)
        Com_dept_name.grid(row=6, column=3)

        #---------------------------------------------------------------------------------------------------------------

        lbl_building = Label(Data_frame_left, text="Building:", font=("times new roman", 12, "bold"), padx=2,
                                pady=9)
        lbl_building.grid(row=7, column=2, sticky=W)

        Com_floor_building = ttk.Combobox(Data_frame_left,textvariable= self.building,  state="readonly",
                                       font=("arial", 12, "bold"), width=33)
        Com_floor_building['value'] = ("GF	", "F-1	", "F-2", "F-3","F-4","F-5","F-6")
        Com_floor_building.current(0)
        Com_floor_building.grid(row=7, column=3)

        #---------------------------------------------------------------------------------------------------------------

        lbl_patient_care = Label(Data_frame_left, text="Patient_Care:", font=("times new roman", 12, "bold"), padx=2,
                                pady=6)
        lbl_patient_care.grid(row=7, column=0, sticky=W)

        Com_patient_care = ttk.Combobox(Data_frame_left, textvariable=self.patient_care, state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        Com_patient_care['value'] = (
        "Primary", "Secondary", "tertiary","Emergency")
        Com_patient_care.current(0)
        Com_patient_care.grid(row=7, column=1)

        #----------------------------------------------------------------------------------------------------------------
        lbl_state = Label(Data_frame_left, text="State:", font=("times new roman", 12, "bold"), padx=2,
                                pady=6)
        lbl_state.grid(row=5, column=0, sticky=W)

        Com_state_name = ttk.Combobox(Data_frame_left,textvariable=self.state , state="readonly",
                                      font=("arial", 12, "bold"), width=33)
        Com_state_name['value'] = (
        "Andhra Pradesh	", "Arunachal Pradesh	", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
        "Haryana", "Himachal Pradesh	", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh	",
        "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
        "Punjab", "Rajasthan", "Sikkim	", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh	", "Uttarakhand",
        "West Bengal	")
        Com_state_name.current(0)
        Com_state_name.grid(row=5, column=1)


        # lbl_ref = Label(Data_frame_left, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        # lbl_ref.grid(row=1, column=0, sticky=W)
        # textref = Entry(Data_frame_left, textvariable=self.Ref, font=("arial", 13, "bold"), width=35)
        # textref.grid(row=1, column=1)
        #
        # lbl_dose = Label(Data_frame_left, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        # lbl_dose.grid(row=2, column=0, sticky=W)
        # textdose = Entry(Data_frame_left, textvariable=self.Dose, font=("arial", 13, "bold"), width=35)
        # textdose.grid(row=2, column=1)
        #
        # lbl_tablet_no = Label(Data_frame_left, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=4)
        # lbl_tablet_no.grid(row=3, column=0, sticky=W)
        # texttablets = Entry(Data_frame_left, textvariable=self.Numberoftablets, font=("arial", 13, "bold"), width=35)
        # texttablets.grid(row=3, column=1)
        #
        # lbl_lot = Label(Data_frame_left, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        # lbl_lot.grid(row=4, column=0, sticky=W)
        # textlot = Entry(Data_frame_left, textvariable=self.Lot, font=("arial", 13, "bold"), width=35)
        # textlot.grid(row=4, column=1)
        #
        # lbl_issue_date = Label(Data_frame_left, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        # lbl_issue_date.grid(row=5, column=0, sticky=W)
        # textissuedate = Entry(Data_frame_left, textvariable=self.Issuedate, font=("arial", 13, "bold"), width=35)
        # textissuedate.grid(row=5, column=1)



        lbl_patient_info = Label(Data_frame_left, font=("arial", 12, "bold"), text="Patient Info:", padx=2, pady=4)
        lbl_patient_info.grid(row=6, column=0, sticky=W)
        textdailydose = Entry(Data_frame_left, textvariable=self.patient_info, font=("arial", 13, "bold"), width=35)
        textdailydose.grid(row=6, column=1)

        # lbl_side_effect = Label(Data_frame_left, font=("arial", 12, "bold"), text="Department:", padx=2, pady=6)
        # lbl_side_effect.grid(row=8, column=0, sticky=W)
        # textsideeffect = Entry(Data_frame_left, textvariable=self.sideEffect, font=("arial", 13, "bold"), width=35)
        # textsideeffect.grid(row=8, column=1)

        # lbl_add_info = Label(Data_frame_left, font=("arial", 12, "bold"), text="Floor/Building:", padx=2)
        # lbl_add_info.grid(row=0, column=2, sticky=W)
        # textaddinfo = Entry(Data_frame_left, textvariable=self.FurtherInfo, font=("arial", 13, "bold"), width=35)
        # textaddinfo.grid(row=0, column=3)

        lbl_hospital_Id = Label(Data_frame_left, font=("arial", 12, "bold"), text="Hospital ID:", padx=2, pady=6)
        lbl_hospital_Id.grid(row=0, column=0, sticky=W)
        text_hospital_Id = Entry(Data_frame_left, textvariable=self.hospital_id, font=("arial", 13, "bold"), width=35)
        text_hospital_Id.grid(row=0, column=1)

        lbl_patient_id_no = Label(Data_frame_left, font=("arial", 12, "bold"), text="Patient_ID No:", padx=2, pady=6)
        lbl_patient_id_no.grid(row=4, column=2, sticky=W)
        text_patient_id_no = Entry(Data_frame_left, textvariable=self.patient_id_no, font=("arial", 13, "bold"), width=35)
        text_patient_id_no.grid(row=4, column=3)


        lbl_gardians = Label(Data_frame_left, font=("arial", 12, "bold"), text="Gardians Name:", padx=2, pady=6)
        lbl_gardians.grid(row=2, column=0, sticky=W)
        text_gardians = Entry(Data_frame_left, textvariable=self.gardians_name, font=("arial", 13, "bold"), width=35)
        text_gardians.grid(row=2, column=1)

        lbl_pincode = Label(Data_frame_left, font=("arial", 12, "bold"), text="Pincode:", padx=2, pady=6)
        lbl_pincode.grid(row=3, column=2, sticky=W)
        text_pincode = Entry(Data_frame_left, textvariable=self.pincode, font=("arial", 13, "bold"), width=35)
        text_pincode.grid(row=3, column=3)

        lbl_phone_no = Label(Data_frame_left, font=("arial", 12, "bold"), text="Phone No.", padx=2, pady=6)
        lbl_phone_no.grid(row=3, column=0, sticky=W)
        text_NHS_no = Entry(Data_frame_left, textvariable=self.phone_no, font=("arial", 13, "bold"), width=35)
        text_NHS_no.grid(row=3, column=1)

        lbl_city = Label(Data_frame_left, font=("arial", 12, "bold"), text="City:", padx=2, pady=6)
        lbl_city.grid(row=5, column=2, sticky=W)
        text_city = Entry(Data_frame_left, textvariable=self.city, font=("arial", 13, "bold"), width=35)
        text_city.grid(row=5, column=3)



        lbl_Paitent_name = Label(Data_frame_left, font=("arial", 12, "bold"), text="Patient_Name:", padx=2, pady=6)
        lbl_Paitent_name.grid(row=1, column=0, sticky=W)
        text_patient_name = Entry(Data_frame_left, textvariable=self.patient_name, font=("arial", 13, "bold"), width=35)
        text_patient_name.grid(row=1, column=1)

        lbl_age = Label(Data_frame_left, font=("arial", 12, "bold"), text="Age:", padx=2, pady=6)
        lbl_age.grid(row=1, column=2, sticky=W)
        text_age = Entry(Data_frame_left, textvariable=self.age, font=("arial", 13, "bold"), width=35)
        text_age.grid(row=1, column=3)

        lbl_address = Label(Data_frame_left, font=("arial", 12, "bold"), text="Address", padx=2, pady=6)
        lbl_address.grid(row=2, column=2, sticky=W)
        text_address = Entry(Data_frame_left, textvariable=self.address, font=("arial", 13, "bold"), width=35)
        text_address.grid(row=2, column=3)

        # ===============================Dateframe_right===========================
        self.txtPrescription = Text(Data_frame_right, font=("arial", 13, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ===============================Button_frame============================
        btn_data_to_db = Button(Button_frame, text="Upload Data", command=self.data_transfer_to_db,fg="White", bg="Pink", font=("arial", 16, "bold"),
                                  width=18, padx=1, pady=2,background="brown")
        btn_data_to_db.grid(row=0, column=0)

        btn_prescription_data = Button(Button_frame, text="Prescription Data", fg="White", bg="Pink",
                                       font=("arial", 16, "bold"), width=18, padx=1, pady=2,command=self.prescription_data)
        btn_prescription_data.grid(row=0, column=1)

        btn_Update = Button(Button_frame, text="Update", fg="White", bg="Pink", font=("arial", 16, "bold"), width=19,
                            padx=1, pady=2,background="brown",command=self.update)
        btn_Update.grid(row=0, column=2)

        btn_delete = Button(Button_frame, text="Delete", fg="White", bg="Pink", font=("arial", 16, "bold"), width=18,
                            padx=1, pady=1,command=self.delete)
        btn_delete.grid(row=0, column=3)

        btn_Clear = Button(Button_frame, text="Clear", fg="White",bg="Pink", font=("arial", 16, "bold"), width=19,
                           padx=1, pady=2, background="brown",command=self.clear)
        btn_Clear.grid(row=0, column=4)

        btn_Exit = Button(Button_frame, text="Exit", fg="White", bg="Pink", font=("arial", 16, "bold"), width=18,
                          padx=1, pady=2,command=self.Exit)
        btn_Exit.grid(row=0, column=5)

        #================================Table===========================
        #================================Scrollbar=======================
        scroll_x = ttk.Scrollbar(Details_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Details_frame, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Details_frame, column=("Hospital_ID","Hospital_card","Patient_Name","Age","Gardians_name","Address","Phone_No","Pincode","ID_CARD","Patient_ID_No","State","City",
                                                                   "Dept_Name","Patient_Care","Building"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.xview)

        self.hospital_table.heading("Hospital_ID", text="Hospital ID")
        self.hospital_table.heading("Hospital_card", text="Hospital Card")
        self.hospital_table.heading("Patient_Name", text="Patient Name")
        self.hospital_table.heading("Age", text="Age")
        self.hospital_table.heading("Gardians_name", text="Gardians name")
        self.hospital_table.heading("Address", text="Address")
        self.hospital_table.heading("Phone_No", text="Phone No.")
        self.hospital_table.heading("Pincode", text="Pincode")
        self.hospital_table.heading("ID_CARD", text="ID CARD")
        self.hospital_table.heading("Patient_ID_No", text="Patient_ID No.")
        self.hospital_table.heading("State", text="State")
        self.hospital_table.heading("City", text="City")
        self.hospital_table.heading("Dept_Name", text="Dept Name")
        self.hospital_table.heading("Patient_Care", text="Patient Care")
        self.hospital_table.heading("Building", text="Building")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)

        #===========================================================set the width of column of data in botton frame=========================================

        self.hospital_table.column("Hospital_ID", width=100)
        self.hospital_table.column("Hospital_card", width=100)
        self.hospital_table.column("Patient_Name", width=100)
        self.hospital_table.column("Age", width=60)
        self.hospital_table.column("Gardians_name", width=100)
        self.hospital_table.column("Address", width=100)
        self.hospital_table.column("Phone_No", width=100)
        self.hospital_table.column("Pincode", width=100)
        self.hospital_table.column("ID_CARD", width=100)
        self.hospital_table.column("Patient_ID_No", width=100)
        self.hospital_table.column("State", width=100)
        self.hospital_table.column("City", width=100)
        self.hospital_table.column("Dept_Name",width=100)
        self.hospital_table.column("Patient_Care", width=100)
        self.hospital_table.column("Building",width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def data_transfer_to_db(self):
        if self.hospital_id.get() == "" or self.age.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='Nokia?tl3',
                    host='127.0.0.1',
                    database='hospital_db'
                )

                my_cursor = conn.cursor()

                sql_query = """INSERT INTO hospital 
                               (hospital_id, hospital_card, patient_name, age, gardians_name, address, phone_no, pincode,
                                id_card, patient_id_no, state, city, dept_name, patient_care, building)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                data = (
                    self.hospital_id.get(), self.hospital_card.get(), self.patient_name.get(), self.age.get(),
                    self.gardians_name.get(),
                    self.address.get(), self.phone_no.get(), self.pincode.get(), self.id_card.get(),
                    self.patient_id_no.get(), self.state.get(), self.city.get(), self.dept_name.get(),
                    self.patient_care.get(), self.building.get()
                )

                my_cursor.execute(sql_query, data)
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Record has been inserted")
            except Error as err:
                messagebox.showerror("Error", f"Error occurred: {err}")

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='Nokia?tl3',
                                       host='127.0.0.1',
                                       database='hospital_db')

        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event = ""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.hospital_id.set(row[0])
        self.hospital_card.set(row[1])
        self.patient_name.set(row[2])
        self.age.set(row[3])
        self.gardians_name.set(row[4])
        self.address.set(row[5])
        self.phone_no.set(row[6])
        self.pincode.set(row[7])
        self.id_card.set(row[8])
        self.patient_id_no.set(row[9])
        self.state.set(row[10])
        self.city.set(row[11])
        self.dept_name.set(row[12])
        self.patient_care.set(row[13])
        self.building.set(row[14])


    def update(self):
        conn = mysql.connector.connect(user='root', password='Nokia?tl3',
                                       host='127.0.0.1',
                                       database='hospital_db')

        my_cursor = conn.cursor()
        sql_update_data = ("""UPDATE hospital 
                            SET hospital_card=%s, patient_name=%s, age=%s, gardians_name=%s, address=%s, phone_no=%s, pincode=%s,
                                id_card=%s, patient_id_no=%s, state=%s, city=%s, dept_name=%s, patient_care=%s, building=%s 
                            WHERE hospital_id=%s""")

        data_2 = (self.hospital_card.get(), self.patient_name.get(),
                  self.age.get(), self.gardians_name.get(), self.address.get(), self.phone_no.get(),
                  self.pincode.get(), self.id_card.get(), self.patient_id_no.get(), self.state.get(),
                  self.city.get(),self.dept_name.get(),self.patient_care.get(),self.building.get(), self.hospital_id.get())

        my_cursor.execute(sql_update_data, data_2)
        self.fetch_data()
        # Commit the changes
        conn.commit()
        # Close cursor and connection
        my_cursor.close()
        conn.close()

        messagebox.showinfo("Success", "Record has been updated ")

    def prescription_data(self):
        self.txtPrescription.insert(END,"Hospital ID:\t\t\t" + self.hospital_id.get() + "\n")
        self.txtPrescription.insert(END,"Hospital Card:\t\t\t" + self.hospital_card.get() + "\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t" + self.patient_name.get() + "\n")
        self.txtPrescription.insert(END,"Age:\t\t\t" + self.age.get() + "\n")
        self.txtPrescription.insert(END,"Gardians Name:\t\t\t" + self.gardians_name.get() + "\n")
        self.txtPrescription.insert(END,"Address:\t\t\t" + self.address.get() + "\n")
        self.txtPrescription.insert(END,"ID Card:\t\t\t" + self.id_card.get() + "\n")
        self.txtPrescription.insert(END,"Patient ID:\t\t\t" + self.patient_id_no.get() + "\n")
        self.txtPrescription.insert(END,"State:\t\t\t" + self.state.get() + "\n")
        self.txtPrescription.insert(END,"City:\t\t\t" + self.city.get() + "\n")
        self.txtPrescription.insert(END,"Dept Name:\t\t\t" + self.dept_name.get() + "\n")
        self.txtPrescription.insert(END, "Patient Info:\t\t\t" + self.patient_info.get() + "\n")
        self.txtPrescription.insert(END,"Patient Care:\t\t\t" + self.patient_care.get() + "\n")
        self.txtPrescription.insert(END,"Building:\t\t\t" + self.building.get() + "\n")
        self.txtPrescription.insert(END,"Phone No:\t\t\t" + self.phone_no.get() + "\n")
        self.txtPrescription.insert(END,"Pincode:\t\t\t" + self.pincode.get() + "\n")

    def delete(self):
        conn = mysql.connector.connect(user='root', password='Nokia?tl3',
                                       host='127.0.0.1',
                                       database='hospital_db')
        mycursor = conn.cursor()
        query = "DELETE FROM hospital WHERE hospital_id=%s"
        value = (self.hospital_id.get(),)  # Corrected to properly define a tuple
        mycursor.execute(query, value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")

    def clear(self):
        self.hospital_id.set("")
        self.hospital_card.set("")
        self.patient_name.set("")
        self.age.set("")
        self.gardians_name.set("")
        self.address.set("")
        self.phone_no.set("")
        self.pincode.set("")
        self.id_card.set("")
        self.patient_id_no.set("")
        self.state.set("")
        self.city.set("")
        self.patient_info.set("")
        self.dept_name.set("")
        self.patient_care.set("")
        self.building.set("")
        self.txtPrescription.delete("1.0",END)

    def Exit(self):
        Exit = messagebox.askyesno("hHospital Database System","Confirm you want to exit")
        if Exit>0:
            root.destroy()
            return




root=Tk()
ob=Hospital(root)
root.mainloop()