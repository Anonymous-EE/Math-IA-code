import matplotlib.pyplot as plt
import numpy as np
import statistics

#ONE IS LOSING BECAUSE OF THE OTHER. PROBLEM IN MATH_IA_UPDATED FILE CHECK TOP OF IT
class ValueFunction:
    def __init__(self, current_state, X_O):
        self.current_state=current_state
        self.X_O=X_O
        self.value = 0
        self.actionvalue = 0

    def win_or_not (self):
        current_state=self.current_state
        X_O=self.X_O
        win=False

        nums_horizontal=[]
        for i in range (0, len(current_state)):
            if i%3==0:
                nums_horizontal.append(i)

        nums_vertical=[0,1,2]

        if win==False:
            for i in nums_horizontal:
                if current_state[i]==X_O:
                    if current_state[i+1]==X_O:
                        if current_state[i+2]==X_O:
                            win=True

        if win==False:  
            for i in nums_vertical:
                if current_state[i]==X_O:
                    if current_state[i+3]==X_O:
                        if current_state[i+6]==X_O:
                            win=True

        if win==False:
            if current_state[0]==X_O:
                if current_state[4]==X_O:
                    if current_state[8]==X_O:
                        win=True
            if current_state[2]==X_O:
                if current_state[4]==X_O:
                    if current_state[6]==X_O:
                        win=True

        return win

    def get_all_next_moves (self):
        current_state=self.current_state
        X_O=self.X_O
        nums=[]
        for i in range (0, len(current_state)):
            nums.append(i)
        move1=[]
        copy_current_state=current_state.copy()
        if win_or_not(copy_current_state, 1)==False and win_or_not(copy_current_state, 2)==False:
            for i in nums:
                if copy_current_state[i]==0:
                    copy_current_state[i]=X_O
                    move1.append(copy_current_state)
                    copy_current_state=current_state.copy()
            return move1
        else:
            return []


def win_or_not (current_state, X_O):
    win=False

    nums_horizontal=[]
    for i in range (0, len(current_state)):
        if i%3==0:
            nums_horizontal.append(i)

    nums_vertical=[0,1,2]

    if win==False:
        for i in nums_horizontal:
            if current_state[i]==X_O:
                if current_state[i+1]==X_O:
                    if current_state[i+2]==X_O:
                        win=True

    if win==False:  
        for i in nums_vertical:
            if current_state[i]==X_O:
                if current_state[i+3]==X_O:
                    if current_state[i+6]==X_O:
                        win=True

    if win==False:
        if current_state[0]==X_O:
            if current_state[4]==X_O:
                if current_state[8]==X_O:
                    win=True
        if current_state[2]==X_O:
            if current_state[4]==X_O:
                if current_state[6]==X_O:
                    win=True

    return win

def get_all_next_moves (current_state, X_O):
    nums=[]
    for i in range (0, len(current_state)):
        nums.append(i)
    move1=[]
    copy_current_state=current_state.copy()
    if win_or_not(copy_current_state, 1)==False and win_or_not(copy_current_state,2)==False:
        for i in nums:
            if copy_current_state[i]==0:
                copy_current_state[i]=X_O
                move1.append(copy_current_state)
                copy_current_state=current_state.copy()
        return move1
    else:
        return []

