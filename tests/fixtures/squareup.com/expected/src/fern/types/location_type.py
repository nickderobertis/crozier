

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LocationType(str, enum.Enum):
    """
    A location's physical or mobile type.
    """

    PHYSICAL = "PHYSICAL"
    MOBILE = "MOBILE"

    def visit(self, physical: typing.Callable[[], T_Result], mobile: typing.Callable[[], T_Result]) -> T_Result:
        if self is LocationType.PHYSICAL:
            return physical()
        if self is LocationType.MOBILE:
            return mobile()
