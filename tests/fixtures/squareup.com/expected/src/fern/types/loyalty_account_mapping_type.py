

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LoyaltyAccountMappingType(str, enum.Enum):
    """
    The type of mapping.
    """

    PHONE = "PHONE"

    def visit(self, phone: typing.Callable[[], T_Result]) -> T_Result:
        if self is LoyaltyAccountMappingType.PHONE:
            return phone()
