import requests
from config import API_URL


def obter_curriculos(token):
    try:
        response = requests.get(
            f"{API_URL}/curriculo/me/",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )

        if response.status_code == 200:
            return response.json()
        else:
            return []
    except:
        return []
    

def obter_curriculo(token, id):
    try:
        response = requests.get(
            f"{API_URL}/curriculo/{id}/",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )

        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None
    

def criar_curriculo(token, dados_curriculo):
    try:
        response = requests.post(
            f"{API_URL}/criar_curriculo/",
            json=dados_curriculo,
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )

        if response.status_code == 201:
            return True
        else:
            return False
    except:
        return False
    

def editar_curriculo(token, id, dados):
    try:
        response = requests.put(
            f"{API_URL}/curriculo/editar/{id}/",
            headers={"Authorization": f"Bearer {token}"},
            json=dados,
            timeout=10
        )

        return response.status_code == 200
    except:
        return False
    
    
def deletar_curriculo(token, id):
    response = requests.delete(
        f"{API_URL}/curriculo/deletar/{id}/",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10
    )

    if response.status_code in (200, 204):
        return True
    else:
        print("Erro:", response.status_code, response.text)
        return False

