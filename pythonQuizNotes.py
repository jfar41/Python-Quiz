def q1():
    print("hello" * 5)
    # multiplying a str by an int n repeats str n  times
    # output: "hellohellohellohellohello"

def q2():
    x, y = 4, 5
    y, x = x, y
    print(x)
    print(y)


def q3():
    z = 9
    lst = [0] * z
    # create 9 instances of 0 within the array
    print(lst[:-1])
    # will return values from 0 idx until 1 from the end (exclude last idx)
    # output: [0, 0, 0, 0, 0, 0, 0, 0]


def q4():
    def help(x):
        return x % 2 == 0
    lst = [i**2 for i in range(10)]
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    lst = filter(help, lst)
    # [0, 4, 16, 36, 64]
    print(list(lst)[::2])
    # some_sequence[::3] means get every 3rd item, first item included
    # output: [0, 16, 64]


def q5():
    # output: 0 1 1 2 2 3
    z = 0
    for i in range(1, 10):
        if (i + 1 // 2) % 7 == 0:
            # floor division takes precedence over addition,
            # so statement equal to: if (i + (1 // 2)) % 7 == 0
            # or: if (i + 0) % 7 == 0
            break
        else:
            z += int(i % 2 == 0)
            # int(False) == 0
            # int(True) == 1
            print(z)
    else:
        # when using iterator like for loop, if break or return statement encountered then that means
        # we met a condition. No need to run else statement. If condition was never resolved
        # with break or return in loop, else statement gets called outside loop
        print("end")


def q6():
    # output: "no"
    import math

    for i in range(1, 100):
        # condition will never be met, so will exit
        # loop without any condition being resolved
        if math.sqrt(i) == (i - 5)**2:
            print(i)
            break
    else:
        print("no")



def q7():
    class A:
        def __init__(self, x):
            self.x = x

        def __eq__(self, other):
            return self.x == other.x
    a = A(2)
    b = A(2)
    print(a == b)
    # if didn't define the __eq__ dunder method with the comparison criteria,
    # statement would be False. Needed for objects of user-defined classes.
    # In this case, True since __eq__ provided and evaluates to True
    print(a is b)
    # False
    # 'is' operator compares  memory locations. Different objects == different locations in mem
    print(b is a)
    # False
    print(a is a)
    # True
    print(a == a)
    # True


def q8():
    class A:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def print(self):
            print(self.x, self.y)

    class B(A):
        # inherits class A __init__ dunder method, overrides print of class A
        def print(self):
            print(self.y, self.x)

    class C(B):
        # inherits class B functionality
        def __init__(self, x, y, z):
            super().__init__(x, y)
            self.z = z

    d = A(2, 4)
    e = B(4, 5)
    g = C(3, 4, 7)
    g.x = g.z
    d.print()  # 2, 4
    e.print()  # 5, 4
    g.print()  # 4, 7


def q9():
    def x(z):
        def q(x, y):
            x = y + z + x
            print(x)

        return q

    for i in range(10):
        func = x(i)
        func(i, i - 1)
    # output: {0: -1, 1: 2, 2: 5, 3: 8, 4: 11, 5: 14, 6: 17, 7: 20, 8: 23, 9: 26}
    # where {i: func(i, i - 1)}


def q10():
    def d(f):
        def w(*args, **kwargs):
            r = f(*args, **kwargs)  # r == 6
            r += 1  # r == 7
            return r
        return w

    @d
    def a(x):
        return x + 1

    print(a(5))
    # output: 7