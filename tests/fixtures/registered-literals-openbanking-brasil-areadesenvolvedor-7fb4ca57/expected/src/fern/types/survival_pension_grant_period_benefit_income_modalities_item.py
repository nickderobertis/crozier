

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem(enum.StrEnum):
    """
    Modalidades de renda disponíveis para contratação.
      A considerar os seguintes domínios:
      1. Pagamento Único
      2. Renda por Prazo Certo;
      3. Renda Temporária;
      4. Renda Temporária Reversível;
      5. Renda Temporária com mínimo garantido;
      6. Renda Temporária Reversível com Mínimo Garantido;
      7. Renda Vitalícia;
      8. Renda Vitalícia Reversível ao Beneficiário Indicado
      9. Renda Vitalícia Reversível ao Cônjuge com Continuidade de Menores
      10. Renda Vitalícia com o Mínimo Garantido;
      11. Renda Vitalícia com Prazo mínimo garantido.
    """

    PAGAMENTO_UNICO = "PAGAMENTO_UNICO"
    RENDA_PRAZO_CERTO = "RENDA_PRAZO_CERTO"
    RENDA_TEMPORARIA = "RENDA_TEMPORARIA"
    RENDA_TEMPORARIA_REVERSIVEL = "RENDA_TEMPORARIA_REVERSIVEL"
    RENDA_TEMPORARIA_MINMO_GARANTIDO = "RENDA_TEMPORARIA_MINMO_GARANTIDO"
    RENDA_TEMPORARIA_REVERSIVEL_MININO_GARANTIDO = "RENDA_TEMPORARIA_REVERSIVEL_MININO_GARANTIDO"
    RENDA_VITALICIA = "RENDA_VITALICIA"
    RENDA_VITALICIA_REVERSIVEL_BENEFICIARIO_INDICADO = "RENDA_VITALICIA_REVERSIVEL_BENEFICIARIO_INDICADO"
    RENDA_VITALICIA_CONJUGE_CONTINUIDADE_MENORES = "RENDA_VITALICIA_CONJUGE_CONTINUIDADE_MENORES"
    RENDA_VITALICIA_MINIMO_GARANTIDO = "RENDA_VITALICIA_MINIMO_GARANTIDO"
    RENDA_VITALICIA_PRAZO_MINIMO_GRANTIDO = "RENDA_VITALICIA_PRAZO_MINIMO_GRANTIDO"

    def visit(
        self,
        pagamento_unico: typing.Callable[[], T_Result],
        renda_prazo_certo: typing.Callable[[], T_Result],
        renda_temporaria: typing.Callable[[], T_Result],
        renda_temporaria_reversivel: typing.Callable[[], T_Result],
        renda_temporaria_minmo_garantido: typing.Callable[[], T_Result],
        renda_temporaria_reversivel_minino_garantido: typing.Callable[[], T_Result],
        renda_vitalicia: typing.Callable[[], T_Result],
        renda_vitalicia_reversivel_beneficiario_indicado: typing.Callable[[], T_Result],
        renda_vitalicia_conjuge_continuidade_menores: typing.Callable[[], T_Result],
        renda_vitalicia_minimo_garantido: typing.Callable[[], T_Result],
        renda_vitalicia_prazo_minimo_grantido: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.PAGAMENTO_UNICO:
            return pagamento_unico()
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_PRAZO_CERTO:
            return renda_prazo_certo()
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_TEMPORARIA:
            return renda_temporaria()
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_TEMPORARIA_REVERSIVEL:
            return renda_temporaria_reversivel()
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_TEMPORARIA_MINMO_GARANTIDO:
            return renda_temporaria_minmo_garantido()
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_TEMPORARIA_REVERSIVEL_MININO_GARANTIDO:
            return renda_temporaria_reversivel_minino_garantido()
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_VITALICIA:
            return renda_vitalicia()
        if (
            self
            is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_VITALICIA_REVERSIVEL_BENEFICIARIO_INDICADO
        ):
            return renda_vitalicia_reversivel_beneficiario_indicado()
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_VITALICIA_CONJUGE_CONTINUIDADE_MENORES:
            return renda_vitalicia_conjuge_continuidade_menores()
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_VITALICIA_MINIMO_GARANTIDO:
            return renda_vitalicia_minimo_garantido()
        if self is SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem.RENDA_VITALICIA_PRAZO_MINIMO_GRANTIDO:
            return renda_vitalicia_prazo_minimo_grantido()
