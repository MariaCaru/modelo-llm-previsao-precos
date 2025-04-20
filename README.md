# 🏙️ NYC Rental Price Predictor

**Precificação inteligente para aluguéis temporários em Nova York**

[![GitHub stars](https://img.shields.io/github/stars/MariaCaru/modelo-llm-previsao-precos?style=social)](https://github.com/MariaCaru/modelo-llm-previsao-precos)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MariaCaru/modelo-llm-previsao-precos/blob/main/notebooks/nyc_rental_price_analysis.ipynb)

## 🌟 Visão Geral

### 📌 Sobre o Projeto
Modelo de machine learning que combina:
- **Técnicas de NLP** para análise de descrições textuais
- **Algoritmos de regressão** para dados estruturados
- **Geolocalização implícita** através de padrões de bairros

**Objetivo principal:**  
Prever preços diários de aluguéis no Airbnb NYC com precisão 50% maior que métodos tradicionais.

### 🎯 Aplicações Práticas
| Público-Alvo | Benefício |
|--------------|----------|
| 🏠 Anfitriões | Precificação competitiva automática |
| 🧳 Hóspedes | Identificação de ofertas justas |
| 📊 Analistas | Insights sobre fatores de precificação |

## 🔍 Detalhes do Modelo

### 🧠 Arquitetura Técnica
**Algoritmo Principal:**  
`Gradient Boosting Regressor` (scikit-learn).

## 📈 Etapas do Projeto

| **Tarefas** | **Status** |
|-----------------|------------|
| 💾 Coleta e Preparação dos Dados | ✅ |
| 🌐 Análise Exploratória dos Dados | ✅ |
| 🤖 Modelagem e Previsão | ✅ |
| 📄 Interpretação e Conclusões | ✅ |


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


## 🛠️ Estrutura do Código
```
modelo-llm-previsao-precos/
├── dataset/                                # Pasta de dados
│   ├── nyc_airbnb_listings.csv             # Dados brutos(CSV)
│ 
│── modelos/                                # Modelos treinados
│   └── precificacao_gb_v1.pkl 
│
├── notebooks/                              # Jupyter notebooks
│   └── analise_precos.ipynb                # Análise de Dados 
│                
├── predictors/                             # Pasta exemplos de uso - modelos treinados
│   └── nyc_predictor.py                    # Script python com modelo de previsão
│   └── examples/                           # Pasta de exemplo de uso
│   └──example_usage.py                     # Script de exemplo de uso
│
├── requirements.txt                        # Dependências
└── README.md                               # Documentação

```

## 🤔 Como Utilizar

### 1. Instalação:
```python
# Clone o repositório
git clone https://github.com/MariaCaru/
cd modelo-llm-previsao-precos.git

# Instale as dependências
pip install -r requirements.txt 
```

### 2. Previsão com o NYCPredictor(example_usage.py):
```python
from predictors.nyc_predictor import NYCPredictor

# Inicializa o predictor
predictor = NYCPredictor()

# Faz a previsão
preco = predictor.predict(
    bairro_group="Brooklyn",    # Escolha o bairro
    room_type="Private room",   # Tipo de acomodação
    minimo_noites=2,            # Mínimo de noites
    numero_de_reviews=30,       # Número de reviews
    disponibilidade_365=200     # Dias disponíveis/ano
)

print(f"Preço diário previsto: ${preco:.2f}")
```
#### Menu de Opções Válidas:
```
🗺️ Para bairro_group:
  1. Bronx       🏟️
  2. Brooklyn    🎨
  3. Manhattan   🏙️  
  4. Queens      ✈️  
  5. Staten Island 🌉

🛌 Para room_type:
  1. "Entire home/apt"  🏠 (Casa/Apartamento inteiro)
  2. "Private room"     🛏️  (Quarto privativo)
  3. "Shared room"      🧑🤝🧑 (Quarto compartilhado)
```

### 3. Executando o Exemplo Completo (terminal)
```
python predictors/examples/example_usage.py
```

#### Exemplo de Saída Esperada:
```
🛎️  Simulador de Preços - Airbnb NYC

📊 Resultado da Predição:
• Bairro: Manhattan
• Tipo de Quarto: Entire home/apt
• Preço Diário Previsto: $245.50

ℹ️  Metadados do Modelo:
- Versão: v1.2
- Último treino: 2023-11-15
- RMSE: 48.20
- R2 Score: 0.78
- Tipo do Modelo: GradientBoostingRegressor
- Features: bairro_group, room_type, minimo_noites, numero_de_reviews, disponibilidade_365
```
## 🚧 Dificuldades

| **Áreas**                               | **Descrição** |
|-----------------------------------------|---------------|
| **Limpeza dos dados**                   | Entender quais dados utilizar e quais não seriam necessários. |
| **Transformação dos dados**             | Escolher a melhor forma de transformar os dados para que o modelo performe bem. |
| **Ajuste do modelo ML**                 | Ajustar os parâmetros do modelo para melhorar a precisão. |

## 📈 Próximas Melhorias
- [ ] Testar XGBoost (`pip install xgboost` quando necessário)
- [ ] Feature Engineering: criar `distancia_pontos_turisticos`
- [ ] Gráfico SHAP para explicar previsões

## 📚 Referências

| Tópicos | Descrição |
|--------|-----------|
|[scikit-learn](https://scikit-learn.org/stable/) | Machine Learning in Python |
|[Rocketseat](https://blog.rocketseat.com.br/como-fazer-um-bom-readme/) | Como fazer um bom README |
|[NLTK](https://www.nltk.org/_modules/nltk.html) | Documentação do NLTK |
|[hoteis.com](https://www.hoteis.com/go/eua/distritos-nova-york) | Informações sobre os bairros de Nova York |
|[novayorkevoce](https://novayorkevoce.com/blog/distritos-de-nova-york/#:~:text=ingresso%20da%20Broadway!-,Queens,alugu%C3%A9is%20dos%20im%C3%B3veis%20ali%20localizados.&text=%C3%89%20considerada%20uma%20das%20regi%C3%B5es,a%20noite%20de%20Nova%20York.) | Curiosidades sobre os bairros de Nova York |


## Autora

<table>
  <tbody>
    <tr>
      <td valign="top" width="14.28%"><a href="https://github.com/MariaCaru"><img src="https://avatars.githubusercontent.com/u/127962556?v=4" width="100px;" alt="Maria Carolina C."/><br /><sub><b>Maria Carolina Cunha</b></sub></a><br />
    </td>
  </tdbody>
</table>