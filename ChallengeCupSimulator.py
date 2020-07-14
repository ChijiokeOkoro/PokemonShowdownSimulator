from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import PokemonMoveCalculator
import GetTyping
import random
import time

clicker = webdriver.Chrome()


# go to the pokemon showdown home page and enter
clicker.get('https://pokemonshowdown.com/')
clicker.maximize_window()
clicker.find_element_by_xpath('//a[@class="button greenbutton"]').click()
time.sleep(5)

# sign in to user account
clicker.find_element_by_xpath('//button[@name="login"]').click()
clicker.find_element_by_xpath('//input[@class="textbox autofocus"]').send_keys('TesterAcct')
clicker.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(2)

# enter in password and log in
clicker.find_element_by_xpath('//input[@type="password"]').send_keys('password')
clicker.find_element_by_xpath('//strong[text()="Log in"]').submit()
time.sleep(2)

# select a metagame provided on showdown
clicker.find_element_by_xpath('//button[@class="select formatselect"]').click()
clicker.find_element_by_xpath('//button[@value="gen8challengecup1v1"]').click()

# Would advise user to mute volume before continuing
# select the amount of games that you want to play
loop = input("Enter how many games you want to play: ")
loopInt = int(loop)
games = 0

while games < loopInt:
# click the "Battle!" button and wait 60 secs for a game to occur
    clicker.find_element_by_xpath('//button[@class="button mainmenu1 big"]').click()

    try: # found a battle against opponent

    # turns on timer and sends message to opponent
        WebDriverWait(clicker, 600).until(EC.url_contains('gen8challengecup1v1'))
        try:
            clicker.find_element_by_xpath('//button[@class="button timerbutton"]').click()
            clicker.find_element_by_xpath('//button[@name="timerOn"]').click()
        except:
            pass
# messages intro for opponent
        clicker.find_element_by_xpath('//textarea[@placeholder]').send_keys('GL HF!')
        clicker.find_element_by_xpath('//textarea[@placeholder]').submit()

# gets the names of each player
        names = clicker.find_elements_by_xpath('//div[@class="trainer"]')
        start = 'Battle started between ' + names[0].text + ' and ' + names[1].text + '!'

# chooses a random pokemon to fight
        pokemon = random.randint(0,5)
        time.sleep(1)

        if pokemon == 0:
            choice = clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|0"]').text
            clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|0"]').click()
        elif pokemon == 1:
            choice = clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|1"]').text
            clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|1"]').click()
        elif pokemon == 2:
            choice = clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|2"]').text
            clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|2"]').click()
        elif pokemon == 3:
            choice = clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|3"]').text
            clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|3"]').click()
        elif pokemon == 4:
            choice = clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|4"]').text
            clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|4"]').click()
        else:
            choice = clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|5"]').text
            clicker.find_element_by_xpath('//button[@data-tooltip="switchpokemon|5"]').click()

# waits until opponent has chosen mon for 300
        battle = 0
        started = 0
        while battle < 60 and started == 0: # waits 3 minutes for the opponent to select a pokemon
            try:  # both players have selected a mon and the battle will commence
                WebDriverWait(clicker,3).until(EC.visibility_of(clicker.find_element_by_xpath('//div[@class="battle-history"]')))
                print('Reached battle now will start')
                started = 1
                time.sleep(2)
                mons = clicker.find_elements_by_xpath('//div[@class="battle-history"]//strong')
                monstr = []
                for x in mons:
                    monstr.append(x.text)
            except: # both players are still selecting a mon
                time.sleep(3)
                battle+=1

    # gets your mons and opponents typing
        types = GetTyping.typings(mons[0].text, mons[1].text)

        battleEnd = 0
        turn = 1
        while battleEnd == 0:
            try: # end of battle has occurred
                WebDriverWait(clicker,5).until(EC.visibility_of(clicker.find_element_by_xpath('//*[text()=" won the battle!"]')))
                clicker.find_element_by_xpath('//textarea[@placeholder]').send_keys('gg wp!')
                clicker.find_element_by_xpath('//textarea[@placeholder]').submit()
                clicker.find_element_by_xpath('//button[@class="closebutton"]').click()
                print('Battle has ended')
                battleEnd = 1
                games+=1
            except: # waits for the next turn to occur
                turnEnd = 0
                turnStr = '"Turn ' + str(turn) + '"'
                while turnEnd == 0:
                    try: # selects the move from the movepool
                        WebDriverWait(clicker, 5).until(
                            EC.visibility_of(clicker.find_element_by_xpath('//*[text()='+ turnStr +']')))
                        moves = clicker.find_elements_by_name('chooseMove')
                        move = PokemonMoveCalculator.calcpower(moves, types, monstr, choice)
                        moves[move].click()
                        turn+=1
                        turnEnd = 1
                    except: #checks if battle has ended
                        try:
                            WebDriverWait(clicker, 300).until(
                                EC.visibility_of(clicker.find_element_by_xpath('//*[text()=" won the battle!"]')))
                            clicker.find_element_by_xpath('//textarea[@placeholder]').send_keys('gg wp!')
                            clicker.find_element_by_xpath('//textarea[@placeholder]').submit()
                            clicker.find_element_by_xpath('//button[@class="closebutton"]').click()
                            battleEnd = 1
                            turnEnd = 1
                            games +=1
                        except:
                            pass
                        pass
                pass



    except: # unable to find a battle and terminates the loop
        games = loopInt
        clicker.find_element_by_xpath('//button[@name="cancelSearch"]').click()
        clicker.close()


time.sleep(3)
try:
    clicker.close()
    print('Code terminated')
except:
    print('Code terminated')
