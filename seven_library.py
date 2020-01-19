import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
from tkinter import *
import smtplib
from threading import *
def c1():
    # Reading CSV File for extracting its data
    df=pd.read_csv('C:/Users/ATUL KUMAR/Desktop/class cgpa.csv')
     
    # Plotting Graph from extracted data
    plt.bar(df['Roll'],df['CGPA'],label='Roll Number vs Semester-2 CGPA',linestyle='-')
    plt.title("MCE 2nd Semester(CSE) SGPA Graph")
    plt.xlabel("Roll Number")
    plt.ylabel("2nd Semester SGPA")
    plt.legend()
    plt.show()


df=pd.read_csv('C:/Users/ATUL KUMAR/Desktop/class cgpa.csv')
num=np.array(df)

# Connecting to database and uploading Result
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='cse2k18')
m=mydb.cursor()
i=0
#while(i<len(num)):
    #a=int(num[i,0])
    #b=float(num[i,1])
    #sql="INSERT INTO semester(Roll_No,CGPA) VALUES(%s,%s)"
    #val=(a,b)
    #m.execute(sql,val)
    #mydb.commit()
    #i=i+1


#Configuration for mail sending service


#GUI Creation for Show Result Window
root=Tk()
root.title("2nd Semester Result")
def cgpa():
    roll=cal.get()
    sql=m.execute(f"SELECT CGPA FROM semester WHERE Roll_No={roll}")
    result=m.fetchone()
    a=result[0]
    Label(root,text=str(a)).grid(row=3,column=5)
def send():
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()               
    s.login('mcemotihari.2k18@gmail.com','MCEmotihari.2k18') 
    roll=cal.get()
    sql=m.execute(f"SELECT CGPA FROM semester WHERE Roll_No={roll}")
    result=m.fetchone()
    a=result[0]
    sql=m.execute(f"SELECT EMAIL FROM semester WHERE Roll_No={roll}")
    result=m.fetchone()
    b=result[0]
    subject="Second semester Result"
    msg=f"Congratulation!You have passed your 2nd Semester Exam.Your SGPA is {a}."
    msg1="subject:{}\n\n{}".format(subject,msg)
    s.sendmail('mcemotihari.2k18@gmail.com',f'{b}',f'{msg1}')

root.geometry("600x600")
Label(root,text="Enter Roll No.").grid(row=1,column=2)
cal=Entry(root)
cal.grid(row=2,column=2)
Label(root,text="SGPA:").grid(row=3,column=4)
btn=Button(root,text="Show Result",command=cgpa)
btn.grid(row=4,column=1)
btn2=Button(root,text="Send on Mail",command=send)
btn2.grid(row=4,column=2)
t1=Thread(target=c1)
t1.start()
print("Threading complete")

