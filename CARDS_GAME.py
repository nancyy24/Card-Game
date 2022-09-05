#functions used play1(),play2(),play3(),play4(),win()
import random
# for NOW THE PLAYER1 WILL SELECT ITS OWN CARD
def play1():
    global player1
    global chosen_card
    global max_card
    global chosen_card_list
    global playerflag
    print("PLAYER1 TURN")
    if playerflag[0]==1:
        print("DISPLAY THE PLAYER 1 CARDS",player1)
        print("SELECT ONE OF THE CARD")
        x=input("ENTER THE SUIT OF CARD ::")
        y=input("ENTER THE VALUE OF CARD ::")
        list_for_palyer1.append(x)
        list_for_palyer1.append(y)
        list_player1_tuple=tuple(list_for_palyer1)
        chosen_card=list_player1_tuple
        max_card=list_player1_tuple
        print("THE CHOSEN CARD FOR PLAYER1 ::",chosen_card)
        chosen_card_list["player1"]=chosen_card
        player1.remove(list_player1_tuple)
    elif playerflag[0]==0:
        print("DISPLAY THE PLAYER1 CARDS",player1)
        print("SELECT ONE OF THE CARD")
        x=input("ENTER THE SUIT OF CARD ::")
        y=input("ENTER THE VALUE OF CARD :: ")
        list_for_palyer1.append(x)
        list_for_palyer1.append(y)
        list_player1_tuple=tuple(list_for_palyer1)
        chosen_card=list_player1_tuple
        print("PLAYER1 CHOSEN CARD",chosen_card)
        chosen_card_list["player1"]=chosen_card
        #finding the maximum card
        if chosen_card[0] == max_card[0] and card_weight[chosen_card[1]] > card_weight[max_card[1]]:
            max_card=chosen_card
        elif chosen_card[0] == max_card[0] and card_weight[chosen_card[1]] < card_weight[max_card[1]]:
            max_card=max_card
        elif chosen_card[0] != max_card[0]:
            max_card=max_card
        player1.remove(list_player1_tuple)
        
    return


def play2():
    global player2
    global chosen_card
    global max_card
    global chosen_card_list
    global same_suit
    global diff_suit
    global card_weight
    global playerflag
    print("PLAYER2 TURN") 
    if playerflag[1]==1:
        #for NOW WE WILL FIND FROM THE MAXIMUM WEIGHTED CARD:
        player2.sort(key= lambda y:card_weight[y[1]])
        chosen_card=player2[-1]
        max_card=player2[-1]
        player2.pop(-1)
        print("CHOSEN CARD FOR PLAYER2 ::",chosen_card)
        chosen_card_list["player2"]=chosen_card
    else:
        for i in player2:
            if i[0]==max_card[0]:
                same_suit.append(i)
            else:
                diff_suit.append(i)
        if len(same_suit)>0:
        #sorting will take place
            same_suit.sort(key= lambda y:card_weight[y[1]])
            if card_weight[same_suit[-1][1]] > card_weight[max_card[1]]:
                chosen_card=same_suit[-1]
                max_choice=1
            else:
                chosen_card=same_suit[0]
                max_choice=2
        else:
            diff_suit.sort(key = lambda y :card_weight[y[1]])
            chosen_card=diff_suit[0]
            max_choice=3
        print("CHOSEN CARD FOR PLAYER2",chosen_card)
        chosen_card_list["player2"]=chosen_card
        player2.remove(chosen_card)
        if max_choice==1:
            max_card=chosen_card
        elif max_choice ==2:
            max_card=max_card
        elif max_choice==3:
            max_card=max_card
        same_suit=[]
        diff_suit=[]
    return 


def play3():
    global player3
    global chosen_card
    global max_card
    global chosen_card_list
    global same_suit
    global diff_suit
    global card_weight
    global playerflag
    print("PLAYER3 TURN")
    if playerflag[2]==1:
        #for NOW WE WILL FIND FROM THE MAXIMUM WEIGHTED CARD:
        player3.sort(key= lambda y:card_weight[y[1]])
        chosen_card=player3[-1]
        max_card=player3[-1]
        player3.pop(-1)
        print("CHOSEN CARD FOR PLAYER3",chosen_card)
        chosen_card_list["player3"]=chosen_card
    else:
        for i in player3:
            if i[0]==max_card[0]:
                same_suit.append(i)
            else:
                diff_suit.append(i)
        if len(same_suit)>0:
        #sorting will take place
            same_suit.sort(key= lambda y:card_weight[y[1]])
            if card_weight[same_suit[-1][1]] > card_weight[max_card[1]]:
                chosen_card=same_suit[-1]
                max_choice=1
            else:
                chosen_card=same_suit[0]
                max_choice=2
        else:
            diff_suit.sort(key = lambda y :card_weight[y[1]])
            chosen_card=diff_suit[0]
            max_choice=3
        print("CHOSEN CARD FOR PLAYER3",chosen_card)
        chosen_card_list["player3"]=chosen_card
        player3.remove(chosen_card)
        if max_choice==1:
            max_card=chosen_card
        elif max_choice ==2:
            max_card=max_card
        elif max_choice==3:
            max_card=max_card
        same_suit=[]
        diff_suit=[]
    return 


