

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CitusSourceMetadataKind(enum.StrEnum):
    CITUS = "citus"

    def visit(self, citus: typing.Callable[[], T_Result]) -> T_Result:
        if self is CitusSourceMetadataKind.CITUS:
            return citus()
