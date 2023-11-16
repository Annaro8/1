from tkinter import*
from tkinter import messagebox 
mansLogs=Tk()
mansLogs.title("TicTacToe")

speletajsX= True 
count=0

def btnClick(button):    #padod visu pogu
    global speletajsX, count  #kādi mainīgie tiks izmantoti visā programā
    if button["text"]==""and speletajsX==True:   #Spēlē X spēlētājs
        button ["text"]="❤"   #maina uz X ❤ ♡
        speletajsX= False
        count+=1    #palielina rūtiņu skaitu
        checkWinner()
    elif button["text"]=='' and speletajsX==False:
       button["text"]='☆'
       speletajsX=True
       count+=1 
       checkWinner()
    else:
        messagebox.showerror('TicTacToe','Tā nedrīkst!!')
    return


def checkWinner():
    global checkWinner
    winner=False #ja  būs neizšķirts
    if(btn1["text"]=="❤" and btn2["text"]=="❤" and btn3["text"]=="❤" or btn4["text"]=="❤" and btn5["text"]=="❤" and btn6["text"]=="❤" or btn7["text"]=="❤" and btn8["text"]=="❤" and btn9["text"]=="❤" or btn1["text"]=="❤" and btn4["text"]=="❤" and btn7["text"]=="❤" or btn2["text"]=="❤" and btn5["text"]=="❤" and btn8["text"]=="❤" or btn3["text"]=="❤" and btn6["text"]=="❤" and btn9["text"]=="❤" or btn1["text"]=="❤" and btn5["text"]=="❤" and btn9["text"]=="❤" or btn3["text"]=="❤" and btn5["text"]=="❤" and btn7["text"]=="❤"):
        winner = True
        messagebox.showinfo("TicTacToe", "Speletajs ❤ ir uzvarētājs!!")
    elif(btn1["text"]=="☆" and btn2["text"]=="☆" and btn3["text"]=="☆" or btn4["text"]=="☆" and btn5["text"]=="☆" and btn6["text"]=="☆" or btn7["text"]=="☆" and btn8["text"]=="☆" and btn9["text"]=="☆" or btn1["text"]=="☆" and btn4["text"]=="☆" and btn7["text"]=="☆" or btn2["text"]=="☆" and btn5["text"]=="☆" and btn8["text"]=="☆" or btn3["text"]=="☆" and btn6["text"]=="☆" and btn9["text"]=="☆" or btn1["text"]=="☆" and btn5["text"]=="☆" and btn9["text"]=="☆" or btn3["text"]=="☆" and btn5["text"]=="☆" and btn7["text"]=="☆"):
        winner = True
        messagebox.showinfo("TicTacToe", "Spēlētājs ☆ ir uzvarētājs!!")
    elif count==9 and winner==False:
        messagebox.showinfo("TicTacToe", "Neizšķirts..")


btn1=Button(mansLogs, text="", width=6, height=3, font=('Helvica',24),command=lambda:btnClick(btn1))
btn2=Button(mansLogs, text="", width=6, height=3, font=('Helvica',24),command=lambda:btnClick(btn2))
btn3=Button(mansLogs, text="", width=6, height=3, font=('Helvica',24),command=lambda:btnClick(btn3))
btn4=Button(mansLogs, text="", width=6, height=3, font=('Helvica',24),command=lambda:btnClick(btn4))
btn5=Button(mansLogs, text="", width=6, height=3, font=('Helvica',24),command=lambda:btnClick(btn5))
btn6=Button(mansLogs, text="", width=6, height=3, font=('Helvica',24),command=lambda:btnClick(btn6))
btn7=Button(mansLogs, text="", width=6, height=3, font=('Helvica',24),command=lambda:btnClick(btn7))
btn8=Button(mansLogs, text="", width=6, height=3, font=('Helvica',24),command=lambda:btnClick(btn8))
btn9=Button(mansLogs, text="", width=6, height=3, font=('Helvica',24),command=lambda:btnClick(btn9))



btn1.grid(row=0, column=0)
btn2.grid(row=1, column=0)
btn3.grid(row=2, column=0)
btn4.grid(row=0, column=1)
btn5.grid(row=1, column=1)
btn6.grid(row=2, column=1)
btn7.grid(row=0, column=2)
btn8.grid(row=1, column=2)
btn9.grid(row=2, column=2)




mansLogs.mainloop()