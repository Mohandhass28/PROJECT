from tkinter import *

import Path_Search_Algo
import maze

gri = maze.maz
T = Tk()
def fun():
    for i in range(len(gri)):
        for j in range(len(gri[i])):
            Label(T, text=gri[i][j],padx=20,pady=20,font=20000).\
                grid(row=i,column=j)
fun()

def paceg():
    getpath = Path_Search_Algo.path().find_path(gri)
    fun()
    r,c = getpath.pop(0)
    Label(T, text='*',pady=20,padx=20,font=20000)\
            .grid(row=r,column=c)

def start_agin():
    fun()


button = Button(T,text='Next',padx=30,pady=2,command=paceg)\
    .grid(row=10,column=0,pady=10,padx=10,columnspan=9)


T.mainloop()