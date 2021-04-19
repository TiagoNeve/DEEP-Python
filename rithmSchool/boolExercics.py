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
num = 0
for i in "What's my length?":
    num = num + 1

print(num)


def test_sete():
    assert num == 17


linha()
print("08")
print("i am shouting".upper())
