from subclasses import tree


def test_single():
    class Single: pass
    want = ['Single']
    got = list(tree(Single))
    assert want == got


def test_one_sub():
    class Mother: pass
    class Child(Mother): pass
    want = [
        'Mother',
        '    Child',
    ]
    got = list(tree(Mother))
    assert want == got


def test_three_subs():
    class A: pass
    class D(A): pass
    class B(A): pass
    class C(A): pass
    want = [
        'A',
        '    B',
        '    C',
        '    D',
    ]
    got = list(tree(A))
    assert want == got


def test_three_levels():
    class A: pass
    class B1(A): pass
    class C(B1): pass
    class D2(C): pass
    class B2(A): pass
    class D1(C): pass
    want = [
        'A',
        '    B1',
        '        C',
        '            D1',
        '            D2',
        '    B2',
    ]
    got = list(tree(A))
    assert want == got
