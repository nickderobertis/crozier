

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TenantsGet200ResponseTenantStatus(enum.StrEnum):
    ACTIVE = "active"
    SUSPENDED = "suspended"

    def visit(self, active: typing.Callable[[], T_Result], suspended: typing.Callable[[], T_Result]) -> T_Result:
        if self is TenantsGet200ResponseTenantStatus.ACTIVE:
            return active()
        if self is TenantsGet200ResponseTenantStatus.SUSPENDED:
            return suspended()