def get_all_possible_states():
        list_done=[]
        all_lists=[]
        initial_board = [0,0,0,0,0,0,0,0,0]

        all_lists.append(initial_board)
        for k in range (0,9):
            if not get_all_next_moves (initial_board, 1)[k] in all_lists:
                all_lists.append(get_all_next_moves (initial_board, 1)[k])
        
        list_done.append(initial_board)
        for i in range (0, len(all_lists)):
            for k in range (0,8):
                if not all_lists[i] in list_done:
                    if win_or_not(all_lists[i],1)==False and win_or_not(all_lists[i],2)==False:
                        if not get_all_next_moves (all_lists[i], 2)[k] in all_lists:
                            all_lists.append(get_all_next_moves(all_lists[i],2)[k])
            list_done.append(all_lists[i])
        
        for i in range (0, len(all_lists)):
            for k in range (0,7):
                if not all_lists[i] in list_done:
                    if win_or_not(all_lists[i],1)==False and win_or_not(all_lists[i],2)==False:
                        if not get_all_next_moves(all_lists[i], 1)[k] in all_lists:
                            all_lists.append(get_all_next_moves(all_lists[i],1)[k])
            list_done.append(all_lists[i])
        
        for i in range (0, len(all_lists)):
            for k in range (0,6):
                if not all_lists[i] in list_done:
                    if win_or_not(all_lists[i],1)==False and win_or_not(all_lists[i],2)==False:
                        if not get_all_next_moves (all_lists[i], 2)[k] in all_lists:
                            all_lists.append(get_all_next_moves(all_lists[i],2)[k])
            list_done.append(all_lists[i])
        
        for i in range (0, len(all_lists)):
            for k in range (0,5):
                if not all_lists[i] in list_done:
                    if win_or_not(all_lists[i],1)==False and win_or_not(all_lists[i],2)==False:
                        if not get_all_next_moves(all_lists[i], 1)[k] in all_lists:
                            all_lists.append(get_all_next_moves(all_lists[i],1)[k])
            list_done.append(all_lists[i])

        for i in range (0, len(all_lists)):
            for k in range (0,4):
                if not all_lists[i] in list_done:
                    if win_or_not(all_lists[i],1)==False and win_or_not(all_lists[i],2)==False:
                        if not get_all_next_moves (all_lists[i], 2)[k] in all_lists:
                            all_lists.append(get_all_next_moves(all_lists[i],2)[k])
            list_done.append(all_lists[i])

        for i in range (0, len(all_lists)):
            for k in range (0,3):
                if not all_lists[i] in list_done:
                    if win_or_not(all_lists[i],1)==False and win_or_not(all_lists[i],2)==False:
                        if not get_all_next_moves(all_lists[i], 1)[k] in all_lists:
                            all_lists.append(get_all_next_moves(all_lists[i],1)[k])
            list_done.append(all_lists[i])

        for i in range (0, len(all_lists)):
            for k in range (0,2):
                if not all_lists[i] in list_done:
                    if win_or_not(all_lists[i],1)==False and win_or_not(all_lists[i],2)==False:
                        if not get_all_next_moves (all_lists[i], 2)[k] in all_lists:
                            all_lists.append(get_all_next_moves(all_lists[i],2)[k])
            list_done.append(all_lists[i])
        
        for i in range (0, len(all_lists)):
            for k in range (0,1):
                if not all_lists[i] in list_done:
                    if win_or_not(all_lists[i],1)==False and win_or_not(all_lists[i],2)==False:
                        if not get_all_next_moves(all_lists[i], 1)[k] in all_lists:
                            all_lists.append(get_all_next_moves(all_lists[i],1)[k])
            list_done.append(all_lists[i])

        return ((all_lists))

def getWhosTurn(state, reverse=False):

    numzero=0
    for i in range (0, len(state)):
        if state[i]==0:
            numzero+=1
    
    if numzero%2==1:
        if not reverse:
            return 1
        else:
            return 2
    else:
        if not reverse:
            return 2
        else:
            return 1

def is_draw (current_state):
    draw=False
    numzeroes=0
    for i in range (0, len(current_state)):
        if current_state[i]==0:
            numzeroes+=1
    if numzeroes==0:
        if win_or_not(current_state, 1)==False:
            if win_or_not(current_state, 2)==False:
                draw=True
    return draw

allStates = get_all_possible_states()

dictionary_X = {}
dictionary_O = {}
for state in allStates:
    dictionary_X[str(state)] = ValueFunction(state, getWhosTurn(state))
    dictionary_O[str(state)] = ValueFunction(state, getWhosTurn(state))

 

