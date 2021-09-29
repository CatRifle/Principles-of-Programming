import re


class DiffCommandsError(Exception):
    def __init__(self, text):
        self.text = text


class DiffCommands:
    def __init__(self, file_name):
        self.filename = file_name
        self.num = 0
        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()
        self.L = []
        self.cursor = []
        time = 0

        for line in lines:
            form_1 = re.match('(\d+)(a)(\d+)((,)(\d+))?', line)
            form_2 = re.match('(\d+)((,)(\d+))?(c)(\d+)((,)(\d+))?', line)
            form_3 = re.match('(\d+)((,)(\d+))?(d)(\d+)', line)

            if 'd' in line:
                l, r = line.split('d')
                if ',' in r:
                    raise DiffCommandsError("Cannot possibly be the commands for the diff of two files")
                if ' ' in r:
                    raise DiffCommandsError("Cannot possibly be the commands for the diff of two files")
                if time == 0 and int(r) != 0:
                    raise DiffCommandsError("Cannot possibly be the commands for the diff of two files")

            if (not form_1) and (not form_2) and (not form_3):
                raise DiffCommandsError("Cannot possibly be the commands for the diff of two files")
            if form_1 or form_2 or form_3:
                self.L.append(line)
                self.num = self.num + 1
            if form_1:
                if (form_1.group(2) == 'a') and (form_1.group(4) == None):
                    cursor = [int(form_1.group(1)), int(form_1.group(1)), int(form_1.group(3)) - 1,
                              int(form_1.group(3))]
                    self.cursor.append(cursor)
                if (form_1.group(2) == 'a') and (form_1.group(4) != None):
                    cursor = [int(form_1.group(1)), int(form_1.group(1)), int(form_1.group(3)) - 1,
                              int(form_1.group(6))]
                    self.cursor.append(cursor)
            elif form_2:
                if (form_2.group(5) == 'c') and (form_2.group(9) == None):
                    cursor = [int(form_2.group(1)) - 1, int(form_2.group(1)), int(form_2.group(6)) - 1,
                              int(form_2.group(6))]
                    self.cursor.append(cursor)
                if (form_2.group(5) == 'c') and (form_2.group(9) != None):
                    cursor = [int(form_2.group(1)) - 1, int(form_2.group(4)), int(form_2.group(6)) - 1,
                              int(form_2.group(9))]
                    self.cursor.append(cursor)
            elif form_3:
                if (form_3.group(5) == 'd') and (form_3.group(4) == None):
                    cursor = [int(form_3.group(1)) - 1, int(form_3.group(1)), int(form_3.group(6)),
                              int(form_3.group(6))]
                    self.cursor.append(cursor)
                if (form_3.group(5) == 'd') and (form_3.group(4) != None):
                    cursor = [int(form_3.group(1)) - 1, int(form_3.group(4)), int(form_3.group(6)),
                              int(form_3.group(6))]
                    self.cursor.append(cursor)
            time = time + 1

        i = 0
        while i < len(self.cursor) - 1:
            if (self.cursor[i + 1][0] - self.cursor[i][1]) != (self.cursor[i + 1][2] - self.cursor[i][3]):
                raise DiffCommandsError("Cannot possibly be the commands for the diff of two files")

            if (self.cursor[i + 1][0] - self.cursor[i][1]) == 0:
                raise DiffCommandsError("Cannot possibly be the commands for the diff of two files")

            if (self.cursor[i + 1][2] - self.cursor[i][3]) == 0:
                raise DiffCommandsError("Cannot possibly be the commands for the diff of two files")
            i = i + 1

        f = open(self.filename, "r")
        lines = f.readlines()
        self.Arr = []
        for line in lines:
            self.Arr.append(line.strip())
        f.close()

    def InitArray(self):
        f = open(self.filename, "r")
        lines = f.readlines()
        Array = []
        for line in lines:
            Array.append(line.strip())
        f.close()
        return Array

    def find_cursor(self):
        return self.cursor

    def __str__(self):
        f = open(self.filename, "r")
        lines = f.readlines()
        String = ''
        for line in lines:
            String = String + line
        f.close()
        return String.strip()


