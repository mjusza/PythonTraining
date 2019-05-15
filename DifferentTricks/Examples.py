print("1) Dictionary instead of if/elif/else construction:")
caseOptions = {"a": 1, "b": 2, "c": 3}
print(f"selectedValue: {caseOptions.get('a', 'Wrong choice!')}")
print(f"selectedValue: {caseOptions.get('d', 'Wrong choice!')}")

print("\n2) Case options built on if/else and dictionary:")
def caseWithIfAndDict(choice):
    if choice in caseOptions:
        print(f"choice: {choice}")
    else:
        print("Wrong choice!")


caseWithIfAndDict("b")
caseWithIfAndDict("v")

print("\n3) 3-argument expression")
value = 5 if 0 else 7
print(f"value: {value}")
value = ['a', 'b'][bool(0)]
print(f"value: {value}")

print(f"1 & 2: {1 & 2}")
print(f"1 | 2: {1 | 2}")

print(f"5 and 0 and 1: {5 and 0 and 1}")
print(f"0 or 1 or 2: {0 or 1 or 2}")

value = (5 and 0) or 6
print(f"value: {value}")
value = (5 and 1) or 6
print(f"value: {value}")

# if f1() or f2(): ...

# tmp1, tmp2 = f1(), f2()
# if tmp1 or tmp2: ...

# write .... and see what happens in PyCharm
# def f1() : ... # ... = pass
# x = ... # ... = None