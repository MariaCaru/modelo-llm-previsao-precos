import joblib
import pandas as pd
from pathlib import Path
from typing import Optional, Dict, Any

class NYCPredictor:
    def __init__(self, model_path: Optional[str] = None):
        self.model_path = Path(model_path) if model_path else Path(__file__).parent.parent / "modelos" / "precificacao_gb_v1.pkl"
        try:
            # Carrega o pacote do modelo
            model_package = joblib.load(self.model_path)
            
            # Extrai componentes
            self.model = model_package['model']
            self.feature_order = model_package['feature_order']
            self.median_values = model_package['median_values']
            self.metadata = model_package['metadata']
            
            # Mapeamentos dinâmicos
            self.bairro_encoding = {
                'Manhattan': 3,
                'Brooklyn': 2,
                'Queens': 4,
                'Bronx': 1,
                'Staten Island': 5
            }
            
            self.room_type_encoding = {
                'Entire home/apt': 1,
                'Private room': 2,
                'Shared room': 3
            }
            
            print("✅ Modelo carregado com sucesso")
            print(f"Features esperadas: {self.feature_order}")
            
        except Exception as e:
            raise RuntimeError(f"Falha ao carregar modelo: {str(e)}")
    
    def get_metadata(self) -> Dict[str, Any]:
        """Retorna os metadados completos do modelo"""
        return self.metadata
    
    def _get_median_value(self, feature: str, encoded_value: int, default: float = 100.0) -> float:
        """Obtém valores medianos de forma segura"""
        try:
            return self.median_values.get(feature, {}).get(encoded_value, default)
        except:
            return default

    def predict(self,
                bairro_group: str,
                room_type: str,
                minimo_noites: int,
                numero_de_reviews: int,
                disponibilidade_365: int) -> float:
        
        try:
            # Validação dos inputs
            if bairro_group not in self.bairro_encoding:
                raise ValueError(f"Bairro inválido. Opções: {list(self.bairro_encoding.keys())}")
            
            if room_type not in self.room_type_encoding:
                raise ValueError(f"Tipo de quarto inválido. Opções: {list(self.room_type_encoding.keys())}")

            # Obtém valores codificados
            bairro_encoded = self.bairro_encoding[bairro_group]
            room_encoded = self.room_type_encoding[room_type]

            # Prepara dados de forma dinâmica
            input_data = {
                'bairro_group_encoded': bairro_encoded,
                'room_type_encoded_dummies': room_encoded,
                'minimo_noites_mediana': minimo_noites,
                'numero_de_reviews_mediana': numero_de_reviews,
                'disponibilidade_365': disponibilidade_365,
                'media_preco_bairro': self._get_median_value('media_preco_bairro', bairro_encoded),
                'media_preco_tipo_quarto': self._get_median_value('media_preco_tipo_quarto', room_encoded)
            }

            # Garante a ordem correta das features
            df = pd.DataFrame([input_data])[self.feature_order]
            preco = float(self.model.predict(df)[0].round(2))
            
            print("\n🔍 Dados enviados para predição:")
            for k, v in input_data.items():
                print(f"{k}: {v}")
                
            return preco
            
        except Exception as e:
            raise RuntimeError(f"Erro na predição: {str(e)}")


if __name__ == "__main__":
    print("\n=== Teste do Predictor ===")
    try:
        predictor = NYCPredictor()
        
        preco = predictor.predict(
            bairro_group="Manhattan",
            room_type="Entire home/apt",
            minimo_noites=1,
            numero_de_reviews=45,
            disponibilidade_365=355,
        )
        print(f"\n💵 Preço previsto: ${preco:.2f}")
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")