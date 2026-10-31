

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class InferredReturnsEnumLikeResponseResultDataStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InferredReturnsEnumLikeResponseResultDataStatus.ACTIVE:
            return active()
        if self is InferredReturnsEnumLikeResponseResultDataStatus.INACTIVE:
            return inactive()
        if self is InferredReturnsEnumLikeResponseResultDataStatus.PENDING:
            return pending()
