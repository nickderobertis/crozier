

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiModelsTargetProtocol(enum.StrEnum):
    """
    ???
    """

    HTTP10 = "HTTP/1.0"
    HTTP11 = "HTTP/1.1"
    HTTP20 = "HTTP/2.0"
    HTTP30 = "HTTP/3.0"

    def visit(
        self,
        http10: typing.Callable[[], T_Result],
        http11: typing.Callable[[], T_Result],
        http20: typing.Callable[[], T_Result],
        http30: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OtoroshiModelsTargetProtocol.HTTP10:
            return http10()
        if self is OtoroshiModelsTargetProtocol.HTTP11:
            return http11()
        if self is OtoroshiModelsTargetProtocol.HTTP20:
            return http20()
        if self is OtoroshiModelsTargetProtocol.HTTP30:
            return http30()
