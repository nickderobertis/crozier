

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceTypeType(enum.StrEnum):
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"
    UNKNOWN = "Unknown"

    def visit(
        self,
        electric: typing.Callable[[], T_Result],
        hybrid: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceTypeType.ELECTRIC:
            return electric()
        if self is ServiceTypeType.HYBRID:
            return hybrid()
        if self is ServiceTypeType.UNKNOWN:
            return unknown()
