from tkinter import *
import os
     
creds = 'tempfile.temp'

#signup tab----------------------

def Signup():
	global pwordE
	global nameE
	global roots

	roots = Tk()
	roots.title('Signup')
	instruction = Label(roots, text='Please Enter new Credentials').grid(row=0, column=0, sticky=E)

	nameL = Label(roots, text='New Username: ').grid(row=1, column=0, sticky=W)
	pwordL = Label(roots,text='New Password: ').grid(row=2, column=0, sticky=W)

	nameE = Entry(roots)
	pwordE = Entry(roots, show='*')
	nameE.grid(row=1, column=1)
	pwordE.grid(row=2, column=1)

	signupButton = Button(roots, text='Signup', command=FSSignup)
	signupButton.grid(columnspan=2, sticky=W)
	roots.mainloop()

def FSSignup():
	with open(creds, 'w') as f:
		f.write(nameE.get())	
		f.write('\n')
		f.write(pwordE.get())
		f.close()

	roots.destroy()
	Login()


def Login():
	global nameEL
	global pwordEL
	global rootA

	rootA = Tk()
	rootA.title('Login')

	instruction = Label(rootA, text='Please Login\n')
	instruction.grid(sticky=E)

	nameL = Label(rootA, text='Username: ')
	pwordL = Label(rootA, text='Password: ')
	nameL.grid(row=1, sticky=W)
	pwordL.grid(row=2, sticky=W)

	nameEL = Entry(rootA)
	pwordEL = Entry(rootA, show='*')
	nameEL.grid(row=1, column=1)
	pwordEL.grid(row=2, column=1)

	loginB = Button(rootA, text='Login', command=CheckLogin)
	loginB.grid(columnspan=2, sticky=W)

	rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser)
	rmuser.grid(columnspan=2, sticky=W)
	rootA.mainloop()

def CheckLogin():
	with open(creds) as f:
		data = f.readlines()
		uname = data[0].rstrip()
		pword = data[1].rstrip()

	if nameEL.get() == uname and pwordEL.get() == pword:
		r = Tk()
		r.title(':D')
		r.geometry('150x50')
		rlbl = Label(r, text='\n[+] Logged In')
		rlbl.pack()
		r.mainloop()
	else:
		r = Tk()	
		r.title('D:')
		r.geometry('150x50')
		rlbl = Label(r, text='\n[! Invalid Login')
		rlbl.pack()
		r.mainloop()	

def DelUser():
	os.remove(creds)
	rootA.destroy()
	Signup()

if os.path.isfile(creds):
	Login()
else:
	Signup()

import time
time.sleep(2)

#--------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import collections
import heapq
from tkinter import  *
import tkinter
from PIL import ImageTk, Image
from sklearn.linear_model import LinearRegression



root3=Tk()

root3.title("welcome")

label=Label(root3,text="welcome to Cathay Pacific").grid(row=0, column=0)
label=Label(root3,text="please enter the day and month of travel in the terminal").grid(row=1, column=0)
root3.mainloop()


dataset=pd.read_csv("dsc.csv")
input1=-1
while(input1<0 or input1>7):
        print("enter the day of week of travel(1-7)")
        input1=int(input())
input2=-1
while(input2<0 or input2>30):
        print("enter the day of month of travel(1-30)")
        input2=int(input())

testa=np.array([[int(input1),int(input2)]])#test case sample to be asked from user
dataset=dataset.fillna(1000)

regressora=LinearRegression()
j=0;
n=0
count=0
a=[["A","B",0],["B","C",0],["A","D",0],["D","C",0],["A","E",0],["E","C",0],["B","A",0],["D","A",0],["E","A",0]
,["C","D",0],["C","E",0],["C","B",0]]
for k in range(0,3):#number of edges of starting node
    for i in range(0,4):#number of straight edges connecting nodes
        
        traina=dataset.loc[j:j+10000,['DAY_OF_WEEK','DAY_OF_MONTH']]#x matrix gets updated every node
        
        #d=dataset.loc[0:10,['ARR_TIME']]

        ##d=pd.to_datetime(d);

        trainb=dataset.loc[j:j+10000,['ARR_TIME']];#Y matrix
        regressora.fit(traina,trainb)
        

        d=regressora.predict(testa);
        a[n][2]=float(d)
        n=n+1
        print(d)
        j=j+10
    
    print("new node")
print(a)



def incalc(a, source, sink):
    global count
    count=1
    # create a weighted DAG - {node:[(cost,neighbour), ...]}
    graph = collections.defaultdict(list)
    for l, r, c in a:
        graph[l].append((c,r))
    # create a priority queue and hash set to store visited nodes
    queue, visited = [(0, source, [])], set()
    heapq.heapify(queue)
    # traverse graph with BFS
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        # visit the node if it was not visited before
        if node not in visited:
            visited.add(node)
            path = path + [node]
            # hit the sink
            if node == sink:
                return (cost,path)
            # visit neighbours
            for c, neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(queue, (cost+c, neighbour, path))
    return float("inf")
