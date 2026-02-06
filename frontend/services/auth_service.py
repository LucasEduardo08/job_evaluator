import requests
from config import API_URL


def login(username, password):
    try:
        response = requests.post(
            f"{API_URL}/login/",
            json={
                "username": username,
                "password": password
            },
            timeout=10
        )

        if response.status_code == 200:
            return response.json().get("access")
        else:
            return None
    except:
        return None


def criar_conta(username, password, email, nome, telefone, endereco, data_nascimento):
    try:
        response = requests.post(
            f"{API_URL}/criar_usuario/",
            json={
                "username": username,
                "password": password,
                "email": email,
                "nome": nome,
                "telefone": telefone,
                "endereco": endereco,
                "data_nascimento": data_nascimento
            },
            timeout=10
        )

        print("STATUS:", response.status_code)
        print("BODY:", response.text)

        return response.status_code == 201

    except Exception as e:
        print("ERRO NA REQUEST:", e)
        return False
