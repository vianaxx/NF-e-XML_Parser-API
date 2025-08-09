import requests

# URL da API pública
api_url = "https://catfact.ninja/fact"

try:
    # Requisição simples sem proxy
    response = requests.get(api_url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        print(f"🐱 Fato aleatório sobre gatos: {data['fact']}")
    else:
        print(f"❌ Erro {response.status_code}:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print("⚠️ Erro na requisição:")
    print(e)
