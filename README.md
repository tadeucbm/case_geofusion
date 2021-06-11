# Case Técnico Geofusion - Previsão de Faturamento

![image](https://user-images.githubusercontent.com/73614098/121671593-bd8fb780-ca7c-11eb-88b9-306fe30765d8.png)

---
## Introdução
Este projeto foi desenvolvido como resolução do Case Técnico para a vaga de Estagiário de Machine Learning pela Geofusion. Foi solicitada uma análise exploratória e o desenvolvimento de um modelo de Regressão. O conjunto de dados carrega uma série de informações sociodemográficas, e o faturamento da empresa, em cada bairro.

Devido a pequena quantidade de dados, fiz a coleta de algumas informações adicionais na web. Do site da Wikipédia, coletei os seguintes dados por bairro: IDH, Subprefeitura, Região Administrativa e Área. Com isso, foi possível realizar algumas análises de público alvo mais acuradas, além de melhorar o desempenho do modelo.

A entrega desse projeto está sendo feita de algumas maneiras. Este documento contém os principais insights do projeto, além da análise dos resultados do modelo de Machine Learning. Os notebooks - Webscraping, Projeto e Análise - estão todos na pasta 'notebooks'. O modelo final foi entregue em produção pelo Heroku e **possivelmente um bot no telegram**.

Esse documento serve como um guia do projeto. A descrição das etapas estão inclusas nas próximas sessões.

---
## 1.0. O Problema
Um cliente do ramo alimentício no Rio de Janeiro solicitou uma análise para poder entender melhor o seu público alvo. Do conjunto de dados, estão disponíveis algumas métricas sociogeograficas de cara bairro - Renda média, idade, população e domicilios. Além disso, estão disponíveis os seus resepctivos faturamentos brutos. Estão disponíveis, ao total, 160 bairros a análise.

Análise do Problema:
- **Granularidade**: Por bairro;
- **Tipo de Modelo**: Regressão.

---
## 2.0. A Solução
A solução do problema está entregue em dois formatos:
- **Análise Exploratória dos Dados** -> Fornecimento de Insights sobre as principais variáveis que impactam o faturamento do cliente. 
- **Bot no Telegram** -> Modelo de Regressão em produção no Heroku. Os resultados estão disponíveis através de um Bot no aplicativo **Telegram**.

---
## 3.0. Insights
![''](https://raw.githubusercontent.com/tadeucbm/case_geofusion/main/img/MinMap_faturamento.png?token=ARRUGERTMM2D3L25HV5A26DAYOL3Y)

### Os Maiores Faturamentos
![''](https://raw.githubusercontent.com/tadeucbm/case_geofusion/main/img/top_10_bairros_faturamento.png?token=ARRUGEXIXC7POAMNFVIUZCLAYOL2O)



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