def update_value_function_X ():
    global dictionary_X
    for key, value in dictionary_X.items():
        actions = value.get_all_next_moves()
        if len(actions)>0:
            pi=1/len(actions)

            vnew=0
            for action in actions:
                if win_or_not(action, 1)==True:
                    Reward = +10
                    vnew+=(pi*Reward)
                elif win_or_not(action, 2)==True:
                    Reward = -10
                    vnew+=(pi*Reward)
                elif is_draw(action)==True:
                    Reward = 0
                    vnew+=(pi*Reward)
                else:
                    Reward = -1
                    
                    new_states = get_all_next_moves(action, getWhosTurn(action))
                    Pss = 1/len(new_states)

                    value_sum = 0
                
                    for state in new_states:
                        value_sum += dictionary_X[str(state)].value
                    alpha = (value_sum * Pss)+Reward
                    beta = pi * alpha
                    vnew += beta
            value.value=vnew
        
        else:
            vnew=0
            if win_or_not(value.current_state, 1)==True:
                    Reward = +10
                    vnew+=(Reward)
            elif win_or_not(value.current_state, 2)==True:
                    Reward = -10
                    vnew+=(Reward)
            elif is_draw(value.current_state)==True:
                    Reward = 0
                    vnew+=(Reward)
            value.value=vnew


def update_value_function_O ():
    global dictionary_O
    for key, value in dictionary_O.items():
        actions = value.get_all_next_moves()
        if len(actions)>0:
            pi=1/len(actions)

            vnew=0
            for action in actions:
                if win_or_not(action, 1)==True:
                    Reward = -10
                    vnew+=(pi*Reward)
                elif win_or_not(action, 2)==True:
                    Reward = +10
                    vnew+=(pi*Reward)
                elif is_draw(action)==True:
                    Reward = 0
                    vnew+=(pi*Reward)
                else:
                    Reward = -1
                    
                    new_states = get_all_next_moves(action, getWhosTurn(action))
                    Pss = 1/len(new_states)

                    value_sum = 0
                
                    for state in new_states:
                        value_sum += dictionary_O[str(state)].value
                    alpha = (value_sum * Pss)+Reward
                    beta = pi * alpha
                    vnew += beta
            value.value=vnew
        
        else:
            vnew=0
            if win_or_not(value.current_state, 1)==True:
                    Reward = -10
                    vnew+=(Reward)
            elif win_or_not(value.current_state, 2)==True:
                    Reward = +10
                    vnew+=(Reward)
            elif is_draw(value.current_state)==True:
                    Reward = 0
                    vnew+=(Reward)
            value.value=vnew


update_value_function_X()
update_value_function_X()
update_value_function_X()
update_value_function_X()
update_value_function_X()

update_value_function_O()
update_value_function_O()
update_value_function_O()
update_value_function_O()
update_value_function_O()

listofvaluesX=[]
listofstatesX=[]
for key, value in dictionary_X.items():
    listofvaluesX.append(value.value)
    listofstatesX.append(key)

listofvaluesO=[]
listofstatesO=[]
for key, value in dictionary_O.items():
    listofvaluesO.append(value.value)
    listofstatesO.append(key)



for n, i in enumerate(listofvaluesX):
    if i==-11:
        listofvaluesX[n]=-10

for k, j in enumerate(listofvaluesO):
    if j<-10:
        listofvaluesO[k]=-10


plt.boxplot([listofvaluesX, listofvaluesO], vert=False)
plt.show()

modeO= statistics.mode(listofvaluesO)
meanO = np.round(np.mean(listofvaluesO), 2)
medianO = np.round(np.median(listofvaluesO), 2)
min_valueO = np.round(min(listofvaluesO), 2)
max_valueO = np.round(max(listofvaluesO), 2)

quartile_1O = np.round(np.quantile(listofvaluesO, 0.25), 2)
quartile_3O = np.round(np.quantile(listofvaluesO, 0.75), 2)

iqrO = np.round(quartile_3O - quartile_1O, 2)


