# Use a biblioteca requests para consumir a API pública de clima (por exemplo, OpenWeatherMap) e exibir a temperatura de uma cidade.

import requests
from os import environ
from dotenv import load_dotenv 

load_dotenv()

API_KEY = environ['API_KEY']
cidade = input("Digite o nome da cidade: ").strip()
idioma = 'pt_br'

if API_KEY and cidade:
    try:
        requisicao = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&lang={idioma}&appid={API_KEY}").json()
        temperatura = requisicao['main']['temp'] - 273.15 
        umidade = requisicao['main']['humidity']
        clima = requisicao['weather'][0]['description']
        vento = requisicao['wind']['speed']
        
        print(f"Cidade: {requisicao['name']}")
        print(f"Temperatura: {temperatura:.1f}°C")
        print(f"Clima: {clima}")
        print(f"Umidade: {umidade}%")
        print(f"Vento: {vento:.1f}m/s")
    except requests.RequestException as error:
        print(f"Erro na requisição: {error}")
    except KeyError:
        print(f"Erro: Não foi possível encontrar as informações da cidade. Verifique o nome digitado.")
    except Exception as error:
        print(f"Ocorreu um erro inesperado: {error}")

    


