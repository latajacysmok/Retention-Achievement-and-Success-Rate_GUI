from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

Success_Rate = Tk()
Success_Rate.geometry("1350x700")
Success_Rate.resizable(0, 0)
Success_Rate.title("Retention Achievement and Success Rate")

def exit():
    Success_Rate.destroy()

def reset():
    StarterA.set("")
    StarterB.set("")
    StarterC.set("")
    StarterD.set("")
    StarterE.set("")
    LeftA.set("")
    LeftB.set("")
    LeftC.set("")
    LeftD.set("")
    LeftE.set("")
    StPA.set("")
    StPB.set("")
    StPC.set("")
    StPD.set("")
    StPE.set("")
    RetentionA.set("")
    RetentionB.set("")
    RetentionC.set("")
    RetentionD.set("")
    RetentionE.set("")
    AchievementA.set("")
    AchievementB.set("")
    AchievementC.set("")
    AchievementD.set("")
    AchievementE.set("")
    SuccessA.set("")
    SuccessB.set("")
    SuccessC.set("")
    SuccessD.set("")
    SuccessE.set("")
    RetentionF.set("")
    AchievmentF.set("")
    SuccessF.set("")
#---

def Retention_Rate():
    Std_Left_Ret_A1 = float(LeftA.get())
    Std_Left_Ret_A2 = float(StarterA.get())
    retention_rate_A = ((Std_Left_Ret_A1 / Std_Left_Ret_A2)*100)
    ret_Rate_A = ('%.1f' % (retention_rate_A) + "%")
    RetentionA.set(ret_Rate_A)

    Std_Left_Ret_B1 = float(LeftB.get())
    Std_Left_Ret_B2 = float(StarterB.get())
    retention_rate_B = ((Std_Left_Ret_B1 / Std_Left_Ret_B2) * 100)
    ret_Rate_B = ('%.1f' % (retention_rate_A) + "%")
    RetentionB.set(ret_Rate_B)

    Std_Left_Ret_C1 = float(LeftC.get())
    Std_Left_Ret_C2 = float(StarterC.get())
    retention_rate_C = ((Std_Left_Ret_C1 / Std_Left_Ret_C2) * 100)
    ret_Rate_C = ('%.1f' % (retention_rate_C) + "%")
    RetentionC.set(ret_Rate_C)

    Std_Left_Ret_D1 = float(LeftD.get())
    Std_Left_Ret_D2 = float(StarterD.get())
    retention_rate_D = ((Std_Left_Ret_D1 / Std_Left_Ret_D2) * 100)
    ret_Rate_D = ('%.1f' % (retention_rate_D) + "%")
    RetentionD.set(ret_Rate_D)

    Std_Left_Ret_E1 = float(LeftE.get())
    Std_Left_Ret_E2 = float(StarterE.get())
    retention_rate_E = ((Std_Left_Ret_E1 / Std_Left_Ret_E2) * 100)
    ret_Rate_E = ('%.1f' % (retention_rate_E) + "%")
    RetentionE.set(ret_Rate_E)

#---
def Achievement_Rate():
    Std_Left_Ach_A1 = float(StPA.get())
    Std_Left_Ach_A2 = float(LeftA.get())
    Achieve_rate_A = ((Std_Left_Ach_A1 / Std_Left_Ach_A2)*100)
    Ach_Rate_A = ('%.1f' % (Achieve_rate_A) + "%")
    AchievementA.set(Ach_Rate_A)

    Std_Left_Ach_B1 = float(StPB.get())
    Std_Left_Ach_B2 = float(LeftB.get())
    Achieve_rate_B = ((Std_Left_Ach_B1 / Std_Left_Ach_B2) * 100)
    Ach_Rate_B = ('%.1f' % (Achieve_rate_B) + "%")
    AchievementB.set(Ach_Rate_B)

    Std_Left_Ach_C1 = float(StPC.get())
    Std_Left_Ach_C2 = float(LeftC.get())
    Achieve_rate_C = ((Std_Left_Ach_C1 / Std_Left_Ach_C2) * 100)
    Ach_Rate_C = ('%.1f' % (Achieve_rate_C) + "%")
    AchievementC.set(Ach_Rate_C)

    Std_Left_Ach_D1 = float(StPD.get())
    Std_Left_Ach_D2 = float(LeftD.get())
    Achieve_rate_D = ((Std_Left_Ach_D1 / Std_Left_Ach_D2) * 100)
    Ach_Rate_D = ('%.1f' % (Achieve_rate_D) + "%")
    AchievementD.set(Ach_Rate_D)

    Std_Left_Ach_E1 = float(StPE.get())
    Std_Left_Ach_E2 = float(LeftE.get())
    Achieve_rate_E = ((Std_Left_Ach_E1 / Std_Left_Ach_E2) * 100)
    Ach_Rate_E = ('%.1f' % (Achieve_rate_E) + "%")
    AchievementE.set(Ach_Rate_E)

