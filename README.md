
![Rossmann_Logo](https://user-images.githubusercontent.com/78666925/184509590-c06577fd-b0fb-4f46-98e1-26162402c86a.png)
<h1 align="center"> PREDIÇÃO DE VENDAS DAS UNIDADES ROSSMANN  </h1>

<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO%20&color=GREEN&style=for-the-badge"/>
</p>

## Problema de Negócio
A companhia Rossmann é uma das maiores lojas farmacêuticas da Europa. Contando com mais de 3000 unidades espalhadas por vários países do continente como Espanha, Alemanha, Turquia, Polônia e entre outros. 

Em uma reunião semestral com todos os gerentes de cada unidade o CFO () tem como objetivo fazer um investimento de reforma nas lojas. Para que isso seja concretizado, os gerente das unidades tem como desafio prever as vendas diárias de um período de 6 semanas em suas respectivas unidades para que parte do lucro das vendas seja separado para que essa ação aconteça. Entre tanto cada unidade tem sua singularidade de fatores que influenciam as vendas, como feriados, promoções, sazonalidade e entre outros fatores. E que acaba gerando previsões muitos discrepantes entre as unidades. 

 Outra dificuldade que CFO tem é de acessar as previsão de vendas de cada unidades. Pois como trata-se de uma empresa com inúmeras lojas espalhadas por quase toda a região da Europa, os gerentes enviam suas predições por meio de e-mail, onde o CFO tem uma grande dificuldade de visualizar cada predição feita por esses gerentes.

## Planejamento da Solução:
Após lido essa introdução da companhia, vimos aqui qual é a questão de negócio a ser solucionado:  Prever as próximas seis semanas de vendas de cada unidade da empresa. 
Para que o CFO consiga acessar de uma forma fácil, as previsões serão agrupadas em único lugar. 

Como trata-se de um grande volume de dados, o projeto será feito por meio da métodológia CRISP-DM, que se baseia em trabalhar de uma forma ciclíca as soluções dos problemas, com isso entregando todas as etapas do projeto o mais rápido possível com o intuito de gerar valor ao time de negócios. 



![metodo_ciclico_CRISP_DS](https://user-images.githubusercontent.com/78666925/184556632-b96a775d-7dbc-4427-9699-402c57d0dd39.png)

## 0 - Implementação

 ### 0.1 - Preparação do Ambiente Virtual
  Nessa etapa é necessário ter o gerenciador de pacotes pip e do gerenciador de ambiente virtual virtualenv. 
     
   Abra o terminal vá até a pasta de destino aonde será criando o ambiente e execute o seguinte comando:
 
   No MacOS ou Linux:
 
 ``` virtualenv --python=/usr/bin/python3.8 <projetorossmann> ```
 
 
   Caso você use o Anaconda:
 
   ```  conda create -n projetorossmann python=3.8 ```
      

      
   
 
## Questão de Negócio
 Como foi visto na parte "Problema de Negócio", o problema central da empresa Rossmann no momento é saber as previsões de vendas das próximas 6 semanas. Já que os dados forncecidos pelos seus gerentes encontram-se com muitas divergências. 

## Entendimento do Negócio
Já tendo conhecimento da problématica, foi procurado entender o motivo para que essa previsão seja elaborada. O objetivo dessa previsão é para reformas em todas as unidades Rossmann sejam feitas. 

Objetivo do projeto: Então este projeto pretente fazer as previsões dos pŕoximos dias do faturamento de todas as lojas, utilizando os métodos cientificos de análise. Já que os gerentes não contém esse conhecimento técnico. 

Então para isso, foi decido contrator um cientista de dados que tenha essa habilidade para resolver tal problemática. 

## Coleta dos Dados
Os dados utilizados neste projeto foram retirado do site abaixo:

https://www.kaggle.com/competitions/rossmann-store-sales/data

## Limpeza dos Dados
Nessa parte foram feitas as seguintes atividades:

Descrição dos Dados: Nessa etapa foram verificados o dimensionamento das linhas e colunas; tratamentos de dados nulos; 

## Exploração dos Dados

## Modelagem dos dados

## Algoritmo Machine Learning

## Avaliação do Algoritmo 

## Modelo em Produção

