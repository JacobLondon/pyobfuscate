import random
import os

def true():
    random.seed(os.urandom(128))
    choices = [
        '(not()in{})',
        '(not()in[])',
        '(not()in())',
        '(not [])'
    ]
    return random.choice(choices)

def false():
    random.seed(os.urandom(128))
    choices = [
        '(not not()in{})',
        '(()in{})',
        '(()in[])',
        '(()in())',
        '(not not [])'
    ]
    return random.choice(choices)

def number(x):
    if x == 0:
        return f'{false()}'

    builder = []
    for _ in range(x):
        builder.append(f'{true()}')
    return '+'.join(builder)

def string(s):
    builder = []
    for letter in s:
        assert letter in letters
        builder.append(letters[letter])
    return '+'.join(builder)

letters = {}
for i in range(128):
    letters[chr(i)] = f"chr({number(i)})"


letters['a'] = f'str({false()})[{number(1)}]'
letters['b'] = f'str(type({true()}))[{number(8)}]'
letters['c'] = f'str(type({true()}))[{number(1)}]'
letters['d'] = f'str(type(dict()))[{number(8)}]'
letters['e'] = f'str({true()})[{number(3)}]'
letters['F'] = f'str({false()})[{number(0)}]'
letters['h'] = f'str(type(print))[{number(31)}]'
letters['m'] = f'str(type(print))[{number(28)}]'
letters['p'] = f'str(type(type))[{number(10)}]'
letters['r'] = f'str({true()})[{number(1)}]'
letters['s'] = f'str({false()})[{number(3)}]'
letters['T'] = f'str({true()})[{number(0)}]'
letters['t'] = f'str(type(()))[{number(8)}]'
letters['u'] = f'str(type(()))[{number(9)}]'
letters['y'] = f'str(type(type))[{number(9)}]'
letters['z'] = f'str(type(zip((), ())))[{number(8)}]'
letters['\''] =f'str(type({true()}))[{number(7)}]'
letters['-'] = f'str(print)[{number(6)}]'
letters['<'] = f'str(type)[{number(0)}]'
letters['>'] = f'str(type)[{number(13)}]'
letters['{'] = f'str(dict())[{number(0)}]'
letters['}'] = f'str(dict())[{number(1)}]'
letters['['] = f'str(list())[{number(0)}]'
letters[']'] = f'str(list())[{number(1)}]'
letters['('] = f'str(tuple())[{number(0)}]'
letters[')'] = f'str(tuple())[{number(1)}]'

def _try_read(filename):
    try:
        with open(filename, 'r') as fp:
            return fp.read()
    except:
        return None

def _main():
    import sys
    if len(sys.argv) != 2:
        print(f"Error: Must specify '{sys.argv[0]} ARG'")
        return 1

    text = _try_read(sys.argv[1])
    if not text is None:
        converted = string(text)
        print("exec(", sep='', end='')
        print(converted, sep='', end='')
        print(")")
    else:
        print(string(sys.argv[1]))

    return 0

if __name__ == '__main__':
    exit(_main())
