dir()
print(*dir(), sep='  ')
print(__builtins__.__doc__)
print(*dir(__builtins__), sep='  ')

#all lower-case names not starting with _
names = [s for s in dir(__builtins__) if s == s.lower() and s[0] != '_']
print(*names, sep='  ')

for name in names:
    obj = getattr(__builtins__, name)
    print(f'{name:12s}', type(obj).__name__)

categories = []
for name in names:
    obj = getattr(__builtins__, name)
    #if obj is input:
    #    categories.append(('builtin_function_or_method', 'input'))
    #else:
    categories.append((type(obj).__name__, name))

from itertools import groupby
from operator import itemgetter

for category, group in groupby(sorted(categories), itemgetter(0)):
    print('─' * 20, category)
    for _, name in group:
        print(name)

# mixed-case or upper-case names 
Names = [s for s in dir(__builtins__) if s.lower() != s]

Exceptions = [s for s in Names if callable(getattr(__builtins__, s))]
print(*Exceptions, sep='  ')

Const = [s for s in Names if not callable(getattr(__builtins__, s))]
print(*Const, sep='  ')

Specials = [s for s in dir(__builtins__) if s[0] == '_']
print(*Specials, sep='  ')

print('\n'.join(f'{n:16s} {getattr(__builtins__, n)!r}' for n in Specials))
