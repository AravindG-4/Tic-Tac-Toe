from tkinter import*

root = Tk()
root.geometry("500x500")
root.title("TIC TAC TOE")

frame1=Frame(root)
frame1.pack()

titlelabel1=Label(frame1,text="Tic Tac Toe" , font=30)
titlelabel1.pack()

frame2=Frame(root)
frame2.pack()

board = { 1:" " ,2:" " ,3:" ",
          4:" " ,5:" " ,6:" ", 
          7:" " ,8:" " ,9:" " }

turn="X"

#check for win

def win(player):
    if board[1]==board[2] and board[2]==board[3] and board[3]==player:
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[6]==player:
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[9]==player:
        return True
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player:
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[8]==player:
        return True
    elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
        return True
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player:
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
        return True

#click reaction

def onclick(event):
    global turn
    button=event.widget
    buttontxt=str(button)
    clicked=buttontxt[-1]

    if clicked=="n":
        clicked=1
    else:
        clicked=int(clicked)

    if not win(turn):
        if button["text"]==" ":
            if turn=="X":
                button["text"]="X"
                board[clicked] = turn
                if win(turn):
                  print(turn,"wins the game")
                  print("Game over!")
                else:
                  turn="O"
            else:
                button["text"]="O"
                board[clicked] = turn
                if win(turn):
                  print(turn,"wins the game")
                  print("Game over!")
                else:
                  turn="X"
        


#Tic Tac Toe board

#first row button

button1 = Button(frame2 , text=" " , width=4 , height=2 , font=("Arial",35) , bg="yellow")
button1.grid(row=0 , column=0)
button1.bind("<Button-1>",onclick)

button2 = Button(frame2 , text=" " , width=4 , height=2 , font=("Arial",35) , bg="yellow")
button2.grid(row=0 , column=1)
button2.bind("<Button-1>",onclick)

button3 = Button(frame2 , text=" " , width=4 , height=2 , font=("Arial",35) , bg="yellow")
button3.grid(row=0 , column=2)
button3.bind("<Button-1>",onclick)

#second row button

button4 = Button(frame2 , text=" " , width=4 , height=2 , font=("Arial",35) , bg="yellow")
button4.grid(row=1 , column=0)
button4.bind("<Button-1>",onclick)

button5 = Button(frame2 , text=" " , width=4 , height=2 , font=("Arial",35) , bg="yellow")
button5.grid(row=1 , column=1)
button5.bind("<Button-1>",onclick)

button6 = Button(frame2 , text=" " , width=4 , height=2 , font=("Arial",35) , bg="yellow")
button6.grid(row=1 , column=2)
button6.bind("<Button-1>",onclick)

#third row button

button7 = Button(frame2 , text=" " , width=4 , height=2 , font=("Arial",35) , bg="yellow")
button7.grid(row=2 , column=0)
button7.bind("<Button-1>",onclick)

button8 = Button(frame2 , text=" " , width=4 , height=2 , font=("Arial",35) , bg="yellow")
button8.grid(row=2 , column=1)
button8.bind("<Button-1>",onclick)

button9 = Button(frame2 , text=" " , width=4 , height=2 , font=("Arial",35) , bg="yellow")
button9.grid(row=2 , column=2)
button9.bind("<Button-1>",onclick)

root.mainloop()