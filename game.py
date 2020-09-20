import json
from random import randint
import math

#           _____                _____                    _____                _____                    _____          
#          /\    \              /\    \                  /\    \              /\    \                  /\    \         
#         /::\    \            /::\    \                /::\    \            /::\    \                /::\    \        
#        /::::\    \           \:::\    \              /::::\    \           \:::\    \              /::::\    \       
#       /::::::\    \           \:::\    \            /::::::\    \           \:::\    \            /::::::\    \      
#      /:::/\:::\    \           \:::\    \          /:::/\:::\    \           \:::\    \          /:::/\:::\    \     
#     /:::/__\:::\    \           \:::\    \        /:::/__\:::\    \           \:::\    \        /:::/__\:::\    \    
#     \:::\   \:::\    \          /::::\    \      /::::\   \:::\    \          /::::\    \       \:::\   \:::\    \   
#   ___\:::\   \:::\    \        /::::::\    \    /::::::\   \:::\    \        /::::::\    \    ___\:::\   \:::\    \  
#  /\   \:::\   \:::\    \      /:::/\:::\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \  /\   \:::\   \:::\    \ 
# /::\   \:::\   \:::\____\    /:::/  \:::\____\/:::/  \:::\   \:::\____\    /:::/  \:::\____\/::\   \:::\   \:::\____\
# \:::\   \:::\   \::/    /   /:::/    \::/    /\::/    \:::\  /:::/    /   /:::/    \::/    /\:::\   \:::\   \::/    /
#  \:::\   \:::\   \/____/   /:::/    / \/____/  \/____/ \:::\/:::/    /   /:::/    / \/____/  \:::\   \:::\   \/____/ 
#   \:::\   \:::\    \      /:::/    /                    \::::::/    /   /:::/    /            \:::\   \:::\    \     
#    \:::\   \:::\____\    /:::/    /                      \::::/    /   /:::/    /              \:::\   \:::\____\    
#     \:::\  /:::/    /    \::/    /                       /:::/    /    \::/    /                \:::\  /:::/    /    
#      \:::\/:::/    /      \/____/                       /:::/    /      \/____/                  \:::\/:::/    /     
#       \::::::/    /                                    /:::/    /                                 \::::::/    /      
#        \::::/    /                                    /:::/    /                                   \::::/    /       
#         \::/    /                                     \::/    /                                     \::/    /        
#          \/____/                                       \/____/                                       \/____/         


class stats:
    def __init__(self, money : int = 50, trust : int = 10, political : int = 10, social : int = 10, environmental : int = 10, economic : int = 10):
        '''
        a container of information for the 6 game stats:
        money 
        trust 
        political 
        social 
        enviormental 
        economic
        '''
        self.money = money
        self.trust = trust
        self.political = political
        self.social = social
        self.environmental = environmental
        self.economic = economic
    
    def returnArray(self):
        '''
        makes array of stats:
        money 
        trust 
        political 
        social 
        enviormental 
        economic

        and returns them in same order
        '''
        toReturn = []
        toReturn.append(self.money)
        toReturn.append(self.trust)
        toReturn.append(self.political)
        toReturn.append(self.social)
        toReturn.append(self.environmental)
        toReturn.append(self.economic)

        return toReturn

    def loadFromArray(self, array : list):
        '''
        makes from array of stats:
        money 
        trust 
        political 
        social 
        enviormental 
        economic

        into seperate variables inside of object
        '''
        self.money = array[0]
        self.trust = array[1]
        self.political = array[2]
        self.social = array[3]
        self.environmental = array[4]
        self.economic = array[5]
    
    def addStuff(self, toAdd):
        '''
        add the toAdd stats object into self.

        toAdd -> stats(Object)
        '''
        self.money += toAdd.money
        self.trust += toAdd.trust
        self.political += toAdd.political
        self.social += toAdd.social
        self.environmental += toAdd.environmental
        self.economic += toAdd.economic

