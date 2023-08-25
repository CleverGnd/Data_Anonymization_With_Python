<h1 align="center">Projeto de Anonimização de Dados com Python</h1>

</div align="center">
Este projeto tem como objetivo demonstrar um exemplo simples de anonimização de dados, um conceito importante atualmente, especialmente relacionado à Lei Geral de Proteção de Dados Pessoais (LGPD).
<br>
A anonimização de dados é uma técnica utilizada para proteger a privacidade e confidencialidade das informações pessoais. Ela consiste em transformar os dados de forma que sejam muito difíceis de serem associados a uma pessoa específica.
<br>
<br>

Curso: Anonimização de Dados com Python
[QualiFacti](https://qualifacti.facti.com.br/)

<h2> Resumo </h2>

* [Arquivos](#Arquivos)
* [Como utilizar este projeto](#ComoExecutar)
* [Funcionalidades](#Funcionalidades)
* [Avisos!](#Avisos)
* [Autor](#autor)

</div align="center">
O projeto foi desenvolvido utilizando o PostgreSQL como banco de dados, o VScode como ambiente de desenvolvimento e a linguagem Python. Além disso, foram utilizadas algumas bibliotecas básicas do Python.
<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

<h3 id="Arquivos">Arquivos</h3>

O projeto consiste em dois arquivos:

- [query.sql](.\query.sql): Este arquivo contém a query SQL para criar o banco de dados de exemplo, juntamente com duas tabelas: "cliente" e "contatos". Os dados nessas tabelas foram gerados aleatoriamente utilizando a biblioteca Faker do Python.
- [anonimizacao.py](.\anonimizacao.py ): Este arquivo contém o código-fonte do projeto em Python. Ele implementa funções para realizar a anonimização dos dados, utilizando métodos como criptografia, mascaramento e generalização.

<h3 id="ComoExecutar">Como utilizar este projeto</h3>

Para executar o projeto, siga as etapas abaixo:
1. Certifique-se de ter o Python em sua máquina. Você pode baixar o Python em [python.org](https://www.python.org/downloads/);
2. Certifique-se de ter o PostgreSQL em sua máquina. Você pode baixar o PostgreSQL em [postgresql.org](https://www.postgresql.org/download/);
3. Clone este repositório em sua máquina;
4. Execute o arquivo [query.sql](.\query.sql) para criar o banco de dados de exemplo;
5. Edite o arquivo [anonimizacao.py](.\anonimizacao.py) e altere as variáveis de conexão com o banco de dados para que elas correspondam às configurações do seu banco de dados;
6. Execute o arquivo [anonimizacao.py](.\anonimizacao.py);
7. Siga as instruções no terminal para escolher o método de anonimização desejado.

<h3 id="Funcionalidades">Funcionalidades</h3>

Alguns exemplos de como os dados são anonimizados:

- Criptografia: É o processo de transformar dados em uma forma ilegível usando um algoritmo e uma chave. Isso garante a confidencialidade dos dados, permitindo que apenas as pessoas com a chave correta possam acessá-los. Sendo útil para proteger informações confidenciais, como senhas de usuário, armazenando-as em um formato seguro.
*Neste projeto foi utilizado o algoritmo de hash SHA256.

``` bash
E-mail original: lucas_freitas@almeida.com
E-mail anonimizado: 4a4280edc61a93d7684bb74ab09c446d327b9fadf5377eddc2b0937ab0cf0edf
```
- Mascaramento: Consiste em substituir caracteres específicos em um valor por caracteres genéricos, como asteriscos. Isso oculta informações sensíveis, preservando o formato geral do dado. Pode ser útil para ocultar partes sensíveis de informações, como números de telefone ou endereços de e-mail, exibindo apenas uma representação mascarada desses valores.
``` bash
Telefone original: (71) 43410-7964
Telefone anonimizado: ***************
```

- Generalização: Envolve a substituição de valores específicos em um dado por representações mais genéricas. Isso reduz a granularidade dos dados, protegendo a privacidade. Útil para preservar a privacidade dos dados, como em um conjunto de dados de pesquisa, onde os valores reais são substituídos por representações genéricas.
``` bash
CPF original: 580.421.673-26
CPF anonimizado: 000.000.000-00
```

<h3 id="Avisos">Avisos</h3>

Lembre-se de que este projeto é apenas uma demonstração simplificada da anonimização de dados e não leva em consideração todos os aspectos e requisitos da LGPD ou de outras regulamentações de proteção de dados. É importante entender os requisitos específicos da sua aplicação e buscar orientações legais adequadas antes de implementar a anonimização de dados em um ambiente de produção.

<h2 id="autor">Autor</h2>

[![Linkedin Badge](https://img.shields.io/badge/-CleversonGuandalin-%230077B5?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/cleversonguandalin/)](https://www.linkedin.com/in/cleversonguandalin/)

Para mais informações sobre o curso "Anonimização de Dados com Python" e outros cursos oferecidos pela QualiFacti, acesse [qualifacti.facti.com.br](https://qualifacti.facti.com.br/).

