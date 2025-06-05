import tkinter #tkinter is a built-in library in Python for creating GUI applictions


def set_tile(row, column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"]!="":
        return

    board[row][column]["text"]=curr_player #set the text of the button to the current player

    if curr_player==playerO:#swiitch player
        curr_player=playerX
    else:       
        curr_player=playerO
        label["text"]=curr_player+"'s turn" #if the current player is X

    #check_winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Horizontal check
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != "":
            label.config(text=board[row][0]["text"] + " wins!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    for column in range(3):
        # Vertical check
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != "":
            label.config(text=board[0][column]["text"] + " wins!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
        
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "":
        # Diagonal check (top-left to bottom-right)
        label.config(text=board[0][0]["text"] + " wins!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return    
    
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "":
        # Diagonal check (top-right to bottom-left)
        label.config(text=board[0][2]["text"] + " wins!", foreground=color_yellow)
        for i in range(3):
            board[i][2-i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    
    #tie check
    if turns == 9:
        label.config(text="It's a tie!", foreground=color_yellow)
        for row in range(3):
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
        game_over = True

def new_game():
    global turns, game_over
    turns = 0
    game_over = False
    label.config(text=curr_player+"'s turn", foreground="white")
    label["text"] = curr_player + "'s turn"

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray) #reset the text and colors of the buttons

#game setup
playerX="X"
playerO="O"
curr_player=playerX
board=[[0,0,0],
       [0,0,0],
       [0,0,0]] #3X3 board

#custom colors
color_blue="#4584b6"
color_yellow="#f7d74c"
color_gray="#d9d9d9"
color_light_gray="#f2f2f2"

turns=0
game_over=False

#window setup
window=tkinter.Tk() #create the game window
window.title("Tic Tac Toe") #set the title of the window
window.resizable(False,False) #make the window not resizable

frame=tkinter.Frame(window)
label=tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas",20),background=color_gray,
                    foreground="white") #create a frame for the window



label.grid(row=0,column=0,columnspan=3, sticky="we")#add the label to the frame
for row in range(3):
    for column in range(3):
        board[row][column]=tkinter.Button(frame, text="", font=("Consolas",50, "bold"),
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column)) #create a button for each tile in the board

        board[row][column].grid(row=row+1, column=column) #add the button to the frame

button=tkinter.Button(frame, text="Reset", font=("Consolas",20), background=color_gray,
                      foreground="white", command=new_game)   
button.grid(row=4,column=0, columnspan=3, sticky="we") #create a button to reset the game and add it to the frame
frame.pack()#add the frame to the window
window.update()
window_width=window.winfo_width() #get the width of the window
window_height=window.winfo_height() #get the height of the window
screen_width=window.winfo_screenwidth() #get the width of the screen
screen_height=window.winfo_screenheight() #get the height of the screen

#calculate the position of the window to center it on the screen
window_x=int(screen_width/2 - window_width/2) #calculate the x position of the window
window_y=int(screen_height/2 - window_height/2) #calculate the y position of the window

#format "(w)x(h)+(x)+(y)" to set the position of the window
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}") #set the size and position of the window
window.mainloop() #start the main loop of the window
