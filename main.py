#Default Board

def game():

    mat_dict={'a':"1",'b':"2",'c':"3",'d':"4",'e':"5",'f':"6",'g':"7",'h':"8",'i':"9"}
    print("     |     |     ")
    print(f"  {mat_dict['a']}  |  {mat_dict['b']}  |  {mat_dict['c']}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {mat_dict['d']}  |  {mat_dict['e']}  |  {mat_dict['f']}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {mat_dict['g']}  |  {mat_dict['h']}  |  {mat_dict['i']}  ")
    print("     |     |     ")
    
#Replacing the value of board

from IPython.display import clear_output
def board(mat_dict):
    #mat_dict={'a':" ",'b':" ",'c':" ",'d':" ",'e':" ",'f':" ",'g':" ",'h':" ",'i':" "}
    clear_output()
    print("     |     |     ")
    print(f"  {mat_dict['a']}  |  {mat_dict['b']}  |  {mat_dict['c']}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {mat_dict['d']}  |  {mat_dict['e']}  |  {mat_dict['f']}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {mat_dict['g']}  |  {mat_dict['h']}  |  {mat_dict['i']}  ")
    print("     |     |     ")
    #return "     |     |     \n"+f"  {mat_dict['a']}  |  {mat_dict['b']}  |  {mat_dict['c']}  \n"+"     |     |     \n"+"-----------------\n"+"     |     |     \n"+f"  {mat_dict['d']}  |  {mat_dict['e']}  |  {mat_dict['f']}  \n"+"     |     |     \n"+"-----------------\n"+"     |     |     \n"+f"  {mat_dict['g']}  |  {mat_dict['h']}  |  {mat_dict['i']}  \n"+"     |     |     \n"
    
#To replace the position of matrix with 'X' for player1

def replace_p1(pos,mat_dict):

    if pos=="1":
        mat_dict['a']="X"

    elif pos=="2":
        mat_dict['b']="X"

    elif pos=="3":
        mat_dict['c']="X"

    elif pos=="4":
        mat_dict['d']="X"

    elif pos=="5":
        mat_dict['e']="X"

    elif pos=="6":
        mat_dict['f']="X"

    elif pos=="7":
        mat_dict['g']="X"

    elif pos=="8":
        mat_dict['h']="X"

    elif pos=="9":
        mat_dict['i']="X"

#To replace the position of matrix with 'O' for player2

def replace_p2(pos,mat_dict):

    if pos=='1':
        mat_dict['a']="O"

    elif pos=='2':
        mat_dict['b']="O"

    elif pos=='3':
        mat_dict['c']="O"

    elif pos=='4':
        mat_dict['d']="O"

    elif pos=='5':
        mat_dict['e']="O"

    elif pos=='6':
        mat_dict['f']="O"

    elif pos=='7':
        mat_dict['g']="O"

    elif pos=='8':
        mat_dict['h']="O"

    elif pos=='9':
        mat_dict['i']="O"
        
#To check the result and exit if any player won!

def check_win(mat_dict):
    if (mat_dict['a']=='X' and mat_dict['b']=='X' and mat_dict['c']=='X') or (mat_dict['d']=='X' and mat_dict['e']=='X' and mat_dict['f']=='X') or (mat_dict['g']=='X' and mat_dict['h']=='X' and mat_dict['i']=='X'):
        return "Congratulations Player1 Won!"
    elif (mat_dict['a']=='X' and mat_dict['d']=='X' and mat_dict['g']=='X') or (mat_dict['b']=='X' and mat_dict['e']=='X' and mat_dict['h']=='X') or (mat_dict['c']=='X' and mat_dict['f']=='X' and mat_dict['i']=='X'):
        return "Congratulations Player1 Won!"
    elif (mat_dict['a']=='X' and mat_dict['e']=='X' and mat_dict['i']=='X') or (mat_dict['c']=='X' and mat_dict['e']=='X' and mat_dict['g']=='X'):
        return "Congratulations Player1 Won!"
    if (mat_dict['a']=='O' and mat_dict['b']=='O' and mat_dict['c']=='O') or (mat_dict['d']=='O' and mat_dict['e']=='O' and mat_dict['f']=='O') or (mat_dict['g']=='O' and mat_dict['h']=='O' and mat_dict['i']=='O'):
        return "Congratulations Player2 Won!"
    elif (mat_dict['a']=='O' and mat_dict['d']=='O' and mat_dict['g']=='O') or (mat_dict['b']=='O' and mat_dict['e']=='O' and mat_dict['h']=='O') or (mat_dict['c']=='O' and mat_dict['f']=='O' and mat_dict['i']=='O'):
        return "Congratulations Player2 Won!"
    elif (mat_dict['a']=='O' and mat_dict['e']=='O' and mat_dict['i']=='O') or (mat_dict['c']=='O' and mat_dict['e']=='O' and mat_dict['g']=='O'):
        return "Congratulations Player2 Won!"
    elif mat_dict['a']!=" " and mat_dict['b']!=" " and mat_dict['c']!=" " and mat_dict['d']!=" " and mat_dict['e']!=" " and mat_dict['f']!=" " and mat_dict['g']!=" " and mat_dict['h']!=" " and mat_dict['i']!=" ":
        return "There is a Tie!"
 
