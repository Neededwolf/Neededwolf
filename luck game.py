import random,time,math,keyboard

back = 1
i = 1

x = 100
roll_time = 2     # you can chage this to make the game faster
points = 0   # you can add points to get a starting boost
rolls = 0
rebirths = 0
rebirth_points = 0
ascentions = 0
point_giver = 1
first_rebirth = 1
rebirth_points_giver = 0.1

print('WIP -Work In Progress, NCS - Not Coming Soon, STC - Soon To Come ')

#gamerules / features


print('Welcome to my luck game')
time.sleep(0.5)
print()
print("i can't be bothered to used the keyboard library")
print('but it makes the game less confussing, you have to type the letters when there is a gap for rolling')
print('press q then [enter] or just [enter] to roll or the hotkeys then [enter] to use them')
time.sleep(3)
print()
print('hotkeys are...')

print('q - to roll')
print('1 - to see your overall stats')
print('2 - to see your point')
print('3 - to see these hotkeys')
print('r - to rebirth (WIP)')
print('a - to ascend (NCS)')
print('u - to see your upgrades (WIP) (you need to say buy or no)')
print('t - to see the tutorial (WIP) ')
print()
#=========================game========================#
def try_again():
    time.sleep(roll_time)
    roll()



def hotkeys():
    print('1 - to see your overall stats')
    print('2 - to see your point')
    print('3 - to see these hotkeys')
    print('r - to rebirth (WIP)')
    print('a - to ascend (NCS)')
    print('u - to see your upgrades (WIP) (you need to say buy or no)')
    print('t - to see the tutorial (WIP) ')
    time.sleep(5)
    roll()


def points_give():
    global points
    points += point_giver
    print("you got",point_giver,"point(s) for rolling your highest possible number!")
    roll()

def stats():
    global rolls,points,x
    chance = x
    if rebirths < 1:
        print("you roll speed is",roll_time)
        print("points - ",points)
        print("rolls - ",rolls)
        print("chance - 1 in a",x)
        time.sleep(3)
        roll()
    if rebirths >= 1:
        print("you roll speed is",roll_time)
        print("points - ",points)
        print("rolls - ",rolls)
        print("chance - 1 in a",x)
        print("rebirth points",rebirth_points)
        time.sleep(3)
        roll()


def rebirth_upgrade1():
    global rebirth_points_giver
    rupgrade_1 = str(input("would you like to 'buy' times 5 rebirth points for 0.5 rebirth points?: ")) #WIP=================
    if rupgrade_1 == 'buy':
        rebirth_points_giver = rebirth_points_giver * 5
        print('i am not planing to add more stuff so this is currently the last upgrade :0') #WIP/NCS/STC========================================
        


#rebirth
def rebirth():
    global points,rebirths,roll_time,point_giver,points,i,x,first_rebirth
    if i == 5 and first_rebirth == 1:
        print('you can buy a rebirth for 1000 points')
        print("it will reset most your stats but double your points gain and half your roll time")
        print("you will also unlock rebirth upgrades and upgrade points which can be gotten from rolling 1")
        rebirth_buy = str(input("would you like to 'buy' a rebirth?"))
        if rebirth_buy == 'buy' and points >= 1000:
            print("rebirths aren't added yet but they are (STC)")#STC
            print("you didn't loss any points either")
            first_rebirth = 2
            rebirths += 1
            x = 100
            point_giver = 1
            roll_time = 2
            points = 0 # set to 0 ================
            point_giver = point_giver ^ (rebirths+1)
            roll_time = roll_time/(rebirths*2)
            i = 1
            roll()
        elif rebirth_buy == 'buy' and points <= 1000:
            print("you don't have enough points")
            roll()
        elif rebirth_buy == 'no':
            print('goodbye')
        else:
            print('that is not a valid option')
            rebirth()
    elif i != 5:
        print('you can not rebirth yet get all the normal upgrade to unlock this')
        roll()
    elif i == 5 and first_rebirth != 1:
        print("would you like to 'buy' a rebirth?")
        rebirth_next = str(input("or would you like to go to rebirth upgrades ('next')"))
        if rebirth_next == 'buy' and points >= 1000:
            print("rebirths aren't added yet but they are (STC)")#STC
            print("you didn't loss any points either")
            rebirths += 1
            x = 100
            point_giver = 1
            roll_time = 2
            points = 10000 #set to 0 =========
            point_giver = point_giver ^ (rebirths+1)
            roll_time = roll_time/(rebirths*2)
            i = 1
            roll()
        elif rebirth_next == 'buy' and points <= 1000:
            print("you don't have enough points")
            roll()
        elif rebirth_next == 'no':
            print('goodbye')
        elif rebirth_next == 'next':
            rebirth_upgrade1()
        else:
            print('that is not a valid option')
            rebirth()
        
#normal upgrades
def upgrade4():
    global points,i,roll_time,point_giver,x
    if i == 4:
        print("would you like to 'buy' -40% roll speed +1 points and better roll chance for 100 points")
        upgrade_4 = str(input("this upgrade is the second final one so after this you will unlock rebirths"))
        if upgrade_4 == 'buy' and points >= 100:
            print('you bought -40% roll speed +1 points and better roll chance for 100 points')
            points = points - 100
            i = 5
            x = x/12.8
            point_giver = point_giver * 2
            roll_time = roll_time/2.5
            print('your roll time is',roll_time,'your roll chance is 1 in',x,'and you get 2 points now')
            roll()
        elif upgrade_4 == 'buy' and points <= 100:
            print("you don't have enough points")
            roll()
        elif upgrade_4 == 'no':
            print('goodbye')
        else:
            print('that is not a valid option')
            upgrade4()
    elif i != 4:
        print('see you at the next upgrade')
        rebirth()
            
