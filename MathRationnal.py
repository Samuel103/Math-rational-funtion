import tkinter as tk


#app
app = tk.Tk()
app.geometry('800x600')
app.title('MathSec5')
###########################Find F(x)/Y/a/x rational##################################

#function
def findY():
    A = a.get()   
    X = x.get()
    H = h.get()
    K = k.get()
    answer = (float(A)/(float(X)-float(H)))+float(K)
    res.config(text=answer)
    
def findA():
    y = Y.get()
    X = x.get()
    H = h.get()
    K = k.get()
    answerA = (float(y)-float(K))*(float(X)-float(H))
    res.config(text=answerA)
   

#var a
tk.Label(app,text='a').grid(row=0)
a = tk.Entry(app)
a.grid(row=0,column=1)
#var y
tk.Label(app,text='y/F(x)').grid(row=1)
Y = tk.Entry(app)
Y.grid(row=1,column=1)
#var x
tk.Label(app,text='X').grid(row=2)
x = tk.Entry(app)
x.grid(row=2,column=1)
#var h
tk.Label(app,text='h').grid(row=3)
h = tk.Entry(app)
h.grid(row=3,column=1)
#var k
tk.Label(app,text='k').grid(row=4)
k = tk.Entry(app)
k.grid(row=4,column=1)
#Button
tk.Button(app, text='findF(x)', command=findY).grid(row=5,column=1) 
tk.Button(app,text='findA', command=findA).grid(row=6,column=1)
#label
res = tk.Label(app)
res.grid(row =7)




app.mainloop()