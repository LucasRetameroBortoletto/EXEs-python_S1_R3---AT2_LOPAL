# 🐍 AT2 — Exercícios de Lógica de Programação em Python

Repositório com as resoluções dos exercícios da **Atividade 2 (AT2)** da disciplina de Lógica de Programação, cobrindo estruturas de repetição (`for`, `while`), condicionais, listas, dicionários e manipulação de strings.

---

## 📁 Estrutura do Repositório

```
📦 S1_R3_AT2_LOPAL
 ┣ 📄 Exe.1.py
 ┣ 📄 Exe.2.py
 ┣ 📄 Exe.3.py
 ┣ 📄 Exe.4.py
 ┣ 📄 Exe.5.py
 ┣ 📄 Exe.6.py
 ┣ 📄 Exe.7.py
 ┣ 📄 Exe.8.py
 ┣ 📄 Exe.9.py
 ┣ 📄 Exe.10.py
 ┣ 📄 Exe.11.py
 ┗ 📄 README.md
```

---

## 📝 Descrição dos Exercícios

---

### Exercício 1 — Par ou Ímpar (`Exe.1.py`)

Percorre todos os números de **0 a 100** usando um laço `for` e, para cada número, verifica se ele é **par ou ímpar** com o operador módulo (`%`), exibindo a classificação de cada um.

> Conceitos: `for`, `if/else`, operador `%`, `range()`, `format()`

<img width="1312" height="641" alt="image" src="https://github.com/user-attachments/assets/28299880-5028-4c04-99db-27255107e892" />



---

### Exercício 2 — Maior e Menor Valor (`Exe.2.py`)

Solicita ao usuário **três números inteiros**, armazena-os em uma lista e utiliza as funções nativas `max()` e `min()` para identificar e exibir o **maior** e o **menor** valor digitado.

> Conceitos: `input()`, listas, `max()`, `min()`, `format()`

<img width="1315" height="638" alt="image" src="https://github.com/user-attachments/assets/67ddefb8-f34c-4af7-bed6-370c4658e61d" />


---

### Exercício 3 — Fatiamento Progressivo de String (`Exe.3.py`)

Recebe uma **palavra** digitada pelo usuário e a imprime de forma progressiva — primeiro apenas a primeira letra, depois as duas primeiras, e assim por diante até exibir a palavra completa. Utiliza fatiamento de strings (`string[0:n]`) dentro de um laço `for`.

> Conceitos: `for`, slicing de strings, contador auxiliar

<img width="1313" height="641" alt="image" src="https://github.com/user-attachments/assets/42f93d58-074f-4fea-a5d3-850a26da51b3" />


---

### Exercício 4 — Sequência de Fibonacci (`Exe.4.py`)

Gera a **sequência de Fibonacci** com a quantidade de termos informada pelo usuário. A lista já é iniciada com os dois primeiros termos `[1, 1]` e os próximos são calculados somando os dois anteriores dentro de um laço `for`.

> Conceitos: `for`, `range()`, listas, `append()`, variáveis auxiliares

<img width="1294" height="637" alt="image" src="https://github.com/user-attachments/assets/b37f0fed-40de-47c9-9768-9f8b0cda62dc" />



---

### Exercício 5 — Validação de Cadastro (`Exe.5.py`)

Formulário completo de cadastro com **validação em tempo real** para cinco campos, utilizando laços `while True` com `break` para garantir que o usuário só avance com dados válidos:

| Campo | Regra de validação |
|---|---|
| Nome | Mínimo de 4 caracteres |
| Idade | Entre 1 e 150 anos |
| Salário | Valor maior que zero |
| Sexo | Apenas `F` ou `M` (case-insensitive) |
| Estado Civil | `S` (Solteiro), `C` (Casado), `V` (Viúvo) ou `D` (Divorciado) |

Ao final, os dados são exibidos formatados com alinhamento usando f-strings.

> Conceitos: `while True`, `break`, `len()`, `upper()`, `float()`, f-strings com formatação

<img width="1577" height="973" alt="image" src="https://github.com/user-attachments/assets/69acc7de-b707-4d41-9066-1e75814d5fb0" />



---

### Exercício 6 — Verificador de Número Primo (`Exe.6.py`)