#           _____                    _____                    _____                    _____          
#          /\    \                  /\    \                  /\    \                  /\    \         
#         /::\    \                /::\    \                /::\____\                /::\    \        
#        /::::\    \              /::::\    \              /::::|   |               /::::\    \       
#       /::::::\    \            /::::::\    \            /:::::|   |              /::::::\    \      
#      /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/\:::\    \     
#     /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \    
#    /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /::::\   \:::\    \   
#   /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \  
#  /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \  /:::/\:::\   \:::\    \ 
# /:::/____/  ___\:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\/:::/__\:::\   \:::\____\
# \:::\    \ /\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /\:::\   \:::\   \::/    /
#  \:::\    /::\ \::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    /  \:::\   \:::\   \/____/ 
#   \:::\   \:::\ \/____/            \::::::/    /               /:::/    /    \:::\   \:::\    \     
#    \:::\   \:::\____\               \::::/    /               /:::/    /      \:::\   \:::\____\    
#     \:::\  /:::/    /               /:::/    /               /:::/    /        \:::\   \::/    /    
#      \:::\/:::/    /               /:::/    /               /:::/    /          \:::\   \/____/     
#       \::::::/    /               /:::/    /               /:::/    /            \:::\    \         
#        \::::/    /               /:::/    /               /:::/    /              \:::\____\        
#         \::/____/                \::/    /                \::/    /                \::/    /        
#                                   \/____/                  \/____/                  \/____/         

