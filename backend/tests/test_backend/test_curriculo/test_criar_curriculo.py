import pytest
from http import HTTPStatus
from polls.models import Curriculo, Educacao, Competencia
from django.urls import reverse


@pytest.mark.django_db
def test_criar_curriculo_completo(
    api_client_autenticado,
    curriculo_data
):

    url = reverse("criar_curriculo")

    response = api_client_autenticado.post(
        url,
        curriculo_data,
        format="json"
    )

    assert response.status_code == HTTPStatus.CREATED

    curriculo = Curriculo.objects.get(id=response.data["id"])

    assert (
        curriculo.nome_curriculo
        == curriculo_data["nome_curriculo"]
    )

    assert (
        curriculo.area_atuacao
        == curriculo_data["area_atuacao"]
    )

    assert (
        curriculo.resumo_perfil
        == curriculo_data["resumo_perfil"]
    )

    assert Educacao.objects.filter(
        curriculo=curriculo
    ).count() == 1

    assert Competencia.objects.filter(
        curriculo=curriculo
    ).count() == 2


@pytest.mark.django_db
def test_criar_curriculo_com_area_atuacao(
    api_client_autenticado,
    curriculo_data
):

    curriculo_data.pop("area_atuacao")

    url = reverse("criar_curriculo")

    response = api_client_autenticado.post(
        url,
        curriculo_data,
        format="json"
    )

    assert response.status_code == HTTPStatus.CREATED

    curriculo = Curriculo.objects.get(id=response.data["id"])

    assert curriculo.area_atuacao is None

@pytest.mark.django_db
def test_criar_curriculo_sem_area_atuacao(
    api_client_autenticado,
    curriculo_data
):

    curriculo_data.pop("area_atuacao")

    url = reverse("criar_curriculo")

    response = api_client_autenticado.post(
        url,
        curriculo_data,
        format="json"
    )

    assert response.status_code == HTTPStatus.CREATED

    curriculo = Curriculo.objects.get(id=response.data["id"])

    assert curriculo.area_atuacao is None


@pytest.mark.django_db
def test_criar_curriculo_competencia_incompleta(
    api_client_autenticado,
    curriculo_data
):

    curriculo_data["competencias"] = [
        {
            "nome_competencia": "Python"
        }
    ]

    url = reverse("criar_curriculo")

    response = api_client_autenticado.post(
        url,
        curriculo_data,
        format="json"
    )

    assert response.status_code == HTTPStatus.CREATED

    curriculo = Curriculo.objects.get(id=response.data["id"])

    competencia = Competencia.objects.get(
        curriculo=curriculo
    )

    assert competencia.nome_competencia == "Python"
    