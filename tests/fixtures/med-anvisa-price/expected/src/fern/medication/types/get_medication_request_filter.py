

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetMedicationRequestFilter(enum.StrEnum):
    SUBSTANCIA = "SUBSTÂNCIA"
    CNPJ = "CNPJ"
    LABORATORIO = "LABORATÓRIO"
    CODIGO_GGREM = "CÓDIGO GGREM"
    REGISTRO = "REGISTRO"
    EAN1 = "EAN 1"
    EAN2 = "EAN 2"
    EAN3 = "EAN 3"
    PRODUTO = "PRODUTO"
    APRESENTACAO = "APRESENTAÇÃO"
    CLASSE_TERAPEUTICA = "CLASSE TERAPÊUTICA"
    TIPO_DE_PRODUTO_STATUS_DO_PRODUTO = "TIPO DE PRODUTO (STATUS DO PRODUTO)"
    REGIME_DE_PRECO = "REGIME DE PREÇO"
    PF_SEM_IMPOSTOS = "PF Sem Impostos"
    PF0 = "PF 0%"
    PF12 = "PF 12%"
    PF17 = "PF 17%"
    PF17ALC = "PF 17% ALC"
    PF175 = "PF 17,5%"
    PF175ALC = "PF 17,5% ALC"
    PF18 = "PF 18%"
    PF18ALC = "PF 18% ALC"
    PF20 = "PF 20%"
    PMC0 = "PMC 0%"
    PMC12 = "PMC 12%"
    PMC17 = "PMC 17%"
    PMC17ALC = "PMC 17% ALC"
    PMC175 = "PMC 17,5%"
    PMC175ALC = "PMC 17,5% ALC"
    PMC18 = "PMC 18%"
    PMC18ALC = "PMC 18% ALC"
    PMC20 = "PMC 20%"
    RESTRICAO_HOSPITALAR = "RESTRIÇÃO HOSPITALAR"
    CAP = "CAP"
    CONFAZ87 = "CONFAZ 87"
    ICMS0 = "ICMS 0%"
    ANALISE_RECURSAL = "ANÁLISE RECURSAL"
    LISTA_DE_CONCESSAO_DE_CREDITO_TRIBUTARIO_PIS_COFINS = "LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)"
    COMERCIALIZACAO2019 = "COMERCIALIZAÇÃO 2019"

    def visit(
        self,
        substancia: typing.Callable[[], T_Result],
        cnpj: typing.Callable[[], T_Result],
        laboratorio: typing.Callable[[], T_Result],
        codigo_ggrem: typing.Callable[[], T_Result],
        registro: typing.Callable[[], T_Result],
        ean1: typing.Callable[[], T_Result],
        ean2: typing.Callable[[], T_Result],
        ean3: typing.Callable[[], T_Result],
        produto: typing.Callable[[], T_Result],
        apresentacao: typing.Callable[[], T_Result],
        classe_terapeutica: typing.Callable[[], T_Result],
        tipo_de_produto_status_do_produto: typing.Callable[[], T_Result],
        regime_de_preco: typing.Callable[[], T_Result],
        pf_sem_impostos: typing.Callable[[], T_Result],
        pf0: typing.Callable[[], T_Result],
        pf12: typing.Callable[[], T_Result],
        pf17: typing.Callable[[], T_Result],
        pf17alc: typing.Callable[[], T_Result],
        pf175: typing.Callable[[], T_Result],
        pf175alc: typing.Callable[[], T_Result],
        pf18: typing.Callable[[], T_Result],
        pf18alc: typing.Callable[[], T_Result],
        pf20: typing.Callable[[], T_Result],
        pmc0: typing.Callable[[], T_Result],
        pmc12: typing.Callable[[], T_Result],
        pmc17: typing.Callable[[], T_Result],
        pmc17alc: typing.Callable[[], T_Result],
        pmc175: typing.Callable[[], T_Result],
        pmc175alc: typing.Callable[[], T_Result],
        pmc18: typing.Callable[[], T_Result],
        pmc18alc: typing.Callable[[], T_Result],
        pmc20: typing.Callable[[], T_Result],
        restricao_hospitalar: typing.Callable[[], T_Result],
        cap: typing.Callable[[], T_Result],
        confaz87: typing.Callable[[], T_Result],
        icms0: typing.Callable[[], T_Result],
        analise_recursal: typing.Callable[[], T_Result],
        lista_de_concessao_de_credito_tributario_pis_cofins: typing.Callable[[], T_Result],
        comercializacao2019: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetMedicationRequestFilter.SUBSTANCIA:
            return substancia()
        if self is GetMedicationRequestFilter.CNPJ:
            return cnpj()
        if self is GetMedicationRequestFilter.LABORATORIO:
            return laboratorio()
        if self is GetMedicationRequestFilter.CODIGO_GGREM:
            return codigo_ggrem()
        if self is GetMedicationRequestFilter.REGISTRO:
            return registro()
        if self is GetMedicationRequestFilter.EAN1:
            return ean1()
        if self is GetMedicationRequestFilter.EAN2:
            return ean2()
        if self is GetMedicationRequestFilter.EAN3:
            return ean3()
        if self is GetMedicationRequestFilter.PRODUTO:
            return produto()
        if self is GetMedicationRequestFilter.APRESENTACAO:
            return apresentacao()
        if self is GetMedicationRequestFilter.CLASSE_TERAPEUTICA:
            return classe_terapeutica()
        if self is GetMedicationRequestFilter.TIPO_DE_PRODUTO_STATUS_DO_PRODUTO:
            return tipo_de_produto_status_do_produto()
        if self is GetMedicationRequestFilter.REGIME_DE_PRECO:
            return regime_de_preco()
        if self is GetMedicationRequestFilter.PF_SEM_IMPOSTOS:
            return pf_sem_impostos()
        if self is GetMedicationRequestFilter.PF0:
            return pf0()
        if self is GetMedicationRequestFilter.PF12:
            return pf12()
        if self is GetMedicationRequestFilter.PF17:
            return pf17()
        if self is GetMedicationRequestFilter.PF17ALC:
            return pf17alc()
        if self is GetMedicationRequestFilter.PF175:
            return pf175()
        if self is GetMedicationRequestFilter.PF175ALC:
            return pf175alc()
        if self is GetMedicationRequestFilter.PF18:
            return pf18()
        if self is GetMedicationRequestFilter.PF18ALC:
            return pf18alc()
        if self is GetMedicationRequestFilter.PF20:
            return pf20()
        if self is GetMedicationRequestFilter.PMC0:
            return pmc0()
        if self is GetMedicationRequestFilter.PMC12:
            return pmc12()
        if self is GetMedicationRequestFilter.PMC17:
            return pmc17()
        if self is GetMedicationRequestFilter.PMC17ALC:
            return pmc17alc()
        if self is GetMedicationRequestFilter.PMC175:
            return pmc175()
        if self is GetMedicationRequestFilter.PMC175ALC:
            return pmc175alc()
        if self is GetMedicationRequestFilter.PMC18:
            return pmc18()
        if self is GetMedicationRequestFilter.PMC18ALC:
            return pmc18alc()
        if self is GetMedicationRequestFilter.PMC20:
            return pmc20()
        if self is GetMedicationRequestFilter.RESTRICAO_HOSPITALAR:
            return restricao_hospitalar()
        if self is GetMedicationRequestFilter.CAP:
            return cap()
        if self is GetMedicationRequestFilter.CONFAZ87:
            return confaz87()
        if self is GetMedicationRequestFilter.ICMS0:
            return icms0()
        if self is GetMedicationRequestFilter.ANALISE_RECURSAL:
            return analise_recursal()
        if self is GetMedicationRequestFilter.LISTA_DE_CONCESSAO_DE_CREDITO_TRIBUTARIO_PIS_COFINS:
            return lista_de_concessao_de_credito_tributario_pis_cofins()
        if self is GetMedicationRequestFilter.COMERCIALIZACAO2019:
            return comercializacao2019()
