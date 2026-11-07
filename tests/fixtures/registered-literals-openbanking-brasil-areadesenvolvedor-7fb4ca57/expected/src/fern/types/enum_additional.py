

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumAdditional(enum.StrEnum):
    SORTEIO = "SORTEIO"
    SERVICOS_ASSISTENCIAS_COMPLEMENTARES_PAGO = "SERVICOS_ASSISTENCIAS_COMPLEMENTARES_PAGO"
    SERVICOS_ASSISTENCIA_COMPLEMENTARES_GRATUITO = "SERVICOS_ASSISTENCIA_COMPLEMENTARES_GRATUITO"
    OUTROS = "OUTROS"
    NAO_HA = "NAO_HA"

    def visit(
        self,
        sorteio: typing.Callable[[], T_Result],
        servicos_assistencias_complementares_pago: typing.Callable[[], T_Result],
        servicos_assistencia_complementares_gratuito: typing.Callable[[], T_Result],
        outros: typing.Callable[[], T_Result],
        nao_ha: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumAdditional.SORTEIO:
            return sorteio()
        if self is EnumAdditional.SERVICOS_ASSISTENCIAS_COMPLEMENTARES_PAGO:
            return servicos_assistencias_complementares_pago()
        if self is EnumAdditional.SERVICOS_ASSISTENCIA_COMPLEMENTARES_GRATUITO:
            return servicos_assistencia_complementares_gratuito()
        if self is EnumAdditional.OUTROS:
            return outros()
        if self is EnumAdditional.NAO_HA:
            return nao_ha()
