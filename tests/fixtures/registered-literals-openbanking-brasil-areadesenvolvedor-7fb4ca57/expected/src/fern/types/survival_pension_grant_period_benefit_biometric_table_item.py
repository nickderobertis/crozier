

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurvivalPensionGrantPeriodBenefitBiometricTableItem(enum.StrEnum):
    """
    Tábua biométrica utilizada como parâmetro para conversão em renda atuarial que deve observar a relação discriminada de coberturas, conforme Tabela II.2 do Anexo II.
    Deverá ser informada a tábua biométrica aplicável à modalidade de renda padrão do plano.
    """

    AT2000MALE = "AT_2000_MALE"
    AT2000FEMALE = "AT_2000_FEMALE"
    AT2000MALE_FEMALE = "AT_2000_MALE_FEMALE"
    AT2000MALE_SUAVIZADA10 = "AT_2000_MALE_SUAVIZADA_10"
    AT2000FEMALE_SUAVIZADA10 = "AT_2000_FEMALE_SUAVIZADA_10"
    AT2000MALE_FEMALE_SUAVIZADA10 = "AT_2000_MALE_FEMALE_SUAVIZADA_10"
    AT2000MALE_SUAVIZADA15 = "AT_2000_MALE_SUAVIZADA_15"
    AT2000FEMALE_SUAVIZADA15 = "AT_2000_FEMALE_SUAVIZADA_15"
    AT2000MALE_FEMALE_SUAVIZADA15 = "AT_2000_MALE_FEMALE_SUAVIZADA_15"
    AT83MALE = "AT_83_MALE"
    AT83FEMALE = "AT_83_FEMALE"
    AT83MALE_FEMALE = "AT_83_MALE_FEMALE"
    BR_EMSSB_MALE = "BR_EMSSB_MALE"
    BR_EMSSB_FEMALE = "BR_EMSSB_FEMALE"
    BR_EMSSB_MALE_FEMALE = "BR_EMSSB_MALE_FEMALE"

    def visit(
        self,
        at2000male: typing.Callable[[], T_Result],
        at2000female: typing.Callable[[], T_Result],
        at2000male_female: typing.Callable[[], T_Result],
        at2000male_suavizada10: typing.Callable[[], T_Result],
        at2000female_suavizada10: typing.Callable[[], T_Result],
        at2000male_female_suavizada10: typing.Callable[[], T_Result],
        at2000male_suavizada15: typing.Callable[[], T_Result],
        at2000female_suavizada15: typing.Callable[[], T_Result],
        at2000male_female_suavizada15: typing.Callable[[], T_Result],
        at83male: typing.Callable[[], T_Result],
        at83female: typing.Callable[[], T_Result],
        at83male_female: typing.Callable[[], T_Result],
        br_emssb_male: typing.Callable[[], T_Result],
        br_emssb_female: typing.Callable[[], T_Result],
        br_emssb_male_female: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT2000MALE:
            return at2000male()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT2000FEMALE:
            return at2000female()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT2000MALE_FEMALE:
            return at2000male_female()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT2000MALE_SUAVIZADA10:
            return at2000male_suavizada10()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT2000FEMALE_SUAVIZADA10:
            return at2000female_suavizada10()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT2000MALE_FEMALE_SUAVIZADA10:
            return at2000male_female_suavizada10()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT2000MALE_SUAVIZADA15:
            return at2000male_suavizada15()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT2000FEMALE_SUAVIZADA15:
            return at2000female_suavizada15()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT2000MALE_FEMALE_SUAVIZADA15:
            return at2000male_female_suavizada15()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT83MALE:
            return at83male()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT83FEMALE:
            return at83female()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.AT83MALE_FEMALE:
            return at83male_female()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.BR_EMSSB_MALE:
            return br_emssb_male()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.BR_EMSSB_FEMALE:
            return br_emssb_female()
        if self is SurvivalPensionGrantPeriodBenefitBiometricTableItem.BR_EMSSB_MALE_FEMALE:
            return br_emssb_male_female()
