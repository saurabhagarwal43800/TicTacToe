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

def board(mat_dict):

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