#---
def success_Rate():
    Std_Left_Ret_A1 = float(LeftA.get())
    Std_Left_Ret_A2 = float(StarterA.get())
    rention_rate_A = ((Std_Left_Ret_A1/Std_Left_Ret_A2)*100)

    Std_Left_Ach_A1 = float(StPA.get())
    Std_Left_Ach_A2 = float(LeftA.get())
    Achieve_rate_A = ((Std_Left_Ach_A1 / Std_Left_Ach_A2) * 100)

    Success_A = (rention_rate_A * Achieve_rate_A)
    Suc_Rate_A = ('%.1f' % (Success_A / 100) + "%")
    SuccessA.set(Suc_Rate_A)

    Std_Left_Ret_B1 = float(LeftB.get())
    Std_Left_Ret_B2 = float(StarterB.get())
    rention_rate_B = ((Std_Left_Ret_B1 / Std_Left_Ret_B2) * 100)

    Std_Left_Ach_B1 = float(StPB.get())
    Std_Left_Ach_B2 = float(LeftB.get())
    Achieve_rate_B = ((Std_Left_Ach_B1 / Std_Left_Ach_B2) * 100)

    Success_B = (rention_rate_B * Achieve_rate_B)
    Suc_Rate_B = ('%.1f' % (Success_B / 100) + "%")
    SuccessB.set(Suc_Rate_B)

    Std_Left_Ret_C1 = float(LeftC.get())
    Std_Left_Ret_C2 = float(StarterC.get())
    rention_rate_C = ((Std_Left_Ret_C1 / Std_Left_Ret_C2) * 100)

    Std_Left_Ach_C1 = float(StPC.get())
    Std_Left_Ach_C2 = float(LeftC.get())
    Achieve_rate_C = ((Std_Left_Ach_C1 / Std_Left_Ach_C2) * 100)

    Success_C = (rention_rate_C * Achieve_rate_C)
    Suc_Rate_C = ('%.1f' % (Success_C / 100) + "%")
    SuccessC.set(Suc_Rate_C)

    Std_Left_Ret_D1 = float(LeftD.get())
    Std_Left_Ret_D2 = float(StarterD.get())
    rention_rate_D = ((Std_Left_Ret_D1 / Std_Left_Ret_D2) * 100)

    Std_Left_Ach_D1 = float(StPD.get())
    Std_Left_Ach_D2 = float(LeftD.get())
    Achieve_rate_D = ((Std_Left_Ach_D1 / Std_Left_Ach_D2) * 100)

    Success_D = (rention_rate_D * Achieve_rate_D)
    Suc_Rate_D = ('%.1f' % (Success_D / 100) + "%")
    SuccessD.set(Suc_Rate_D)

    Std_Left_Ret_E1 = float(LeftE.get())
    Std_Left_Ret_E2 = float(StarterE.get())
    rention_rate_E = ((Std_Left_Ret_E1 / Std_Left_Ret_E2) * 100)

    Std_Left_Ach_E1 = float(StPE.get())
    Std_Left_Ach_E2 = float(LeftE.get())
    Achieve_rate_E = ((Std_Left_Ach_E1 / Std_Left_Ach_E2) * 100)

    Success_E = (rention_rate_E * Achieve_rate_E)
    Suc_Rate_E = ('%.1f' % (Success_E / 100) + "%")
    SuccessE.set(Suc_Rate_E)