def upgrade3():
    global back,points,i,roll_time,x
    back = 1
    if i == 3:
        upgrade_3 = str(input("would you like to 'buy' -50% roll speed and better roll chance for 20 points?"))
        if upgrade_3 == 'buy' and points >= 20:
            print("you bought -50% roll speed and better roll chance for 20 points")
            points = points - 20
            roll_time = roll_time/2
            x = x/1.25
            i = 4
            print("you now can roll every",roll_time,"seconds and have a 1 in",x,'chance')
            print('see you at the next upgrade!')
            roll()
        elif upgrade_3 == 'buy' and points <= 20:
            print("you don't have enough points")
        elif upgrade_3 == 'no':
            print('goodbye')
        else:
            print('that is not a valid option')
            upgrade3()
    elif i != 3:
        print('see you at the next upgrade!')
        upgrade4()
    
def upgrade2():
    global points,back,roll_time,x,i
    if i == 2 and back == 1:
        print()
        print()
        print("###YOU MUST TYPE 1 OR 2, OR THE GAME BREAKS AND YOU LOSS ALL PROGRESS###")
        print("would you like to buy faster roll speed for 5 points (say 1) or a better roll chance for 6 points (say 2) (0 to leave)?")
        
        upgrade_2_choice = int(input(": "))
        if upgrade_2_choice == 1 and points >= 5:
            print('you bought -50% roll time for 5 points')
            points = points - 5
            roll_time = roll_time/2
            print(roll_time)
            print('see you at roll chance upgrade!')
            back = 3
            roll()
        elif upgrade_2_choice == 1 and points <= 5:
            print("you don't have enough points")
            roll()
        elif upgrade_2_choice == 0:
            print('goodbye')
            roll()   
        elif upgrade_2_choice == 2 and points >= 6:
            print('you bought a better roll chance')
            points = points - 6
            x = x/1.25
            back = 2
            print(x,'is now your roll chance')
            print('see you at the next upgrade')
        elif upgrade_2_choice == 2 and points <= 6:
            print("you don't have enough points")
            roll()
        elif upgrade_2_choice == 0:
            print('goodbye')
            roll()
        else:
            print('that is not a valid option')
            upgrade2()
    elif i == 2 and back == 2:
        upgrade_2_choice = str(input("would you like to 'buy' faster roll speed for 5 points"))                               
        if upgrade_2_choice == 'buy' and points <= 5:
            print("you don't have enough points")
            roll()
        elif upgrade_2_choice == 'buy' and points >= 5:
            print('you bought -50% roll time for 5 points')
            points = points - 5
            roll_time = roll_time/2
            back = 0
            i = 3
            print(roll_time)
            print('see you at the next upgrade (WIP)') #WIP
            roll()

        elif upgrade_2_choice == 'no':
            print('goodbye')
            roll()
        else:
            print('that is not a valid option')
            upgrade2()
    elif i == 2 and back == 3:
        print("would you like to 'buy' a better roll chance for 6 points")
        upgrade_2_choice = str(input(': '))
        if upgrade_2_choice == 'buy' and points >= 6:
            print('you bought a better roll chance')
            points = points - 6
            x = x/1.25
            back = 0
            i = 3
            print(x)
            print('see you at the next upgrade (WIP)') #WIP
            roll()
        elif upgrade_2_choice == 'buy' and points <= 6:
            print("you don't have enough points")
            roll()
        elif upgrade_2_choice == 'no':
            print('goodbye')
            roll()
        else:
            print('that is not a valid option')
            upgrade2()
    elif i != 2:
        print('see you at the next upgrade!')
        upgrade3()


    
def upgrade1():
    global roll_time,i,points
    if i == 1:
        upgrade_1 = str(input("would you like to 'buy' -50% roll time for 3 points? currently at 2 seconds")).lower()
        if upgrade_1 == 'buy' and points >= 3:
            print('you bought -50% roll time for 3 points')
            points = points - 3
            roll_time = roll_time/2
            print(roll_time)
            print('see you at the next upgrade!')
            i = 2
            roll()
        elif upgrade_1 == 'buy' and points <= 3:
            print("you don't have enough points")
            roll()
        elif upgrade_1 == 'no':
            print('goodbye')
            roll()
        else:
            print(upgrade1,' is not a choice please try again')
            upgrade1()
    elif i != 1:
        print('see you at the next upgrade!')
        back = 1
        upgrade2()

def current_points():
    print('you currently have',points,'point(s)')
    roll()

def tutorial():
    print('to play the game you need to press q for a bit until you get 3 points to make the game faster')
    print('once you get all upgrades and 1k points you can rebirth (WIP) this will double your points gain and half your roll speed')
    print('once you get 1k rebirths you can ascend (NCS) this will boost you by a TON and you unlock automation (might come in rebirths instead)')
    time.sleep(10)
    roll()
def rebirth_points_gain():
    global rebirth_points,rebirth_points_giver
    rebirth_points += rebirth_points_giver
    roll()
def roll():
    global rolls,roll_amount
    roll = random.randint(1,x)
    roll_press = input('you can now roll: ')
    time.sleep(0.1)
    if roll_press == '1':
        stats()
    elif roll_press == '2':
        current_points()
    elif roll_press == '3':
        hotkeys()
    elif roll_press == 'r':
        rebirth()
    elif roll_press == 'a':
        print('ascentions are in NCS status')
        try_again()
    elif roll_press == 'u':
        upgrade1()
    elif roll_press == 't':
        tutorial()
    else:
        rolls += 1
        print(roll)
        if roll == x:
            points_give()
        elif roll == 1 and rebirths >= 1:
            rebirth_points_gain()
        elif roll != x or roll != 1:
            try_again()

roll()

