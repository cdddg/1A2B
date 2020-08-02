import argparse
import random


class Possibility:
    def __init__(self):
        self.riddle = ''.join(random.sample(list('1234567890'), 4))
        self.alls = [str(i).zfill(4) for i in range(123, 10000) if len(set(str(i).zfill(4))) == 4]
        self.solves = []


class NAMB(Possibility):
    def __init__(self):
        super().__init__()

    @classmethod
    def compare(cls, riddle: str, answer: list) -> (int, int):
        a, b = 0, 0
        # index, value
        for i, v in enumerate(answer):
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


class GameMode(NAMB):
    def __init__(self):
        super().__init__()

    def __input(self, description):
        return input(f'{description}')

    def player2pc(self):
        '''player solve the pc riddle'''
        warehouse = self.alls

        n = 0
        while 1:
            n += 1
            answer = self.__input('input: ')
            a, b = self.compare(self.riddle, answer)
            print(f'player, {n}, {answer}, {a}A{b}B')
            if a < 4:
                solves = self.remaining(answer, warehouse, a, b)
                warehouse = solves
            else:
                return answer

    def pc2pc(self):
        '''pc1 solve the pc2 riddle'''
        answer = random.choice(self.alls)
        warehouse = self.alls

        n = 0
        while 1:
            n += 1
            a, b = self.compare(self.riddle, answer)
            print(f'pc1, {n}, {answer}, {a}A{b}B')
            if a < 4:
                solves = self.remaining(answer, warehouse, a, b)
                answer = random.choice(solves)
                warehouse = solves
            else:
                return answer

    def pc2player(self):
        '''pc solve the player riddle'''
        self.riddle = self.__input('input player riddle: ')
        answer = random.choice(self.alls)
        warehouse = self.alls

        n = 0
        while 1:
            n += 1
            a, b = self.compare(self.riddle, answer)
            print(f'pc, {n}, {answer}, {a}A{b}B')
            if a < 4:
                solves = self.remaining(answer, warehouse, a, b)
                answer = random.choice(solves)
                warehouse = solves
            else:
                return answer

    def pc2prompt(self):
        '''pc solve the problem according to the prompt'''
        warehouse = self.alls
        answer = self.__input('first number input: ')
        a = int(self.__input('a: '))
        b = int(self.__input('b: '))

        n = 0
        while 1:
            n += 1
            print(f'pc, {n}, {answer}, {a}A{b}B')
            if a < 4:
                solves = self.remaining(answer, warehouse, a, b)
                answer = random.choice(solves)
                warehouse = solves
                print(f'--next answer, {answer}')
                a = int(self.__input('a: '))
                b = int(self.__input('b: '))
            else:
                return answer


if __name__ == '__main__':
    game = GameMode()
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    for mode in [game.player2pc, game.pc2pc, game.pc2player, game.pc2prompt]:
        group.add_argument(f'--{mode.__name__}', action='store_true', help=f'{mode.__doc__}')
    args = parser.parse_args()
    for k, v in args.__dict__.items():
        if v is True:
            func = getattr(game, k)
            func()
            print('--end')