#---
def Average():
    Std_Left_Ret_A1 = float(LeftA.get())
    Std_Left_Ret_A2 = float(StarterA.get())

    Std_Left_Ret_B1 = float(LeftB.get())
    Std_Left_Ret_B2 = float(StarterB.get())


    Std_Left_Ret_C1 = float(LeftC.get())
    Std_Left_Ret_C2 = float(StarterC.get())

    Std_Left_Ret_D1 = float(LeftD.get())
    Std_Left_Ret_D2 = float(StarterD.get())

    Std_Left_Ret_E1 = float(LeftE.get())
    Std_Left_Ret_E2 = float(StarterE.get())

    retention_rate_A = ((Std_Left_Ret_A1 / Std_Left_Ret_A2) * 100)
    retention_rate_B = ((Std_Left_Ret_B1 / Std_Left_Ret_B2) * 100)
    retention_rate_C = ((Std_Left_Ret_A1 / Std_Left_Ret_C2) * 100)
    retention_rate_D = ((Std_Left_Ret_D1 / Std_Left_Ret_D2) * 100)
    retention_rate_E = ((Std_Left_Ret_E1 / Std_Left_Ret_E2) * 100)

    Average_rention_rate=(retention_rate_A + retention_rate_B + retention_rate_C + retention_rate_D + retention_rate_E)/5
    RentionA_Average = ('%.1f' % (Average_rention_rate) + "%")
    RetentionF.set(RentionA_Average)

    Std_Left_Ach_A1 = float(StPA.get())
    Std_Left_Ach_A2 = float(LeftA.get())

    Std_Left_Ach_B1 = float(StPB.get())
    Std_Left_Ach_B2 = float(LeftB.get())

    Std_Left_Ach_C1 = float(StPC.get())
    Std_Left_Ach_C2 = float(LeftC.get())

    Std_Left_Ach_D1 = float(StPD.get())
    Std_Left_Ach_D2 = float(LeftD.get())

    Std_Left_Ach_E1 = float(StPE.get())
    Std_Left_Ach_E2 = float(LeftE.get())

    Achieve_rate_A = ((Std_Left_Ach_A1 / Std_Left_Ach_A2) * 100)
    Achieve_rate_B = ((Std_Left_Ach_B1 / Std_Left_Ach_B2) * 100)
    Achieve_rate_C = ((Std_Left_Ach_C1 / Std_Left_Ach_C2) * 100)
    Achieve_rate_D = ((Std_Left_Ach_D1 / Std_Left_Ach_D2) * 100)
    Achieve_rate_E = ((Std_Left_Ach_E1 / Std_Left_Ach_E2) * 100)

    Average_Achieve_rate = (
                            Achieve_rate_A + Achieve_rate_B + Achieve_rate_C + Achieve_rate_D + Achieve_rate_E) / 5
    AchievementA_Average = ('%.1f' % (Average_Achieve_rate) + "%")
    AchievmentF.set(AchievementA_Average)

    Success_A = (retention_rate_A * Achieve_rate_A)
    Success_B = (retention_rate_B * Achieve_rate_B)
    Success_C = (retention_rate_C * Achieve_rate_C)
    Success_D = (retention_rate_D * Achieve_rate_D)
    Success_E = (retention_rate_E * Achieve_rate_E)

    Average_Success_rate = ((Success_A + Success_B + Success_C + Success_D + Success_E)/5)/100
    Success_Average = ('%.1f' % (Average_Success_rate)) + "%"
    SuccessF.set(Success_Average)

