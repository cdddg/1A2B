# encoding: utf-8
import random


class Possibility:

    def __init__(self):
        self.riddle = ''.join(random.sample(list('1234567890'), 4))
        self.alls = [str(i).zfill(4) for i in range(123, 10000) if len(set(str(i).zfill(4))) == 4]
        self.solves = []


class XAYB(Possibility):

    def __init__(self):
        super().__init__()
        # print(vars(self))

    @classmethod
    def compare(cls, riddle, answer):
        a, b = 0, 0
        # index, value
        for i, v  in enumerate(answer):
            if v in riddle:
                if v == riddle[i]:
                    a += 1
                else:
                    b += 1
        return a, b

    @classmethod
    def remaining(cls, answer, warehouse, a, b):
        '''取得剩餘的可能數'''
        # N個不同物件中一次取出R個的'組合'數為: N!/(R!*(N-R)!)
        response = []
        for number in warehouse:
            _a, _b = 0, 0
            for i, v in enumerate(answer):
                _a += 1 if v == number[i] else 0
                _b += 1 if v in number else 0
            if _a == a and (_b - _a) == b:
                response += [number]
        return response


class GameMode(XAYB):

    def __init__(self):
        super().__init__()

    def player2pc(self):
        '''player solve pc'''

        warehouse = self.alls
        n = 0
        while 1:
            n += 1
            answer = input('-' * 15 + ' input: ')
            a, b = self.compare(self.riddle, answer)
            print(f'{n}, {answer}, {a}A{b}B')
            if a < 4:
                solves = self.remaining(answer, warehouse, a, b)
                warehouse = solves
            else:
                return answer

    def pc2pc(self):
        '''pc1 solove pc2 riddle'''
        answer = random.choice(self.alls)
        warehouse = self.alls
        n = 0
        while 1:
            n += 1
            a, b = self.compare(self.riddle, answer)
            print(f'{n}, {answer}, {a}A{b}B')
            if a < 4:
                solves = self.remaining(answer, warehouse, a, b)
                answer = random.choice(solves)
                warehouse = solves
            else:
                return answer

    def pc2player(self, player_riddle):
        '''pc solove player riddle'''
        self.riddle = player_riddle
        answer = random.choice(self.alls)
        warehouse = self.alls
        n = 0
        while 1:
            n += 1
            a, b = self.compare(self.riddle, answer)
            print(f'{n}, {answer}, {a}A{b}B')
            if a < 4:
                solves = self.remaining(answer, warehouse, a, b)
                answer = random.choice(solves)
                warehouse = solves
            else:
                return answer


if __name__ == '__main__':
    print(GameMode().player2pc.__doc__)
    GameMode().player2pc()

    print(GameMode().pc2pc.__doc__)
    GameMode().pc2pc()

    print(GameMode().pc2player.__doc__)
    GameMode().pc2player(input(':'))