class mainGameMannager:
    def __init__(self):
        '''
        mannages the internal game. 
        All backend calculations should be done here!
        '''
        self.allJSONids = []
        self.questionaireJSONids = []

        self.playerValues = stats()
        self.AIone = stats()
        self.AItwo = stats()

        self.current = None
        self.all = self.loadAllJSON() # start with a JSON
        self.questionaire = None
        self.questions = 0
        self.currentCuestionNumber = 0
        self.calcStats = stats()

    def loadRandomJSON(self):
        '''
        loads a random JSON from self.all.

        returns 3 variables:
            title -> str
            tip -> str
            questions -> array(one element per possible answer).
                each element of the array has 4 parts, [ID, question string, type(select/input), mods(class type stats)]
        
        '''
        if self.questionaire == None:
            print('there is no info to use...')
            return False, False, False
        else:
            if len(self.questionaire) == 0:
                # codigo por si acaso queremos agregar otra cosa
                return 'no more questions', False, self.playerValues.returnArray() # podemos regresar calculos aqui!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            questionToRemove = self.questionaireJSONids.pop(randint(0,len(self.questionaireJSONids)-1))
            self.current = self.questionaire.pop(questionToRemove) # cambiar a otro
            questions = []
            tip = None
            for name in self.current:
                if name == 'question':
                    title = self.current[name]
                elif name == 'tip':
                    tip = self.current[name]
                else:
                    questions.append([name, self.current[name]['answer'], self.current[name]['type'], self.current[name]['mods']])
            
            # get AI for max thingy
            possible = []
            for i in range(len(questions)):
                possible.append(questions[i][3])
            mon = []
            trust = []
            for posibility in possible:
                mon.append(posibility[0])
                trust.append(posibility[1])
                
            mon = max(mon)
            trust = max(trust)

            for posibility in possible:
                if posibility[0] == mon:
                    self.calcStats.loadFromArray(posibility)
                    self.AIone.addStuff(self.calcStats)
                if posibility[1] == trust:
                    self.calcStats.loadFromArray(posibility)
                    self.AItwo.addStuff(self.calcStats)

            return title, tip, questions

    def updateStats(self, statClass : stats):
        '''
        updates current player values
        '''
        self.playerValues.addStuff(statClass)

    def loadAllJSON(self):
        '''
        returns json as dictionary
        '''
        with open("static/data/levels.json") as f:
            data = json.load(f)

        self.allJSONids = []
        for JSONid in data:
            self.allJSONids.append(JSONid)
        
        return data

    def startGame(self, amountOfQuestions : int):
        '''
        chooses random questions from master JSON, and stores them in questionaire
        the amount of questions it chooses is defined by amountOfQuestions
        '''
        # first, select things
        self.questionaire = {}
        self.questionaireJSONids = []

        for i in range(amountOfQuestions):
            idToAppend = self.allJSONids.pop(randint(0,len(self.allJSONids)-1))
            toAppend = self.all.pop(idToAppend)
            self.questionaire[idToAppend] = toAppend
            self.questionaireJSONids.append(idToAppend)
            print(idToAppend)
        
        # second, choose a random one
        print(self.questionaireJSONids)
        return self.loadRandomJSON()

    def updateMetricsAndReturnNext(self, metrics : list = [0,0,0,0,0,0]):
        '''
        adds metrics into playerValues

        returns randomJSON
        if no more JSON files are in current play session, returns 'no more questions', playerValues as array
        '''
        self.calcStats.loadFromArray(metrics)
        self.playerValues.addStuff(self.calcStats)

        return self.loadRandomJSON()

    def calculateVotes(self):
        
        totalVoters = 200 #CAMBIAR
        
        # money, turn into votes
    
        # self.playerVotes = abs(self.playerValues.money // 2400)
        # self.ai1votes = abs(self.AIone.money // 2400)
        # self.ai2votes = abs(self.AItwo.money // 2400)
        self.playerVotes = 0
        self.ai1votes = 0
        self.ai2votes = 0

        moneyVoters = [self.playerValues.money, self.AIone.money, self.AItwo.money] 
        self.calcProb(moneyVoters, 4000)
        
        # trust 
        # Votes %percentage
        trustVoters = [self.playerValues.trust, self.AIone.trust, self.AItwo.trust] #PASS CORRECTONE?? [012 0132 0123]
        self.calcProb(trustVoters, 4000)

        socialVoters = [self.playerValues.social, self.AIone.social, self.AItwo.social]
        self.calcProb(socialVoters, 4000)

        politicalVoters = [self.playerValues.political, self.AIone.political, self.AItwo.political]
        self.calcProb(politicalVoters,4000)
         
        environmentalVoters = [self.playerValues.environmental, self.AIone.environmental, self.AItwo.environmental]
        self.calcProb(environmentalVoters, 1000)
        
        economicVoters = [self.playerValues.economic, self.AIone.economic, self.AItwo.economic]
        self.calcProb(economicVoters, 4000)
        
        
    def calcProb(self, arr : list, voters : int = 500):
        # top everything up
        print(arr)
        minumum = min(arr)
        for i in range(3):
            arr[i] -= minumum
            arr[i] += 50
        print(arr)
        # get porcentages
        probPercentage = sum(arr)
        try:
            self.playerVotes += int(arr[0]/probPercentage * voters)
        except:
            self.playerVotes += 0
        try:
            self.ai1votes += int(arr[1]/probPercentage * voters)
        except:
            self.ai1votes += 0 
        try:
            self.ai2votes += int(arr[2]/probPercentage * voters)
        except:
            self.ai2votes +=0
        
    def gimmeWinner (self):
        return True if max([self.playerVotes, self.ai1votes, self.ai2votes]) == self.playerVotes else False


if __name__ == '__main__':
    game = mainGameMannager()
    title, tip, questions = game.startGame(3)
    print(title, tip)

    # for i in range(len(questions)):
    #     print (i, questions[i][1])

    # title, tip, questions = game.updateMetricsAndReturnNext(questions[int(input('answer > '))][3])
    # print(title, tip)

    # for i in range(len(questions)):
    #     print (i, questions[i][1])

    # title, tip, questions = game.updateMetricsAndReturnNext(questions[int(input('answer > '))][3])
    # print(title, tip)

    # for i in range(len(questions)):
    #     print (i, questions[i][1])

    # title, tip, questions = game.updateMetricsAndReturnNext(questions[int(input('answer > '))][3])

    # game.calculateVotes()

    # print(game.playerVotes, game.ai1votes, game.ai2votes)

    # print(game.gimmeWinner())

