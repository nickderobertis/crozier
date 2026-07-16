

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObExternalAccountType1Code(str, enum.Enum):
    """
    Specifies the type of account (personal or business).
    """

    BUSINESS = "Business"
    PERSONAL = "Personal"

    def visit(self, business: typing.Callable[[], T_Result], personal: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObExternalAccountType1Code.BUSINESS:
            return business()
        if self is ObExternalAccountType1Code.PERSONAL:
            return personal()
