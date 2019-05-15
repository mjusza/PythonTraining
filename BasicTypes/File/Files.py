myfile = open("test.txt", "w")
myfile.write("siema, co slychac?\n")
myfile.write("ehh, nuuda :/\n")
myfile.close();

myfile = open("test.txt")
readLine = myfile.readline();
print(f"readLine = {readLine.rstrip()}")
readLine = myfile.readline();
print(f"readLine = {readLine.rstrip()}")
myfile.close()

myfile = open("test.txt")
print(f"\ncala zawartosc:\n{myfile.read()}")
myfile.close()

print("uzycie iteratora:")
for line in open("test.txt"):
    print(line, end=":)")

print("\n\nwstep do serializacji")

S = "siema"
A, B, C = 1, 2, 3
D = {'a' : 1, 'b' : 2}
L = [3, 2, 1]

myfile = open("objectFile.txt", 'w')
myfile.write(f"S\n")
myfile.write(f"{A},{B},{C}\n")
myfile.write(f"{str(D)}-_-{str(L)}\n")
myfile.close()

print("zaczynamy")
myfile = open("objectFile.txt")
line = myfile.readline()
print(line.rstrip())

print("\nkolejna linia")
line = myfile.readline()
print(line)
print(type(line))
print(line.split(","))
parts = line.split(",")
lista = [int(liczba) for liczba in parts]
print(lista)

print("\nostatnia linia")
line = myfile.readline()
parts = line.split("-_-")
print(parts)
lista = [eval(element) for element in parts]
print(lista)
print(lista[0])
print(lista[1])
myfile.close()

myfile = open("objectFile.txt", 'wb')
import pickle
dataToSerialize = [S, A, B, C, D, L]
pickle.dump(dataToSerialize, myfile)
myfile.close()

with open("objectFile.txt", 'rb') as myFile:
    dane = pickle.load(myFile)
    print(f"odtworzone dane: {dane}")

for dana in dane :
    print(f"dana: {dana}, typ danej: {type(dana)}")