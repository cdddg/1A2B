# ！/usr/bin/env python
# encoding: utf-8

import random
import os
import csv

googloDinosaur = """                        
                                     MqggGq6p6ZZZ6ZZpZp6pMk           
                                  lLTDDRDRDDDRDDDDDRDRDRDRDic:        
                                  DDDMR:  YDg#d#dgd#g#d#g#MDDS        
                                  RDGdBXiiZMgqgqgqgdgqgdgqg#Dl        
                                  MDdddBRDMgqg6gqgdgq#qgd#dGRJ        
                                  BRgqgd#dgdgq##BBRBDBDBRBDRDU        
                                  MDqg6gqgqgqggMgBMBMBBDRDRDRk        
                                  BR#qgqdqddggD2                      
                                  gDddqgqdqg#DRDdGMBMBBD              
      ,Kk                      :Y;MMgdgqgqgGB::rcckKkUOX              
      YDD,                 .,. GRDMgqdqgqgqBM                         
      iRD.                 MDRDRGggqgqgqgqgMR                         
      ;DBBRD           DRDDDMM##qgqdqdqddddGDDDDDDk                   
      iDMGRDqMk     JBqDDMBg#qdqgdgqg6dqgq#MD  :DDp                   
      iD#gdMRDBYYUlYGDRMdgdgqdqg6gdgqdqgdgqRR   iY,                   
      LDDG#d#gBDDRDDRdgqdqgqdqdqgqgqdqgqgq#RD                         
      iDdBRBg#d#g#dgdg6gqgqgqg6gqdqgddqgd#RDR                         
         PDDDG#qgqd6g6gqgqdqgqdqd6gqgqggMDJ;Y                         
            DDRMg#qgqgqgqgqdqgqdqgqgq##DRD.                           
            ,.rDDD#dgdgqddgqgqgqgqgqBRDS.:                            
               k7QDDM#qgqgd#MDDBd#qBq7K,                              
                 ,BS#G#qg#BRMSoMDMGDS                                 
                    TDgGMRRDL  ODBBDp                                 
                    XRBRDM        GRq                                 
                    ODM           MDo                                 
                    dDDrLi        DRDYp;                              
                    cM6RDG        QGgDRK


\t\t\t\tGuess the number of game

For a set of numbers guessed, if the number is correct and the position is correct,
you get "A". If the number is correct and wrong, 
you get "B". Follow the prompts to guess the answer and finally get the correct answer.

\t\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\t\t┃\t\tpress Enter to start\t\t┃
\t\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""


class YAXB(object):

    def __init__(self):
        print('setting default all answer list.')
        self.player1_random = ""
        self.random = "".join(random.sample(list('1234567890'), 4))
        self.numarray = list()
        for i in range(123, 10000):
            i = str(i)
            if len(i) == 3:
                i = '0' + str(i)
            if len(i) == len(set(i)):
                self.numarray += [i]

    def create_random(self):
        self.random = "".join(random.sample(list('1234567890'), 4))

    @staticmethod
    def check_format(answer):
        if len(answer) != 4:
            resp = (False, 'Format error, please re-Input your answer')
        else:
            try:
                """Check if the value entered is a number"""
                int(answer)
                if len(answer) == len(set(answer)):
                    resp = (True, '')
                else:
                    resp = (False, 'Format error, please re-Input your answer')
            except ValueError:
                resp = (False, 'Format error, please re-Input your answer')

        return resp

    def calculation(self, answer, source):
        randomNumber = self.random if source == 'pc' else self.player1_random
        a, b = 0, 0
        for i in range(4):
            if answer[i] in randomNumber:
                if answer[i] == randomNumber[i]:
                    a += 1
                else:
                    b += 1
        return a, b

    def probability(self, answer_pc):
        default = self.numarray
        text = [self.random, 'Time']
        loop = 0
        while 1:
            loop += 1
            pr = list()
            a, b = self.calculation(answer=answer_pc, source='pc')
            """Find numbers that are probability answer"""
            for number in default:
                _a, _b = 0, 0
                for j in range(4):
                    _a += 1 if answer_pc[j] == number[j] else 0
                    _b += 1 if answer_pc[j] in number else 0
                if _a == a and (_b - _a) == b:
                    pr += [number]

            print(loop, "", answer_pc, f'{a}A{b}B')
            text += [f'{answer_pc} {a}A{b}B']
            """Break out for the correct answer"""
            if a == 4:
                break
            else:
                default = pr
                answer_pc = random.choice(pr)

        text[1] = loop
        return text

    def probability_player1(self, answer_pc):
        while 1:
            self.player1_random = input('Input your answer: ')
            boolean, message = self.check_format(answer=self.player1_random)
            if boolean:
                break
            else:
                print(message)

        printText = ""
        text = [['Time']]
        default = self.numarray
        loop = 0
        while 1:
            loop += 1
            while True:
                answer_p1 = input(f'\nPlease enter the number you guessed - round{loop}: ')
                boolean, message = self.check_format(answer=answer_p1)
                if boolean:
                    break
                else:
                    print(message)
            p1_a, p1_b = self.calculation(answer=answer_p1, source='pc')
            pc_a, pc_b = self.calculation(answer=answer_pc, source='player1')

            pr = list()
            """Find numbers that are probability answer"""
            for number in default:
                _a, _b = 0, 0
                for j in range(4):
                    _a += 1 if answer_pc[j] == number[j] else 0
                    _b += 1 if answer_pc[j] in number else 0
                if _a == pc_a and (_b - _a) == pc_b:
                    pr += [number]

            os.system('cls')
            t = [f'{loop}', f'Player:{answer_p1} {p1_a}A{p1_b}B', f'PC:{answer_pc} {pc_a}A{pc_b}B']
            text += [t]
            printText += '\n' + "\t".join(t)
            print(printText)

            """Break out for the correct answer"""
            if p1_a == 4 or pc_a == 4:
                p1_result, pc_result = "", ""
                if p1_a == pc_a:
                    p1_result = pc_result = 'Deuce'
                elif p1_a > pc_a:
                    p1_result = 'Player-Winner (Player answer:%s)' % self.player1_random
                elif p1_a < pc_a:
                    pc_result = 'PC-Winner (PC answer:%s)' % self.random
                text += [['answer', self.player1_random, self.random]]
                text += [['result', p1_result, pc_result]]

                while True:
                    endGame = input(f'\n{p1_result} {pc_result}, Restart game (y/n)').lower()
                    if endGame == 'y':
                        return True, text
                    elif endGame == 'n':
                        return False, text
            else:
                default = pr
                answer_pc = random.choice(pr)
        # N個不同物件中一次取出R個的'組合'數為: N!/(R!*(N-R)!)


class Playmode(object):
    def main(self):
        print(f'{googloDinosaur}\n')

        while True:
            os.system('cls')
            print('Welcome to guess the number of game, please to select game mode.\n')
            print('1. Random mode  - Computer to answer exercises.')
            print('2. Players mode  - Players against computer.')

            mode = input(': ')
            if mode == '1':
                while True:
                    try:
                        num = input('Please enter the number of rounds\n: ')
                        int(num)
                        break
                    except ValueError:
                        pass
                self.pcgame(int(num))
            elif mode == '2':
                self.player1()

    @staticmethod
    def pcgame(num=1):
        AB = YAXB()
        num = int(num)
        text = [
            ['Random', 'Time', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['max', '0'],
            ['min', '0']
        ]
        max_v, min_v, loop = 0, 0, 1

        while loop <= num:
            AB.create_random()
            answer = ''.join(random.sample(list('1234567890'), 4))
            resp = AB.probability(answer_pc=answer)
            text += [resp]
            max_v = int(resp[1]) if loop == 1 else (int(resp[1]) if int(resp[1]) > max_v else max_v)
            min_v = int(resp[1]) if loop == 1 else (int(resp[1]) if int(resp[1]) < min_v else min_v)
            loop += 1
            print(max_v, min_v)
            print('-')

        text[1][1] = str(max_v)
        text[2][1] = str(min_v)
        f = open('1A2B.csv', 'w+', newline='')
        csvCursor = csv.writer(f)
        csvCursor.writerows(text)
        f.close()
        ifexit = input('Records is saving. press key to exit. (y/n)').lower()
        if ifexit == 'y':
            exit()

    @staticmethod
    def player1():
        AB = YAXB()
        text = [['Player to PC mode']]
        loop = 0

        while True:
            loop += 1
            text += [[], [f'Round{loop}']]
            os.system('cls')
            answer = ''.join(random.sample(list('1234567890'), 4))
            resp = AB.probability_player1(answer)
            text += [_ for _ in resp[1]]
            text += []
            if not resp[0]:
                break

        f = open('1A2B.csv', 'w+', newline='')
        csvCursor = csv.writer(f)
        csvCursor.writerows(text)
        f.close()
        input('Records is saving. press key to exit.')

    # def Player2(self):
    #     pass


if __name__ == '__main__':
    Playmode().main()
