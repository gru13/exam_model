from cgitb import text
from tkinter import *
from time import strftime
from tkinter.ttk import Notebook
# ------------------constant_variable-&-Database-------
Exam_name = "Exam Name"
# applicant_detail is in form of list that contain [application no,applicant name,photo,Exam_name,[*[subject,questionno,ans]]]
applicant_detail = ['20221089',"Guruprasath.M.R",r"./nullphtid.png",Exam_name,[]]
#  Database is dict and  in form of {**subjectname:[Frame,[*question ,*[*choices]],Frame(qno frame),[Frame(q frame),*qno_buttons(current_postion),1]]}
Database={
    "Physcis":[Frame,["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],Frame,[Frame]],
    "Maths":[Frame,[],[],[],[],[],[],[],Frame,[Frame]],
    "Chemistry":[Frame,[],[],[],[],[],[],[],Frame,[Frame]],
}
# ------------------------------------------
# ------------------function----------------
def cur_time(x:Label):
    x.config(text=strftime('%I:%M:%S %p'))
    x.after(1000,lambda :cur_time(x))
def qnos_command(cur_pos,subject,qno):
    print(cur_pos,subject,qno)

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
# Second frame contain a notebook  
#  (env-> Win,ext->Frame)
second_frame = Frame(Win)
second_frame.pack(fill=X)
second_frame_Notebook = Notebook(second_frame)
second_frame_Notebook.pack(fill=BOTH)
# Creating tabs
for a in Database:
    # print(a)
    # print(Database[a])
    # print(Database[a][0])
    Database[a][0]=Database[a][0](second_frame_Notebook)
    Database[a][0].pack()
    second_frame_Notebook.add(Database[a][0],text=a)
    no_of_question_len = len(Database[a]) - 3 #-3 because of 3 frame
    for i in range(no_of_question_len):
        Database[a][-1].append(Button)
    Database[a][-1].append(1)
    # print(Database[a][-1])
# creating qnos 
for a in Database:
    # print(a)
    # print(Database[a])
    no_of_question_len = len(Database[a]) - 3 #-3 because of 3 frame
    # print(no_of_question_len)
    Database[a][-1][0] = Database[a][-1][0](Database[a][0])
    Database[a][-1][0].pack(side=LEFT) # question nos tab frame
    # qnosf is Database[a][-1][0]
    for ax in range(1,no_of_question_len+1):
        q = Database[a][-1][ax](Database[a][-1][0],text=str(ax),command=lambda q= [Database[a][-1][-1],a,ax]:qnos_command(q[0],q[1],q[2]))
        Database[a][-1][ax] = q 
    # align of qnos
    # print(Database[a])
    # Button are in region of Database[a][-1][1:-1]
    l_contain_b_index = []
    if no_of_question_len % 3 == 0:
        for aa in range(0,no_of_question_len,3):
            for b in range(0,3):
                # print(a,b)
                l_contain_b_index.append([aa,b])
    else:
        remain = no_of_question_len % 3
        for aa in range(int((no_of_question_len-remain)/3)):
            for b in range(0,3):
                l_contain_b_index.append([aa,b])
        # print(remain)
        for ad in range(remain):
            l_contain_b_index.append([int((no_of_question_len-remain)/3),ad])
    print(l_contain_b_index)
    for ad in range(1,len(l_contain_b_index)+1):
        Database[a][-1][ad].grid(row=l_contain_b_index[ad-1][0],column=l_contain_b_index[ad-1][1])

# --------------------------------------------
Win.mainloop()
#----------------------------------------------------------