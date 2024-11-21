# Pattern #1: Simple Number Triangle Pattern
def pattern_1():
    print("Pattern #1: Simple Number Triangle Pattern")
    for i in range(1, 6):
        print(" ".join([str(i)] * i))
    print()

# Pattern #2: Inverted Pyramid of Numbers
def pattern_2():
    print("Pattern #2: Inverted Pyramid of Numbers")
    for i in range(5, 0, -1):
        print(" " * (5 - i) + " ".join([str(i)] * i))
    print()

# Pattern #3: Half Pyramid Pattern of Numbers
def pattern_3():
    print("Pattern #3: Half Pyramid Pattern of Numbers")
    for i in range(1, 6):
        print(" " * (5 - i) + " ".join([str(j) for j in range(1, i + 1)]))
    print()

# Pattern #4: Inverted Pyramid of Descending Numbers
def pattern_4():
    print("Pattern #4: Inverted Pyramid of Descending Numbers")
    for i in range(5, 0, -1):
        print(" " * (5 - i) + " ".join([str(i)] * i))
    print()

# Pattern #5: Inverted Pyramid of the Same Digit
def pattern_5():
    print("Pattern #5: Inverted Pyramid of the Same Digit")
    for i in range(5, 0, -1):
        print(" " * (5 - i) + " ".join([str(5)] * i))
    print()

# Pattern #6: Reverse Pyramid of Numbers
def pattern_6():
    print("Pattern #6: Reverse Pyramid of Numbers")
    for i in range(1, 6):
        print(" " * (5 - i) + " ".join([str(j) for j in range(i, 0, -1)]))
    print()

# Pattern #7: Inverted Half Pyramid Number Pattern
def pattern_7():
    print("Pattern #7: Inverted Half Pyramid Number Pattern")
    for i in range(6, 0, -1):
        print(" ".join([str(j) for j in range(i)]))
    print()

# Pattern #8: Pyramid of Natural Numbers Less Than 10
def pattern_8():
    print("Pattern #8: Pyramid of Natural Numbers Less Than 10")
    n = 1
    for i in range(1, 4):
        row = [str(j) for j in range(n, n + i)]
        print(" ".join(row))
        n = n + i
    print()

# Pattern #9: Reverse Pattern of Digits from 10
def pattern_9():
    print("Pattern #9: Reverse Pattern of Digits from 10")
    num = 1
    for i in range(1, 5):
        row = [str(j) for j in range(num, num - i, -1)]
        print(" ".join(row))
        num = num + i
    print()

# Pattern #10: Unique Pyramid Pattern of Digits
def pattern_10():
    print("Pattern #10: Unique Pyramid Pattern of Digits")
    for i in range(1, 6):
        row = [str(j) for j in range(1, i + 1)] + [str(j) for j in range(i - 1, 0, -1)]
        print(" ".join(row))
    print()

# Pattern #11: Connected Inverted Pyramid Pattern of Numbers
def pattern_11():
    print("Pattern #11: Connected Inverted Pyramid Pattern of Numbers")
    for i in range(5, 0, -1):
        row = [str(j) for j in range(5, i - 1, -1)]
        row += [str(j) for j in range(i, 6)]
        print(" ".join(row))
    print()

# Pattern #12: Even Number Pyramid Pattern
def pattern_12():
    print("Pattern #12: Even Number Pyramid Pattern")
    for i in range(1, 6):
        row = [str(10 - 2 * j) for j in range(i)]
        print(" ".join(row))
    print()

# Pattern #13: Pyramid of Horizontal Tables
def pattern_13():
    print("Pattern #13: Pyramid of Horizontal Tables")
    for i in range(7):
        row = [str(i * j) for j in range(i + 1)]
        print(" ".join(row))
    print()

# Pattern #14: Pyramid Pattern of Alternate Numbers
def pattern_14():
    print("Pattern #14: Pyramid Pattern of Alternate Numbers")
    for i in range(1, 10, 2):
        print(" ".join([str(i)] * i))
    print()

# Pattern #15: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers
def pattern_15():
    print("Pattern #15: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers")
    for i in range(1, 6):
        print(" " * (5 - i) + " ".join([str(j) for j in range(1, i + 1)]))
    print()

# Pattern #16: Equilateral Triangle with Stars (Asterisk Symbol)
def pattern_16():
    print("Pattern #16: Equilateral Triangle with Stars (Asterisk Symbol)")
    for i in range(1, 8):
        print(" " * (7 - i) + "* " * i)
    print()

# Pattern #17: Downward Triangle Pattern of Stars
def pattern_17():
    print("Pattern #17: Downward Triangle Pattern of Stars")
    for i in range(6, 0, -1):
        print(" " * (6 - i) + "* " * i)
    print()

# Pattern #18: Pyramid Pattern of Stars
def pattern_18():
    print("Pattern #18: Pyramid Pattern of Stars")
    for i in range(1, 6):
        print("* " * i)
    print()

# Main program to call all patterns
def main():
    pattern_1()
    pattern_2()
    pattern_3()
    pattern_4()
    pattern_5()
    pattern_6()
    pattern_7()
    pattern_8()
    pattern_9()
    pattern_10()
    pattern_11()
    pattern_12()
    pattern_13()
    pattern_14()
    pattern_15()
    pattern_16()
    pattern_17()
    pattern_18()

if __name__ == "__main__":
    main()
dd