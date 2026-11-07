

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurvivalPensionMinimumPremiumPeriodicity(enum.StrEnum):
    DIARIO = "DIARIO"
    SEMANAL = "SEMANAL"
    QUINZENAL = "QUINZENAL"
    MENSAL = "MENSAL"
    BIMESTRAL = "BIMESTRAL"
    TRIMESTRAL = "TRIMESTRAL"
    SEMESTRAL = "SEMESTRAL"
    ANUAL = "ANUAL"
    UNICO = "UNICO"

    def visit(
        self,
        diario: typing.Callable[[], T_Result],
        semanal: typing.Callable[[], T_Result],
        quinzenal: typing.Callable[[], T_Result],
        mensal: typing.Callable[[], T_Result],
        bimestral: typing.Callable[[], T_Result],
        trimestral: typing.Callable[[], T_Result],
        semestral: typing.Callable[[], T_Result],
        anual: typing.Callable[[], T_Result],
        unico: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurvivalPensionMinimumPremiumPeriodicity.DIARIO:
            return diario()
        if self is SurvivalPensionMinimumPremiumPeriodicity.SEMANAL:
            return semanal()
        if self is SurvivalPensionMinimumPremiumPeriodicity.QUINZENAL:
            return quinzenal()
        if self is SurvivalPensionMinimumPremiumPeriodicity.MENSAL:
            return mensal()
        if self is SurvivalPensionMinimumPremiumPeriodicity.BIMESTRAL:
            return bimestral()
        if self is SurvivalPensionMinimumPremiumPeriodicity.TRIMESTRAL:
            return trimestral()
        if self is SurvivalPensionMinimumPremiumPeriodicity.SEMESTRAL:
            return semestral()
        if self is SurvivalPensionMinimumPremiumPeriodicity.ANUAL:
            return anual()
        if self is SurvivalPensionMinimumPremiumPeriodicity.UNICO:
            return unico()
