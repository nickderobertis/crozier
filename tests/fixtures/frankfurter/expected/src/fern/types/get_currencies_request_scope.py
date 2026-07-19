

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetCurrenciesRequestScope(enum.StrEnum):
    ALL = "all"

    def visit(self, all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCurrenciesRequestScope.ALL:
            return all_()
