

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class V1PaymentTaxInclusionType(str, enum.Enum):
    """ """

    ADDITIVE = "ADDITIVE"
    INCLUSIVE = "INCLUSIVE"

    def visit(self, additive: typing.Callable[[], T_Result], inclusive: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1PaymentTaxInclusionType.ADDITIVE:
            return additive()
        if self is V1PaymentTaxInclusionType.INCLUSIVE:
            return inclusive()
