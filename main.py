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
    #mat_dict={'a':" ",'b':" ",'c':" ",'d':" ",'e':" ",'f':" ",'g':" ",'h':" ",'i':" "}
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
