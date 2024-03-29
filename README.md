
![Rossmann_Logo](https://user-images.githubusercontent.com/78666925/184509590-c06577fd-b0fb-4f46-98e1-26162402c86a.png)
<h1 align="center"> PREVISÃO DE VENDAS DAS UNIDADES ROSSMANN  </h1>

<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO%20&color=GREEN&style=for-the-badge"/>
</p>

Tabela de conteúdos
=================
<!--ts-->
   * [Problema de Negócio](#problema-de-negócio)
   * [Planejamento da Solução](#planejamento-da-solução)
   * [Entendimento do Negócio](#entendimento-do-negócio)
   * [Coleta dos Dados](#coleta-dos-dados)
   * [Limpeza dos Dados](#limpeza-dos-dados)
   * [Exploração dos Dados](#exploração-dos-dados)
   * [Modelagem dos Dados](#modelagem-dos-dados)
   * [Algoritmo de Machine Learning](#algoritmo-de-machine-learning)
   * [Avaliação do Algoritmo](#avaliação-do-algoritmo)
   * [Modelo em Produção](#modelo-em-produção)

<!--te-->

## Problema de Negócio
A companhia Rossmann é uma das maiores lojas farmacêuticas da Europa. Contando com mais de 3000 unidades espalhadas por vários países do continente como Espanha, Alemanha, Turquia, Polônia e entre outros. 

Em uma reunião semestral com todos os gerentes de cada unidade o CFO (Chief Financial Officer) tem como objetivo fazer um investimento de reforma nas lojas. Para que isso seja concretizado, os gerente das unidades tem como desafio prever as vendas diárias de um período de 6 semanas em suas respectivas unidades para que parte do lucro das vendas seja separado para que essa ação aconteça. Entre tanto cada unidade tem sua singularidade de fatores que influenciam as vendas, como feriados, promoções, sazonalidade e entre outros fatores. E que acaba gerando previsões muitos discrepantes entre as unidades. 

 Outra dificuldade que CFO tem é de acessar as previsão de vendas de cada unidades. Pois como trata-se de uma empresa com inúmeras lojas espalhadas por quase toda a região da Europa, os gerentes enviam suas predições por meio de e-mail, onde o CFO tem uma grande dificuldade de visualizar cada predição feita por esses gerentes.

## Planejamento da Solução:
Após lido essa introdução da companhia, vimos aqui qual é a questão de negócio a ser solucionado:  Prever as próximas seis semanas de vendas de cada unidade da empresa. 
Para que o CFO consiga acessar de uma forma fácil, as previsões serão agrupadas em único lugar. 

Como trata-se de um grande volume de dados, o projeto será feito por meio da métodológia CRISP, que se baseia em trabalhar de uma forma ciclíca as soluções dos problemas, com isso entregando todas as etapas do projeto o mais rápido possível com o intuito de gerar valor ao time de negócios. 

![metodo_ciclico_CRISP_DS](https://user-images.githubusercontent.com/78666925/184556632-b96a775d-7dbc-4427-9699-402c57d0dd39.png)
 
## Questão de Negócio
Como foi visto na parte "Problema de Negócio", o problema central da empresa Rossmann no momento é saber as previsões de vendas das próximas 6 semanas. Já que os dados forncecidos pelos seus gerentes encontram-se com muitas divergências. 

## Entendimento do Negócio
Já tendo conhecimento da problématica, foi procurado entender o motivo para que essa previsão seja elaborada. O objetivo dessa previsão é para reformas em todas as unidades Rossmann sejam feitas. 

Objetivo do projeto: Este projeto pretente fazer as devidas previsões de todo o faturamento das lojas. Utilizando os métodos cientificos de análise dos dados coletados. Já que os atuais gerentes das unidades não possuem tal conhecimento técnico. 
Para isso, foi decidido contratar um cientista de dados, que tenha essa habilidade para resolver essa problemática. 

## Coleta dos Dados
Os dados utilizados neste projeto podem ser acessados clicando neste link abaixo: 

[Dados do Projeto Rossmann](https://www.kaggle.com/competitions/rossmann-store-sales/data)

## Limpeza dos Dados
Nessa etapa é objetivo é saber qual é o desafio do problema. Então para isso foram feitas as seguintes atividades:

**Descrição dos Dados:** 

- Dimensionamento das linhas e colunas;
- Verificação dos tipos de dados do conjuto de dados;
- Descobrindo a quantidade de valores nulos e o quanto representa em percentual em relação ao todo dataset;
- Tratamento de todos os valores nulos encontrados, onde foi assumindo uma premissa de negócio de acordo com o contéudo de cada coluna;
- Alteração dos tipos de colunas para facilitar o trabalho com os dados;
- Descrição Estatística das váriveis numéricas e catégoricas;
- Feature Engineering: Nessa fase foi elaborada novas features, a partir de um mapa mental, onde foram levantados algumas hipoteses de acordo com elementos citados neste mapa que de alguma maneira podem afetar as vendas. 
 
 ![MindMapHpyothesis](https://user-images.githubusercontent.com/78666925/185799071-f6ce28e1-59c3-4532-810e-9e63b8a90ea0.png)

## Exploração dos Dados

Nessa etapa o objetivo princial é adquirir mais conhecimento sobre o modelo de negócio que estamos trabalhando, além de validar hipóteses levantadas pelo time de negócio da empresa.   

- Filtragem dos dados: Foram feitas a remoção das lojas que estavam fechadas naquele dia e como consequência a remoção das lojas que não obtiveram vendas naquele respectivo dia. 
- Seleções das colunas: Foram feitas as escolhas das feature mais relevantes para o modelo de négocio;
- Analise univáriada: Nessa atividade foram feitas uma série de plotagem de gŕaficos para saber como uma única varáivel dos dadoss afeta o fenômeno das vendas;
- Análise bivariada : Nesa fase foram feitas a exploração mais afundo de duas ou mais váriaveis afim de gerar validaçês das hipotéses listadas, adquirir mais conhecimento sobre o modelo de negócio do projeto e gerar novas insights. 
- Análise multivariada: Foi vericado as correlações entre ás váriaveís tanto numérica quanto categoricas. 

Nas imagens abaixo alguns exemplos das hipótes validadas ou não validadas:

**H3** - Lojas com competidores mais próximo deveriam venderiam menos.
- **Falso**: Lojas vendem mais com competidores mais próximo.
![h3-hipotese-03](https://user-images.githubusercontent.com/78666925/185766363-3d882055-beaf-4d5f-bdfb-ee1b2aeddcf5.png)


**H6**- Lojas com mais promoções consecutivas deveriam vender mais.
- **Falso**: Lojas com mais promoções sucessivas não vendem mais.
![h6-hipotese-06](https://user-images.githubusercontent.com/78666925/185766332-eea19ef0-92f7-49c3-8b45-7f6503bb128a.png)


**H10** - Lojas deveriam vender mais depois do dia 10 de cada mês.
- **Verdade** : Lojas vendem MAIS após o dia 10 de cada mês.
![h10-hipote-10](https://user-images.githubusercontent.com/78666925/185766389-f3bb69da-dd10-4563-81ff-7282bec97c38.png)

## Modelagem dos dados
Nessa fase os dados foram preparados para serem incluídas dentro de um modelo de machine learning, mas para isso os dados precisam ser numéricas e dentro de uma mesma escala. Então foram executadas as seguintes ações:

- Rescaling: Para features numéricas Foram usados os métodos RobustScaler para as váriaveis com outiliers mais acentuados, onde objetivo deste metodo é coletar os quartil dos dados. E para outras váriaveis com menos outiliers foi optado a utilização do MinMaxScaler para esse dimensionamento;
- Encoding: Para features categoricas foram usados os métodos one hot enconding, label enconding  e ordinal enconding;
- Tranformação de Grandeza: Foi feita uma transformação da feature "sales", que é nossa váriavel resposta, para que possa está na mesma escal numérica que os demais features. 
- Transformação de Natureza: Nas features que há um período de tempo ciclíco, foi feita uma normalização, calculando a distância de um período ao outro, usando seno e conseno. 
- Seleção das Features: E finalizando nossa etapa de modelagem dos dados, foi utlizando o algorimo Borutapy que tem o objetivo de remover as colunas que são colineares, ous seja, que não acrescentam melhorias na performance da previsão de vendas deste projeto. 

## Algoritmo de Machine Learning
Nessa fase foram feitos as utilizações de alguns modelos de Machine Learning, afim de saber o tão complexo era os dados do projeto. Então foi escolhido inicialmente um modelo de média como "baseline" e outros quatros modeleos para testar se nossos dados são lineares ou não lineares. 
Para esse teste inicial foi dividido uma parte dos dados para o aprendizado do modelo. 

Os modelos selecionados para os testes foram:

- Linear Regression
- Linear Regression-Lasso	
- Random Forest
- XgBoost Regressor Model

Após o teste o algoritmo que teve um melhor desempenho foi o modelo não-linear Random Forest. Demostrando que nosso projeto contém dados bastantes complexos. 

**Etapa 2:**

Nesta etapa foi feita validações de todos os algoritmos testados anteriomente. Mas para que essa validação seja feita, foi desmembrado uma parte dos dados novamente, entre tanto, essa parte é combinado com outras partes para que a previsão seja realmente mais efetiva. 

Após esse novo ciclo de teste concluído, novamente o modelo Random Forest foi o que teve melhor desempenho. Tabela abaixo aponta o desempenho real de todos os modelos testados no projeto. 

| Model Name | MAE CV | MAPE CV | RMSE CV
| --- | --- | --- | --- |
| Random Forest- CV| 837.59 +/- 218.04	|0.12 +/- 0.02 | 1232.55 +/- 338.98|
| XgBoost Regressor -CV| 1069.73 +/- 232.37| 0.15 +/- 0.03 | 1521.13 +/- 351.27 |
| Linear Regression-CV	| 2036.42 +/- 273.82| 0.3 +/- 0.02	|  2863.19 +/- 450.99 |
| Linear Regression-Lasso-CV| 0.29 +/- 0.01| 0.15 +/- 0.03 | 2960.02 +/- 508.61 |

Apesar do modelo Random Forest te tido o melhor desempenho entre todos, no projeto foi optado por utilizar o algoritmo XgBoost Regressor. Pois como essa é a primeira fase do CRISP, onde o foco maior é agregar valor ao time de négocio da empresa o mais rápido possível, o modelo XgBoost tem uma assertividade muito próxima do Random Forest. Entre tanto esse modelo leva menos tempo para rodar e consegue ser também mais leve e isso  será uma grande vantagem na fase final deste projeto, onde será feita uma hospedagem do modelo em um servidor externo.

## Avaliação do Algoritmo

Após ter feito a seleção do algoritmo para efetuar a previsão das vendas, é necessária saber o quanto a empresa terá de retorno financeiro após o tratamento e modelagem dos dados coletados. Então para isso é necessário intepretar e traduzir os erros do modelo para o time de negócio saiba o tão proximo a previsão está das reais vendas. 

Na tabela abaixo é uma amostra das lojas, que tiveram neste projeto uma melhor performance de previsão do faturamento. 
 

|      store          |    predictions      |     best_scenario   | wors_scenario  |    MAE        |     MAPE  |
| ------------------- | ------------------- | ------------------- | -------------  | ------------- | --------- |  
|  1089               |  377792.40625	      |   377792.461136     | 377792.351364  | 568.940865    |  0.054886 |
|  259                |   555878.12500      |   555878.180920     | 555878.069080  | 677.860215	   |  0.055920 |
|  741                |   555878.12500      |   298727.932730     | 298727.817270  | 463.810903    |  0.057730 |
	
**ERRO MAE:** Esse é interessante apontar para o time de négocio a métrica de erro MAE, pois esse tipo de métrica subtriar dos valores reais os valores preditos e com isso temos a diferença que pode occorer, com isso ocasionando um cenário positivo ou negativo das previsões feitas. 

**ERRO MAPE:** Já a métrica de erro MAPE é uma métrica que fornece o percentual de erro das previsões estimadas. Ela é uma excelente métrica para demostar o ao time de negócios o tão longe ou perto as previsões estão dos números reais das vendas.  

E com isso é possível dizer que após todas essas etapas concluídas o retorno financeiro deste projeto será dentro destes três cenários na tabela a seguir:

|      Scenarios      |         Values      |   
| ------------------- | ------------------- |   
|  predictions	       |  R$287,726,528.00   |   
|  worst_scenario     |  R$287,726,366.55   |   
|  best_scenario      |  R$287,726,634.87   |  

## Modelo em Produção
Como citado anteriomente, além do problema central deste projeto que são as previsões do faturamente das proóximas seis semanas, outro dor que o cliente tem é a dificuldade dele obter essas informações. Já que os gerentes enviam os dados por e-mail. Para resolver esse outro problema foi criador um boot do telegram, onde o CFO só deve colocar quais lojas ele tem interesse de saber e imediatamente é dada a resposta. 

Abaixo uma demostração prática do deploy. 

![telegram_rossmann_gif](https://user-images.githubusercontent.com/78666925/185808542-3e02602d-9d29-4d6e-b9de-c7122cbfb622.gif)

##  Implementação

 ### 0.1 - Preparação do Ambiente Virtual
  Nessa etapa é necessário ter o gerenciador de pacotes pip e do gerenciador de ambiente virtual virtualenv. 
     
   Abra o terminal, vá até a pasta de destino, aonde será criando o ambiente e execute o seguinte comando:
 
   No MacOS ou Linux:
 
 ``` virtualenv --python=/usr/bin/python3.8 <projetorossmann> ```
 
 
   Caso você use o Anaconda:
 
   ```  conda create -n projetorossmann python=3.8 ```
   
   
