

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumInsurancePensionCategory(enum.StrEnum):
    """
    Indicar a categoria do Produto&#58;<br><ol><li>Tradicional</li><li>Microsseguro</li></ol>
    """

    TRADICIONAL = "TRADICIONAL"
    MICROSSEGURO = "MICROSSEGURO"

    def visit(
        self, tradicional: typing.Callable[[], T_Result], microsseguro: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is EnumInsurancePensionCategory.TRADICIONAL:
            return tradicional()
        if self is EnumInsurancePensionCategory.MICROSSEGURO:
            return microsseguro()
