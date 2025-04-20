"""
Exemplo de uso do NYCPredictor
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from nyc_predictor import NYCPredictor

def main():
    print("🛎️  Simulador de Preços - Airbnb NYC")
    
    # Inicializa o predictor
    predictor = NYCPredictor()
    
    inputs = {
        "bairro_group": "Manhattan",  
        "room_type": "Entire home/apt",
        "minimo_noites": 3,
        "numero_de_reviews": 45,
        "disponibilidade_365": 180,
    }
    
    try:
        # Faz a predição
        preco = predictor.predict(
            bairro_group="Manhattan",
            room_type="Entire home/apt",
            minimo_noites=1,
            numero_de_reviews=45,
            disponibilidade_365=355,
        )
        
        # Exibe resultados
        print("\n📊 Resultado da Predição:")
        print(f"• Bairro: {inputs['bairro_group']}")
        print(f"• Tipo de Quarto: {inputs['room_type']}")
        print(f"• Preço Diário Previsto: ${preco:.2f}")
        
        # Mostra métricas do modelo
        metadata = predictor.get_metadata()
        print(f"\nℹ️  Metadados do Modelo:")
        print(f"- Versão: {metadata['version']}")
        print(f"- Último treino: {metadata['last_trained']}")
        print(f"- RMSE: {metadata['performance']['RMSE']}")
        print(f"- R2 Score: {metadata['performance']['R2']}")
        print(f"- Tipo do Modelo: {metadata['model_type']}")
        print(f"- Features: {', '.join(metadata['features'])}")
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")

if __name__ == "__main__":
    main()