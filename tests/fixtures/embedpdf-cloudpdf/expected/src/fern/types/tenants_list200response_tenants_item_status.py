

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TenantsList200ResponseTenantsItemStatus(enum.StrEnum):
    ACTIVE = "active"
    SUSPENDED = "suspended"

    def visit(self, active: typing.Callable[[], T_Result], suspended: typing.Callable[[], T_Result]) -> T_Result:
        if self is TenantsList200ResponseTenantsItemStatus.ACTIVE:
            return active()
        if self is TenantsList200ResponseTenantsItemStatus.SUSPENDED:
            return suspended()
