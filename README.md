# Case Técnico Geofusion - Previsão de Faturamento

![image](https://user-images.githubusercontent.com/73614098/121671593-bd8fb780-ca7c-11eb-88b9-306fe30765d8.png)

---
## Introdução
Este projeto foi desenvolvido como resolução do Case Técnico para a vaga de Estagiário de Machine Learning pela Geofusion. Foi solicitada uma análise exploratória e o desenvolvimento de um modelo de Regressão. O conjunto de dados carrega uma série de informações sociodemográficas, e o faturamento da empresa, em cada bairro.

Devido a pequena quantidade de dados, fiz a coleta de algumas informações adicionais na web. Do site da Wikipédia, coletei os seguintes dados por bairro: IDH, Subprefeitura, Região Administrativa e Área. Com isso, foi possível realizar algumas análises de público alvo mais acuradas, além de melhorar o desempenho do modelo.

A entrega desse projeto está sendo feita de algumas maneiras. Este documento contém os principais insights do projeto, além da análise dos resultados do modelo de Machine Learning. Os notebooks - Webscraping, Projeto e Análise - estão todos na pasta 'notebooks'. O modelo final foi entregue em produção pelo Heroku e **possivelmente um bot no telegram**.

Esse documento serve como um guia do projeto. A descrição das etapas estão inclusas nas próximas sessões.

## Índice
- [01. O Problema de Negócio](https://github.com/tadeucbm/case_geofusion#01-o-problema-de-neg%C3%B3cio)
- [02. A Solução](https://github.com/tadeucbm/case_geofusion#02-a-solu%C3%A7%C3%A3o)
- [03. Insights](https://github.com/tadeucbm/case_geofusion#30-insights)
- [04. Aplicação do Modelo de Machine Learning](https://github.com/tadeucbm/case_geofusion#40-aplica%C3%A7%C3%A3o-do-modelo-de-machine-learning)
- [05. Performance do Modelo de Machine Learning](https://github.com/tadeucbm/case_geofusion#50-performance-do-modelo-de-machine-learning)
- [06. Resultados de Negócio](https://github.com/tadeucbm/case_geofusion#60-resultados-de-neg%C3%B3cio)
- [07. Coclusões](https://github.com/tadeucbm/case_geofusion#70-conclus%C3%B5es)
- [08. Lições aprendidas](https://github.com/tadeucbm/case_geofusion#80-li%C3%A7%C3%B5es-aprendidas)
- [09. Próximos PAssos](https://github.com/tadeucbm/case_geofusion#90-pr%C3%B3ximos-passos)

---
## 01. O Problema de Negócio
Um cliente do ramo alimentício no Rio de Janeiro solicitou uma análise para poder entender melhor o seu público alvo. Do conjunto de dados, estão disponíveis algumas métricas sociogeograficas de cara bairro - Renda média, idade, população e domicilios. Além disso, estão disponíveis os seus resepctivos faturamentos brutos. Estão disponíveis, ao total, 160 bairros para análise.

Análise do Problema:
- **Granularidade**: Por bairro;
- **Tipo de Modelo**: Regressão.

---
## 02. A Solução
A solução do problema está entregue em dois formatos:
- **Análise Exploratória dos Dados** -> Fornecimento de Insights sobre as principais variáveis que impactam o faturamento do cliente. 
- **Bot no Telegram** -> Modelo de Regressão em produção no Heroku. Os resultados estão disponíveis através de um Bot no aplicativo **Telegram**.

---
## 3.0. Insights

Através da Análise Exploratória dos Dados, foi possível identificar alguns padrões sociodemográficos do público alvo do cliente. Algumas variáveis possuem um impacto sobre o problema em maior dimensão. As seguintes visões do problema foram analisadas:

![image](https://user-images.githubusercontent.com/73614098/121753047-80a8dc80-cadf-11eb-9776-76cda62d860d.png)

 Alguns bairros se destacam no nível de receita. O gráfico a seguir elenca os dez principais bairros por ordem de faturamento bruto:

![image](https://user-images.githubusercontent.com/73614098/121832202-89441300-cc97-11eb-92d3-4dfa7ee89a14.png)

Ao colocar os dados médios dos dez principais bairros em faturamento, alguns padrões são verificados:

![image](https://user-images.githubusercontent.com/73614098/121832546-50f10480-cc98-11eb-8a96-3a01f16b239c.png)

Com o mapa de calor do faturamento dos bairros da cidade, é visível o padrão geográfico existente:

![image](https://user-images.githubusercontent.com/73614098/121749035-ff018080-cad7-11eb-95cc-5956c70b9991.png)

Os principais pontos de faturamento se concentram na **Zona Sul** e no **Centro**, além da **Barra da Tijuca**. O comércio na Zona Norte também possui um padrão médio interessante. Já o consumo na zona oeste é bem abaixo das demais localizações.


Ao analisar a correlação entre as variáveis disponíveis, algumas se destacaram:

### IDH x Faturamento
O IDH possui alto impacto sobre o Faturamento.

![image](https://user-images.githubusercontent.com/73614098/121832660-91e91900-cc98-11eb-950a-85db62b82797.png)

### Renda Média x Faturamento

A Renda Média Domiciliar também apresenta alta influência no Faturamento.

![image](https://user-images.githubusercontent.com/73614098/121832671-99a8bd80-cc98-11eb-9b21-57d40e160679.png)

### Tipo de Domicílio x Faturamento

O Faturamento possui boa correlação com o Tipo de Residência predominante no bairro. Bairros de padrão mais elevado apresentam altos níveis de receita para o comércio.

![image](https://user-images.githubusercontent.com/73614098/121833054-7f231400-cc99-11eb-8c24-2978d610865d.png)

### Idade x Faturamento

A Idade também demonstra alta correlação com o Faturamento. Percebe-se que bairros de idade média superior costumam ser mais rentáveis.

![image](https://user-images.githubusercontent.com/73614098/121833243-eb9e1300-cc99-11eb-9982-764ba537b765.png)

### Perfil

Dessa forma, é possível traçar um perfil médio do público alvo desse comércio:

![image](https://user-images.githubusercontent.com/73614098/121834823-b72c5600-cc9d-11eb-870e-0f22782e5eb4.png)

---
## 4.0. Aplicação do Modelo de Machine Learning
Por ser um problema com poucos dados, todo cuidado foi necessário para não prejudicar a performance do modelo. Valores irreais foram retirados. Alguns Outliers também tiveram que ser limitados. 

Além disso, os dados foram separados entre Treino e Teste na proporção 70/30. A escolha do modelo foi feita com o uso do **CrossValidation**. A métrica de escolha utilizada foi o **MAPE** (Mean Absolute Percentage Error). Ela toma como base o erro percentual de cada previsão individual, e calcula a média final. O modelo com o menor MAPE deverá ser o escolhido.

O comparativo dos modelos utilizados ficou da seguinte maneira:

![image](https://user-images.githubusercontent.com/73614098/121836359-4424de80-cca1-11eb-8775-e725446279fe.png)

Tanto a DecisionTreeRegressor quanto a RandomForestRegressor, dois modelos com base em árvores de decisão, tiveram larga vantagem sobre os demais. Como a **Random Forest** apresentou valores melhores, ela foi a escolhida como o modelo a ser utilizado nesse primeiro ciclo.

---
## 5.0. Performance do Modelo de Machine Learning

Modelo escolhido, devemos melhorar seus Hiperparametros e avaliar a sua capacidade de generalização. 

Sobre os dados de Teste o modelo de **Random Forest Regressor** Aprensentou um valor de MAPE de **0.1051**. Ou seja, em média, o modelo em 10.50% os valores de faturamentos para dados nunca vistos antes.

Também avaliei o modelo utilizando o **CrossValidation**, só que dessa vez em todo o Dataset. 

![image](https://user-images.githubusercontent.com/73614098/121838665-5c4b2c80-cca6-11eb-982c-7491d38b4f75.png)

O Modelo funciona de maneira satisfatória. Consegue aprender bon padrões dos dados de treinos. Mas também é capaz de generalizar para dados nunca vistos. 
Todas as nossas previsões seguiram as tendências dos faturamentos reais. Os erros existentes são mínimos. 

![image](https://user-images.githubusercontent.com/73614098/121925551-0a88bd80-cd0b-11eb-8b45-c5a71a454314.png)


---
## 6.0. Resultados de Negócio
Visualizar os possíveis cenários é a melhor forma de traduzir o modelo para os resultados de negócio. Dessa forma, o cliente pode ter o valores previstos de faturamento e tomar decisões com base neles.

![image](https://user-images.githubusercontent.com/73614098/121926681-35274600-cd0c-11eb-8ac7-fbb15ee281f5.png)

O modelo final foi entregue em produção. Através de um questionário com 10 questões, é possível fazer uma previsão de faturamento de um bairro. Esse repositório está acompanhado de um arquivo chamado API Tester. Nele é possível usar a API.


---
## 7.0. Conclusões

Este primeiro ciclo do projeto foi um sucesso. Mesmo com uma pequena base de dados, foi possível entregar uma Análise Exploratória de Dados com Insights sobre o negócio do cliente. Também foi entregue um modelo em produção capaz de fazer previsões sobre novos bairros, de forma acurada. O objetivo final foi concluido: Apoiar a tomada de decisão do cliente.

--- 
## 8.0. Lições Aprendidas

Esse projeto foi desafiador. Como desenvolver um modelo bom com poucos dados foi o principal ponto de reflexão. Devido a isso, acabei me aprofundando no funcionamento de algumas técnicas de avaliação.
A Análise Exploratória de Dados também agregou de forma positiva. Além de desenvolver algumas técnicas e conhecer novas bibliotecas, foi possível obter um maior conhecimento de negócio.

---
## 9.0. Próximos Passos

Os próximos passos para aumentar a escala e a eficiência do modelo são:

- Criar um Pipeline de avaliação do modelo, em tempo real;
- Obter mais dados de outros bairros do Estado;
- Testar novos algorítmos;
- Testar novas Features;
- Buscar novas informações para os dados.

---

<br/><br/>
<br/><br/>
<p align="center">
    <a href="https://www.linkedin.com/in/tadeumadureira/" target="_blank"><img alt="GitHub" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
    <a href="https://github.com/tadeucbm" target="_blank"><img alt="linkedin" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
    <a href="mailto:tadeucastbm@gmail.com?subject=HelloTadeu,%20From%20Github" target="_blank"><img alt="gmail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>


