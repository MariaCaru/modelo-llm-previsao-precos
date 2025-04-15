<h1>Modelo de previsão de preços para aluguéis temporários em Nova York</h1>
<p>

  Este projeto consiste desenvolver um modelo de previsão de preços de aluguéis 
temporários na cidade de Nova York a partir do dataset.
</p>
<hr>

## 📊 Resultados Atuais
- Modelo atual reduz erros em **49%** vs. precificação humana média
- **Próximos passos**: Ver [notebook](#) para detalhes das melhorias planejadas

## 📈 Etapas do Projeto

| **Tarefas** | **Status** |
|-----------------|------------|
| 💾 Coleta e Preparação dos Dados | ✅ |
| 🌐 Análise Exploratória dos Dados | ✅ |
| 🤖 Modelagem e Previsão | ✅ |
| 📄 Interpretação e Conclusões | ✅ |
---

## 💻 Tecnologias Utilizadas
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib e Seaborn](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Scikit-learn (sklearn)](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)

---


## 🤔 Como Utilizar

### Pré-requisitos:
* Python 3.x
* Bibliotecas: pandas, pickle
* Arquivo do modelo: `modelo_preco_imovel.pkl`

### Primeiros passos
1. Baixar o arquivo do modelo (modelo_preco_imovel.pkl)

2. Instalar as bibliotecas necessárias (pandas e pickle)

3.Criar um script Python com o código de carregamento do modelo e previsão, utilizando o arquivo .pkl baixado.

#### Exemplo do script Python (predict.py):
---
```python
import pandas as pd
import pickle

# Carregar o modelo
with open('modelo_preco_imovel.pkl', 'rb') as arquivo:
    modelo = pickle.load(arquivo)

# Criar dados de entrada
novo_imovel = {
    'bairro_group_encoded': 3,  # Manhattan
    'room_type_encoded_dummies': 1,  # Entire home/apt
    'minimo_noites_mediana': 2,
    'numero_de_reviews_mediana': 50,
    'disponibilidade_365': 200,
    'media_preco_tipo_quarto': 200, # Valor da mediana da coluna no dataset
    'media_preco_bairro': 180 # Valor da mediana da coluna no dataset
}
novo_imovel = pd.DataFrame([novo_imovel])

# Fazer a previsão
preco_previsto = modelo.predict(novo_imovel)[0]
print(f'O preço previsto para o imóvel é: {preco_previsto}')
```
---

## 🚧 Dificuldades

| **Áreas**                               | **Descrição** |
|-----------------------------------------|---------------|
| **Limpeza dos dados**                   | Entender quais dados utilizar e quais não seriam necessários. |
| **Transformação dos dados**             | Escolher a melhor forma de transformar os dados para que o modelo performe bem. |
| **Ajuste do modelo ML**                 | Ajustar os parâmetros do modelo para melhorar a precisão foi um desafio. |
---


## 📚 Referências

| Tópicos | Descrição |
|--------|-----------|
|[scikit-learn](https://scikit-learn.org/stable/) | Mensagens de Commit Semântico com Emojis |
|[README](https://blog.rocketseat.com.br/como-fazer-um-bom-readme/) | Como fazer um bom README |
|[NLTK](https://www.nltk.org/_modules/nltk.html) | Documentação do NLTK |
|[hoteis.com](https://www.hoteis.com/go/eua/distritos-nova-york) | Informações sobre os bairros de Nova York |
|[novayorkevoce](https://novayorkevoce.com/blog/distritos-de-nova-york/#:~:text=ingresso%20da%20Broadway!-,Queens,alugu%C3%A9is%20dos%20im%C3%B3veis%20ali%20localizados.&text=%C3%89%20considerada%20uma%20das%20regi%C3%B5es,a%20noite%20de%20Nova%20York.) | Curiosidades sobre os bairros de Nova York |
---

## Autora

<table>
  <tbody>
    <tr>
      <td valign="top" width="14.28%"><a href="https://github.com/MariaCaru"><img src="https://avatars.githubusercontent.com/u/127962556?v=4" width="100px;" alt="Maria Carolina C."/><br /><sub><b>Maria Carolina Cunha</b></sub></a><br />
    </td>
  </tdbody>
</table>