#---
def OverRetention():
    Std_Left_Ret_A1 = float(LeftA.get())
    Std_Left_Ret_A2 = float(StarterA.get())
    retention_rate_A = ((Std_Left_Ret_A1 / Std_Left_Ret_A2) * 100)
    ret_Rate_A = ('%.1f' % (retention_rate_A) + "%")
    RetentionA.set(ret_Rate_A)

    Std_Left_Ret_B1 = float(LeftB.get())
    Std_Left_Ret_B2 = float(StarterB.get())
    retention_rate_B = ((Std_Left_Ret_B1 / Std_Left_Ret_B2) * 100)
    ret_Rate_B = ('%.1f' % (retention_rate_A) + "%")
    RetentionB.set(ret_Rate_B)

    Std_Left_Ret_C1 = float(LeftC.get())
    Std_Left_Ret_C2 = float(StarterC.get())
    retention_rate_C = ((Std_Left_Ret_C1 / Std_Left_Ret_C2) * 100)
    ret_Rate_C = ('%.1f' % (retention_rate_C) + "%")
    RetentionC.set(ret_Rate_C)

    Std_Left_Ret_D1 = float(LeftD.get())
    Std_Left_Ret_D2 = float(StarterD.get())
    retention_rate_D = ((Std_Left_Ret_D1 / Std_Left_Ret_D2) * 100)
    ret_Rate_D = ('%.1f' % (retention_rate_D) + "%")
    RetentionD.set(ret_Rate_D)

    Std_Left_Ret_E1 = float(LeftE.get())
    Std_Left_Ret_E2 = float(StarterE.get())
    retention_rate_E = ((Std_Left_Ret_E1 / Std_Left_Ret_E2) * 100)
    ret_Rate_E = ('%.1f' % (retention_rate_E) + "%")
    RetentionE.set(ret_Rate_E)

    #---
    Std_Left_Ach_A1 = float(StPA.get())
    Std_Left_Ach_A2 = float(LeftA.get())
    Achieve_rate_A = ((Std_Left_Ach_A1 / Std_Left_Ach_A2) * 100)
    Ach_Rate_A = ('%.1f' % (Achieve_rate_A) + "%")
    AchievementA.set(Ach_Rate_A)

    Std_Left_Ach_B1 = float(StPB.get())
    Std_Left_Ach_B2 = float(LeftB.get())
    Achieve_rate_B = ((Std_Left_Ach_B1 / Std_Left_Ach_B2) * 100)
    Ach_Rate_B = ('%.1f' % (Achieve_rate_B) + "%")
    AchievementB.set(Ach_Rate_B)

    Std_Left_Ach_C1 = float(StPC.get())
    Std_Left_Ach_C2 = float(LeftC.get())
    Achieve_rate_C = ((Std_Left_Ach_C1 / Std_Left_Ach_C2) * 100)
    Ach_Rate_C = ('%.1f' % (Achieve_rate_C) + "%")
    AchievementC.set(Ach_Rate_C)

    Std_Left_Ach_D1 = float(StPD.get())
    Std_Left_Ach_D2 = float(LeftD.get())
    Achieve_rate_D = ((Std_Left_Ach_D1 / Std_Left_Ach_D2) * 100)
    Ach_Rate_D = ('%.1f' % (Achieve_rate_D) + "%")
    AchievementD.set(Ach_Rate_D)

    Std_Left_Ach_E1 = float(StPE.get())
    Std_Left_Ach_E2 = float(LeftE.get())
    Achieve_rate_E = ((Std_Left_Ach_E1 / Std_Left_Ach_E2) * 100)
    Ach_Rate_E = ('%.1f' % (Achieve_rate_E) + "%")
    AchievementE.set(Ach_Rate_E)

    #---
    Std_Left_Ret_A1 = float(LeftA.get())
    Std_Left_Ret_A2 = float(StarterA.get())
    rention_rate_A = ((Std_Left_Ret_A1 / Std_Left_Ret_A2) * 100)

    Std_Left_Ach_A1 = float(StPA.get())
    Std_Left_Ach_A2 = float(LeftA.get())
    Achieve_rate_A = ((Std_Left_Ach_A1 / Std_Left_Ach_A2) * 100)

    Success_A = (rention_rate_A * Achieve_rate_A)
    Suc_Rate_A = ('%.1f' % (Success_A / 100) + "%")
    SuccessA.set(Suc_Rate_A)

    Std_Left_Ret_B1 = float(LeftB.get())
    Std_Left_Ret_B2 = float(StarterB.get())
    rention_rate_B = ((Std_Left_Ret_B1 / Std_Left_Ret_B2) * 100)

    Std_Left_Ach_B1 = float(StPB.get())
    Std_Left_Ach_B2 = float(LeftB.get())
    Achieve_rate_B = ((Std_Left_Ach_B1 / Std_Left_Ach_B2) * 100)

    Success_B = (rention_rate_B * Achieve_rate_B)
    Suc_Rate_B = ('%.1f' % (Success_B / 100) + "%")
    SuccessB.set(Suc_Rate_B)

    Std_Left_Ret_C1 = float(LeftC.get())
    Std_Left_Ret_C2 = float(StarterC.get())
    rention_rate_C = ((Std_Left_Ret_C1 / Std_Left_Ret_C2) * 100)

    Std_Left_Ach_C1 = float(StPC.get())
    Std_Left_Ach_C2 = float(LeftC.get())
    Achieve_rate_C = ((Std_Left_Ach_C1 / Std_Left_Ach_C2) * 100)

    Success_C = (rention_rate_C * Achieve_rate_C)
    Suc_Rate_C = ('%.1f' % (Success_C / 100) + "%")
    SuccessC.set(Suc_Rate_C)

    Std_Left_Ret_D1 = float(LeftD.get())
    Std_Left_Ret_D2 = float(StarterD.get())
    rention_rate_D = ((Std_Left_Ret_D1 / Std_Left_Ret_D2) * 100)

    Std_Left_Ach_D1 = float(StPD.get())
    Std_Left_Ach_D2 = float(LeftD.get())
    Achieve_rate_D = ((Std_Left_Ach_D1 / Std_Left_Ach_D2) * 100)

    Success_D = (rention_rate_D * Achieve_rate_D)
    Suc_Rate_D = ('%.1f' % (Success_D / 100) + "%")
    SuccessD.set(Suc_Rate_D)

    Std_Left_Ret_E1 = float(LeftE.get())
    Std_Left_Ret_E2 = float(StarterE.get())
    rention_rate_E = ((Std_Left_Ret_E1 / Std_Left_Ret_E2) * 100)

    Std_Left_Ach_E1 = float(StPE.get())
    Std_Left_Ach_E2 = float(LeftE.get())
    Achieve_rate_E = ((Std_Left_Ach_E1 / Std_Left_Ach_E2) * 100)

    Success_E = (rention_rate_E * Achieve_rate_E)
    Suc_Rate_E = ('%.1f' % (Success_E / 100) + "%")
    SuccessE.set(Suc_Rate_E)

    #---
    Std_Left_Ret_A1 = float(LeftA.get())
    Std_Left_Ret_A2 = float(StarterA.get())

    Std_Left_Ret_B1 = float(LeftB.get())
    Std_Left_Ret_B2 = float(StarterB.get())

    Std_Left_Ret_C1 = float(LeftC.get())
    Std_Left_Ret_C2 = float(StarterC.get())

    Std_Left_Ret_D1 = float(LeftD.get())
    Std_Left_Ret_D2 = float(StarterD.get())

    Std_Left_Ret_E1 = float(LeftE.get())
    Std_Left_Ret_E2 = float(StarterE.get())

    retention_rate_A = ((Std_Left_Ret_A1 / Std_Left_Ret_A2) * 100)
    retention_rate_B = ((Std_Left_Ret_B1 / Std_Left_Ret_B2) * 100)
    retention_rate_C = ((Std_Left_Ret_A1 / Std_Left_Ret_C2) * 100)
    retention_rate_D = ((Std_Left_Ret_D1 / Std_Left_Ret_D2) * 100)
    retention_rate_E = ((Std_Left_Ret_E1 / Std_Left_Ret_E2) * 100)

    Average_rention_rate = (
                           retention_rate_A + retention_rate_B + retention_rate_C + retention_rate_D + retention_rate_E) / 5
    RentionA_Average = ('%.1f' % (Average_rention_rate) + "%")
    RetentionF.set(RentionA_Average)

    Std_Left_Ach_A1 = float(StPA.get())
    Std_Left_Ach_A2 = float(LeftA.get())

    Std_Left_Ach_B1 = float(StPB.get())
    Std_Left_Ach_B2 = float(LeftB.get())

    Std_Left_Ach_C1 = float(StPC.get())
    Std_Left_Ach_C2 = float(LeftC.get())

    Std_Left_Ach_D1 = float(StPD.get())
    Std_Left_Ach_D2 = float(LeftD.get())

    Std_Left_Ach_E1 = float(StPE.get())
    Std_Left_Ach_E2 = float(LeftE.get())

    Achieve_rate_A = ((Std_Left_Ach_A1 / Std_Left_Ach_A2) * 100)
    Achieve_rate_B = ((Std_Left_Ach_B1 / Std_Left_Ach_B2) * 100)
    Achieve_rate_C = ((Std_Left_Ach_C1 / Std_Left_Ach_C2) * 100)
    Achieve_rate_D = ((Std_Left_Ach_D1 / Std_Left_Ach_D2) * 100)
    Achieve_rate_E = ((Std_Left_Ach_E1 / Std_Left_Ach_E2) * 100)

    Average_Achieve_rate = (
                               Achieve_rate_A + Achieve_rate_B + Achieve_rate_C + Achieve_rate_D + Achieve_rate_E) / 5
    AchievementA_Average = ('%.1f' % (Average_Achieve_rate) + "%")
    AchievmentF.set(AchievementA_Average)

    Success_A = (retention_rate_A * Achieve_rate_A)
    Success_B = (retention_rate_B * Achieve_rate_B)
    Success_C = (retention_rate_C * Achieve_rate_C)
    Success_D = (retention_rate_D * Achieve_rate_D)
    Success_E = (retention_rate_E * Achieve_rate_E)

    Average_Success_rate = ((Success_A + Success_B + Success_C + Success_D + Success_E) / 5) / 100
    Success_Average = ('%.1f' % (Average_Success_rate)) + "%"
    SuccessF.set(Success_Average)
