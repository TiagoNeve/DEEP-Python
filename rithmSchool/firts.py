
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

# Strings
print("="*20)
for x in "word":
    print(x)

x = "my favorite "\
    "string"
print(x)  # my favorite string

my_str = "can't touch this"
# my_str[6] = " "
# TypeError : 'str' object does not support item assignment

new_str = "hello "
for c in "world":
    new_str += c  # Adicionando cada letra na variável new_str

print(new_str)  # hello world

# String métodos
print("="*20)
string = "this is nIce"
print(string.upper())  # THIS IS NICE
print(string.lower())  # this is nice
print(string.capitalize())  # This is nice
print(string.title())  # This Is Nice

instructor = 'elie'
print(instructor.find('e'))  # 0
print(instructor.find('E'))  # -1
print(instructor.find('ie'))  # 2
print(instructor.find('ies'))  # -1

print(string.isalpha())  # False
print(string.isspace())  # False

print(string.partition(' '))  # Retorna a string separadas em tupla.

# Interpolação de strings com Strings formatadas.
first_name = "Tiago"
last_name = "Neves"
city = "Fortaleza"
mood = "muito bem"

greeting = f"Olá, meu nome é {first_name} {last_name}, eu moro em" \
    f" {city} e estou {mood}"
print(greeting)
