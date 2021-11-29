print("Welcome to Choose Your Own Adventure! After each option in the story, type your response and press ENTER.")
name = input('Enter your name:')
setting = input('Enter the setting:')
def intro():
  print("Your name is {n} and you’re currently on a streetside in {s} waiting to get in a taxi.".format(s= setting, n=name))
  print("Once you step in the driver asks you where you want to go")
  print('1: Village')
  print('2: Airport')
  print('3: Gas Station')
  i = input("Your choice: ")
  if i == "1":
    village()
  elif i == "2":
    airport()
  elif i == "3":
    gasstation()
  else:
    intro()

#Original Options
def village():
  print("The drive begins and you see a variety of exotic scenery on your way there. Once you arrive at the Village Entrance, the driver drops you off and you decide where to go")
  print('1: The Library')
  print('2: A Diner')
  print('3: A Sketchy Alleyway')
  i = input("Your choice: ")
  if i == "1":
    library()
  elif i == "2":
    diner()
  elif i == "3":
    alley()
  else:
    village()

def airport():
  print("The driver leaves you at a nearby airport and you realize you don’t have enough money to get a flight…")
  print('1: Rob Someone')
  print('2: Look through the trash')
  print('3: Sneak on to the flight')
  i = input("Your choice: ")
  if i == "1":
    rob()
  elif i == "2":
    trash()
  elif i == "3":
    sneak()
  else:
    airport()

def gasstation():
  print("The driver drops you off at a gas station just a few miles away. You enter to find some cheap food when you’re suddenly surrounded by 3 ominous men.")
  print('1: Start a Fight')
  print('2: Ignore them')
  print('3: Strike up a conversation')
  i = input("Your choice: ")
  if i == "1":
    fight()
  elif i == "2":
    ignore()
  elif i == "3":
    convo()
  else:
    gasstation()

#Second Set of Options: Village
def library():
  print("At the library you begin to read and read until the sun has set. The very next day and the day after that you do the same. You realize after a week or so of reading that you’ve gained enough knowledge to do something amazing.")
  print('1: Conquer the World')
  print('2: Start a Business')
  i = input("Your choice: ")
  if i == "1":
    conquer()
  elif i == "2":
    busi()
  else:
    library()
  
def diner():
  print("At the diner you suddenly feel the pangs of hunger that made you visit the diner in the first place. However, after entering, you realize that although the diner is in pristine condition, it is completely abandoned and you are the only one in there.")
  print('1: Renovate and Run the Diner')
  print('2: Wait')
  i = input("Your choice: ")
  if i == "1":
    renovate()
  elif i == "2":
    wait()
  else:
    diner()
  
def alley():
  print("In the sketchy alleyway you expect to get robbed, but instead you meet a peculiar, mysterious man standing there.")
  print("He says, “It takes guts to walk into a sketchy alleyway instead of just going to a library or diner. I now offer you a choice: Red pill, or Blue pill?”")
  print('1: Take the Red Pill')
  print('2: Take the Blue Pill')
  i = input("Your choice: ")
  if i == "1":
    red()
  elif i == "2":
    blue()
  else:
    alley()

#Second Set of Options: Airport
def rob():
  print("You try your hand at pickpocketing, yet the first person you try it on realizes what’s happening and immediately punches you in the face, knocking you unconscious. Congratulations, You’ve completed the “Don’t Steal” ending!")

def trash():
  print("You begin to rummage through a nearby trash can when suddenly, you find a check for 100,000 dollars!")
  print('1: Cash it in')
  print('2: Try to Return it to its Owner')
  i = input("Your choice: ")
  if i == "1":
    cash()
  elif i == "2":
    good()
  else:
    trash()  
  
def sneak():
  print("You try and sneak through security to get onto the flight. It goes smoothly and you reach a sitting area before the flight. When it’s time to board, a flight attendant asks you for a ticket, and you do not comply. Two TSA agents promptly cuff you and escort you out of the premises. Congratulations, You’ve completed the “Don’t Mess with the TSA” ending!") 


#Second Set of Options: Gas station
def fight():
  print("You suddenly start a fight throwing punches left and right. The 3 men surround you, and you’re backed up to a nearby counter filled with gas station items.")
  print('1: Throw Random Food Items at them')
  print('2: Start to Sing')
  print('3: Use Martial Arts')
  i = input("Your choice: ")
  if i == "1":
    throw()
  elif i == "2":
    sing()
  elif i == "3":
    jujitsu()
  else:
    fight()
  
def ignore():
  print("You ignore them and buy your junk food. After you exit the gas station, you realize that you’re still in the middle of nowhere with no money to get a ride or more food. You live the rest of your life outside of the gas station scrounging for scraps. Congratulations, You’ve completed the “Spent All Your Money on Junk Food” ending!")