#-------variable
StarterA = StringVar()
StarterB = StringVar()
StarterC = StringVar()
StarterD = StringVar()
StarterE = StringVar()

LeftA = StringVar()
LeftB = StringVar()
LeftC = StringVar()
LeftD = StringVar()
LeftE = StringVar()

StPA = StringVar()
StPB = StringVar()
StPC = StringVar()
StPD = StringVar()
StPE = StringVar()

RetentionA = StringVar()
RetentionB = StringVar()
RetentionC = StringVar()
RetentionD = StringVar()
RetentionE = StringVar()

AchievementA = StringVar()
AchievementB = StringVar()
AchievementC = StringVar()
AchievementD = StringVar()
AchievementE = StringVar()

SuccessA = StringVar()
SuccessB = StringVar()
SuccessC = StringVar()
SuccessD = StringVar()
SuccessE = StringVar()

RetentionF  = StringVar()
AchievmentF = StringVar()
SuccessF    = StringVar()

#---------------------
RetentionF  = StringVar()
AchievmentF = StringVar()
SuccessF    = StringVar()

toplevel = Frame(Success_Rate, width=1350, height=50, bd=8, relief="raise")
toplevel.pack(side=TOP)

bottomlevel = Frame(Success_Rate, width=1350, height=650, bd=8, relief="raise")
bottomlevel.pack(side=BOTTOM)

