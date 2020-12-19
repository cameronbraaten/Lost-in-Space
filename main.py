# Cameron Braaten

# This is a game called 'lost in space'! Have fun!

# December 12 2020

print("Welcome to space!\n")

print("Your mission is to find the dwarf planet Pluto and collect a sample of soil.\n")

playerInventory=[]

choices = ['look around', 'float to the right', 'float up', 'float down', 'float to the left','check inventory','show me the choices','quit']

print("As you wander around the universe, you will have the following action-oriented options each turn:\n")

count=1
for choice in choices:
  print(count,". ",choice,sep='')
  count+=1

print("\nFor example, if you want to look around a room, just type: look around")



def room1(inventory):
  
  print("\nYou're on Mercury, the closest planet to the sun!\n")
  
  while True:

    choice = input("What do you want to do next?\n\n").lower()
    
    if choice in choices:
      
      if choice == 'float to the right':
        room2(playerInventory)
      
      elif choice == 'float up':
        room3(playerInventory)
      
      elif choice == 'float to the left':
        room4(playerInventory)

      elif choice=='float down':
        room6(playerInventory)
      
      elif choice == 'show me the choices':

        print("\n")
        count=1
        for choice in choices:
          print(count,". ",choice,sep='')
          count+=1
        print("\n")
      
      elif choice=='quit':
        quitGame(playerInventory)
      
      elif choice == 'look around':

        mercchoice=input("\nYou see a Fermi Bubble and an Einstein Cross. \n\nWould you like to keep one of these items? Keep in mind, you only have room to pick up one item on each planet you visit (type 'yes' or 'no').\n\n").lower()
        
        if mercchoice=='yes':

          buborcross=input("\nWhich item would you like to pick up? (Type 'Fermi Bubble' or 'Einstein Cross' below)\n\n").lower()
          
          if buborcross=='fermi bubble' :
            
            if "Fermi Bubble" in playerInventory:

              print("\nYou already have the Fermi Bubble.\n")

            elif "Einstein Cross" and "Fermi Bubble" not in playerInventory:

              print("\nThe Fermi Bubble has been added to your inventory.\n")
              playerInventory.append("Fermi Bubble")
            
            else:

              print("\nYou only have room for one item from each planet.\n")
          
          elif buborcross=="Einstein Cross" or buborcross=="einstein cross":
            
            if "Einstein Cross" in playerInventory:

              print("\nYou already have the Einstein Cross.\n")

            elif "Fermi Bubble" not in playerInventory:

              print("\nThe Einstein Cross has been added to your inventory.\n")
              playerInventory.append("Einstein Cross")
            
            else:

              print("\nYou only have room for one item from each planet.\n")
          
          else:

            print("\nThat is not one of the options. You must look around again in order to re-find these items.\n")

        elif mercchoice=='no':

          print("\nAwh too bad, that Fermi Bubble looked cool.\n")
        
        else:
          
          print("\nPlease type 'yes' or 'no'. You will have to look around to find these items again.\n")
      
      elif choice=='check inventory':

        if playerInventory==[]:

          print("\nYou have nothing in your inventory so far!\n")
        
        else:

          count=1
          for item in playerInventory:
            
            if count==1:
              print('\n',count,'. ',item,'\n',sep='')
              count+=1
            elif count%2==0:
              print(count,'. ',item,'\n',sep='')
              count+=1
            else:
              print(count,'. ',item,'\n',sep='')
              count+=1

    else:

      print("\nSorry, you can't do that.\n")

def room2(inventory):
  
  print("\nNow you're on Venus, Earth's twin in size!\n")
  
  while True:
    
    choice = input("What do you want to do next?\n\n").lower()
    
    if choice=='float to the left':
      room1(playerInventory)
    
    elif choice=='float down':
      room7(playerInventory)
    
    elif choice == 'show me the choices':

        print("\n")
        count=1
        for choice in choices:
          print(count,". ",choice,sep='')
          count+=1
        print("\n")
    
    elif choice=='quit':
        quitGame(playerInventory)
    
    elif choice=='look around':

      venchoice=input("\nYou see a Ida Mimas. Would you like to pick it up? (type 'yes' or 'no')\n\n").lower()

      if venchoice!="yes" and venchoice!='no':
        print("\nSorry, you can't do that. You will have to look around again for the Ida Mimas if you still want it.\n")
      
      elif "Ida Mimas" in playerInventory:

        print("\nYou already have an Ida Mimas in your inventory!\n")
      
      else:

        if venchoice=='yes':

          print("\nThe Ida Mimas has been added to your inventory.\n")
          playerInventory.append("Ida Mimas")
      
        elif venchoice=='no':
          print("\nInteresting choice.\n")
    
    elif choice=='check inventory':
      
      if playerInventory==[]:
        print("\nYou have nothing in your inventory so far!\n")
      
      else:
        
        count=1
        for item in playerInventory:
            
          if count==1:
            print('\n',count,'. ',item,'\n',sep='')
            count+=1
          elif count%2==0:
            print(count,'. ',item,'\n',sep='')
            count+=1
          else:
            print(count,'. ',item,'\n',sep='')
            count+=1
    
    elif choice=='float to the right' or choice=='float up':

      print("\nYou begin floating off into a black abyss of nothingness. Let's try a different direction.\n")
    
    else:

      print("\nSorry, you can't do that.\n")

