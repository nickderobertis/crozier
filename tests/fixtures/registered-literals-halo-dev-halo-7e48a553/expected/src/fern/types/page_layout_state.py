

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PageLayoutState(enum.StrEnum):
    """
    Compatibility state of the page layout contract.
    """

    SUPPORTED = "SUPPORTED"
    MISSING = "MISSING"
    INVALID = "INVALID"

    def visit(
        self,
        supported: typing.Callable[[], T_Result],
        missing: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PageLayoutState.SUPPORTED:
            return supported()
        if self is PageLayoutState.MISSING:
            return missing()
        if self is PageLayoutState.INVALID:
            return invalid()