#------bottomlevel
tops = Frame(bottomlevel, width=1330, height=50, bd=8, relief="raise")
tops.pack(side=TOP)

bottom = Frame(bottomlevel, width=1330, height=650, bd=8, relief="raise")
bottom.pack(side=BOTTOM)

#------bottomlevel---toplevel
lblInfo = Label(toplevel, font=('arial', 52, 'bold'), text="Retention Achievement & Success Rate",
                fg='black', bd=8, anchor='w')
lblInfo.grid(row=0, column=0)
#------horizontally
lblGroup1 = Label(tops, font=('arial', 14, 'bold'), text=" Group ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroup1.grid(row=0, column=0)

lblGroup2 = Label(tops, font=('arial', 14, 'bold'), text=" Starter ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroup2.grid(row=0, column=1)

lblGroup3 = Label(tops, font=('arial', 14, 'bold'), text=" Left ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroup3.grid(row=0, column=2)

lblGroup4 = Label(tops, font=('arial', 14, 'bold'), text=" Student to Pass ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroup4.grid(row=0, column=3)

lblGroup5 = Label(tops, font=('arial', 14, 'bold'), text=" Retention ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroup5.grid(row=0, column=4)

lblGroup6 = Label(tops, font=('arial', 14, 'bold'), text=" Achievement ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroup6.grid(row=0, column=5)

lblGroup7 = Label(tops, font=('arial', 14, 'bold'), text=" Success",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroup7.grid(row=0, column=6)

#------vertical
lblGroupA = Label(tops, font=('arial', 14, 'bold'), text=" A ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroupA.grid(row=1, column=0)

lblGroupB = Label(tops, font=('arial', 14, 'bold'), text=" B ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroupB.grid(row=2, column=0)

lblGroupC = Label(tops, font=('arial', 14, 'bold'), text=" C ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroupC.grid(row=3, column=0)

lblGroupD = Label(tops, font=('arial', 14, 'bold'), text=" D ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroupD.grid(row=4, column=0)

lblGroupE = Label(tops, font=('arial', 14, 'bold'), text=" E ",
                fg='black', bd=20, relief="raise", width=12, justify="center")
lblGroupE.grid(row=5, column=0)

#------small rectangle
#------Starter
txtStarterA = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StarterA)
txtStarterA.grid(row=1, column=1)

txtStarterB = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StarterB)
txtStarterB.grid(row=2, column=1)

txtStarterC = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StarterC)
txtStarterC.grid(row=3, column=1)

txtStarterD = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StarterD)
txtStarterD.grid(row=4, column=1)

txtStarterE = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StarterE)
txtStarterE.grid(row=5, column=1)
#------Left
txtLeftA = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=LeftA)
txtLeftA.grid(row=1, column=2)

txtLeftB = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=LeftB)
txtLeftB.grid(row=2, column=2)

txtLeftC = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=LeftC)
txtLeftC.grid(row=3, column=2)

txtLeftD = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=LeftD)
txtLeftD.grid(row=4, column=2)

txtLeftE = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=LeftE)
txtLeftE.grid(row=5, column=2)
#------Student to Pass
txtStPA = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StPA)
txtStPA.grid(row=1, column=3)

