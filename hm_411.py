\

def total_sal():

        time = float(input('Выработка в часах: '))
        salary = int(input('Ставка в час:  '))
        bonus = int(input('Премия:  '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')


total_sal()