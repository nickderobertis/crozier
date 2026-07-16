

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderServiceChargeType(str, enum.Enum):
    """ """

    AUTO_GRATUITY = "AUTO_GRATUITY"
    CUSTOM = "CUSTOM"

    def visit(self, auto_gratuity: typing.Callable[[], T_Result], custom: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrderServiceChargeType.AUTO_GRATUITY:
            return auto_gratuity()
        if self is OrderServiceChargeType.CUSTOM:
            return custom()