txtStPB = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StPB)
txtStPB.grid(row=2, column=3)

txtStPC = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StPC)
txtStPC.grid(row=3, column=3)

txtStPD = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StPD)
txtStPD.grid(row=4, column=3)

txtStPE = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='white', width=12, justify="center",
                    textvariable=StPE)
txtStPE.grid(row=5, column=3)
#------Retention
txtRetentionA = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=RetentionA)
txtRetentionA.grid(row=1, column=4)

txtRetentionB = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=RetentionB)
txtRetentionB.grid(row=2, column=4)

txtRetentionC = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=RetentionC)
txtRetentionC.grid(row=3, column=4)

txtRetentionD = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=RetentionD)
txtRetentionD.grid(row=4, column=4)

txtRetentionE = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=RetentionE)
txtRetentionE.grid(row=5, column=4)
#------Achievement
txtAchievementA = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=AchievementA)
txtAchievementA.grid(row=1, column=5)

txtAchievementB = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=AchievementB)
txtAchievementB.grid(row=2, column=5)

txtAchievementC = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=AchievementC)
txtAchievementC.grid(row=3, column=5)

txtAchievementD = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=AchievementD)
txtAchievementD.grid(row=4, column=5)

txtAchievementE = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=AchievementE)
txtAchievementE.grid(row=5, column=5)
#------Success
txtSuccessA = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=SuccessA)
txtSuccessA.grid(row=1, column=6)

txtSuccessB = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=SuccessB)
txtSuccessB.grid(row=2, column=6)

txtSuccessC = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=SuccessC)
txtSuccessC.grid(row=3, column=6)

txtSuccessD = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=SuccessD)
txtSuccessD.grid(row=4, column=6)

txtSuccessE = Entry(tops, font=('arial', 14, 'bold'), bd=20, bg='powder blue', width=12, justify="center",
                    textvariable=SuccessE)
txtSuccessE.grid(row=5, column=6)

#-------Average
lblOverallAver = Label(tops, font=('arial', 14, 'bold'), text=" Overall Average: ",
                fg='black', bd=20, relief="flat", width=12, justify="center")
lblOverallAver.grid(row=6, column=3)

lblRetAverage = Entry(tops, font=('arial', 14, 'bold'),
                    bd = 20, width = 12, bg='powder blue', justify = "center", textvariable=RetentionF)
lblRetAverage.grid(row=6, column=4)

lblAchAverage = Entry(tops, font=('arial', 14, 'bold'),
                    bd = 20, width = 12, bg='powder blue', justify = "center", textvariable=AchievmentF)
lblAchAverage.grid(row=6, column=5)

lblSuccessAverage = Entry(tops, font=('arial', 14, 'bold'),
                    bd = 20, width = 12, bg='powder blue', justify = "center", textvariable=SuccessF)
lblSuccessAverage.grid(row=6, column=6)

#--------Button
btnWOverAllRAS = Button(bottom, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=12,
                        text="OverAll_RAS", command=OverRetention).grid(row=0, column=0)

btnRetention = Button(bottom, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=12,
                        text="Retention", command=Retention_Rate).grid(row=0, column=1)

btnAchievement = Button(bottom, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=12,
                        text="Achievement", command=Achievement_Rate).grid(row=0, column=2)

btnSuccess = Button(bottom, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=12,
                        text="Success", command=success_Rate).grid(row=0, column=3)

btnAverage = Button(bottom, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=12,
                        text="Average", command=Average).grid(row=0, column=4)

btnReset = Button(bottom, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=12,
                        text="Reset", command=reset).grid(row=0, column=5)

btnExit = Button(bottom, pady=8, bd=8, fg="black", font=('arial', 16, 'bold'), width=12,
                        text="Exit", command=exit).grid(row=0, column=6)
Success_Rate.mainloop()

