

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CockroachSourceMetadataKind(enum.StrEnum):
    COCKROACH = "cockroach"

    def visit(self, cockroach: typing.Callable[[], T_Result]) -> T_Result:
        if self is CockroachSourceMetadataKind.COCKROACH:
            return cockroach()