modeX= statistics.mode(listofvaluesX)
meanX = np.round(np.mean(listofvaluesX), 2)
medianX = np.round(np.median(listofvaluesX), 2)
min_valueX = np.round(min(listofvaluesX), 2)
max_valueX = np.round(max(listofvaluesX), 2)

quartile_1X = np.round(np.quantile(listofvaluesX, 0.25), 2)
quartile_3X = np.round(np.quantile(listofvaluesX, 0.75), 2)

iqrX = np.round(quartile_3X - quartile_1X, 2)

print('MinX: %s' % min_valueX)
print('MeanX: %s' % meanX)
print('ModeX: %s' % modeX)
print('MaxX: %s' % max_valueX)
print('25th percentileX: %s' % quartile_1X)
print('MedianX: %s' % medianX)
print('75th percentileX: %s' % quartile_3X)
print('Interquartile range (IQR)X: %s' % iqrX)

print ("ok now time for O values")

print('MinO: %s' % min_valueO)
print('MeanO: %s' % meanO)
print('ModeO: %s' % modeO)
print('MaxO: %s' % max_valueO)
print('25th percentileO: %s' % quartile_1O)
print('MedianO: %s' % medianO)
print('75th percentileO: %s' % quartile_3O)
print('Interquartile range (IQR)O: %s' % iqrO)





# def move_X_will_make(current_state):    
#     maxVal = -100000000000
#     move_ = None
#     next_moves=get_all_next_moves(current_state,getWhosTurn(current_state))
#     for move in next_moves:
#         valueofmove = dictionary_X[str(move)].value
#         if valueofmove > maxVal:
#             maxVal = valueofmove
#             move_ = move
#     return move_, dictionary_X[str(move_)].value

# def move_O_will_make(current_state):    
#     maxVal = -100000000000
#     move_ = None
#     next_moves=get_all_next_moves(current_state, getWhosTurn(current_state))
#     for move in next_moves:
#         valueofmove = dictionary_O[str(move)].value
#         if valueofmove > maxVal:
#             maxVal = valueofmove
#             move_ = move
#     return move_, dictionary_X[str(move_)].value


# def second_update_value_function_O():
#     global dictionary_O
#     for key, value in dictionary_O.items():
#         actions=value.get_all_next_moves()
#         if len(actions)>0:
#             policytochoose, valueofpolicytochoose = move_O_will_make(value.current_state)
        
#             pi=1
#             vnew=0
#             if win_or_not(policytochoose, 1)==True:
#                 Reward=-2
#                 vnew+=(pi*Reward)
#             elif win_or_not(policytochoose, 2)==True:
#                 Reward=0
#                 vnew+=(pi*Reward)
#             elif is_draw(policytochoose)==True:
#                 Reward=-0.5
#                 vnew+=Reward
#             else:
#                 Reward=-0.1

#                 Pss=1
#                 statereachedat, value_of_state_reached_at = move_X_will_make(policytochoose)
#                 alpha = (value_of_state_reached_at * Pss) + Reward
#                 beta = pi*alpha
#                 vnew+=beta

#             value.value=vnew
#         else:
#             vnew=0
#             if win_or_not(value.current_state, 1)==True:
#                     Reward = -2
#                     vnew+=(Reward)
#             elif win_or_not(value.current_state, 2)==True:
#                     Reward = 0
#                     vnew+=(Reward)
#             elif is_draw(value.current_state)==True:
#                     Reward = -0.5
#                     vnew+=(Reward)
#             value.value=vnew

            
# second_update_value_function_O()
# second_update_value_function_O()
# second_update_value_function_O()
# second_update_value_function_O()
# second_update_value_function_O()

# print (move_X_will_make([1,1,0,2,2,0,0,0,0]))


"""
tic tac toe board
[
  [x, -, -],
  [-, -, -],
  [-, -, -]
]
user_input -> something 1-9 
if they enter anything else: tell them too go again
check if the user_input is already taken
add it to the board
check if user won: checking rows, columns and diagonals
toggle between users upon succesful moves
# """

# board = [
#   [0, 0, 0],
#   [0, 0, 0],
#   [0, 0, 0]
# ]