#If player1 get a first chance to start the game
          
def chance_p1():
    mat_dict={'a':" ",'b':" ",'c':" ",'d':" ",'e':" ",'f':" ",'g':" ",'h':" ",'i':" "}
    check_list=[]
    game()
    i=1
    while(i!=0):
        if i%2!=0:
            #Player1 chance
            pos=input("Press the number Player1 to make a move")
            pos=int(pos)
            if pos>=1 and pos<=9:
                if pos not in check_list:
                    check_list.append(pos)
                    replace_p1(str(pos),mat_dict)
                    i+=1
                else:
                    print("You cannot make the move at the reserved location")
            
            else:
                print("Invalid Choice")
                
        else:
            #Player2 chance
            #os.system('clear')
            pos=input("Press the number Player2 to make a move:")
            pos=int(pos)
            if pos>=1 and pos<=9:
                if pos not in check_list:
                    check_list.append(pos)
                    replace_p2(str(pos),mat_dict)
                    i+=1
                else:
                    print("You cannot make the move at the reserved location")
            
            else:
                print("Invalid Choice")
                
        board(mat_dict)
        win=check_win(mat_dict)
        if win=="Congratulations Player1 Won!" or win=="Congratulations Player2 Won!" or win=="There is a Tie!":
            print(win)
            break
        else:
            continue 
          
#If player2 get a first chance to start the game
          
def chance_p2():
    mat_dict={'a':" ",'b':" ",'c':" ",'d':" ",'e':" ",'f':" ",'g':" ",'h':" ",'i':" "}
    check_list=[]
    game()
    i=1
    while(i!=0):
        if i%2==0:
            #os.system('clear')
            #Player1 chance
            pos=input("Press the number Player1 to make a move")
            pos=int(pos)
            if pos>=1 and pos<=9:
                if pos not in check_list:
                    check_list.append(pos)
                    replace_p1(str(pos),mat_dict)
                    i+=1
                else:
                    print("You cannot make the move at the reserved location")
            
            else:
                print("Invalid Choice")
                
        else:
            #Player2 chance
            pos=input("Press the number Player2 to make a move:")
            pos=int(pos)
            if pos>=1 and pos<=9:
                if pos not in check_list:
                    check_list.append(pos)
                    replace_p2(str(pos),mat_dict)
                    i+=1
                else:
                    print("You cannot make the move at the reserved location")
            
            else:
                print("Invalid Choice")
                
        board(mat_dict)
        win=check_win(mat_dict)
        if win=="Congratulations Player1 Won!" or win=="Congratulations Player2 Won!" or win=="There is a Tie!":
            print(win)
            break
        else:
            continue 
          
#Ask players that he wants to be player1 or player2 and if he chooses any other choice then it will show invalid choice

def assign_player():  
    pl=input("Press 1 for Player1 or Press 2 for Player2:")
    if pl=="1":
        return "Now you are Player1"
    elif pl=="2":
        return "Now you are Player2"
    else:
        print("Invalid Choice")
        return assign_player()

#Ask player if he wants to play the game or not. If yes then continue the game and if no then exit       

def choice():
    print("---------------WELCOME TO TIC TAC TOE---------------")
    print("Do you want to play the Game?")
    ch=input("yes or no:\n")
    if ch!="yes" and ch!="no" and ch!="Yes" and ch!="No" and ch!="YES" and ch!="NO":
        print("Invalid input")
        choice()
    else:
        if ch=="Yes" or ch=="yes" or ch=="YES":
            print("Choose the player number")
            s=assign_player()
            print(s)
            if s=="Now you are Player1":
                chance_p1()
            else:
                chance_p2()
            choice()
        elif ch=="No" or ch=="no" or ch=="NO":
            print("Have a good day!")
        else:
            print("Thank you for playing")
          
choice()
    
    

