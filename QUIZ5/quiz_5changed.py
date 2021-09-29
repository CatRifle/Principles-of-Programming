# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# In both functions below, grid is supposed to be a sequence of strings
# all of the same length, consisting of nothing but spaces and *s,
# and represent one or more "full polygons" that do not "touch" each other.


dial = {1: ['C2', 'D10', 'H7', 'D6'], 2: ['D5', 'C4', 'Dj', 'H5'], 3: ['D2', 'Hj', 'C7', 'Sk'], 4: ['D7', 'Cj', 'H9', 'S6'], 5: ['Hk', 'C1', 'C6', 'S2'], 6: ['C3', 'C9', 'S8', 'H6'], 7: ['D1', 'C10', 'S3', 'Ck'], 8: ['C5', 'H2', 'D8', 'D3'], 9: ['Dq', 'Sj', 'Sq', 'D9'], 10: ['S5', 'S9', 'Hq', 'H3'], 11: ['Dk', 'S10', 'S7', 'S4'], 12: ['H8', 'H10', 'D4', 'C8']}

centre = ['H1', 'S1', 'H4', 'Cq']


def init_posi(dial):
    i = 1
    while (i < len(dial) + 1):
        j = 0
        while (j < 4):
            L = list(dial[i][j])
            L.insert(0, '*')
            dial[i][j] = ''.join(L)
            j = j + 1
        i = i + 1
    return dial


def str_to_card(string):
    L = list(string)
    colour = L[0];
    num = L[1:]
    num = ''.join([str(i) for i in num])
    dic1 = {'S': 0, 'H': 1, 'D': 2, 'C': 3}
    dic2 = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'j': 10, 'q': 12, 'k': 13}
    first_point = 0x1F0A1
    card = chr(first_point + dic1[colour] * 16 + dic2[num])
    return card


def hour_after_playing_from_beginning_for_at_most(hour, nb_of_steps, dial, centre):
    init = centre[-1]
    L_init = list(init)
    V_init = L_init[1]
    dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 11, 'q': 12, 'k': 13, '':0}
    num_init = dic[V_init]
    dic1 = {'*': 'hidden'}
    D = init_posi(dial)
    # turn init dial to position hidden
    i = 0

    while (i < 4):  # turn init centre to position hidden
        L = list(centre[i])
        L.insert(0, '*')
        centre[i] = ''.join(L)
        i = i + 1
    card = centre.pop()
    tempV = card[2:]
    num = dic[tempV]
    num_step = 0
    while (num_step < nb_of_steps ):

        if num == 13:
              if ('*' not in card  ):
                  print('Could not play that far...')
                  return
              else:
                Card = card.replace('*', '')
                card = Card
                centre.insert(0, card)
                T = list(D[hour])
                card = centre.pop()

                tempV = card[2:]
                num = dic[tempV]
                num_step = num_step + 1

        else:
            if ('*' not in card):
                print('Could not play that far...')
                return
            else:
                Card = card.replace('*', '')
                card = Card
                D[num].insert(0, card)
                T = list(D[hour])
                card = D[num].pop()

                tempV = card[2:]
                num = dic[tempV]
                num_step = num_step + 1
    i = 0
    L = []
    while (i < len(T)):
        if ('*' not in T[i]):
            Q = str_to_card(T[i])
            L.append(Q)
            i = i + 1
        else:
            K = T[i].replace('*', '')
            Q = 'hidden' + str_to_card(K)
            L.append(Q)
            i = i + 1
    L = '  '.join([str(i) for i in L])
    print(L)
    return


hour_after_playing_from_beginning_for_at_most(5, 52, dial, centre)


def kings_at_end_of_game(dial, centre):
    init = centre[-1]
    L_init = list(init)
    V_init = L_init[1]
    dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 11, 'q': 12, 'k': 13,
           '': 0}
    num_init = dic[V_init]
    dic1 = {'*': 'hidden'}
    D = init_posi(dial)
    # turn init dial to position hidden
    i = 0

    while (i < 4):  # turn init centre to position hidden
        L = list(centre[i])
        L.insert(0, '*')
        centre[i] = ''.join(L)
        i = i + 1
    card = centre.pop()
    tempV = card[2:]
    num = dic[tempV]

    cmpare_centre = [i for i in centre]
    cmpare_centre.sort()
    Expect = ['Ck', 'Dk', 'Hk', 'Sk']
    while (Expect != cmpare_centre):

        if num == 13:
            if ('*' not in card):
                print('Could not play that far...')
                return
            else:
                Card = card.replace('*', '')
                card = Card
                centre.insert(0, card)
                T = list(D[hour])
                card = centre.pop()

                tempV = card[2:]
                num = dic[tempV]
                cmpare_centre = [i for i in centre]
                cmpare_centre.sort()


        else:
            if ('*' not in card):
                print('Could not play that far...')
                return
            else:
                Card = card.replace('*', '')
                card = Card
                D[num].insert(0, card)
                T = list(D[hour])
                card = D[num].pop()

                tempV = card[2:]
                num = dic[tempV]
                cmpare_centre = [i for i in centre]
                cmpare_centre.sort()
    i = 0
    L = []
    P = [i for i in centre]
    while (i < len(P)):
        if ('*' not in P[i]):
            Q = str_to_card(P[i])
            L.append(Q)
            i = i + 1

    L = '  '.join([str(i) for i in L])
    print(L)
    return

kings_at_end_of_game(dial, centre)