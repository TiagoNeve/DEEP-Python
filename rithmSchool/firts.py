
print("Eae mundão")

# Variáveis
a, b = 1, "YOLO"
nothing = None

_cats = "meow"  # Válido
abc123 = 1970  # Válido

# 2cats = 1  # SyntaxError - invalid syntax
# hey@you = 1  # SyntaxError - cannot assing to operator

print(type(a))  # int
print(type(b))  # str
print(type(nothing))  # NoneType

myVariable = 3  # Cai fora daqui, isso não é javascript
my_variable = 3  # Muito melhor
AVOGRADO_CONSTANT = 6.022140857 * 10 ** 23
__no_touchy__ = 3  # Alguém não quer que você mecha nisso.

# Tipo de dados
print("="*20)
print(type(False))  # bool
print(type("nice"))  # str
print(type({}))  # dict
print(type([]))  # list
print(type(()))  # tuple
print(type(None))  # NoneType

# Tipagem dinâmica

x = 3
y = " cats"
#print(x + y)
# TypeError: unsupported operand type(s) for +: 'int' and 'str';