class OriginalNewFiles:
    def __init__(self, file_name1, file_name2):
        self.fi1 = file_name1
        self.fi2 = file_name2

        f1_doc = open(self.fi1, "r")
        lines_1 = f1_doc.readlines()
        self.arr_1 = ['']
        for line in lines_1:
            self.arr_1.append(line.strip())
        f1_doc.close()

        f2_doc = open(self.fi2, "r")
        lines_2 = f2_doc.readlines()
        self.arr_2 = ['']
        for line in lines_2:
            self.arr_2.append(line.strip())
        f2_doc.close()

        self.File1 = []
        self.File2 = []

        file1 = open(file_name1, "r")
        for line in file1:
            self.File1.append(line)

        file2 = open(file_name2, "r")
        for line in file2:
            self.File2.append(line)

    def is_a_possible_diff(self, diff):
        shift = 0
        fn = []
        len_a1 = len(self.arr_1)
        len_a2 = len(self.arr_2)
        for ele in diff.Arr:

            if 'a' in ele:
                List = ele.split('a', 1)
                Element_L = List[0]
                Element_R = List[1]
                p1 = int(Element_L)
                if ',' not in Element_R:
                    p2 = int(Element_R)
                    if p1 >= len_a1:
                        return False
                    i = shift
                    while i <= p1:
                        fn.append(self.arr_1[i])
                        i = i + 1
                    fn.append(self.arr_2[p2])
                    shift = p1 + 1

                else:
                    if p1 >= len_a1:
                        return False
                    i = shift
                    while i <= p1:
                        fn.append(self.arr_1[i])
                        i = i + 1
                    shift = p1 + 1
                    List1 = Element_R.split(',', 1)
                    p2 = int(List1[0])
                    p3 = int(List1[1])
                    j = p2
                    while j <= p3:
                        fn.append(self.arr_2[j])
                        j = j + 1

            elif 'd' in ele:
                List = ele.split('d', 1)
                Element_L = List[0]
                if ',' in Element_L:
                    List1 = Element_L.split(',', 1)
                    p1 = int(List1[0])
                    p2 = int(List1[1])
                    if p1 >= len_a1 + 1:
                        return False
                    i = shift
                    while i <= p1 - 1:
                        fn.append(self.arr_1[i])
                        i = i + 1
                    shift = p2 + 1
                else:
                    p1 = int(Element_L)
                    if p1 >= len_a1 + 1:
                        return False
                    i = shift
                    while i <= p1 - 1:
                        fn.append(self.arr_1[i])
                        i += 1
                    shift = p1 + 1

            elif 'c' in ele:
                List = ele.split('c', 1)
                Element_L = List[0]
                Element_R = List[1]
                if ',' in Element_L:
                    List1 = Element_L.split(',', 1)
                    p1 = int(List1[0])
                    p2 = int(List1[1])
                    if p1 > len_a1:
                        return False
                    j = shift
                    while j <= p1 - 1:
                        fn.append(self.arr_1[j])
                        j = j + 1
                    shift = p2 + 1
                    if ',' not in Element_R:
                        p3 = int(Element_R)
                        fn.append(self.arr_2[p3])
                    else:
                        List2 = Element_R.split(',', 1)
                        p3 = int(List2[0])
                        p4 = int(List2[1])
                        i = p3
                        while i <= p4:
                            fn.append(self.arr_2[i])
                            i += 1

                else:
                    p1 = int(Element_L)
                    if p1 > len_a1:
                        return False
                    i = shift
                    while i <= p1 - 1:
                        fn.append(self.arr_1[i])
                        i += 1

                    shift = p1 + 1
                    if ',' not in Element_R:
                        p3 = int(Element_R)
                        fn.append(self.arr_2[p3])
                    else:
                        List1 = Element_R.split(',', 1)
                        p3 = int(List1)
                        p4 = int(List1)
                        j = p3
                        while j <= p4:
                            fn.append(self.arr_2[j])
                            j += 1

        if len(fn) != len_a2:
            gap = len_a2 - len(fn)
            a = len_a1
            supply = self.arr_1[a - gap:]
            fn = fn + supply

        if fn != self.arr_2:
            return False
        return True

    def output_diff(self, diffput):
        self.diffput = diffput
        diff_array = diffput.find_cursor()
        diff_init = diffput.InitArray()
        length = len(diff_array)
        i = 0
        while i < length:
            if (diff_array[i][0] != diff_array[i][1]) and (diff_array[i][2] != diff_array[i][3]):
                print(diff_init[i])
                if diff_array[i][1] != diff_array[i][0]:
                    m = diff_array[i][0]
                    while (m < diff_array[i][1]):
                        print('<', self.arr_1[m + 1])
                        m = m + 1

                if diff_array[i][3] != diff_array[i][2]:
                    print('---')
                    n = diff_array[i][2]
                    while (n < diff_array[i][3]):
                        print('>', self.arr_2[n + 1])
                        n = n + 1
                i = i + 1

            elif (diff_array[i][0] != diff_array[i][1]) and (diff_array[i][2] == diff_array[i][3]):
                print(diff_init[i])
                j = diff_array[i][0]
                while (j < diff_array[i][1]):
                    print('<', self.arr_1[j + 1])
                    j = j + 1
                i = i + 1

            elif (diff_array[i][0] == diff_array[i][1]):
                print(diff_init[i])
                k = diff_array[i][2]
                while (k < diff_array[i][3]):
                    print('>', self.arr_2[k + 1])
                    k = k + 1
                i = i + 1

    def output_unmodified_from_original(self, diff):
        self.diff = diff
        diff_array = diff.find_cursor()
        len_da = len(diff_array)
        diff_init = diff.InitArray()
        diff_array.insert(0, [0, 0, 0, 0])
        a = len(self.arr_1)
        b = len(self.arr_2)
        diff_array.append([a, a, b, b])

        try:
            i = 0
            while i <= len(diff_array) - 1:
                if diff_array[i][1] != diff_array[i][0]:
                    print('...')
                j = diff_array[i][1]
                while j <= diff_array[i + 1][0] - 1:
                    print(self.arr_1[j + 1])
                    j = j + 1
                i = i + 1
        except IndexError:
            pass

    def output_unmodified_from_new(self, diff):
        self.diff = diff
        diff_array = diff.find_cursor()

        diff_array.insert(0, [0, 0, 0, 0])
        a = len(self.arr_1)
        b = len(self.arr_2)
        diff_array.append([a, a, b, b])

        try:
            m = 0
            while m <= len(diff_array) - 1:
                if diff_array[m][3] != diff_array[m][2]:
                    print('...')
                n = diff_array[m][3]
                while n <= diff_array[m + 1][2] - 1:
                    print(self.arr_2[n + 1])
                    n = n + 1
                m = m + 1
        except IndexError:
            pass

    def emerge_Num(self, L1, L2):

        emerge_new = []
        i = 0
        while i <= len(L1) - 1:
            j = 0
            while j <= len(L2) - 1:
                emerge_new.append([L1[i], L2[j]])
                j = j + 1
            i = i + 1
        return emerge_new

    def duplicate(self, L_dupli, item):
        L_new = []
        for i in L_dupli:
            L_new.append(i)
        L_new.append(item)
        return L_new

    def emerge_List(self, L1, L2):

        emerge_new = []
        i = 0
        while i <= len(L1) - 1:
            item1 = L1[i]  # ele1 is a list
            j = 0
            while j <= len(L2) - 1:
                item2 = L2[j]  # ele2 is a number
                new_item = self.duplicate(item1, item2)
                emerge_new.append(new_item)
                j = j + 1
            i = i + 1
        return emerge_new

    def seek_lcs(self):
        check = False
        L1 = []
        len_F1 = len(self.File1)
        len_F2 = len(self.File2)

        for i in range(len_F1):
            L1.append([])
            j = 0
            while j <= len_F2 - 1:
                if self.File1[i] == self.File2[j]:
                    L1[i].append(j + 1)
                j = j + 1

        i = 0
        while i <= len(L1) - 2:
            for j in range(i + 1, len(L1)):
                if L1[i] != [] and L1[i] == L1[j]:
                    check = True
                    break
            i = i + 1
            if check is True:
                break

        if check is True:
            L1 = []
            i = 0
            while i <= len_F2 - 1:
                L1.append([])
                j = 0
                while j <= len_F1 - 1:
                    if self.File2[i] == self.File1[j]:
                        L1[i].append(j + 1)
                    j = j + 1
                i = i + 1

        len_L1 = len(L1)
        len_max = 0
        for s in L1:
            if s:
                len_max = len_max + 1

        File_self = []
        i = 0
        while i < len_L1:
            if L1[i]:
                File_self.append(i + 1)
            i = i + 1

        k = 0
        t = len_L1 - len_max
        while k < t:
            L1.remove([])
            k = k + 1

        len1 = len(L1)

        if len1 > 1:
            generate = self.emerge_Num(L1[0], L1[1])
            i = 2
            while i <= len1 - 1:
                generate = self.emerge_List(generate, L1[i])
                i = i + 1
        else:
            generate = []
            for i in L1[0]:
                generate.append([i])

        for ele in generate:
            j = 1
            while j <= len(ele) - 1:
                if ele[j - 1] >= ele[j] + 1:
                    generate.remove(ele)
                j += 1

        if check is True:
            return generate, File_self
        else:
            return File_self, generate

    def LCS_to_List(self, L1, L2):
        len1 = len(self.File1)
        len2 = len(self.File2)
        docs = []

        if type(L1[0]) == int:

            for j in range(len(L2)):

                s1_init = 0
                s2_init = 0
                docs.append('')
                for i in range(len(L1)):
                    s1 = L1[i]
                    s2 = L2[j][i]
                    diff_1 = s1 - s1_init
                    diff_2 = s2 - s2_init

                    if diff_1 == 1:
                        if diff_2 == 1:
                            s1_init = s1
                            s2_init = s2
                            continue
                        elif diff_2 == 2:
                            docs[j] = docs[j] + str(s1_init) + 'a' + str(s2_init + 1) + '\n'
                            s1_init = s1
                            s2_init = s2
                        else:
                            docs[j] = docs[j] + str(s1_init) + 'a' + str(s2_init + 1) + ',' + str(s2 - 1) + '\n'
                            s1_init = s1
                            s2_init = s2

                    elif diff_2 == 1:
                        if diff_1 == 1:
                            s1_init = s1
                            s2_init = s2
                            continue
                        elif diff_1 == 2:
                            docs[j] = docs[j] + str(s1_init + 1) + 'd' + str(s2_init) + '\n'
                            s1_init = s1
                            s2_init = s2
                        else:
                            docs[j] = docs[j] + str(s1_init + 1) + ',' + str(s1 - 1) + 'd' + str(s2_init) + '\n'
                            s1_init = s1
                            s2_init = s2

                    else:
                        if diff_1 == 2 and diff_2 == 2:
                            docs[j] = docs[j] + str(s1_init + 1) + 'c' + str(s2_init + 1) + '\n'
                            s1_init = s1
                            s2_init = s2

                        else:
                            docs[j] = docs[j] + str(s1_init + 1) + ',' + str(s1 - 1) + 'c' + str(
                                s2_init + 1) + ',' + str(s2 - 1) + '\n'
                            s1_init = s1
                            s2_init = s2

                diff_1 = len1 - s1_init
                diff_2 = len2 - s2_init

                if s1_init != len1 and s2_init != len2:
                    if diff_1 == 1:
                        docs[j] = [docs[j], str(s1_init + 1), 'c', str(s2_init), ',', str(len2), '\n']
                        ''.join(docs[j])

                    else:
                        docs[j] = [docs[j], str(s1_init + 1), ',', str(len1), 'c', str(s2_init), ',', str(len2), '\n']
                        ''.join(docs[j])

                elif s1_init == len1 and s2_init != len2:
                    if diff_2 == 1:
                        docs[j] = [docs[j], str(s1_init), 'a', str(s2_init + 1), '\n']
                        ''.join(docs[j])
                    else:
                        docs[j] = [docs[j], str(s1_init), 'a', str(s2_init + 1), ',', str(len2), '\n']
                        ''.join(docs[j])

                elif s1_init != len1 and s2_init == len2:
                    if diff_1 == 1:
                        docs[j] = [docs[j], str(s1_init + 1), 'd', str(s2_init), '\n']
                        ''.join(docs[j])
                    else:
                        docs[j] = [docs[j], str(s1_init + 1), ',', str(len1), 'd', str(s2_init), '\n']
                        ''.join(docs[j])



        else:

            for j in range(len(L1)):
                s1_init = 0
                s2_init = 0
                docs.append('')

                for i in range(len(L2)):

                    s1 = L1[j][i]
                    s2 = L2[i]
                    diff_1 = s1 - s1_init
                    diff_2 = s2 - s2_init

                    if diff_1 == 1:
                        if diff_2 == 1:
                            s1_init = s1
                            s2_init = s2
                            continue
                        elif diff_2 == 2:
                            docs[j] = docs[j] + str(s1_init) + 'a' + str(s2_init + 1) + '\n'
                            s1_init = s1
                            s2_init = s2

                        else:
                            docs[j] = docs[j] + str(s1_init) + 'a' + str(s2_init + 1) + ',' + str(s2 - 1) + '\n'
                            s1_init = s1
                            s2_init = s2

                    elif diff_2 == 1:
                        if diff_1 == 1:
                            s1_init = s1
                            s2_init = s2
                            continue
                        elif diff_1 == 2:
                            docs[j] = docs[j] + str(s1_init + 1) + 'd' + str(s2_init) + '\n'
                            s1_init = s1
                            s2_init = s2
                        else:
                            docs[j] = docs[j] + str(s1_init + 1) + ',' + str(s1 - 1) + 'd' + str(s2_init) + '\n'
                            s1_init = s1
                            s2_init = s2

                    else:
                        if diff_1 == 2 and diff_2 == 2:
                            docs[j] = docs[j] + str(s1_init + 1) + 'c' + str(s2_init + 1) + '\n'
                            s1_init = s1
                            s2_init = s2

                        else:
                            docs[j] = docs[j] + str(s1_init + 1) + ',' + str(s1 - 1) + 'c' + str(
                                s2_init + 1) + ',' + str(s2 - 1) + '\n'
                            s1_init = s1
                            s2_init = s2

                diff_1 = len1 - s1_init
                diff_2 = len2 - s2_init

                if s1_init != len1 and s2_init != len2:
                    if diff_1 == 1:
                        docs[j] = [docs[j], str(s1_init + 1), 'c', str(s2_init), ',', str(len2), '\n']
                        ''.join(docs[j])

                    else:
                        docs[j] = [docs[j], str(s1_init + 1), ',', str(len1), 'c', str(s2_init), ',', str(len2), '\n']
                        ''.join(docs[j])


                elif s1_init == len1 and s2_init != len2:
                    if diff_2 == 1:
                        docs[j] = [docs[j], str(s1_init), 'a', str(s2_init + 1), '\n']
                        ''.join(docs[j])
                    else:
                        docs[j] = [docs[j], str(s1_init), 'a', str(s2_init + 1), ',', str(len2), '\n']
                        ''.join(docs[j])


                elif s1_init != len1 and s2_init == len2:
                    if diff_1 == 1:
                        docs[j] = [docs[j], str(s1_init + 1), 'd', str(s2_init), '\n']
                        ''.join(docs[j])
                    else:
                        docs[j] = [docs[j], str(s1_init + 1), ',', str(len1), 'd', str(s2_init), '\n']
                        ''.join(docs[j])

        return docs

    def get_all_diff_commands(self):
        file1, file2 = self.seek_lcs()
        txts = self.LCS_to_List(file1, file2)
        L = []
        for i in txts:
            S = ''.join(i)
            L.append(S.strip())
        L.sort()
        return L