def room3(inventory):

  print("\nYou made it to Earth! Did you know 67% of this planet is covered by ocean?\n")
  
  while True:

    choice = input("What do you want to do next?\n\n").lower()
    
    if choice=='float down':
      room1(playerInventory)
    
    elif choice == 'show me the choices':

        print("\n")
        count=1
        for choice in choices:
          print(count,". ",choice,sep='')
          count+=1
        print("\n")
    
    elif choice=='quit':
      quitGame(playerInventory)
    
    elif choice=='check inventory':

      if playerInventory==[]:

        print("\nYou have nothing in your inventory so far!\n")
      
      else:
        
        count=1
        for item in playerInventory:
          if count==1:
            print('\n',count,'. ',item,'\n',sep='')
            count+=1
          elif count%2==0:
            print(count,'. ',item,'\n',sep='')
            count+=1
          else:
            print(count,'. ',item,'\n',sep='')
            count+=1

    elif choice=='look around':

      print("\nYou see a slimy Sea Urchin in the middle of the Atlantic Ocean. This would be a fine specimen to add to the collection!\n")

      print("However, the Sea Urchin is not willing to leave earth unless you solve his riddle.\n")

      riddleAns=input("'I am an odd number. When I remove a letter from the word, I become even. What is the value of my number?'\n\n").lower()
      
      while True:

        if riddleAns=='seven' or riddleAns=='7':
          
          if "Sea Urchin" not in playerInventory:
            
            playerInventory.append("Sea Urchin")
            print("\nCorrect! The Sea Urchin has been added to your inventory.\n")
            break
          
          else:
            
            print("\nYou already found the Sea Urchin!\n")
            break
        
        else:
          
          print("\nIncorrect, if you would like to try again, I would suggest looking around for the Sea Urchin again.\n")
          break
    
    elif choice=='float up' or choice=='float to the left' or choice=='float to the right':

      print("\nYou begin floating off into a black abyss of nothingness. Let's try a different direction.\n")
    
    else:
      print("\nSorry, you can't do that.\n")

def room4(inventory):

  print("\nElon Musk, is that you? Your adventure has taken you to the planet Mars.\n\nMars is covered in a dust made of iron oxides, which gives the entire planet a iconic red hue.\n")
  
  while True:

    choice = input("What do you want to do next?\n\n").lower()
    
    if choice in choices:
      
      if choice=='float down':
        room5(playerInventory)
    
      elif choice=='float to the right':
        room1(playerInventory)
      
      elif choice=='check inventory':

        if playerInventory==[]:
          
          print("\nYou have nothing in your inventory so far!\n")
        
        else:

          count=1
          for item in playerInventory:
            if count==1:
              print('\n',count,'. ',item,'\n',sep='')
              count+=1
            elif count%2==0:
              print(count,'. ',item,'\n',sep='')
              count+=1
            else:
              print(count,'. ',item,'\n',sep='')
              count+=1
      
      elif choice=='quit':
        quitGame(playerInventory)
          
      
      elif choice == 'look around':

        print("\nYou have encountered an alien!\n")

        print("'In order to complete your mission' says the alien, 'you must remember this simple number pattern when you reach Pluto: 2468642'\n")
        
      
      elif choice == 'show me the choices':

        print("\n")
        count=1
        for choice in choices:
          print(count,". ",choice,sep='')
          count+=1
        print("\n")

      else:

        print("\nYou get lost in the black abyss of space. Let's try a different direction.\n")
        
    else:

      print("\nSorry, you can't do that.\n")
      

