import streamlit as st



class ExcelValidatorUI:
    def __init__(self) -> None:
        self.set_page_config()
        
    def set_page_config(self):
        st.set_page_config(
            page_title='Validador de Schema Excel',
            layout='wide'
        )
        
    def display_header(self):
        st.title('Validador de Schema Excel')
        
    def upload_file(self):
        return st.file_uploader('Carregue seu arquivo Excel aqui:', type=['xlsx'])
    
    def display_results(self, result, errors):
        if errors:
            for error in errors:
                st.error(f'Erro na validação: {error}')
            else:
                st.success('O Schema do arquivo Excel está correto!')