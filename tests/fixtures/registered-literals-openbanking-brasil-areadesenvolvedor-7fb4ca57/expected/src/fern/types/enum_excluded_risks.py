

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumExcludedRisks(enum.StrEnum):
    """
    Listagem para indicar quais serão o(s) risco(s) excluído(s) aplicável(is) à(s) cobertura(s).
    """

    ATO_RECONHECIMENTO_PERIGOSO = "ATO_RECONHECIMENTO_PERIGOSO"
    ATO_ILICITO_DOLOSO_PRATICADO_SEGURADO = "ATO_ILICITO_DOLOSO_PRATICADO_SEGURADO"
    OPERACOES_GUERRA = "OPERACOES_GUERRA"
    FURACOES_CICLONES_TERREMOTOS = "FURACOES_CICLONES_TERREMOTOS"
    MATERIAL_NUCLEAR = "MATERIAL_NUCLEAR"
    DOENCAS_LESOES_PREEXISTENTES = "DOENCAS_LESOES_PREEXISTENTES"
    EPIDEMIAS_PANDEMIAS = "EPIDEMIAS_PANDEMIAS"
    SUICIDIO = "SUICIDIO"
    ATO_ILICITO_DOLOSO_PRATICADO_CONTROLADOR = "ATO_ILICITO_DOLOSO_PRATICADO_CONTROLADOR"
    OUTROS = "OUTROS"

    def visit(
        self,
        ato_reconhecimento_perigoso: typing.Callable[[], T_Result],
        ato_ilicito_doloso_praticado_segurado: typing.Callable[[], T_Result],
        operacoes_guerra: typing.Callable[[], T_Result],
        furacoes_ciclones_terremotos: typing.Callable[[], T_Result],
        material_nuclear: typing.Callable[[], T_Result],
        doencas_lesoes_preexistentes: typing.Callable[[], T_Result],
        epidemias_pandemias: typing.Callable[[], T_Result],
        suicidio: typing.Callable[[], T_Result],
        ato_ilicito_doloso_praticado_controlador: typing.Callable[[], T_Result],
        outros: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumExcludedRisks.ATO_RECONHECIMENTO_PERIGOSO:
            return ato_reconhecimento_perigoso()
        if self is EnumExcludedRisks.ATO_ILICITO_DOLOSO_PRATICADO_SEGURADO:
            return ato_ilicito_doloso_praticado_segurado()
        if self is EnumExcludedRisks.OPERACOES_GUERRA:
            return operacoes_guerra()
        if self is EnumExcludedRisks.FURACOES_CICLONES_TERREMOTOS:
            return furacoes_ciclones_terremotos()
        if self is EnumExcludedRisks.MATERIAL_NUCLEAR:
            return material_nuclear()
        if self is EnumExcludedRisks.DOENCAS_LESOES_PREEXISTENTES:
            return doencas_lesoes_preexistentes()
        if self is EnumExcludedRisks.EPIDEMIAS_PANDEMIAS:
            return epidemias_pandemias()
        if self is EnumExcludedRisks.SUICIDIO:
            return suicidio()
        if self is EnumExcludedRisks.ATO_ILICITO_DOLOSO_PRATICADO_CONTROLADOR:
            return ato_ilicito_doloso_praticado_controlador()
        if self is EnumExcludedRisks.OUTROS:
            return outros()
