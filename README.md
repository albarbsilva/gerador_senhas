# 🔐 Gerador de Senhas em Python

Um gerador de senhas simples, seguro e interativo feito em Python. Projeto desenvolvido para fins de aprendizado, cobrindo conceitos fundamentais da linguagem.

---

## 📋 Funcionalidades

- Gerar senhas aleatórias com letras, números e símbolos
- Escolher o tamanho da senha
- Escolher a quantidade de senhas geradas de uma vez
- Tratamento de erros para entradas inválidas
- Loop interativo para gerar novas senhas sem reiniciar o programa

---

## 🧰 O que foi usado

- `random` — para sortear os caracteres aleatoriamente
- `string` — para acessar coleções de caracteres prontas (letras, números e símbolos)
- `for` loop — para repetir a geração de senhas
- `while` loop — para manter o programa rodando até o usuário querer sair
- `try/except` — para tratar erros de entrada do usuário
- `f-strings` — para exibir os resultados de forma organizada

---

## 🚀 Como usar

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/gerador-de-senhas.git
```

**2. Acesse a pasta:**
```bash
cd gerador-de-senhas
```

**3. Rode o programa:**
```bash
python GeradordeSenhas.py
```

> Não é necessário instalar nenhuma dependência externa. As bibliotecas usadas (`random` e `string`) já vêm instaladas com o Python.

---

## 💻 Exemplo de uso

```
=== Gerador de Senhas ===

Qual o tamanho da senha? 12
Quantas senhas você quer gerar? 3

Suas senhas são:
  1. aB#3kP!qXm@9
  2. nL$wKp!2vR#j
  3. Qs$7mN@xWt#4

Gerar outra senha? (s/n): n
Até mais!
```

---

## 📁 Estrutura do projeto

```
gerador-de-senhas/
└── GeradordeSenhas.py
```

---

## 🧠 Conceitos aprendidos

Este projeto foi desenvolvido do zero com foco em aprendizado. Os conceitos cobertos foram:

- Importação de bibliotecas com `import`
- Criação e uso de variáveis
- Definição de funções com `def` e `return`
- Interação com o usuário via `input()`
- Conversão de tipos com `int()`
- Tratamento de erros com `try/except`
- Repetição com `while` e `for`
- Formatação de texto com f-strings

---

## 👩‍💻 Autora

Feito com 💜 por Aline  
Projeto de aprendizado — Python do zero!
