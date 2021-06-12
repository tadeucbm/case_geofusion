# Case Técnico Geofusion - Previsão de Faturamento

![image](https://user-images.githubusercontent.com/73614098/121671593-bd8fb780-ca7c-11eb-88b9-306fe30765d8.png)

---
## Introdução
Este projeto foi desenvolvido como resolução do Case Técnico para a vaga de Estagiário de Machine Learning pela Geofusion. Foi solicitada uma análise exploratória e o desenvolvimento de um modelo de Regressão. O conjunto de dados carrega uma série de informações sociodemográficas, e o faturamento da empresa, em cada bairro.

Devido a pequena quantidade de dados, fiz a coleta de algumas informações adicionais na web. Do site da Wikipédia, coletei os seguintes dados por bairro: IDH, Subprefeitura, Região Administrativa e Área. Com isso, foi possível realizar algumas análises de público alvo mais acuradas, além de melhorar o desempenho do modelo.

A entrega desse projeto está sendo feita de algumas maneiras. Este documento contém os principais insights do projeto, além da análise dos resultados do modelo de Machine Learning. Os notebooks - Webscraping, Projeto e Análise - estão todos na pasta 'notebooks'. O modelo final foi entregue em produção pelo Heroku e **possivelmente um bot no telegram**.

Esse documento serve como um guia do projeto. A descrição das etapas estão inclusas nas próximas sessões.

## Índice
- [01. O Problema de Negócio](https://github.com/tadeucbm/case_geofusion/blob/main/README.md#01-o-problema-de-neg%C3%B3cio)
- [02. A Solução](https://github.com/tadeucbm/case_geofusion/blob/main/README.md#02-a-solu%C3%A7%C3%A3o)
- [03. Exploratory Data Analysis (EDA)](#03-exploratory-data-analysis-eda)
- [04. Data Preprocessing and Feature Selection](#04-data-preprocessing-and-feature-selection)
- [05. Machine Learning Modeling](#05-machine-learning-modeling)
- [06. Hyperparameter Tuning](#06-hyperparameter-tuning)
- [07. Business Performance](#07-business-performance)

---
## 01. O Problema de Negócio
Um cliente do ramo alimentício no Rio de Janeiro solicitou uma análise para poder entender melhor o seu público alvo. Do conjunto de dados, estão disponíveis algumas métricas sociogeograficas de cara bairro - Renda média, idade, população e domicilios. Além disso, estão disponíveis os seus resepctivos faturamentos brutos. Estão disponíveis, ao total, 160 bairros a análise.

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

![image](https://user-images.githubusercontent.com/73614098/121748268-ad0c2b00-cad6-11eb-9cbd-999f164b83c5.png)

Ao colocar os dados médios dos dez principais bairros em faturamento, é possível traçar um perfil do público alvo do comércio:

![image](https://user-images.githubusercontent.com/73614098/121747630-b648c800-cad5-11eb-8923-642460931ab2.png)

Com o mapa de calor do faturamento dos bairros da cidade, é visível o padrão geográfico existente:

![image](https://user-images.githubusercontent.com/73614098/121749035-ff018080-cad7-11eb-95cc-5956c70b9991.png)

Os principais pontos de faturamento se concentram na **Zona Sul** e no **Centro**, além da **Barra da Tijuca**. O comércio na Zona Norte também possui um padrão médio interessante. Já o consumo na zona oeste é bem abaixo das demais localizações.


### IDH x Faturamento

Dentre as variáveis análisadas, uma que demonstrou boa correlação com o faturamento é o IDH do bairro. Os dados de IDH foram coletados através de um algoritmo de Webscraping. Eles foram coletados do site da Wikipedia e agrupados com o Dataset original.

![image](https://user-images.githubusercontent.com/73614098/121753678-e2b61180-cae0-11eb-9bef-ad5769b18b79.png)

As variáveis possuem uma correlação de **0.75**, em uma escala de 0 a 1 das variações positivas. Isso quer dizer que bairros com um alto IDH possuem, no geral, um maior faturamento. Uma análise isolada dessas variáveis não permite determinar um estado de causualidade entre ambas. No entanto, o impacto existente no Indice de Desenvolvimento Humano na receita é alto.

### Renda Média x Faturamento

Outra variável com bom impacto é a Renda Média.




---
## 4.0. Aplicação do Modelo de Machine Learning



---
## 5.0. Performance do Modelo de Machine Learning


---
## 6.0. Resultados



---
## 7.0. Conclusões


--- 
## 8.0. Lições Aprendidas



---
## 9.0. Próximos Passos



---
## 10.0. Bibliografia




<br/><br/>
<br/><br/>
<p align="center">
    <a href="https://www.linkedin.com/in/tadeumadureira/" target="_blank"><img alt="GitHub" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
    <a href="https://github.com/tadeucbm" target="_blank"><img alt="linkedin" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
    <a href="mailto:tadeucastbm@gmail.com?subject=HelloTadeu,%20From%20Github" target="_blank"><img alt="gmail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>


