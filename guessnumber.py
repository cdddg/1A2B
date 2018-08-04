# -*- coding: utf-8 -*-
"""
@Created: 2018/08/04
@Author: Cdg
@Version: ver.1
"""

import random
import os
import csv
import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
"""
SW_HIDE = 0
隱藏窗口。
SW_MAXIMIZE = 3
最大化窗口。
SW_MINIMIZE = 6
最小化窗口。
SW_RESTORE = 9
恢復窗口（未最大化或最小化）。
SW_SHOW = 5
顯示窗口。
SW_SHOWMAXIMIZED = 3
顯示窗口最大化。
SW_SHOWMINIMIZED = 2
最小化顯示窗口。
SW_SHOWMINNOACTIVE = 7
顯示最小化的窗口，但不要激活它。
SW_SHOWNA = 8
以當前狀態顯示窗口但不激活它。
SW_SHOWNOACTIVATE = 4
以最近的大小和位置顯示窗口，但不要激活它。
SW_SHOWNORMAL = 1
顯示窗口並激活它（像往常一樣）。
"""
user32.ShowWindow(kernel32.GetConsoleWindow(), 3)

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


\t\t    Guess the number of game

For a set of numbers guessed, if the number is correct and the position is correct, you get "A". If the number
is correct and wrong, you get "B". Follow the prompts to guess the answer and finally get the correct answer.



\t\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\t\t┃\tpress Enter to start    ┃
\t\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""


class YAXB(object):
    def __init__(self):
        print('setting default all answer list.')
        self.player1_random = ""
        self.random = ""
        self.numarray = list()
        self.numArray()

    def randomSetting(self):
        self.random = str.join("", random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4))
        print('Random number', self.random)

    def numArray(self):
        self.numarray = list()
        for i in range(123, 10000):
            i = str(i)
            if len(i) == 3:
                i = "0" + str(i)
            array = [i[0], i[1], i[2], i[3]]
            if i[0] != i[1] and i[0] != i[2] and i[0] != i[3] and i[1] != i[2] and i[1] != i[3] and i[2] != i[3]:
                self.numarray.append(str.join("", array))

    def calculation(self, Value, answer):
        randomList = None
        if answer == "pc":
            randomList = self.random
        elif answer == "player1":
            randomList = self.player1_random
        A = 0
        B = 0
        for i in range(4):
            if Value[i] in randomList:
                if Value[i] == randomList[i]:
                    A += 1
                else:
                    B += 1
        return A, B

    def probability(self, Value):
        answer1D_default = self.numarray
        loopTime = 0
        loop1A2B = [self.random, 'Time']
        while True:
            loopTime += 1
            answer1D_probability = []
            answer = self.calculation(Value=Value, answer="pc")
            for i in answer1D_default:
                A = 0
                B = 0
                for j in range(4):
                    if Value[j] == i[j]:
                        A += 1
                    if Value[j] in i:
                        B += 1
                if A == answer[0] and (B - A) == answer[1]:
                    answer1D_probability.append(i)
            print(loopTime, "", Value, "", str(answer[0]) + "A" + str(answer[1]) + "B")
            loop1A2B.append(Value + ' %(x)sA%(y)sB' % {"x": answer[0], "y": answer[1]})
            if answer[0] == 4:
                loop1A2B[1] = loopTime
                return loop1A2B
            else:
                answer1D_default = answer1D_probability
                Value = random.choice(answer1D_probability)

    def probability_player1Mode(self, Value_pc):
        answer1D_default = self.numarray
        loopTime = 0
        loop1A2B = []
        textJoin = ""
        #
        while True:
            player1_random = input("Input your answer: ")
            checkVal = PlayMode().check_answer_rule(player1_random)
            if checkVal[0]:
                self.player1_random = player1_random
                break
            else:
                print(checkVal[1])
        #
        while True:
            loopTime += 1
            answer1D_probability = []
            while True:
                Value_player = input("\nPlease enter the number you guessed - round%s: " % loopTime)
                checkVal = PlayMode().check_answer_rule(Value_player)
                if checkVal[0]:
                    break
                else:
                    print(checkVal[1])
            answer_player = self.calculation(Value=Value_player, answer="pc")
            answer_pc = self.calculation(Value=Value_pc, answer="player1")
            for i in answer1D_default:
                A = 0
                B = 0
                for j in range(4):
                    if Value_pc[j] == i[j]:
                        A += 1
                    if Value_pc[j] in i:
                        B += 1
                if A == answer_pc[0] and (B - A) == answer_pc[1]:
                    answer1D_probability.append(i)
            #
            text = [str(loopTime),
                    "Player:%(1)s %(2)sA%(3)sB" % {"1": Value_player, "2": answer_player[0], "3": answer_player[1]},
                    "PC:%(1)s %(2)sA%(3)sB" % {"1": Value_pc, "2": answer_pc[0], "3": answer_pc[1]}]
            textJoin = textJoin + '\n' + str.join("\t", text)
            os.system('cls')
            print(textJoin)
            loop1A2B.append(text)
            if answer_player[0] == 4 or answer_pc[0] == 4:
                result_1 = ""
                result_2 = ""
                if answer_player[0] == answer_pc[0]:
                    result_1 = "Deuce"
                    result_2 = "Deuce"
                elif answer_player[0] > answer_pc[0]:
                    result_1 = "Player-Winner (Player answer:%s)" % self.player1_random
                elif answer_player[0] < answer_pc[0]:
                    result_2 = "PC-Winner (PC answer:%s)" % self.random
                loop1A2B.append(["answer", self.player1_random, self.random])
                loop1A2B.append(["result", result_1, result_2])
                while True:
                    next = input('\n' + result_1 + " " + result_2 + ",  " + "Restart game (y/n) ").lower()
                    if next == "y":
                        return True, loop1A2B
                    elif next == 'n':
                        return False, loop1A2B
            else:
                answer1D_default = answer1D_probability
                Value_pc = random.choice(answer1D_probability)
        # N個不同物件中一次取出R個的"組合"數為: N!/(R!*(N-R)!)


