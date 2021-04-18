# Python 1 - Rithm School

## Iniciando

* Tipos de dados
    - Booleans -> True ou False
    - Numbers -> Int ou FLoats
    - Strings -> Recebem caracteres entre aspas
    - Lists -> [1, 2, 3, "the end"] , São mutáveis
    - Tuples -> (1, 2, 3), são imutáveis
    - Sets -> São quase iguais as listas, porém não são ordenadas por indexes. set("a", "b", "c");
    - Dictionaries -> {"key": "value", "a": 0}, são dados de chave e valores.
* Os arquivos python tem a extensão .py
<hr>
* Variáveis
    As variáveis são declaradas apenas dando nome a elas, e seu tipo
    é definido pelo valor que ela recebe, por exemplo: 
    a = 1 -> Number INT
    b = "YOLO" -> String
    nothing = None -> Variável sem tipo bem definido. NoneType
    É possível definir declarar várias variáveis ao mesmo tempo e 
    definir seus valores :
    a, b = 1, 2 -> a == 1, b == 2
    As variáveis podem ser declaradas iniciando com _ (underline) ou
    letras. No restante pode ter números.
    A conversão adotada no python para nomeação de variáveis é o :
    * lower_snake_case -> para variáveis.
    * CAPITAL_SNAKE_CASE -> para constantes.
    * UpperCamelCase -> para classes.
    Variáveis que começam com dois underline e termina com dois 
    underline, são usadas para variáveis privadas ou aquelas que 
    são incorporadas na linguagem.
* Tipo de dados.
    bool -> True ou False;
    int -> inteiro
    float -> decimal
    str -> String
    list -> coleção ordenada por indices
    dict -> Dicionário de chave: value
    tuple -> coleção não ordenada
    None -> Sem tipo definido
    Para verificar o tipo de uma variável deve-se usar a função
    type(). 
    No python todos as variáveis e dados são objetos, dessa forma 
    a programação orientada a objetos é essencial nessa linguagem
* Tipagem dinâmica.
    No python as variáveis são dinâmicas, podem receber tipos 
    diferentes de dados a qualquer momento, porém somar tipos 
    diferentes irá gerar um erro.
    Desta forma python é dinamicamente tipada e fortemente tipada
    