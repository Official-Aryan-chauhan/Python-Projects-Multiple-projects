# Student Report Card Generator With Saver Time for saver (2-3 Hours)
from playsound3 import playsound
import time
school_name = "X Public School"
from Create_pdf import pdf_maker
import os
if not os.path.exists("report_card_data.txt"):
    with open("report_card_data.txt","w") as f:
        f.write("/")
        f.truncate(0)
        print("INITIALLY FILE CREATED !")
else:

    try:
        name = input("Name of The Student : ").upper().strip()
        class_  = int(input("class OF Student : ").strip())

        if name != "" and len(name) <= 20 and 1 <= class_ <= 12:
            roll_number = (input("Roll Number OF Student : ").strip())
            if 4 <= len(roll_number) <= 6:  
                print("Valid Identity !")
                print("Enter Marks OF Subjects Out of 100 !")
                maths = float(input("Maths : "))
                physics = float(input("Physics : "))
                chemistry = float(input("Chemistry : "))
                
                if 0 <= physics <= 100 and 0 <=  maths <= 100 and 0 <=  chemistry <= 100 :
                    print("Generating--","\n")
                    time.sleep(0.5)
                    #-------------------------
                    total_marks = maths + physics + chemistry 
                    percantage =  round((total_marks*100)/300,1)
                    
                    def grade(p):
                        if 85.00 <= p <=100.00:
                            print("Passed | GRADE - A")
                        elif 60.00 <= p < 85.00:
                            print("Passed | GRADE - B")
                        elif 33.00 <= p <60.00:
                            print("Passed | GRADE - C")
                        elif p < 33.00 :
                            print("Failed !")

                else:
                    playsound("error-011-352286.mp3")
                    print("Invalid Marks !")               
                    
                create_pdf = input('Do You Want To Create  A PDF OF REPORT CARD : ').lower().strip()
                if create_pdf == "y" or create_pdf =="yes":
                    with open("report_card_data.txt","w") as f:
                        f.write(f"{school_name} Report Card \n \n")
                        f.write(f"Name Of Student | {name}    Class  | {class_}   Roll-Number  |  {roll_number} \n")
                        f.write(f"Subject Wise Marks || \n")
                        f.write(f"Mathematics :  {maths} \n") 
                        f.write(f"Physics :  {physics} \n")             #Multiple f.write combine them in one
                        f.write(f"Chemistry :  {chemistry} \n \n")
                        f.write(f"Total Marks {total_marks}/300   ,  Percentage | {round(percantage,1)}%")
                        # f.write(f"Result : {grade(percantage)}")
                        print("Text File Formed !")
                        time.sleep(0.25)

                    pdf_maker()

                else:
                    print("PDF NOT CREATED !","\n")
                    report = f"""{school_name} Report Card \n 
        Name Of Student | {name}    Class  | {class_}   Roll-Number  |  {roll_number}
        Subject Wise Marks ||
        Mathematics :  {maths}
        Physics :  {physics}
        Chemistry :  {chemistry} \n
        Total Marks {total_marks}/300   ,  Percentage | {round(percantage,1)}%
        {grade(percantage)}"""
                    print(report)

            else:
                playsound("error-sound.mp3")
                print("Invalid RolL Nnumber  !")
        else:
            playsound("error-sound.mp3")
            print("Incorrect Name/Class INPUTS !")
    except Exception as e:
        print(e,"Some Error occured !")

