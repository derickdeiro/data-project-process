import pandas as pd
from contrato import Vendas
from dotenv import load_dotenv

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        errors = []
        
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return False, f'Colunas extrans detectadas no Excel: {", ".join(extra_cols)}'
        
        for index, row in df.iterrows():
            try: 
                _ = Vendas(**row.to_dict())
            except Exception as e:
                errors.append(f'Erro na linha {index + 2}: {e}')
                
        return True, errors
    
    except Exception as e:
        return pd.DataFrame(), f'Erro inesperado: {str(e)}'