def room5(inventory):

  print("\nWelcome to the biggest planet in the solar system, Jupiter.")

  print("\nDid you know approximately 1300 Earths could fit into Jupiter?\n")

  while True: 

    jupchoice=input('What do you want to do next?\n\n').lower()

    if jupchoice=='float up':
      room4(playerInventory)
    
    elif jupchoice=='float to the right':
      room6(playerInventory)
      
    elif jupchoice=='check inventory':
      
      if playerInventory==[]:

        print("\nYou have nothing in your inventory so far!\n")
        break
      
      else:
        
        count=1
        for item in playerInventory:
          if count==1:
            print('\n',count,'. ',item,'\n',sep='')
            count+=1
          elif count%2==0:
            print(count,'. ',item,'\n',sep='')
            count+=1
          else:
            print(count,'. ',item,'\n',sep='')
            count+=1
    
    elif jupchoice=='quit':
        quitGame(playerInventory)
    
    elif jupchoice=='show me the choices':
      print("\n")
      count=1
      for choice in choices:
        print(count,". ",choice,sep='')
        count+=1
      print("\n")
      
    
    elif jupchoice=='look around':

      print("\nYou are caught in Jupiter's Great Red Spot, a storm that is 3 times the size of earth and has been raging for over a century!\n")

      print("Lucky enough, you happen to be right next to a teleportation stone. I wonder where it will take you. There is only one way to find out...\n")

      print('*'*100)
      count=0
      while count<8:
        print('*',' '*96,'*')
        count+=1
        if count==4: 
          print('*',' '*45,'POOF',' '*45,'*')
      print("*"*100)
      print('\n')

      room1(playerInventory)

    elif jupchoice=='float down' or jupchoice=='float to the left':

      print("\nYou get lost in the black abyss of space. Let's try a different direction.\n")
      break
    
    else:

      print("\nSorry, you can't do that.\n")
  
  else:

    print("Sorry, you can't do that.")

def room6(inventory):

  print("\nWelcome to Saturn, where we will orbit the sun once every 29.4 Earth years.\n")

  while True:

    choice = input("What do you want to do next?\n\n").lower()
    
    if choice=='float to the right':
      room7(playerInventory)
    
    elif choice=='float to the left':
      room5(playerInventory)

    elif choice=='float up':
      room1(playerInventory)
    
    elif choice=='check inventory':
        if playerInventory==[]:
          print("\nYou have nothing in your inventory so far!\n")
        
        else:

          count=1
          for item in playerInventory:
            if count==1:
              print('\n',count,'. ',item,'\n',sep='')
              count+=1
            elif count%2==0:
              print(count,'. ',item,'\n',sep='')
              count+=1
            else:
              print(count,'. ',item,'\n',sep='')
              count+=1
    
    elif choice=='quit':
        quitGame(playerInventory)
      
    elif choice == 'show me the choices':
        
        print("\n")
        count=1
        for choice in choices:
          print(count,". ",choice,sep='')
          count+=1
        print("\n")

    elif choice== 'look around':
      
      print("\nA scary space monster approaches you and says 'If you have a Fermi Bubble, you must give it to me right now. Or else you will not be leaving Saturn peacefully...'\n")

      if "Fermi Bubble" in playerInventory:

        print("The monster takes your Fermi Bubble and happily runs back to his cave:(\n")
        playerInventory.remove("Fermi Bubble")
      
      else:

        print("You tell the space monster that you don't have a Fermi Bubble and he retreats to his cave.\n")

    elif choice=='float down':

      print("\nYou begin floating off into a black abyss of nothingness. Let's try a different direction.\n")

    else:

      print("\nSorry, you can't do that.\n")

def room7(inventory):

  print("\nCongratulations, you made it to the smelliest planet in the solar system!\n")

  print("Uranus has clouds made of hydrogen sulfide, which makes it smell like rotten eggs.\n")

  while True:

    choice = input("What do you want to do next?\n\n").lower()

    if choice=='float down':
      room8(playerInventory)

    elif choice=='float up':
      room2(playerInventory)

    elif choice=='float to the left':
      room6(playerInventory)

    elif choice=='quit':
        quitGame(playerInventory)

    elif choice=='check inventory':

      if playerInventory==[]:

        print("\nYou have nothing in your inventory so far!\n")
      
      else:

        count=1
        for item in playerInventory:
          if count==1:
            print('\n',count,'. ',item,'\n',sep='')
            count+=1
          elif count%2==0:
            print(count,'. ',item,'\n',sep='')
            count+=1
          else:
            print(count,'. ',item,'\n',sep='')
            count+=1

    elif choice=='show me the choices':

      print("\n")
      count=1
      for choice in choices:
        print(count,". ",choice,sep='')
        count+=1
      print("\n")
    
    elif choice=='look around':
      
      print("\nYou stare off into the gassy abyss and do not see anything relevant to your mission.\n")
    
    elif choice=='float to the right':

      print("\nYou begin floating off into a black abyss of nothingness. Let's try a different direction\n")
    
    else:

      print("\nSorry, you can't do that.\n")

