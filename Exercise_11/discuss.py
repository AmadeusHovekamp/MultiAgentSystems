import sys
import json

file = open(sys.argv[1], 'r')
arg = sys.argv[2]
data = json.load(file)
isin = False

def discuss_s(l, o, arg):
    args = [a for a, bs in data.items() for b in data if l[a] != 'out' and l[b] == 'in' and b in bs]
    if args == []:
        o += ' [M]'
        global isin
        isin = True
        print(o)
    for a in args:
        onew = o + ', out(' + a + ')'
        if l[a] == 'in':
            onew += ' [S]'
            print(onew)
        else:
            lnew = l.copy()
            lnew[a] = 'out'
            discuss_m(lnew, onew, a)

def discuss_m(l, o, arg):
    args = [a for a, bs in data.items() if arg in bs]
    if args == []:
        o += ' [S]'
        print(o)
    for a in args:
        onew = o + ', in(' + a + ')'
        if l[a] == 'out':
            onew += ' [S]'
            print(onew)
        else:
            lnew = l.copy()
            lnew[a] = 'in'
            discuss_s(lnew, onew, a)

def discuss(arg):
    global isin
    isin = True
    o = 'in(' + arg + ')'
    l = {a: 'undec' for a in data}
    l[arg] = 'in'
    discuss_s(l, o, arg)
    print(arg + ' is' + (' ' if isin else ' not ') + 'in for some preferred labeling')

discuss(arg)


