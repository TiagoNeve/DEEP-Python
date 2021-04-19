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

## Strings
* Strings em python
    Uma string no python é um conjunto de caracteres, é possível 
    usar um loop para para mostrar cada caractere de uma string.
    Também é possível definir strings multilinhas usando \ ao fim da
    linha.
    Strins no python não podem ser imutáveis diretamente.
* Unicode vs ASCII
    Em python2 as strings eram usadas em ASCII, mas no python3 essas
    strings passaram a serem usadas em Unicode.
    ASCII -> Não reconhece tantos caracteres,
    Unicode -> Reconhece todos os caracteres e emojis.
* Métodos strings
    .upper() -> Coloca todos os caracteres em maiusculas
    .lower() -> Coloca todos os caracteres em minusculas
    .capitalize() -> Coloca a primeira letra em maiusculo.
    .title() -> Todas as palavras ficam com a letra maiúscula
    .find() -> Procura na string a primeira ocorrência da string
    desejada e caso não encontre retorna -1.
    .isalpha() -> Verifica se todos os caracteres de uma string é
    alfabética. Return bool
    .isspace() -> Verifica se todos os caractes são espaços vazios.
    Return bool
    .islower() -> Verifica se todos os caracteres são minusculos.
    .istitle() -> Verifica se a string está em modo title.
    .endswith() -> Verifica se uma string termina com determinada
    strin passada como argumento.
    .partition() -> Separa a string em 3 itens de uma tupla 
    definindo o separador como argumento.
* Interpolação de strins com Strings formatadas.
    .format() -> Método muito usado para juntar strings em outras
    strings.
    Para evitar o usu de format, você pode definir o f"string", que 
    basta declarar um f antes da string e usar a interpolação como
    o format.