

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SharedLinkScope(enum.StrEnum):
    """
    The scope of the shared link.
    """

    PUBLIC = "public"
    COMPANY = "company"

    def visit(self, public: typing.Callable[[], T_Result], company: typing.Callable[[], T_Result]) -> T_Result:
        if self is SharedLinkScope.PUBLIC:
            return public()
        if self is SharedLinkScope.COMPANY:
            return company()
