from random import randint
from collections import Counter


def max_replicated(list):  # 用来判断two pair 或one pair
    i = 0
    L = []
    while (i < len(list)):
        L.append(list.count(list[i]))
        i = i + 1
    return max(L)


def play():
    dic = {0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Jack', 4: '10', 5: '9'}
    L = []
    P = []
    for i in range(0, 5):
        value = randint(0, 5)
        L.append(dic[value])
        P.append(value)
    L.sort()
    P.sort()
    Q = ' '.join(str(i) for i in P)
    Out = Q.replace("0", 'Ace').replace('1', 'King').replace('2', 'Queen').replace('3', 'Jack').replace('4',
                                                                                                        '10').replace(
        '5', '9')

    print('The roll is:', Out)
    if max_replicated(P) == 5:
        print('It is a Five of a kind')
        check_input_2nd(L)

    if max_replicated(P) == 4:
        print('It is a Four of a kind')
        check_input_2nd(L)

    if (max_replicated(P) == 3):
        if (len(set(P)) == 2):
            print('It is a Full house')
            check_input_2nd(L)
        else:
            print('It is a Three of a kind')
            check_input_2nd(L)

    if (max_replicated(P) == 2):
        if (len(set(P)) == 3):
            print('It is a Two pair')
            check_input_2nd(L)
        else:
            print('It is a One pair')
            check_input_2nd(L)
    if (max_replicated(P) == 1):
        if sum(P) == 10 or sum(P) == 15:
            print('It is a Straight')
            check_input_2nd(L)
        else:
            print('It is a Bust')
            check_input_2nd(L)


# REPLACE PASS ABOVE WITH YOUR CODE

def check_input_2nd(L):
    u = input('Which dice do you want to keep for the second roll? ')
    Y = u.split(' ')
    Y.sort()
    if (u == 'all' or u == 'All' or Y == L):
        print('Ok, done.')
        return
    else:
        C1 = Counter(Y)
        C2 = Counter(L)
        if (all(value <= C2[key] for key, value in C1.items()) or u == ''):
            second_roll(u)
            return
        else:
            print('That is not possible, try again!')
            check_input_2nd(L)
            return


def check_input_3nd(L):
    v = input('Which dice do you want to keep for the third roll? ')
    Y = v.split(' ')
    Y.sort()
    if (v == 'all' or v == 'All' or Y == L):
        print('Ok, done.')
        return
    else:
        C1 = Counter(Y)
        C2 = Counter(L)
        if (all(value <= C2[key] for key, value in C1.items()) or v == ''):
            third_roll(v)
            return
        else:
            print('That is not possible, try again!')
            check_input_3nd(L)
            return


# REPLACE PASS ABOVE WITH YOUR CODE
def third_roll(v):
    dic = {0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Jack', 4: '10', 5: '9'}
    dic1 = {'Ace': 0, 'King': 1, 'Queen': 2, 'Jack': 3, '10': 4, '9': 5}
    if v == '':
        L = []
        P = []
        for i in range(0, 5):
            value = randint(0, 5)
            P.append(value)
            L.append(dic[value])
    else:
        list = v.split(' ')
        L = []
        P = []
        for i in range(0, 5 - len(list)):
            value = randint(0, 5)
            L.append(dic[value])

        L = L + list
        for i in range(0, len(L)):
            r = L[i]
            P.append(dic1[r])
    L.sort()
    P.sort()
    Q = ' '.join(str(i) for i in P)
    Out = Q.replace("0", 'Ace').replace('1', 'King').replace('2', 'Queen').replace('3', 'Jack').replace('4',
                                                                                                        '10').replace(
        '5', '9')
    print('The roll is:', Out)

    if max_replicated(P) == 5:
        print('It is a Five of a kind')
    if max_replicated(P) == 4:
        print('It is a Four of a kind')
    if (max_replicated(P) == 3):
        if (len(set(P)) == 2):
            print('It is a Full house')
        else:
            print('It is a Three of a kind')
    if (max_replicated(P) == 2):
        if (len(set(P)) == 3):
            print('It is a Two pair')
        else:
            print('It is a One pair')
    if (max_replicated(P) == 1):
        if sum(P) == 10 or sum(P) == 15:
            print('It is a Straight')
        else:
            print('It is a Bust')


def second_roll(u):
    dic = {0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Jack', 4: '10', 5: '9'}
    dic1 = {'Ace': 0, 'King': 1, 'Queen': 2, 'Jack': 3, '10': 4, '9': 5}
    if u == '':
        L = []
        P = []
        for i in range(0, 5):
            value = randint(0, 5)
            P.append(value)
            L.append(dic[value])
    else:
        list = u.split(' ')
        L = []
        P = []
        for i in range(0, 5 - len(list)):
            value = randint(0, 5)
            L.append(dic[value])

        L = L + list
        for i in range(0, len(L)):
            r = L[i]
            P.append(dic1[r])
    L.sort()
    P.sort()
    Q = ' '.join(str(i) for i in P)
    Out = Q.replace("0", 'Ace').replace('1', 'King').replace('2', 'Queen').replace('3', 'Jack').replace('4',
                                                                                                        '10').replace(
        '5', '9')
    print('The roll is:', Out)

    if max_replicated(P) == 5:
        print('It is a Five of a kind')
        check_input_3nd(L)

    if max_replicated(P) == 4:
        print('It is a Four of a kind')
        check_input_3nd(L)

    if (max_replicated(P) == 3):
        if (len(set(P)) == 2):
            print('It is a Full house')
            check_input_3nd(L)
        else:
            print('It is a Three of a kind')
            check_input_3nd(L)

    if (max_replicated(P) == 2):
        if (len(set(P)) == 3):
            print('It is a Two pair')
            check_input_3nd(L)
        else:
            print('It is a One pair')
            check_input_3nd(L)
    if (max_replicated(P) == 1):
        if sum(P) == 10 or sum(P) == 15:
            print('It is a Straight')
            check_input_3nd(L)
        else:
            print('It is a Bust')
            check_input_3nd(L)


def simulate(n):
    dic = {0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Jack', 4: '10', 5: '9'}
    dic1 = {'A': 'Five of a kind :', 'B': 'Four of a kind :', 'C': 'Full house     :', 'D': 'Straight       :',
            'E': 'Three of a kind:',
            'F': 'Two pair       :', 'G': 'One pair       :'}
    a = 0;
    b = 0;
    c = 0;
    d = 0;
    e = 0;
    f = 0;
    g = 0;
    h = 0
    for j in range(0, n):
        P = []
        for i in range(0, 5):
            value = randint(0, 5)
            P.append(value)
        if max_replicated(P) == 5:
            a = a + 1
        if max_replicated(P) == 4:
            b = b + 1
        if (max_replicated(P) == 3):
            if (len(set(P)) == 2):
                c = c + 1
            else:
                e = e + 1
        if (max_replicated(P) == 2):
            if (len(set(P)) == 3):
                f = f + 1
            else:
                g = g + 1
        if (max_replicated(P) == 1):
            if sum(P) == 10 or sum(P) == 15:
                d = d + 1
            else:
                h = h + 1

    print(dic1['A'], '{:.2%}'.format(a / n))
    print(dic1['B'], '{:.2%}'.format(b / n))
    print(dic1['C'], '{:.2%}'.format(c / n))
    print(dic1['D'], '{:.2%}'.format(d / n))
    print(dic1['E'], '{:.2%}'.format(e / n))
    print(dic1['F'], '{:.2%}'.format(f / n))
    print(dic1['G'], '{:.2%}'.format(g / n))
    return

    # REPLACE PASS ABOVE WITH YOUR CODE

# DEFINE OTHER FUNCTIONS