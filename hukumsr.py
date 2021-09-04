from tkinter import *
import time
import pyttsx3

b=0

Participants =["Player 1","Player 2","Player 3","Player 4"]

w=[0,0,0,0]
s=[0,0,0,0]
t=[0,0,0,0]
screen = Tk()

r=1

wr1= StringVar()
wr2= StringVar()
wr3= StringVar()
wr4= StringVar()


screen.title("HUKUM SAR")
screen.geometry("500x1000")

player1 = Label(text=Participants[0])
player1.place(x=60,y=20)
player2 = Label(text=Participants[1]).place(x=160,y=20)
player3 = Label(text=Participants[2]).place(x=260,y=20)
player4 = Label(text=Participants[3]).place(x=360,y=20)


def rank():
    global r
    max=-130*r
    maxi=-1
    for i in range(4):
        if t[i]>max:
            max=t[i]
            maxi=i
    rank2s=-130*r
    rank2=-1
    for i in range(4):
        if t[i]>rank2s and i!=maxi:
            rank2s=t[i]
            rank2=i
    rank3,rank4=-1,-1
    for i in range(4):
        if(i!=maxi and i!=rank2 and rank3==-1 ):
            rank3=i
        elif (i != maxi and i != rank2 and rank3 != -1):
            rank4 = i

    if(t[rank3]>t[rank4]):
        return maxi,rank2,rank3,rank4
    else:
        return maxi, rank2, rank4, rank3



def round(a):


    def enterd():

        def calc():

            def fin():
                screen.destroy()
                new=Tk()
                new.title("Result")
                new.geometry("500x250")
                fir,sec,thir,fourt=rank()
                Label(new,text="Winner is :"+Participants[fir]).place(x=50,y=50)
                Label(new, text="second is :" + Participants[sec]).place(x=50, y=100)
                Label(new, text="third is :" + Participants[thir]).place(x=50, y=150)

            s[0] = int(wr1.get())
            s[1] = int(wr2.get())
            s[2] = int(wr3.get())
            s[3] = int(wr4.get())

            wr1.set("")
            wr2.set("")
            wr3.set("")
            wr4.set("")
            global b
            global r
            b = 2
            print(b)
            for i in range(4):
                if s[i] == w[i]:
                    s[i] = w[i] * 10
                elif s[i] > w[i]:
                    s[i] = w[i] * 10 + (s[i] - w[i]) * 2
                elif s[i] < w[i]:
                    s[i] = -w[i] * 10
            for i in range(4):
                t[i] += s[i]
            player1w.destroy()
            player2w.destroy()
            player3w.destroy()
            player4w.destroy()
            scored.destroy()
            calculate.destroy()
            Label(text="round "+str(r)).place(x=5,y=a*20+50)
            Label(text=str(s[0])).place(x=60, y=a * 20 + 50)
            Label(text=str(s[1])).place(x=160, y=a * 20 + 50)
            Label(text=str(s[2])).place(x=260, y=a * 20 + 50)
            Label(text=str(s[3])).place(x=360, y=a * 20 + 50)
            b = 0
            Label(text="total").place(x=5, y=700)
            Label(text=str(t[0])).place(x=60, y=700)
            Label(text=str(t[1])).place(x=160, y=700)
            Label(text=str(t[2])).place(x=260, y=700)
            Label(text=str(t[3])).place(x=360, y=700)

            finish = Button(text="finish",command=fin)
            finish.place(x=220,y=740)
            r += 1
            round(r)

            return

        w[0] = int(wr1.get())
        w[1] = int(wr2.get())
        w[2] = int(wr3.get())
        w[3] = int(wr4.get())
        wr1.set("")
        wr2.set("")
        wr3.set("")
        wr4.set("")
        global b
        b = 1
        write.destroy()
        scored = Label(text="scored")
        scored.place(x=5, y=a * 20 + 50)
        click.destroy()
        calculate = Button(text='calculate', command=calc)
        calculate.place(x=450, y=a * 20 + 50)

        print(b)
        return

    write = Label(text="write")
    write.place(x=5,y=a*20+50)
    player1w = Entry(screen,textvariable = wr1, font=('calibre',10,'normal'))
    player1w.place(x=60,y=a*20+50)
    player2w = Entry(screen,textvariable = wr2, font=('calibre',10,'normal'))
    player2w.place(x=160,y=a*20+50)
    player3w = Entry(screen,textvariable = wr3, font=('calibre',10,'normal'))
    player3w.place(x=260,y=a*20+50)
    player4w = Entry(screen,textvariable = wr4, font=('calibre',10,'normal'))
    player4w.place(x=360,y=a*20+50)
    click = Button(text='enter',command=enterd)
    click.place(x=450,y=a*20+50)

    Label(text='application made by Rahul Guglani',).place(x=10,y=800)
round(1)
mainloop()
