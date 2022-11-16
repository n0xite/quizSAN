#  TODO
# * 1. Randomly generate questions -> load csv as a database
# * 2. Display messages / questions
# * 3. Receive input
# * 4. Verify answers / remove the question from available pool if the answer was correct
# * 5. Add points / end game depending on answer
# * PERSONAL CHALLANGE : try to keep it under 100 lines of code

from pyfiglet import Figlet
from colorama import Fore
import random
import pandas as pd





class Quiz:

    points = 100
    modifer = [100 ,200, 500, 1000, 5000, 10000, 50000]
    qNumber = 1
    def Init(self):
        f = Figlet(font='alligator')
        print(Fore.CYAN + f.renderText('Quiz \n') + Fore.WHITE)

    def csvHandler(self):
        data = pd.read_csv('../db.csv')
        return data

    def questionHandler(self, p):
        data = self.csvHandler()
        ID = random.randrange(1, len(data.index))
        qID = random.randrange(4)
        while data['KATEGORIA'][ID] != p:
            ID = random.randrange(1, len(data.index))
        self.answers = [data['PIERWSZA'][ID], data['DRUGA'][ID], data['TRZECIA'][ID], data['CZWARTA'][ID]]
        self.qOrder = []
        print(data['KATEGORIA'][ID])
        print(data['TREŚĆ PYTANIA'][ID])

        while len(self.qOrder) != 4:
            qID = random.randrange(4)
            if qID not in self.qOrder:
                self.qOrder.append(qID)
                qID = random.randrange(4)
            else:
                qID = random.randrange(4)


        print('A ' + self.answers[self.qOrder[0]])
        print('B ' + self.answers[self.qOrder[1]])
        print('C ' + self.answers[self.qOrder[2]]) #because of this approach, for loop is omitted
        print('D ' + self.answers[self.qOrder[3]])

        self.verify()

    def verify(self):
        a = input('Prawidłowa odpowiedź to odpowiedź: ')
        UserAnswer = ''
        match(a):
            case 'A':
                UserAnswer = self.answers[self.qOrder[0]]
            case 'B':
                UserAnswer = self.answers[self.qOrder[1]]
            case 'C':
                UserAnswer = self.answers[self.qOrder[2]]
            case 'D':
                UserAnswer = self.answers[self.qOrder[3]]


        if UserAnswer == self.answers[0]:
            if Quiz.points == 50000:
                print(Fore.GREEN + 'Gratulacje! Wygrywasz!')
                exit(0)

            Quiz.points = Quiz.modifer[Quiz.qNumber]
            Quiz.qNumber += 1
            print('To poprawna odpowiedź! \n')
            Quiz.questionHandler(self, Quiz.points)

        else:
            print('Koniec gry!')
            exit(0)



if __name__ == '__main__':
    q = Quiz()
    q.Init()
    q.questionHandler(Quiz.points)
    q.verify()