def play4():
    global player4
    global chosen_card
    global chosen_card_list
    global card_weight
    global max_card
    global same_suit
    global diff_suit
    global playerflag
    print("PLAYER4 TURN")
    if playerflag[3]==1:
        #for NOW WE WILL FIND FROM THE MAXIMUM WEIGHTED CARD:
        player4.sort(key= lambda y:card_weight[y[1]])
        chosen_card=player4[-1]
        max_card=player4[-1]
        player4.pop(-1)
        print("CHOSEN CARD FOR PLAYER4",chosen_card)
        chosen_card_list["player4"]=chosen_card
    else:
        for i in player4:
            if i[0]==max_card[0]:
                same_suit.append(i)
            else:
                diff_suit.append(i)
        if len(same_suit)>0:
        #sorting will take place
            same_suit.sort(key= lambda y:card_weight[y[1]])
            if card_weight[same_suit[-1][1]] > card_weight[max_card[1]]:
                chosen_card=same_suit[-1]
                max_choice=1
            else:
                chosen_card=same_suit[0]
                max_choice=2
        else:
            diff_suit.sort(key = lambda y :card_weight[y[1]])
            chosen_card=diff_suit[0]
            max_choice=3
        print("CHOSEN CARD FOR PLAYER4",chosen_card)
        chosen_card_list["player4"]=chosen_card
        player4.remove(chosen_card)
        if max_choice==1:
            max_card=chosen_card
        elif max_choice ==2:
            max_card=max_card
        elif max_choice==3:
            max_card=max_card
        same_suit=[]
        diff_suit=[]    
    return 




#FINDINg THE WINNER
def win():
    global chosen_card_list
    global max_card
    global win_list
    global store_i
    global playerflag
    key_list = list(chosen_card_list.keys())
    val_list = list(chosen_card_list.values())
    position = val_list.index(max_card)
    s=key_list[position]
    print(key_list[position],"IS THE WINNER")
    win_list[s]=win_list[s]+1
    print("THE WINNER LIST FOR THIS TURN IS ::",win_list)
    for i in range(len(playerflag)):
        if s[-1]==str(i+1):
             playerflag[i]=1
        else:
             playerflag[i]=0
    key_list=[]
    val_list=[]
    return 

