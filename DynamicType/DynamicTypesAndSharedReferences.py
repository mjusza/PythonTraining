print("part 1")
a = 3
b = 3
print(f"a = {a}")
print(f"b = {b}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

print("\npart 2")
a = b
b = 5
print(f"a = {a}")
print(f"b = {b}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

print("\npart 3")
a += + 6
print(f"a = {a}")
print(f"b = {b}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

print("\npart 4")
L1 = [ 1, 2, 3]
L2 = L1
print(f"L1 = {L1}")
print(f"L2 = {L2}")
print(f"id(L1) = {id(L1)}")
print(f"id(L2) = {id(L2)}")
print(f"L1 == L2 : {L1 == L2}")
print(f"L1 is L2 : {L1 is L2}")

print("\npart 5")
L1[0] = 11
print(f"L1 = {L1}")
print(f"L2 = {L2}")
print(f"id(L1) = {id(L1)}")
print(f"id(L2) = {id(L2)}")

print("\npart 6")
L1 = [ 1, 2, 3]
L2 = L1[:]
print(f"L1 = {L1}")
print(f"L2 = {L2}")
print(f"id(L1) = {id(L1)}")
print(f"id(L2) = {id(L2)}")
print(f"L1 == L2 : {L1 == L2}")
print(f"L1 is L2 : {L1 is L2}")

print("\npart 7")
L1[0] = 11
print(f"L1 = {L1}")
print(f"L2 = {L2}")
print(f"id(L1) = {id(L1)}")
print(f"id(L2) = {id(L2)}")

print("\npart 8")
L1 = [1, 2, 3]
L2 = [1, 2, 3]
print(f"L1 = {L1}")
print(f"L2 = {L2}")
print(f"id(L1) = {id(L1)}")
print(f"id(L2) = {id(L2)}")
print(f"L1 == L2 : {L1 == L2}")
print(f"L1 is L2 : {L1 is L2}")


# import sys
# print(sys.getrefcount(x))