root=Tk()
i=0
A=[100,100]
B=[500,100]
C=[100,500]
E=[250,250]
D=[500,500]
val=["A","A"]   
def onclicklistner1():
    global i
    val[i]="A"
    i=i+1
    print(i)
    if(i>1):
       cost,c=incalc(a,val[0],val[1])
       canvas.create_text(950,550,fill="white",font="Times 20 italic bold",text=str(round(float(cost/1000),2))+"hrs")
       canvas.update
       print(cost/1000)
       for i in range(0,len(c)-1):
           print(len(c))
           print(c[i])
           if(c[i]=="A" and c[i+1]=="B"):
               canvas.create_line(A,B,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="C"):
               canvas.create_line(A,C,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="D"):
               canvas.create_line(A,D,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="E"):
               canvas.create_line(A,E,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="A"):
               canvas.create_line(B,A,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="C"):
               canvas.create_line(B,C,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="D"):
               canvas.create_line(B,D,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="E"):
               canvas.create_line(B,E,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="A"):
               canvas.create_line(C,A,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="B"):
               canvas.create_line(C,B,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="D"):
               canvas.create_line(C,D,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="E"):
               canvas.create_line(C,E,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="A"):
               canvas.create_line(D,A,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="B"):
               canvas.create_line(D,B,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="C"):
               canvas.create_line(D,C,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="E"):
               canvas.create_line(D,E,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="A"):
               canvas.create_line(E,A,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="B"):
               canvas.create_line(E,B,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="C"):
               canvas.create_line(E,C,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="D"):
               canvas.create_line(E,D,width=4,fill="red")
           i=i+10

       print(c)



def onclicklistner2():
    global i
    global c
    val[i]="B"
    i=i+1
    print("this is a button")
    if(i>1):
       cost,c=incalc(a,val[0],val[1])
       canvas.create_text(950,550,fill="white",font="Times 20 italic bold",text=str(round(float(cost/1000),2))+"hrs")
       canvas.update
       print(cost/1000)
       for i in range(0,len(c)-1):
           print(len(c))
           print(c[i])
           if(c[i]=="A" and c[i+1]=="B"):
               canvas.create_line(A,B,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="C"):
               canvas.create_line(A,C,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="D"):
               canvas.create_line(A,D,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="E"):
               canvas.create_line(A,E,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="A"):
               canvas.create_line(B,A,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="C"):
               canvas.create_line(B,C,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="D"):
               canvas.create_line(B,D,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="E"):
               canvas.create_line(B,E,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="A"):
               canvas.create_line(C,A,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="B"):
               canvas.create_line(C,B,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="D"):
               canvas.create_line(C,D,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="E"):
               canvas.create_line(C,E,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="A"):
               canvas.create_line(D,A,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="B"):
               canvas.create_line(D,B,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="C"):
               canvas.create_line(D,C,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="E"):
               canvas.create_line(D,E,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="A"):
               canvas.create_line(E,A,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="B"):
               canvas.create_line(E,B,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="C"):
               canvas.create_line(E,C,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="D"):
               canvas.create_line(E,D,width=4,fill="red")
           i=i+10

       print(c)




def onclicklistner3():
    global i
    global c
    val[i]="C"
    i=i+1
    print("this is a button")
    if(i>1):
       cost,c=incalc(a,val[0],val[1])
       canvas.create_text(950,550,fill="white",font="Times 20 italic bold",text=str(round(float(cost/1000),2))+"hrs")
       canvas.update
       print(cost/1000)
       for i in range(0,len(c)-1):
           print(len(c))
           print(c[i])
           if(c[i]=="A" and c[i+1]=="B"):
               canvas.create_line(A,B,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="C"):
               canvas.create_line(A,C,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="D"):
               canvas.create_line(A,D,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="E"):
               canvas.create_line(A,E,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="A"):
               canvas.create_line(B,A,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="C"):
               canvas.create_line(B,C,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="D"):
               canvas.create_line(B,D,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="E"):
               canvas.create_line(B,E,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="A"):
               canvas.create_line(C,A,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="B"):
               canvas.create_line(C,B,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="D"):
               canvas.create_line(C,D,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="E"):
               canvas.create_line(C,E,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="A"):
               canvas.create_line(D,A,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="B"):
               canvas.create_line(D,B,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="C"):
               canvas.create_line(D,C,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="E"):
               canvas.create_line(D,E,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="A"):
               canvas.create_line(E,A,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="B"):
               canvas.create_line(E,B,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="C"):
               canvas.create_line(E,C,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="D"):
               canvas.create_line(E,D,width=4,fill="red")
           i=i+10

    
       print(c)




