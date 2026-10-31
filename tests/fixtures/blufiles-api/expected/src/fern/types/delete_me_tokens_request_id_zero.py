

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteMeTokensRequestIdZero(enum.StrEnum):
    ALL = "all"
    EXCEPT = "except"

    def visit(self, all_: typing.Callable[[], T_Result], except_: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteMeTokensRequestIdZero.ALL:
            return all_()
        if self is DeleteMeTokensRequestIdZero.EXCEPT:
            return except_()
