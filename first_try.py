from cProfile import label
from cgitb import text
from email.mime import application
from tkinter import *
from time import strftime
# ------------------constant_variable-&-Database-------
Exam_name = "Exam Name"
# applicant_detail is in form of list that contain [application no,applicant name,photo,Exam_name,[*[subject,questionno,ans]]]
applicant_detail = ['20221089',"Guruprasath.M.R",r"./nullphtid.png",Exam_name,[]]
#  Database is dict and  in form of {**subjectname:[*question ,*[*choices]]}
Database={
    "Physcis":[Frame,[],[],[],[],[],[],[]],
    "Maths":[Frame,[],[],[],[],[],[],[]],
    "Chemistry":[Frame,[],[],[],[],[],[],[]],
}
# ------------------------------------------
# ------------------function----------------
def cur_time(x:Label):
    x.config(text=strftime('%I:%M:%S %p'))
    x.after(1000,lambda :cur_time(x))
# ------------------------------------------
# ------------------main_code---------------
#  (env-> global,ext->Tk{main window})
# Win is main frame contain all container and frame 
Win = Tk()
Win.geometry("1250x720")
Win.title("EXAM")
# ---------------first_frame----------------
#  (env-> Win,ext->Frame)
first_frame = Frame(Win)
first_frame.pack(fill=X)
# first top contaier contain 2 row and first contain name of exam and time 
#  (env-> first_frame,ext->Frame)
ExamNameTime_Frame = Frame(first_frame,highlightbackground="black",highlightthickness=0)
ExamNameTime_Frame.pack(fill=X)
Label(ExamNameTime_Frame,text=Exam_name,font=("Mono",25)).pack()
TimeLabel=Label(ExamNameTime_Frame,text="time")
TimeLabel.pack(anchor="e")
cur_time(TimeLabel)
# 2 row contain App no ,name ,photo  
#  (env-> first_frame,ext->Frame)
# detail frame  
detail_frame =Frame(first_frame)
detail_frame.pack(fill="x")
Label(detail_frame,text=applicant_detail[0],font=("Mono",15)).pack(side="left",fill=X)
Label(detail_frame,text=applicant_detail[1],font=("Mono",15)).pack(side="left",fill=X)
phtid = PhotoImage(file=applicant_detail[2])
Label(detail_frame,image=phtid).pack(anchor="e")
# --------------------------------------------
# ------------second_frame--------------------
# second frame contain tab that contain subject and that contain question number and question ans

# --------------------------------------------
Win.mainloop()