Verifica se um número inteiro informado pelo usuário é **primo**. A lógica tenta dividir o número por todos os inteiros de 2 até ele menos 1; se encontrar algum divisor, confirma que não é primo. Usa o `for/else` do Python para cobrir o caso em que nenhum divisor foi encontrado.

> Conceitos: `for/else`, operador `%`, `range()`, `break`

<img width="1317" height="642" alt="image" src="https://github.com/user-attachments/assets/965aa4c3-ea0c-4ad6-84fa-f85764110db3" />


---

### Exercício 7 — Fatorial (`Exe.7.py`)

Calcula o **fatorial** de um número e exibe tanto o resultado quanto a equação multiplicativa completa (ex: `5! = 5x4x3x2x1 = 120`). A lista com os fatores é invertida com `reverse()` e unida com `"x".join()` para montar a expressão visual.

> Conceitos: `for`, `range()`, listas, `append()`, `reverse()`, `join()`, `format()`

<img width="1315" height="639" alt="image" src="https://github.com/user-attachments/assets/abcb486a-1311-4631-abcd-ab3e66c619de" />


---

### Exercício 8 — Funções Nativas de Lista (`Exe.8.py`)

Demonstra o uso das principais **funções nativas do Python** aplicadas a uma lista pré-definida `[5, 7, 2, 9, 4, 1, 3]`:

| Função | O que faz |
|---|---|
| `len()` | Retorna o tamanho da lista |
| `max()` | Retorna o maior elemento |
| `min()` | Retorna o menor elemento |
| `sum()` | Soma todos os elementos |
| `sorted()` | Retorna a lista em ordem crescente |
| `sorted(..., reverse=True)` | Retorna a lista em ordem decrescente |

> Conceitos: listas, `len()`, `max()`, `min()`, `sum()`, `sorted()`

<img width="1308" height="639" alt="image" src="https://github.com/user-attachments/assets/82bb76f7-b6ad-4bc3-a10b-b02f5ff20581" />


---

### Exercício 9 — Dicionário de Lanchonete (`Exe.9.py`)

Cria e exibe um **dicionário** representando o cardápio de uma lanchonete, associando cada produto ao seu respectivo preço.

| Produto | Preço |
|---|---|
| Salgado | R$ 4,50 |
| Lanche | R$ 6,50 |
| Suco | R$ 3,00 |
| Refrigerante | R$ 3,50 |
| Doce | R$ 1,00 |

> Conceitos: dicionários (`dict`), criação e exibição de pares chave-valor

<img width="1313" height="631" alt="image" src="https://github.com/user-attachments/assets/3ed07b37-48eb-4ed7-81d7-5d024b03ce28" />


---

### Exercício 10 — Sistema de Senha (`Exe.10.py`)

Mantém o usuário em um laço `while True` solicitando uma senha numérica. Se o valor digitado for igual à senha correta (`676767`), exibe "Acesso liberado!!" e encerra o programa com `break`. Caso contrário, exibe mensagem de acesso negado e repete.

> Conceitos: `while True`, `if/else`, `int(input())`, `break`

<img width="1319" height="628" alt="image" src="https://github.com/user-attachments/assets/cd8c8ad5-1381-4b7d-a5a9-54217bfcd545" />


---

### Exercício 11 — Tabuada (`Exe.11.py`)

Solicita um número ao usuário e exibe sua **tabuada completa** de 1 a 10, formatando cada linha como `N x I = resultado` dentro de um laço `for`.

> Conceitos: `for`, `range()`, `format()`, operação aritmética

<img width="1317" height="640" alt="image" src="https://github.com/user-attachments/assets/28325516-9d41-4321-9161-6d6bb01cde1d" />


---

## 🛠️ Como Executar

Certifique-se de ter o **Python 3** instalado. Para rodar qualquer exercício:

```bash
python Exe.1.py
```

Substitua `Exe.1.py` pelo arquivo desejado.

---

## 📚 Conceitos Abordados

- Estruturas de repetição: `for` e `while`
- Estruturas condicionais: `if`, `elif`, `else`
- Funções nativas: `len()`, `max()`, `min()`, `sum()`, `sorted()`, `range()`
- Listas: criação, `append()`, `reverse()`, `join()`
- Dicionários: criação e exibição
- Manipulação de strings: slicing, `upper()`, `format()`, f-strings
- Validação de entrada com `while True` + `break`