print("-----------------------------LETS START THE GAME --------------------------------------")
print("TYPE ANSWERS IN CAPITAL LETTERS")
print("PRESS Y TO START OR CONTINUE THE GAME ")
print("PRESS N TO QUIT THE GAME")
ans=input("ENTER YOUR ANSWER ::")
while ans=="Y":
    print("---------------------------PLAYING ANOTHER GAME ---------------------------------------")  
    cards_list=[]
    for i in ["H","D","C","S"]:
        for j in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
            cards_list.append((i,j))
    print("DISPLAYING ALL THE CARDS :: ",cards_list)

    card_list_copy=cards_list.copy()
    player1=[]
    player2=[]
    player3=[]
    player4=[]

    #for player1
    for i in range(13):
        random_card=random.choice(card_list_copy)
        player1.append(random_card)
        card_list_copy.remove(random_card)
    print("DISPLAYING THE CARDS OF PLAYER1 :: ",player1)


    #for player2
    for i in range(13):
        random_card=random.choice(card_list_copy)
        player2.append(random_card)
        card_list_copy.remove(random_card)

    #for player3
    for i in range(13):
        random_card=random.choice(card_list_copy)
        player3.append(random_card)
        card_list_copy.remove(random_card)

    #for player4
    for i in range(13):
        random_card=random.choice(card_list_copy)
        player4.append(random_card)
        card_list_copy.remove(random_card)

    # ENTERING THE CALL FOR EACH PLAYER
    call_list={"player1":0,"player2":0,"player3":0,"player4":0}
    player_list=[player1,player2,player3,player4]
    x=int(input("ENTER THE NUMBER OF CALLS BEFORE STARTING THE GAME :: "))
    call_list["player1"]=x
    count=0
    for j in player2:
        if j[1]=="K" or j[1]=="Q" or j[1] =="J" or  j[1]=="A":
                count+=1
    call_list["player2"]=count
    count=0
    for j in player3:
        if j[1]=="K" or j[1]=="Q" or j[1] =="J" or  j[1]=="A":
                count+=1
    call_list["player3"]=count
    count=0
    for j in  player4:
        if j[1]=="K" or j[1]=="Q" or j[1] =="J" or  j[1]=="A":
                count+=1
    call_list["player4"]=count
    print("THE CALLS FOR EACH PLAYER :: ",call_list)

    card_weight={"K":13,"Q":12,"J":11,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"A":1}
    same_suit=[]
    diff_suit=[]
    chosen_card_list={}
    list_for_palyer1=[]
    win_list={"player1":0,"player2":0,"player3":0,"player4":0}
    store_i=0
    list_for_palyer1=[]
    print(" PRESS 1 FOR PLAYER 1 TO START \n PRESS 2 FOR PLAYER2 TO START\n PRESS 3 TO PLAYER3 TO START \n PRESS 4 TO PLAYER4 TO START ")
    num=int(input("ENTER THE NUMBER :: "))
    if num==1:
        print("----------------------------GAME BEGINS -----------------------------------------------")
        playerflag=[1,0,0,0]
        play1()
        play2()
        play3()
        play4()
        win()
        print("CARDS PLAYED IN THIS TURN :: ",chosen_card_list)
        chosen_card_list={}
        chosen_card=[]
        list_for_palyer1=[]
    elif num==2:
        print("----------------------------GAME BEGINS -----------------------------------------------")
        playerflag=[0,1,0,0]
        play2()
        play3()
        play4()
        play1()
        win()
        print("CARDS PLAYED IN THIS TURN :: ",chosen_card_list)
        chosen_card_list={}
        chosen_card=[]
        list_for_palyer1=[]

    elif num==3:
        print("----------------------------GAME BEGINS -----------------------------------------------")
        playerflag=[0,0,1,0]
        play3()
        play4()
        play1()
        play2()
        win()
        print("CARDS PLAYED IN THIS TURN :: ",chosen_card_list)
        chosen_card_list={}
        chosen_card=[]
        list_for_palyer1=[]
    elif num==4:
        print("----------------------------GAME BEGINS -----------------------------------------------")
        playerflag=[0,0,0,1]
        play4()
        play1()
        play2()
        play3()
        win()
        print("CARDS PLAYED IN THIS TURN :: ",chosen_card_list)
        chosen_card_list={}
        chosen_card=[]
        list_for_palyer1=[]

    count=1
    while(count<13):
        ###fUNCTION CALLING BASED ON THE WINNER    
        if playerflag[0]==1 :
            print("---------------------------NEXT TURN BEGINS ------------------------------------------")
            play1()
            play2()
            play3()
            play4()
            win()
            print("CARDS PLAYED IN THIS TURN :: ",chosen_card_list)
            chosen_card_list={}
            chosen_card=[]
            list_for_palyer1=[]
        elif playerflag[1]==1:
            print("---------------------------NEXT TURN BEGINS ------------------------------------------")
            play2()
            play3()
            play4()
            play1()
            win()
            print("CARDS PLAYED IN THIS TURN :: ",chosen_card_list)
            chosen_card_list={}
            chosen_card=[]
            list_for_palyer1=[]
        elif playerflag[2]==1:
            print("---------------------------NEXT TURN BEGINS ------------------------------------------")
            play3()
            play4()
            play1()
            play2()
            win()
            print("CARDS PLAYED IN THIS TURN :: ",chosen_card_list)
            chosen_card_list={}
            chosen_card=[]
            list_for_palyer1=[]
        elif playerflag[3]==1:
            print("---------------------------NEXT TURN BEGINS ------------------------------------------")
            play4()
            play1()
            play2()
            play3()
            win()
            print("CARDS PLAYED IN THIS TURN :: ",chosen_card_list)
            chosen_card_list={}
            chosen_card=[]
            list_for_palyer1=[]
        count=count+1


    print("THE WINNER LIST IN THIS TURN :: ",win_list)
    print("DISPLAYING THE CALL LIST BEFORE STARTING THE GAME :: ",call_list)
    score_dict={'player1':0,'player2':0,"player3":0,"player4":0}
    if call_list["player1"] > win_list['player1']:
        score_dict["player1"]=-10*call_list["player1"]
    else:
        score_dict['player1']=10*call_list["player1"]+(win_list["player1"]-call_list["player1"])

    if call_list["player2"] > win_list['player2']:
        score_dict["player2"]=-10*call_list["player2"]
    else:
        score_dict['player2']=10*call_list["player2"]+(win_list["player2"]-call_list["player2"])


    if call_list["player3"] > win_list['player3']:
        score_dict["player3"]=-10*call_list["player3"]
    else:
        score_dict['player3']=10*call_list["player3"]+(win_list["player3"]-call_list["player3"])


    if call_list["player4"] > win_list['player4']:
        score_dict["player4"]=-10*call_list["player4"]
    else:
        score_dict['player4']=10*call_list["player4"]+(win_list["player4"]-call_list["player4"])


    print(" THE FINAL SCORE LIST OF ALL THE PLAYERS :: ",score_dict)
    ans=input("PRESS Y OR N TO CONTINUE OR EXIT THE GAME :: ")

if ans=="N":
    print("THANKS FOR PLAYING THE GAME")
    