def room8(inventory):
  
  print("\nOh my gosh, you made it to Neptune, I hope you like the cold.\n")
  
  print("Neptune is more than 30 times as far from the sun as Earth is, resulting in an average temperature of -200 degrees Celsius.\n")
  
  while True:
    
    choice = input("What do you want to do next?\n\n").lower()
    
    if choice=='float to the right':
      room9(inventory)
    
    elif choice=='float up':
      room2(inventory)
    
    elif choice=='check inventory':

      if inventory==[]:
      
        print("\nYou have nothing in your inventory so far!\n")
      
      else:

        count=1
        for item in playerInventory:
          if count==1:
            print('\n',count,'. ',item,'\n',sep='')
            count+=1
          elif count%2==0:
            print(count,'. ',item,'\n',sep='')
            count+=1
          else:
            print(count,'. ',item,'\n',sep='')
            count+=1
    
    elif choice=='quit':
        print("Bleh")
        quitGame(inventory)
    
    elif choice=='show me the choices':

      print("\n")
      count=1
      for choice in choices:
        print(count,". ",choice,sep='')
        count+=1
      print("\n")

    elif choice=='float to the left' or choice=='float down':

      print("\nYou begin floating off into a black abyss of nothingness. Let's try a different direction.\n")
    
    elif choice=='look around':

      print("\nAs you are looking around, you begin to lose your sense of direction in Neptune's dense blue atmosphere.\n")

      crossyRoad=input("An Einstein Cross is the only item that can save you now. Please tell me you have one... (type 'yes' or 'no').\n\n").lower()

      if crossyRoad=='yes':
        
        if 'Einstein Cross' in inventory:

          print("\nThat's a relief, the Einstein Cross allows you to see even in the worst visibility. You may continue your journey.\n")
        
        else:
          
          print("\nLIAR!\n")

          print("You stumble into an ice volcano (because those totally exist on Neptune), you lose everything in your inventory and are teleported back to Mercury.")

          for item in playerInventory:
            playerInventory.remove(item)
          room1(playerInventory)
      
      elif crossyRoad=='no':
        
        print("\nYou stumble into a ice volcano (because those totally exist on Neptune), you lose everything in your inventory and are teleported back to Mercury.")

        for item in playerInventory:
          playerInventory.remove(item)
        room1(playerInventory)
      
      else:

        print("\nTry typing 'yes' or 'no' next time.\n")

        print("\nYou stumble into a ice volcano (because you can't follow simple directions), you lose everything in your inventory and are teleported back to Mercury.\n")

        for item in playerInventory:
          playerInventory.remove(item)
        room1(playerInventory)
    else:
      
      print("\nSorry, you can't do that.\n")

def room9(inventory):
  
  print("\nYou did it, you're now on Pluto!")

  plutochoice=input("\nType 'Dig' to collect your soil sample.\n\n").lower()

  if plutochoice=='dig':

    playerInventory.append("Soil Sample")
    print("\nSoil Sample has been added to your inventory.\n")

    bubAndUrchCheck(playerInventory)
  
  else:
    print("\nTry typing 'Dig' or 'dig' next time.")
    room9(playerInventory)

def winCheck(inventory):

  numPatt=input("\nNow, you must recite a special number pattern, do you know what it is? (type the pattern below)\n\n")

  if numPatt=='2468642':

    print("\nYou have won the game!\n")
    endGame=input("Type 'quit' to view your final inventory and end the game.\n\n").lower()

    if endGame=='quit':
      quitGame(playerInventory)
    
    else:
      print("\nSorry, you can't do that.\n")
      
      endGame=input("Type 'quit' to view your final inventory and end the game.\n\n").lower()

      if endGame=='quit':
        quitGame(playerInventory)

  else:

    print("\nThat's a shame!\n")
    print("You have been teleported back to Mercury\n")
    room1(playerInventory)

def bubAndUrchCheck(inventory):

  invItems=input("At this point in the game, you must have a Sea Urchin and a Furbi Bubble in your inventory. Did you find these two items on your journey? (type 'yes' or 'no)\n\n").lower()

  if invItems=='yes':

    if "Sea Urchin" in playerInventory and "Fermi Bubble" in playerInventory:

      winCheck(playerInventory)

    else:
      print('\nLIAR!')

      print("\nCome back when you have the proper inventory!\n")

      print("You have been teleported back to the planet Mercury.")
      room1(playerInventory)
  
  elif invItems=='no':
    
    print("Come back when you have the proper inventory!")

    print("You have been teleported back to the planet Mercury.")
    room1(playerInventory)
  
  else:

    print("Let's try that again, maybe check your spelling\n")
    bubAndUrchCheck(playerInventory)

def quitGame(inventory):

  if playerInventory==[]:

    print("\nYou finished the game with nothing in your inventory, truly amazing.")
  
  else:
    count=1
    print("\nFinal Inventory:")
  for item in playerInventory:
      print('\n')
      print(count,". ",item,sep='')
      count+=1
  print('\n')
  print("Thanks for playing!\n")
  quit()

room1(playerInventory)
