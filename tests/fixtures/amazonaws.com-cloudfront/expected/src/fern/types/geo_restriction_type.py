

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GeoRestrictionType(enum.StrEnum):
    BLACKLIST = "blacklist"
    WHITELIST = "whitelist"
    NONE = "none"

    def visit(
        self,
        blacklist: typing.Callable[[], T_Result],
        whitelist: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GeoRestrictionType.BLACKLIST:
            return blacklist()
        if self is GeoRestrictionType.WHITELIST:
            return whitelist()
        if self is GeoRestrictionType.NONE:
            return none()
