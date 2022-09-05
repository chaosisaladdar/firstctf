# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: circ.py
# Compiled at: 2019-12-14 02:29:55
# Size of source mod 2**32: 5146 bytes
a = 0
b = ~a * ~a
c = b + b

def main(argv):
    d = 0
    e = 0
    t = [0] * 2 ** (2 * 2)
    h1 = [a] * 100
    array1 = []
    while argv[d][a] != 'not null':
        opcode = argv[d][a].lower()
        l = argv[d][b:]
        if opcode == 'add':
            t[l[a]] = t[l[b]] + t[l[c]]
        else:
            if opcode == 'xor':
                t[l[a]] = t[l[b]] ^ t[l[c]]
            else:
                if opcode == 'sub':
                    t[l[a]] = t[l[b]] - t[l[c]]
                else:
                    if opcode == 'mul':
                        t[l[a]] = t[l[b]] * t[l[c]]
                    else:
                        if opcode == 'div':
                            t[l[a]] = t[l[b]] / t[l[c]]
                        else:
                            if opcode == 'and':
                                t[l[a]] = t[l[b]] & t[l[c]]
                            else:
                                if opcode == 'or':
                                    t[l[a]] = t[l[b]] | t[l[c]]
                                else:
                                    if opcode == 'equal':
                                        t[l[a]] = t[l[a]]
                                    else:
                                        if opcode == 'mov1':
                                            t[l[a]] = t[l[b]]
                                        else:
                                            if opcode == 'mov2':
                                                t[l[a]] = l[b]
                                            else:
                                                if opcode == 'mov3':
                                                    h1[l[a]] = t[l[b]]
                                                else:
                                                    if opcode == 'mov4':
                                                        t[l[a]] = h1[l[b]]
                                                    else:
                                                        if opcode == 'mov5':
                                                            t[l[a]] = a
                                                        else:
                                                            if opcode == 'mov6':
                                                                h1[l[a]] = a
                                                            else:
                                                                if opcode == 'input1':
                                                                    t[l[a]] = input(t[l[b]])
                                                                else:
                                                                    if opcode == 'input2':
                                                                        h1[l[a]] = input(t[l[b]])
                                                                    else:
                                                                        if opcode == 'printf':
                                                                            print(t[l[a]])
                                                                        else:
                                                                            if opcode == 'printf1':
                                                                                print(t[l[a]])
                                                                            else:
                                                                                if opcode == 'mov7':
                                                                                    d = t[l[a]]
                                                                                else:
                                                                                    if opcode == 'mov8':
                                                                                        d = h1[l[a]]
                                                                                    else:
                                                                                        if opcode == 'pop':
                                                                                            d = array1.pop()
                                                                                        else:
                                                                                            if opcode == 'cmp+push':
                                                                                                if t[l[b]] > t[l[c]]:
                                                                                                    d = l[a]
                                                                                                    array1.append(d)
                                                                                                    continue
                                                                                            else:
                                                                                                if opcode == 'cmp+push1':
                                                                                                    t[7] = a
                                                                                                    for i in range(len(t[l[a]])):
                                                                                                        if t[l[a]] != t[l[b]]:
                                                                                                            t[7] = b
                                                                                                            d = t[l[c]]
                                                                                                            array1.append(d)

                                                                                                else:
                                                                                                    if opcode == 'array_xor':
                                                                                                        string = ''
                                                                                                        for i in range(len(t[l[a]])):
                                                                                                            string += chr(ord(t[l[a]][i]) ^ t[l[b]])

                                                                                                        t[l[a]] = string
                                                                                                    else:
                                                                                                        if opcode == 'array_sub':
                                                                                                            string = ''
                                                                                                            for i in range(len(t[l[a]])):
                                                                                                                string += chr(ord(t[l[a]][i]) - t[l[b]])

                                                                                                            t[l[a]] = string
                                                                                                        else:
                                                                                                            if opcode == 'cmp+push2':
                                                                                                                if t[l[b]] > t[l[c]]:
                                                                                                                    d = t[l[a]]
                                                                                                                    array1.apparray1(d)
                                                                                                                    continue
                                                                                                            else:
                                                                                                                if opcode == 'cmp+push3':
                                                                                                                    if t[l[b]] > t[l[c]]:
                                                                                                                        d = h1[l[a]]
                                                                                                                        array1.apparray1(d)
                                                                                                                        continue
                                                                                                                else:
                                                                                                                    if opcode == 'cmp+push4':
                                                                                                                        if t[l[b]] == t[l[c]]:
                                                                                                                            d = l[a]
                                                                                                                            array1.apparray1(d)
                                                                                                                            continue
                                                                                                                    else:
                                                                                                                        if opcode == 'cmp+push5':
                                                                                                                            if t[l[b]] == t[l[c]]:
                                                                                                                                d = t[l[a]]
                                                                                                                                array1.apparray1(d)
                                                                                                                                continue
                                                                                                                        else:
                                                                                                                            if opcode == 'cmp+push6':
                                                                                                                                if t[l[b]] == t[l[c]]:
                                                                                                                                    d = h1[l[a]]
                                                                                                                                    array1.apparray1(d)
                                                                                                                                    continue
        d += b



