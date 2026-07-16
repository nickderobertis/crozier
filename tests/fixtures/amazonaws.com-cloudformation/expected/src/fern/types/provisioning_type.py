

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProvisioningType(enum.StrEnum):
    NON_PROVISIONABLE = "NON_PROVISIONABLE"
    IMMUTABLE = "IMMUTABLE"
    FULLY_MUTABLE = "FULLY_MUTABLE"

    def visit(
        self,
        non_provisionable: typing.Callable[[], T_Result],
        immutable: typing.Callable[[], T_Result],
        fully_mutable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProvisioningType.NON_PROVISIONABLE:
            return non_provisionable()
        if self is ProvisioningType.IMMUTABLE:
            return immutable()
        if self is ProvisioningType.FULLY_MUTABLE:
            return fully_mutable()
