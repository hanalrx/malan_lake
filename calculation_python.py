# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:18:10 2017

@author: Li Ruoxi
"""


def hilite(string, status, bold):
    attr = []
    if status:
        # green
        attr.append('34')
    else:
        # red
        attr.append('31')
    if bold:
        attr.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

print('\nHi there,')
print('\nWelcome to Ecoins Evaluation System')
print('-------------------------------------')
username=input('Yourname?: ')
print('\n')
ecoins = 1700
housingTypeInML = 200

while True:
#Indentify location and check whether input is valid
    try:
        print( hilite( "Rrogress 8% ▓▓░░░░░░░░░░░░░░░░░░░░░░", True, True ) )
        print( hilite( "Identifying your location...", True, True ) )
        print('\nWhere are you?')
        print(' 1. In Malan Lake')
        print(' 2. Elsewhere')
        print('\n')
        location=input('Please enter an option number:')
        print('\n')
        location=int(location)
        if location == 1 or location ==2:
            break
        else:
            print( hilite( "Please enter a valid number", False,False )) 
    except ValueError:
        print( hilite( "Please enter a valid number", False,False )) 



#CIRCUMSTANCES WHEN INSIDE MALAN LAKE
if location == 1 :
    #HousingType in Malan Lake - 200ecoins
    ecoins = ecoins - housingTypeInML
    while True:
        #How many people share a room
        try:
            print( hilite( "Rrogress 16% ▓▓▓▓░░░░░░░░░░░░░░░░░░░░", True, True ) )
            print( hilite( "Identifying guests numbers...", True, True ) )
            print('\nDo you share a room with others?')
            print(' 1.No')
            print(' 2.Yes,I share room with another one')
            print(' 3.Yes,I share room with other 2 guests')
            print(' 4.Ohters')
            print('\n')
            guestsNumbers=input('Please enter an option number:')
            print('\n')
            guestsNumbers=int(guestsNumbers)
            if guestsNumbers == 1 or guestsNumbers == 2 or guestsNumbers ==3 or guestsNumbers==4:
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    
    while True:
        #Roomtype
        try:
            print( hilite( "Rrogress 24% ▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░", True, True ) )
            print( hilite( "Indentifying housing footprint...", True, True ) )
            print('\nWhich roomtype do you live in?')
            print(' 1.Single room\n 2.Double room\n 3.Twin room\n 4.Others')
            print('\n')
            roomType=input('Please enter an option number:')
            print('\n')
            roomType=int(roomType)
            if roomType == 1 or roomType == 2 or roomType == 3 or roomType == 4 :
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    
    gn = guestsNumbers 
    rt = roomType
    if rt ==1 :
        #Single room: 450ecoins
        rte = 450
    elif rt ==2:
        #Double rom: 600ecoins
        rte = 600
    elif rt ==3:
        #Twin room:750ecoins
        rte = 750
    elif rt==4:
        #Other room types: 1050ecoins
        rte = 1050
    ecoins = ecoins - rte/gn
            
    while True:
        #RoomService
        try:
            print( hilite( "Rrogress 32% ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░", True, True ) )
            print( hilite( "Room service...", True, True ) )
            print('\nDo you use our room service?')
            print(' 1.Yes\n 2.No')
            print('\n')
            roomService=input('Please enter an option number:')
            roomService=int(roomService)
            print('\n')
            if roomService == 1:
                ecoins = ecoins-200
                break
            elif roomService==2:
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    
    while True:
        #Water
        try:
            print( hilite( "Rrogress 40% ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░", True, True ) )
            print( hilite( "Water...", True, True ) )
            print('\nHow many tons of water did you use today?')
            print('\n')
            water=input('Please enter the amount of tons: ')
            water=float(water)
            print('\n')
            ecoins = ecoins - 300*water
            break
        except ValueError:
            print( hilite( "Please enter a valid number", False,False ))   
        
    while True:
        #Electricity
        try:
            print( hilite( "Rrogress 48% ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░", True, True ) )
            print( hilite( "Electricity...", True, True ) )
            print('\nHow many units of electricity did you use today?')
            print('\n')
            ele=input('Please enter the amount of units:')
            print('\n')
            ele=float(ele)
            ecoins = ecoins - 10*ele
            break
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    
    while True:
        #Food1: Animal based products
        try:
            print( hilite( "Rrogress 56% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░", True, True ) )
            print( hilite( "Food-Animal based products...", True, True ) )
            print('\nHow many times did you eat animal based products today?')
            print('Eg: Beef,port,chicken,fish,eggs,diary products')
            print(' 1.No,I didnt eat them today')
            print(' 2.one time')
            print(' 3.two times')
            print(' 4.three times')
            print('\n')
            food1=input('Please enter an option number:')
            print('\n')
            food1=int(food1)
            if food1==1 or food1 ==2 or food1==3 or food1==4:
                ecoins=ecoins-food1*100
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False ))  
            
    while True:
        #Food2 :non-seasonal fruits and vegetables
        try:
            print( hilite( "Rrogress 64% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░", True, True ) )
            print( hilite( "Food-fruits and vegetables...", True, True ) )
            print('\nHow many times did you eat non-seasonal fruits and vegetables today?')
            print(' 1.No,I didnt eat them today')
            print(' 2.one time')
            print(' 3.two times')
            print(' 4.three times')
            print('\n')
            food2=input('Please enter an option number:')
            print('\n')
            food2=int(food2)
            if food2==1 or food2 ==2 or food2==3 or food2==4:
                ecoins=ecoins-food2*60
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    
    while True:
        #Food3 :grain products
        try:
            print( hilite( "Rrogress 72% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░", True, True ) )
            print( hilite( "Grain products...", True, True ) )
            print('\nHow many times did you eat grain products today?')
            print('eg:wheat, rice, cereal, corn, bread, noodles')            
            print(' 1.No,I didnt eat them today')
            print(' 2.one time')
            print(' 3.two times')
            print(' 4.three times')
            print('\n')
            food3=input('Please enter an option number:')
            print('\n')
            food3=int(food3)
            if food3==1 or food3 ==2 or food3==3 or food3==4:
                ecoins=ecoins-food3*10
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
            
    while True:
        #Food3 :Processed, packaged and imported food
        try:
            print( hilite( "Rrogress 80% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░", True, True ) )
            print( hilite( "processed food...", True, True ) )
            print('\nHow many times did you processed, packaged and imported food today?')           
            print(' 1.No,I didnt eat them today')
            print(' 2.one time')
            print(' 3.two times')
            print(' 4.three times')
            print('\n')
            food4=input('Please enter an option number:')
            print('\n')
            food4=int(food4)
            if food4==1 or food4 ==2 or food4==3 or food4==4:
                ecoins=ecoins-food4*50
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    
    while True:
        #Bottled water
        try:
            print( hilite( "Rrogress 88% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░", True, True ) )
            print( hilite( "Bottled water...", True, True ) )
            print('\nHow many bottled water did you drink today?')           
            print(' 1.No,I didnt drink bottled water today')
            print(' 2.One bottle')
            print(' 3.Two bottles')
            print(' 4.Three bottles or more')
            print('\n')
            bottle=input('Please enter an option number:')
            bottle=int(bottle)
            print('\n')
            if bottle==1 or bottle ==2 or bottle==3 or bottle==4:
                ecoins=ecoins-bottle*100
                break
            else:
                print( hilite( "Please enter a valid number", False,False ))  
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    
    while True:
        #Mobility Footprint
        #Number of km travelled
        try:
            print( hilite( "Rrogress 96% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░", True, True ) )
            print( hilite( "Mobility...", True, True ) )
            print('\nHow many kilometers did you travel today?')           
            print(' 1.1km-25km')
            print(' 2.25km-50km')
            print(' 3.50km-130km')
            print(' 4.More than 130km')
            print('\n')
            km=input('Please enter an option number:')
            print('\n')
            km=int(km)
            if km==1:
                #1-25km: -40ecoins
                ecoins=ecoins-40
                break
            elif km == 2:
                #25-50km: - 100ecoins
                ecoins=ecoins-100
                break
            elif km==3:
                #50-130km:-200ecoins
                ecoins=ecoins-200
                break
            elif km==4:
                #more than 130km: -400ecoins
                ecoins=ecoins-400
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    
    while True:
        #Mobility Footprint
        #Walking steps
        try:
            print( hilite( "Rrogress 100% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", True, True ) )
            print( hilite( "Walking steps...", True, True ) )
            print('\nHow many steps did you walk today?')
            print(' 1. <5000steps')
            print(' 2.5000steps-10000steps')
            print(' 3.10000steps-20000steps')
            print(' 4.>20000steps')
            print('\n')
            steps=input('Please enter an option number:')
            print('\n')
            steps = int(steps)
            if steps ==1:
                #walking steps less than 5000, do nothing
                ecoins = ecoins
                break
            elif steps ==2:
                #5000<= walking steps<10000
                ecoins = ecoins + 20
                break
            elif steps == 3:
                #10000<= walking steps <20000
                ecoins = ecoins + 50
                break
            elif steps == 4:
                #walking steps>20000
                ecoins = ecoins+110
                break
            else:
                True
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
            
    
    
#CIRCUMSTANCES WHEN OUTSIDE MALAN LAKE
    

if location == 2 :
    #HousingType outside 
    while True:
        #Housing Footprint
        try:
            print( hilite( "Rrogress 16% ▓▓▓▓░░░░░░░░░░░░░░░░░░░░", True, True ) )
            print( hilite( "Home size...", True, True ) )
            print('\nYour home size in square meters?')
            print(' 1.Smaller than 30')
            print(' 2.30-60')
            print(' 3.60-90')
            print(' 4.90-130')
            print(' 5.130-200')
            print(' 6.Larger than 200')
            print('\n')
            sm=input('Please enter an option number:')
            print('\n')
            sm = int(sm)
            if sm ==1:
                #Smaller than 30:-10ecoins
                sme = 700
                break
            elif sm==2:
                #30-60:-20ecoins
                sme = 900
                break
            elif sm==3:
                #60-90:-40ecoins
                sme = 1300
                break
            elif sm==4:
                #90-130：-200ecoins
                sme = 2000
                break
            elif sm==5:
                #130-200:-300ecoins
                sme = 3000
                break
            elif sm==6:
                #>200:-400ecoins
                sme = 4000
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
            
          
    while True:
        #Housing Type
        try:
            print( hilite( "Rrogress 30% ▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░", True, True ) )
            print( hilite( "Housing Type...", True, True ) )
            print('\nWhich is the housing type of your home?')
            print(' 1.Free standing house\n 2.Row house or building with 2-4 housing units')
            print(' 3.Multi-storey apartment building')
            print(' 4.Green-design residence')
            print('\n')
            housingType2=input('Please enter an option number:')
            print('\n')
            ht2=int(housingType2)
            if ht2== 1:
                #Free ..:-1800ecoins
                ht2e = 1800
                break
            if ht2==2:
                #Row house or building ...: -400coins
                ht2e = 600
                break
            if ht2==3:
                #Multi-Storey apartment...: -300ecoins
                ht2e = 400
                break
            if ht2==4:
                #Green-design...:0
                ht2e = 0
                break
        except ValueError:
            print( hilite( "Please enter a valid number", False,False ))      
          
          
    while True:
        #How many people live in your home(including you)
        try:
            print( hilite( "Rrogress 42% ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░", True, True ) )
            print( hilite( "Housing Type...", True, True ) )
            print('\nHow many people live in your home?')
            print('\n')
            homeMembers=input('Please enter number of your home members:')
            print('\n')
            hm=int(homeMembers)
            smeperperson = sme/hm
            ecoins = ecoins - ht2 - sme/hm
            break
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    

    
    while True:
        #Water
        try:
            print( hilite( "Rrogress 55% ▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░", True, True ) )
            print( hilite( "Water...", True, True ) )
            print('How many tons of water did you use today?')
            print('\n')
            water=input('Please enter the amount of tons: ')
            water=float(water)
            print('\n')
            ecoins = ecoins - 30*water
            break
        except ValueError:
            print( hilite( "Please enter a valid number", False,False ))   
        
    while True:
        #Electricity
        try:
            print( hilite( "Rrogress 67% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░", True, True ) )
            print( hilite( "Electricity...", True, True ) )
            print('\nHow many units of electricity did you use today?')
            print('\n')
            ele=input('Please enter the amount of units:')
            print('\n')
            ele=float(ele)
            ecoins = ecoins - 5*ele
            break
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 





    while True:
        #Mobility Footprint
        #Number of km travelled
        try:
            print( hilite( "Rrogress 85% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░", True, True ) )
            print( hilite( "Mobility...", True, True ) )
            print('\nHow many kilometers did you travel today?')           
            print(' 1. 1km-25km')
            print(' 2. 25km-50km')
            print(' 3. 50km-130km')
            print(' 4. More than 130km')
            print('\n')
            km=input('Please enter an option number:')
            print('\n')
            km=int(km)
            if km==1:
                #1-25km: -40ecoins
                ecoins=ecoins-40
                break
            elif km == 2:
                #25-50km: - 100ecoins
                ecoins=ecoins-100
                break
            elif km==3:
                #50-130km:-200ecoins
                ecoins=ecoins-200
                break
            elif km==4:
                #more than 130km: -400ecoins
                ecoins=ecoins-400
                break
            else:
                print( hilite( "Please enter a valid number", False,False )) 
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
    
    
    #食物定量
    #Food outside:
    #110e+170e+160e+100e+0=540e 
    #We suppose every one consume 540ecoins for food everyday
    ecoins = ecoins - 740 
    
    
    
    while True:
        #Mobility Footprint
        #Walking steps
        try:
            print( hilite( "Rrogress 100% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", True, True ) )
            print( hilite( "Walking steps...", True, True ) )
            print('\nHow many steps did you walk today?')
            print(' 1. <5000steps')
            print(' 2. 5000steps-10000steps')
            print(' 3. 10000steps-20000steps')
            print(' 4. >20000steps')
            print('\n')
            steps=input('Please enter an option number:')
            print('\n')
            steps = int(steps)
            if steps ==1:
                #walking steps less than 5000, do nothing
                ecoins = ecoins
                break
            elif steps ==2:
                #5000<= walking steps<10000
                ecoins = ecoins + 20
                break
            elif steps == 3:
                #10000<= walking steps <20000
                ecoins = ecoins + 50
                break
            elif steps == 4:
                #walking steps>20000
                ecoins = ecoins+ 110
                break
            else:
                True
        except ValueError:
            print( hilite( "Please enter a valid number", False,False )) 
            
   
else:
    True





#OUTPUT YOUR ECOINS LEFT TODAY
#OUTPUT HOW MANY EARTHS DO YOU NEED TO SUPPORT YOUR LIFESTYLE TODAY

earthnumber =(1700-ecoins)/1700
earthnumber = float("{0:.2f}".format(earthnumber))
ecoinsUsed = 1700-ecoins

if ecoins>0:
    print( hilite( "-----------------------------------------------------------", True, True ) )
    print('Hi {},'.format(username))
    print('You used {} ecoins and have {} ecoins left today.'.format(ecoinsUsed,ecoins))
    print('If everyone lived like you, we should need {} earths.'.format(earthnumber))
    print( hilite( "-----------------------------------------------------------", True, True ) )
    print('\n')
elif ecoins<= 0:
    print( hilite( "-----------------------------------------------------------", True, True ) )
    print('Hi {},'.format(username))
    print('You used {} ecoins. You do not have any ecoins left today.'.format(ecoinsUsed))
    print('If everyone lived like you, we should need {} earths.'.format(earthnumber))
    print( hilite( "-----------------------------------------------------------", True, True ) )
    print('\n')


 



















