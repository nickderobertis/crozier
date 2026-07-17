

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1PaymentSurchargeType(enum.StrEnum):
    """ """

    UNKNOWN = "UNKNOWN"
    AUTO_GRATUITY = "AUTO_GRATUITY"
    CUSTOM = "CUSTOM"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        auto_gratuity: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1PaymentSurchargeType.UNKNOWN:
            return unknown()
        if self is V1PaymentSurchargeType.AUTO_GRATUITY:
            return auto_gratuity()
        if self is V1PaymentSurchargeType.CUSTOM:
            return custom()
