

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumTargetAudience(enum.StrEnum):
    """
    A considerar os domínios abaixo:

      1. Pessoa Natural
      2. Pessoa Jurídica
      3. Ambas (Pessoa Natural e Jurídica)
    """

    PESSOA_NATURAL = "PESSOA_NATURAL"
    PESSOA_JURIDICA = "PESSOA_JURIDICA"
    PESSOA_NATURAL_JURIDICA = "PESSOA_NATURAL_JURIDICA"

    def visit(
        self,
        pessoa_natural: typing.Callable[[], T_Result],
        pessoa_juridica: typing.Callable[[], T_Result],
        pessoa_natural_juridica: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumTargetAudience.PESSOA_NATURAL:
            return pessoa_natural()
        if self is EnumTargetAudience.PESSOA_JURIDICA:
            return pessoa_juridica()
        if self is EnumTargetAudience.PESSOA_NATURAL_JURIDICA:
            return pessoa_natural_juridica()
