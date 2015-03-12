import itertools as it
import collections as c
import string

# get rid of comments and blank lines
def preprocess(ls):
    ls = map(lambda l : ''.join(it.takewhile(lambda c : c not in ";\n\r", l)), ls)
    ls = filter(lambda l : any(map(lambda c : c in string.printable, l)), ls)
    return ls

def parse(f):
    ls = preprocess(f.readlines())
    nlines = len(ls)

    i = 0
    expect_header = True

    #NOTE do not mess with section order!
    inp = c.OrderedDict()
    while i < nlines:
        l = ls[i]
        if expect_header:
            if l[0] == '[' and l[-1] == ']':
                name = l[1:-1]
                data = []
                expect_header = False
            else:
                return 0, 'internal error: expected \'[\', found: \'' + l + '\''
        else:
            if l[0] == '[':
                inp[name] = data
                expect_header = True
                i -= 1
            else:
                data.append(l.split())
        i += 1

    # remainder
    if data:
        inp[name] = data

    return 1, inp

def prettyprint(f, inp):
    for name,ls in inp.iteritems():
        f.write('[' + name + ']\n')
        for l in ls:
            f.write(' '.join(l) + '\n')
        f.write('\n')