class PlayMode(object):
    def progress(self):
        print(googloDinosaur)
        input("")
        os.system('cls')
        print("Welcome to guess the number of game, please to select game mode.")
        print("")
        print("1. Random mode  - Computer to answer exercises.")
        print("2. Players mode  - Players against computer.")
        while True:
            mode = input(": ")
            if mode == "1":
                while True:
                    print("Please enter the number of rounds")
                    num = input(": ")
                    try:
                        int(num)
                        break
                    except:
                        pass
                self.pcGame(int(num))
            elif mode == "2":
                self.player1()
            os.system('cls')
            print("Welcome to guess the number game, please to select game mode.")
            print("")
            print("1. Random mode  - Computer to answer exercises.")
            print("2. Players mode  - Players against computer.")

    @staticmethod
    def check_answer_rule(Value):
        if len(Value) != 4:
            return False, "Format error, please re-Input your answer"
        else:
            try:
                int(Value)
                i = Value
                if i[0] != i[1] and i[0] != i[2] and i[0] != i[3] and i[1] != i[2] and i[1] != i[3] and i[2] != i[3]:
                    return True, ""
                else:
                    return False, "Format error, please re-Input your answer"
            except:
                return False, "Format error, please re-Input your answer"

    @staticmethod
    def pcGame(num=1):
        num = int(num)
        YXAB = YAXB()
        array = [['Random', 'Time', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['max', '0'], ['min', '0']]
        max = 0
        min = 0
        loopTime = 1
        while loopTime <= num:
            # YXAB.TestRandom(LoopTime-1)
            YXAB.randomSetting()
            answer = str.join("", random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4))
            rValue = YXAB.probability(answer)
            array.append(rValue)
            if loopTime == 1:
                max = int(rValue[1])
                min = int(rValue[1])
            else:
                max = int(rValue[1]) if int(rValue[1]) > max else max
                min = int(rValue[1]) if int(rValue[1]) < min else min
            loopTime += 1
            print('_')
        array[1][1] = str(max)
        array[2][1] = str(min)
        file = open(os.getcwd() + '\\1A2B.csv', 'w+', newline='')
        csvCursor = csv.writer(file)
        csvCursor.writerows(array)
        file.close()
        input('Records is saving. press key to exit.')

    @staticmethod
    def player1():
        YXAB = YAXB()
        array = [["Player to PC mode"], []]
        loopGame = 0
        while True:
            # YXAB.TestRandom(LoopTime-1)
            loopGame += 1
            array.append(["Round%s" % str(loopGame)])
            YXAB.randomSetting()
            os.system('cls')
            answer = str.join("", random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4))
            rValue = YXAB.probability_player1Mode(answer)
            for _ in rValue[1]:
                array.append(_)
            array.append([])
            if rValue[0]:
                pass
            else:
                break
        file = open(os.getcwd() + '\\1A2B.csv', 'w+', newline='')
        csvCursor = csv.writer(file)
        csvCursor.writerows(array)
        file.close()
        input('Records is saving. press key to exit.')

    def Player2(self):
        pass


if __name__ == "__main__":
    PlayMode().progress()
