from Node import *
from State import State


def main():
    a = State()
    a.throw_in(1)
    a.throw_in(1)
    a.throw_in(1)
    a.throw_in(1)
    a.throw_in(1)
    a.throw_in(1)
    a.throw_in(1)
    a.throw_in(1)
    a.throw_in(1)
    a.throw_in(1)
    print(a)
    b = copy.deepcopy(a)
    print(a.has_won())
    print(b.has_won())



if __name__ == "__main__":
    main()
