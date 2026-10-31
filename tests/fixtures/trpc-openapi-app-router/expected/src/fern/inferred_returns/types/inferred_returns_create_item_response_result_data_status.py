

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class InferredReturnsCreateItemResponseResultDataStatus(enum.StrEnum):
    CREATED = "created"

    def visit(self, created: typing.Callable[[], T_Result]) -> T_Result:
        if self is InferredReturnsCreateItemResponseResultDataStatus.CREATED:
            return created()