def onclicklistner4():
    global i
    global c
    val[i]="D"
    i=i+1
    print("this is a button")
    if(i>1):
       cost,c=incalc(a,val[0],val[1])
       canvas.create_text(950,550,fill="white",font="Times 20 italic bold",text=str(round(float(cost/1000),2))+"hrs")
       canvas.update
       print(cost/1000)
       for i in range(0,len(c)-1):
           print(len(c))
           print(c[i])
           if(c[i]=="A" and c[i+1]=="B"):
               canvas.create_line(A,B,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="C"):
               canvas.create_line(A,C,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="D"):
               canvas.create_line(A,D,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="E"):
               canvas.create_line(A,E,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="A"):
               canvas.create_line(B,A,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="C"):
               canvas.create_line(B,C,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="D"):
               canvas.create_line(B,D,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="E"):
               canvas.create_line(B,E,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="A"):
               canvas.create_line(C,A,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="B"):
               canvas.create_line(C,B,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="D"):
               canvas.create_line(C,D,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="E"):
               canvas.create_line(C,E,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="A"):
               canvas.create_line(D,A,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="B"):
               canvas.create_line(D,B,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="C"):
               canvas.create_line(D,C,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="E"):
               canvas.create_line(D,E,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="A"):
               canvas.create_line(E,A,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="B"):
               canvas.create_line(E,B,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="C"):
               canvas.create_line(E,C,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="D"):
               canvas.create_line(E,D,width=4,fill="red")
           i=i+10
       print(c)



def onclicklistner5():
    global i
    global c
    val[i]="E"
    i=i+1
    print("this is a button")
    if(i>1):
       cost,c=incalc(a,val[0],val[1])
       canvas.create_text(950,550,fill="white",font="Times 20 italic bold",text=str(round(float(cost/1000),2))+"hrs")
       canvas.update
       print(cost)
       for i in range(0,len(c)-1):
           print(len(c))
           print(c[i])
           if(c[i]=="A" and c[i+1]=="B"):
               canvas.create_line(A,B,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="C"):
               canvas.create_line(A,C,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="D"):
               canvas.create_line(A,D,width=4,fill="red")
           if(c[i]=="A" and c[i+1]=="E"):
               canvas.create_line(A,E,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="A"):
               canvas.create_line(B,A,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="C"):
               canvas.create_line(B,C,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="D"):
               canvas.create_line(B,D,width=4,fill="red")
           if(c[i]=="B" and c[i+1]=="E"):
               canvas.create_line(B,E,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="A"):
               canvas.create_line(C,A,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="B"):
               canvas.create_line(C,B,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="D"):
               canvas.create_line(C,D,width=4,fill="red")
           if(c[i]=="C" and c[i+1]=="E"):
               canvas.create_line(C,E,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="A"):
               canvas.create_line(D,A,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="B"):
               canvas.create_line(D,B,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="C"):
               canvas.create_line(D,C,width=4,fill="red")
           if(c[i]=="D" and c[i+1]=="E"):
               canvas.create_line(D,E,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="A"):
               canvas.create_line(E,A,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="B"):
               canvas.create_line(E,B,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="C"):
               canvas.create_line(E,C,width=4,fill="red")
           if(c[i]=="E" and c[i+1]=="D"):
               canvas.create_line(E,D,width=4,fill="red")
           i=i+10

    
       print(c)
def onclicklistner6():
    root.destroy()
  
imgpath = 'world-map.jpg'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img,width=1000,height=1000)
canvas = tkinter.Canvas(root,width=1000,height=1000)
canvas.pack()

canvas.create_image(500, 200, image=photo)
button1=tkinter.Button(canvas,text='Airport 1',command=onclicklistner1)
canvas.create_window(100, 100, width=100, height=25,window=button1)
button2=tkinter.Button(canvas,text='Airport 2',command=onclicklistner2)
canvas.create_window(500, 100, width=100, height=25,window=button2)
button3=tkinter.Button(canvas,text='Airport 3',command=onclicklistner3)
canvas.create_window(100, 500, width=100, height=25,window=button3)
button4=tkinter.Button(canvas,text='Airport 4',command=onclicklistner4)
canvas.create_window(500, 500, width=100, height=25,window=button4)
button5=tkinter.Button(canvas,text='Airport 5',command=onclicklistner5)
canvas.create_window(250,250, width=100, height=25,window=button5)
button6=tkinter.Button(canvas,text='exit',command=onclicklistner6)
canvas.create_window(550,250, width=100, height=25,window=button6)

root.mainloop()
root2=Tk()




root2.title("thank you")
label=Label(root2,text="thank you").grid(row=1, column=0)
root2.mainloop()
