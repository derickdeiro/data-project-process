from time import sleep
import requests
from bs4 import BeautifulSoup
import pytest
import subprocess

@pytest.fixture()
def run_streamlit_process():
    process = subprocess.Popen(['streamlit', 'run', 'src/app.py'])
    sleep(10)
    yield process
    process.kill()
    
    
def test_app_opens(run_streamlit_process):
    # Verificar se a página abre
    response = requests.get('http://localhost:8501')
    status_code = response.status_code
    
    assert status_code == 200
    
    
# def test_check_title_is(run_streamlit_process):
#     sleep(10)
#     response = requests.get('http://localhost:8501')
    
#     if response.status_code == 200:
#         sleep(15)
        
#     content = response.content
#     soup = BeautifulSoup(content, 'html.parser')
    
#     print(soup.prettify())
#     page_title = soup.find('title').text
    
#     expected_title = 'Validador de Schema Excel'
#     assert page_title == expected_title
    
    
# def test_check_streamlit_h1(run_streamlit_process):
#     response = requests.get('http://localhost:8501')
    
#     content = response.content
    
#     soup = BeautifulSoup(content, 'html.parser')
    
#     h1_element = soup.find('h1').text
#     expected_h1 = 'Carregue seu arquivo Excel aqui:'
    
#     assert h1_element == expected_h1
    
    