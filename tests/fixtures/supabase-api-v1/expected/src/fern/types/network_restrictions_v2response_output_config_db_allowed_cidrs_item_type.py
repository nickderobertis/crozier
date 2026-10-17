

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NetworkRestrictionsV2ResponseOutputConfigDbAllowedCidrsItemType(enum.StrEnum):
    V4 = "v4"
    V6 = "v6"

    def visit(self, v4: typing.Callable[[], T_Result], v6: typing.Callable[[], T_Result]) -> T_Result:
        if self is NetworkRestrictionsV2ResponseOutputConfigDbAllowedCidrsItemType.V4:
            return v4()
        if self is NetworkRestrictionsV2ResponseOutputConfigDbAllowedCidrsItemType.V6:
            return v6()
