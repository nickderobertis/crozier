

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PageStatus(enum.StrEnum):
    """
    Whether this page was parsed successfully (`ok`) or failed (`failed`).
    """

    OK = "ok"
    FAILED = "failed"

    def visit(self, ok: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is PageStatus.OK:
            return ok()
        if self is PageStatus.FAILED:
            return failed()