def convo():
  print("You start a conversation with the men, and they lament about how they’ve lost the fourth member of their barbershop quartet. You suddenly feel like being adventurous and volunteer to join them to sing. As a full barbershop quartet, you travel the world singing songs to all, and end up living a happy fulfilling life. Congratulations, You’ve completed the “Do Re Mi” ending!")

  
#Third Set of Options: Library
def conquer():
  print("You begin to use your knowledge and newfound charisma to start to recruit followers for your army to conquer the world. However, your plan goes awry when you realize that everyone you try to recruit thinks you are insane. Your plan to conquer the world are soon noticed by the local government and you end up on every watchlist that the government has. Congratulations,You've completed the 'Wasted Knowledge' ending.")
  
def busi():  
  print("You use your newfound entrepreneurial skills found in reading to start a small coffee shop in the village, and it quickly takes off. It becomes a popular hangout spot for all of the village and you soon have enough money to invest in another location. This snowball effect of good business continues and you become a famous philanthropist for the village and live happily ever after. Congratulations, You’ve completed the “Knowledge is Power” ending!")

  
#Third Set of Options: Diner  
def renovate():
  print("You renovate the diner into a more contemporary establishment. The diner soon becomes a popular place to grab a bite and relax, and you thoroughly enjoy running the place. However, one thing bothers you. You continuously hear a music-box noise play from the freezer, and you’ve never had the bravery to go and investigate the noise… Perhaps you shouldn’t have renovated the diner in the first place. Congratulations, You’ve completed the “Happily Ever After…?” ending!")

def wait():  
  print("You wait for what seems like hours until you suddenly hear a music box noise coming from the freezer. You slowly walk to the freezer and enter. You feel the freezer’s chilly embrace and your teeth begin to chatter. Suddenly, the music box stops. The door slams shut on its own. The lights go out. You’re completely alone in the cold darkness of the freezer, when suddenly the music-box starts back up again. It plays louder and louder, and you begin to hear a growl come from the deepest recesses of the freezer… Congratulations, You’ve completed the “Cursed Diner” ending!")


#Third Set of Options: Alley  
def red():
  print("You reluctantly take the red pill. Suddenly, a shift in your reality occurs. You realize all the truths of the universe you are in. You are in a simulation experiment executed by a program named PYTHON. All the choices thus far have been predetermined and you have merely been an actor for another’s entertainment. This world you live in, this alleyway…It’s all just a game. Congratulations, You’ve completed the “Escaping the Matrix” ending!")

def blue():
  print("You take the blue pill. You suddenly black out. When you wake up, you realize that your name is {n} and you’re currently on a streetside in {s} waiting to get in a taxi… Congratulations, You’ve completed the “Stuck in the Simulation” ending!".format(s= setting, n=name))

  
#Third Set of Options: Trash
def cash():
  print("You attempt to cash it in at a nearby bank. The cashier takes one look at the check and asks you for your name, and you proudly respond, “{n}!”. She then promptly orders an officer to arrest you for attempting to cash in a check that doesn’t belong to you… Congratulations, You’ve completed the “Committing Check Fraud” ending!" .format(n=name))

def good():
  print("You look for a potential owner of the check, when you suddenly find a man who appears to be distraught. He tells you that he’s looking for a check that he was supposed to deliver to a charity far away. You happily give him the check and he accepts it and thanks you with tremendous gratitude. He then offers you a job to work for him due to your kind deed, and you accept. You work as an assistant for this wealthy philanthropist for quite a while, amassing quite a fortune yourself. You then retire and live out the rest of your days happy and fulfilled. Congratulations, You’ve completed the “Good Samaritan” ending!")

  
#Third Set of Options: Fight
def throw():
  print("You throw random food items at them, such as Cheese Puffs, Hot Dogs, etc., but this works to no avail. You finally submit yourself to them, but surprisingly the three men don’t want to fight. They leave you alone and you complete your trip to the gas station. Congratulations! You’ve completed the “Entirely Normal Gas Station Visit” ending!")

def sing():
  print("Weirdly, you decide to sing. The three men admire your surprisingly great voice and well up with tears. After you finish, they lament and tell you about how they lost the fourth member of their barbershop quartet. You suddenly feel like being adventurous and volunteer to join them to sing. As a full barbershop quartet, you travel the world singing songs to all, and end up living a happy fulfilling life. Congratulations, You’ve completed the “Alternate Do Re Mi” ending!")

def jujitsu():
  print("You get into a fighting stance. ‘Eye of the Tiger’ begins to blare in the background. You attempt to pull off the rare Triple-Tiger-Crane-Kick-Lethal-Punch-Maneuver…… Oh wait, you don’t actually know martial arts, do you? Congratulations, You’ve unlocked the “Failed Karate Kid Impression” ending!") 

intro()
