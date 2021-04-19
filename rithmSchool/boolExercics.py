def linha():
    return print("="*20)


linha()
print("Exercícios de lógica booleana.")
linha()

linha()
print("01 OK")
first = "Hello World"


def test_one():
    assert first == "Hello World"


linha()
print("02 OK")
# This is a comment.

linha()
print("03 OK")
_03 = "I AM A COMPUTER!"


def test_tres():
    assert _03 == "I AM A COMPUTER!"


linha()
print("04")
if 1 < 2 < 4:
    _04 = "Math is fun."


def test_quatro():
    assert _04 == "Math is fun."


linha()
print("05")
nope = None


def test_cinco():
    assert nope == None


linha()
print("06")
if True and False:
    print("Impossível entrar aqui")
else:
    print("Entrei.")
linha()
print("07")
len("What's my length?")  # Essa é a resposta certa.
num = 0
for i in "What's my length?":
    num = num + 1

print(num)


def test_sete():
    assert num == 17


linha()
print("08")
print("i am shouting".upper())

linha()
print("09")
_09 = int("1000")
print(type(_09))

linha()
print("10")
_10 = 4
# str -> Muda o tipo do dado para string
print(f"{str(_10)}real")
linha()
print("11")
print(3 * "cool")
linha()
print("12")
# print(1/0) ZeroDivisionError: division by zero
linha()
print("13")
print(type([]))  # list
linha()
print("14")
name = input("Qual o seu nome ?\n")
print(f"Seu nome é {name}")
linha()
print("15")
num_input_user = float(input("Digite um número: \n"))

if num_input_user < 0:
    print("That number is less than 0!")
elif num_input_user > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")
linha()
print("16")
_16 = "apple".find("l")
print(f"A letra l está na posição: {_16 + 1}")
linha()
print("17")
_17 = "xylophone".find("y")
print(_17)
print("y" in "xylophone")
linha()
print("18")
print("my_string".islower())
