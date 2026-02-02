import requests
from config import API_URL


def obter_usuario(token):
    try:
        response = requests.get(
            f"{API_URL}/usuario/me/",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )

        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None
    
def atualizar_usuario(token, nome, email, telefone, endereco, data_nascimento):
    try:
        if data_nascimento:
            data_nascimento = str(data_nascimento)

        response = requests.put(
            f"{API_URL}/usuario/editar/me/",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "endereco": endereco,
                "data_nascimento": data_nascimento
            },
            timeout=10
        )

        return response.status_code == 200

    except Exception as e:
        print("ERRO NA REQUISIÇÃO:", e)
        return False
