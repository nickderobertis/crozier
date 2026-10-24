

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdsAdapterStatusStatus(enum.StrEnum):
    BLOCKED = "blocked"
    ELIGIBLE_NOT_INSTALLED = "eligible_not_installed"

    def visit(
        self, blocked: typing.Callable[[], T_Result], eligible_not_installed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AdsAdapterStatusStatus.BLOCKED:
            return blocked()
        if self is AdsAdapterStatusStatus.ELIGIBLE_NOT_INSTALLED:
            return eligible_not_installed()
