

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSiblingDiscountsV3RequestActiveSiblingFilter(enum.StrEnum):
    ALL_ACTIVE = "all_active"

    def visit(self, all_active: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetSiblingDiscountsV3RequestActiveSiblingFilter.ALL_ACTIVE:
            return all_active()
