

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDomainsDomainIdResponseUserPlan(enum.StrEnum):
    TINY = "tiny"
    HOBBY = "hobby"
    SMALL = "small"
    STANDARD = "standard"
    LARGE = "large"

    def visit(
        self,
        tiny: typing.Callable[[], T_Result],
        hobby: typing.Callable[[], T_Result],
        small: typing.Callable[[], T_Result],
        standard: typing.Callable[[], T_Result],
        large: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDomainsDomainIdResponseUserPlan.TINY:
            return tiny()
        if self is GetDomainsDomainIdResponseUserPlan.HOBBY:
            return hobby()
        if self is GetDomainsDomainIdResponseUserPlan.SMALL:
            return small()
        if self is GetDomainsDomainIdResponseUserPlan.STANDARD:
            return standard()
        if self is GetDomainsDomainIdResponseUserPlan.LARGE:
            return large()
