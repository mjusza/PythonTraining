'''
IMMUTABLE type of object

Numbers:
    - integer: 1, -456
    - floating point: 1.67, 1., 3.14e-10, 3.0e+210
    - complex: 5 +7j
    - decimal with fixed precision: decimal.Decimal(1)
    - fractional
    - long integer
    - Boolean

Operators:
    +, -, *, /, //, >>, **, etc

Mathematical functions:
    pow, abs, round, int, hex, bin

Modules with tools:
    math, random, etc

    # import math
    print(math.pi)

Variables and basic expressions

Comparisons - normal and complex
    X = 2
    Y = 3
    Z = 4

    print(X < Y & Y < Z)
    print(X < Y < Z)
    print(1 == 2 < 3)

Division:
    import math

    print(10 / 4)
    print(10 // 4)
    print(10 / 4.0)
    print(10 // 4.0)
    print(10 / -4)
    print(10 // -4)
    print(math.trunc(10 / -4))
    print(10 / -4.0)
    print(10 // -4.0)

Integers precision:
    print(2 ** 200)

Notation:
    hexadecimal, octal, binary

    0x10, 0o10, 0b10
    hex(16), oct(8), bin(2)

    String to int conversion:
    print(int('100', 16))
    print(int('100', 3))
    print(int('100', 7))

    print(int('0x100'))
    print(eval('0x100'))

Bit level operations:
    and, or, xor, shift

Decimal with fixed precision:
    from decimal import Decimal
    print(Decimal(10))
    print (0.1 + 0.2 - 0.3) - floating point precision is poor
    print(Decimal('0.1') + Decimal('0.2') - Decimal('0.3'))
    print(Decimal(0.1) + Decimal(0.2) - Decimal(0.3))
    print(Decimal('0.00001') + Decimal('0.00002') - Decimal('0.00003'))

    import decimal
    print(decimal.Decimal('1') / decimal.Decimal('123'))
    decimal.getcontext().prec = 5
    print(decimal.Decimal('1') / decimal.Decimal('123'))

    with decimal.localcontext() as context :
        context.prec = 3
        print(decimal.Decimal('1') / decimal.Decimal('123'))
    print(decimal.Decimal('1') / decimal.Decimal('123'))

Fractional:
    from fractions import Fraction
    print(Fraction(1, 3))
    print(Fraction(1, 3) + Fraction(2, 3))
    print(Fraction('.1'))
    print(Fraction(1, 10) + Fraction(1, 10) - Fraction(2, 10))
    print(Fraction.from_float(1.25))
    print(Fraction.from_float(1.1))
    print(2.5.as_integer_ratio())
    print(Fraction(*2.5.as_integer_ratio()))

Boolean:
    True, False

    it is bool type formally, with True/False values as built-in names
    internally True/False are bool instances and bool is derived from int class
    True/False behaves exactly as integers 1 and 0, but with specified display logic

    print(True == 1)
    print(True is 1)
    print(True + 1)
    print(False == 0)

    import sys
    sys.getrefcount(1)
    sys.getrefcount(True)
    id(1)
    id(True)
'''


id