# user = True # when true it refers to x, otherwise o
# turns = 0

# def print_board(board):
#   for row in board:
#     for slot in row:
#       print(f"{slot} ", end="")
#     print()

# def quit(user_input):
#   if user_input.lower() == "q": 
#     print("Thanks for playing")
#     return True
#   else: return False

# def check_input(user_input):
#   # check if its a number
#   if not isnum(user_input): return False
#   user_input = int(user_input)
#   # check if its 1 - 9
#   if not bounds(user_input): return False

#   return True

# def isnum(user_input):
#   if not user_input.isnumeric(): 
#     print("This is not a valid number")
#     return False
#   else: return True

# def bounds(user_input):
#   if user_input > 9 or user_input < 1: 
#     print("This is number is out of bounds")
#     return False
#   else: return True

# def istaken(coords, board):
#   row = coords[0]
#   col = coords[1]
#   if board[row][col] != 0:
#     print("This position is already taken.")
#     return True
#   else: return False

# def coordinates(user_input):
#   row = int(user_input / 3)
#   col = user_input
#   if col > 2: col = int(col % 3)
#   return (row,col)

# def add_to_board(coords, board, active_user):
#   row = coords[0]
#   col = coords[1]
#   board[row][col] = 2

# def current_user(user):
#   if user: return "o"
#   else: return "x"

# def iswin(user, board):
#   if check_row(user, board): return True
#   if check_col(user, board): return True
#   if check_diag(user, board): return True
#   return False

# def check_row(user, board):
#   for row in board:
#     complete_row = True
#     for slot in row:
#       if slot != user:
#         complete_row = False
#         break
#     if complete_row: return True
#   return False 

# def check_col(user, board):
#   for col in range(3):
#     complete_col = True
#     for row in range(3):
#       if board[row][col] != user:
#         complete_col = False
#         break
#     if complete_col: return True
#   return False

# def check_diag(user, board):
#   #top left to bottom right
#   if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
#   elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
#   else: return False


# #this is working except the game doesn't end when the player wins
# while turns < 9:
#     if turns%2==0:
#         print_board(board)
#         print ("OKKKKK")
#         values = []
#         #now it is x persons turn
#         stateofboard = [board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]]
#         nextmoves = get_all_next_moves(stateofboard,1)
#         for move in nextmoves:
#             valueofmove = dictionary_X[str(move)].value
#             values.append(valueofmove)
#         movetomake = max(values)
#         for move in nextmoves:
#             if dictionary_X[str(move)].value==movetomake:
#                 board[0][0]=move[0]
#                 board[0][1]=move[1]
#                 board[0][2]=move[2]
#                 board[1][0]=move[3]
#                 board[1][1]=move[4]
#                 board[1][2]=move[5]
#                 board[2][0]=move[6]
#                 board[2][1]=move[7]
#                 board[2][2]=move[8]
#             if win_or_not(move, 1)==True:
#                 print ("GAME OVER, I WIN L")
#                 break
#         turns+=1
    
#     else:
#         print_board(board)
#         print ("LOL OK")
#         values = []
#         #now it is x persons turn
#         stateofboard = [board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]]
#         nextmoves = get_all_next_moves(stateofboard,2)
#         for move in nextmoves:
#             valueofmove = dictionary_O[str(move)].value
#             values.append(valueofmove)
#         movetomake = max(values)
#         for move in nextmoves:
#             if dictionary_O[str(move)].value==movetomake:
#                 board[0][0]=move[0]
#                 board[0][1]=move[1]
#                 board[0][2]=move[2]
#                 board[1][0]=move[3]
#                 board[1][1]=move[4]
#                 board[1][2]=move[5]
#                 board[2][0]=move[6]
#                 board[2][1]=move[7]
#                 board[2][2]=move[8]
#             if win_or_not(move, 2)==True:
#                 print ("GAME OVER, I WIN L")
#                 break
#         turns+=1

#     if turns == 9: print("Tie!")
