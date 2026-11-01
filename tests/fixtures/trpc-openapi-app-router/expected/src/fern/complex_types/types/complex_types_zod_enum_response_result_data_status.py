

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ComplexTypesZodEnumResponseResultDataStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ComplexTypesZodEnumResponseResultDataStatus.ACTIVE:
            return active()
        if self is ComplexTypesZodEnumResponseResultDataStatus.INACTIVE:
            return inactive()
        if self is ComplexTypesZodEnumResponseResultDataStatus.PENDING:
            return pending()
