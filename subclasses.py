def tree(cls, level=0):
    yield ' ' * 4 * level + cls.__name__
    sublist = sorted(cls.__subclasses__(), key=lambda c: c.__name__)
    for sub in sublist:
        yield from tree(sub, level+1)        
