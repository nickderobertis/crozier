

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumProductModality(enum.StrEnum):
    """
    <ol><li>Funeral</li><li>Prestamista (exceto Habitacional e Rural)</li><li>Viagem</li><li>Educacional</li><li>Dotal (Misto e Puro)</li><li>Acidentes Pessoais</li><li>Vida</li><li>Perda do Certificado de Habilitação de Voo – PCHV</li><li>Doenças Graves ou Doença Terminal</li><li>Desemprego/ Perda de Renda</li><li>Eventos Aleatórios</li><li>Pecúlio</li><li>Pensão prazo certo</li><li>Pensão menores 21 anos</li><li>Pensão menores 24 anos</li><li>Pensão cônjuge vitalícia</li><li>Pensão cônjuge temporária</li></ol>
    """

    FUNERAL = "FUNERAL"
    PRESTAMISTA = "PRESTAMISTA"
    VIAGEM = "VIAGEM"
    EDUCACIONAL = "EDUCACIONAL"
    DOTAL = "DOTAL"
    ACIDENTES_PESSOAIS = "ACIDENTES_PESSOAIS"
    VIDA = "VIDA"
    PERDA_CERTIFICADO_HABILITACAO_VOO = "PERDA_CERTIFICADO_HABILITACAO_VOO"
    DOENCAS_GRAVES_DOENCA_TERMINAL = "DOENCAS_GRAVES_DOENCA_TERMINAL"
    DESEMPREGO_PERDA_RENDA = "DESEMPREGO_PERDA_RENDA"
    EVENTOS_ALEATORIOS = "EVENTOS_ALEATORIOS"
    PECULIO = "PECULIO"
    PENSAO_PRAZO_CERTO = "PENSAO_PRAZO_CERTO"
    PENSAO_MENORES21 = "PENSAO_MENORES_21"
    PENSAO_MENORES24 = "PENSAO_MENORES_24"
    PENSAO_CONJUGE_VITALICIA = "PENSAO_CONJUGE_VITALICIA"
    PENSAO_CONJUGE_TEMPORARIA = "PENSAO_CONJUGE_TEMPORARIA"

    def visit(
        self,
        funeral: typing.Callable[[], T_Result],
        prestamista: typing.Callable[[], T_Result],
        viagem: typing.Callable[[], T_Result],
        educacional: typing.Callable[[], T_Result],
        dotal: typing.Callable[[], T_Result],
        acidentes_pessoais: typing.Callable[[], T_Result],
        vida: typing.Callable[[], T_Result],
        perda_certificado_habilitacao_voo: typing.Callable[[], T_Result],
        doencas_graves_doenca_terminal: typing.Callable[[], T_Result],
        desemprego_perda_renda: typing.Callable[[], T_Result],
        eventos_aleatorios: typing.Callable[[], T_Result],
        peculio: typing.Callable[[], T_Result],
        pensao_prazo_certo: typing.Callable[[], T_Result],
        pensao_menores21: typing.Callable[[], T_Result],
        pensao_menores24: typing.Callable[[], T_Result],
        pensao_conjuge_vitalicia: typing.Callable[[], T_Result],
        pensao_conjuge_temporaria: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumProductModality.FUNERAL:
            return funeral()
        if self is EnumProductModality.PRESTAMISTA:
            return prestamista()
        if self is EnumProductModality.VIAGEM:
            return viagem()
        if self is EnumProductModality.EDUCACIONAL:
            return educacional()
        if self is EnumProductModality.DOTAL:
            return dotal()
        if self is EnumProductModality.ACIDENTES_PESSOAIS:
            return acidentes_pessoais()
        if self is EnumProductModality.VIDA:
            return vida()
        if self is EnumProductModality.PERDA_CERTIFICADO_HABILITACAO_VOO:
            return perda_certificado_habilitacao_voo()
        if self is EnumProductModality.DOENCAS_GRAVES_DOENCA_TERMINAL:
            return doencas_graves_doenca_terminal()
        if self is EnumProductModality.DESEMPREGO_PERDA_RENDA:
            return desemprego_perda_renda()
        if self is EnumProductModality.EVENTOS_ALEATORIOS:
            return eventos_aleatorios()
        if self is EnumProductModality.PECULIO:
            return peculio()
        if self is EnumProductModality.PENSAO_PRAZO_CERTO:
            return pensao_prazo_certo()
        if self is EnumProductModality.PENSAO_MENORES21:
            return pensao_menores21()
        if self is EnumProductModality.PENSAO_MENORES24:
            return pensao_menores24()
        if self is EnumProductModality.PENSAO_CONJUGE_VITALICIA:
            return pensao_conjuge_vitalicia()
        if self is EnumProductModality.PENSAO_CONJUGE_TEMPORARIA:
            return pensao_conjuge_temporaria()
