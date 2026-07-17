

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetCreateStackSetRequestPermissionModel(enum.StrEnum):
    SERVICE_MANAGED = "SERVICE_MANAGED"
    SELF_MANAGED = "SELF_MANAGED"

    def visit(
        self, service_managed: typing.Callable[[], T_Result], self_managed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetCreateStackSetRequestPermissionModel.SERVICE_MANAGED:
            return service_managed()
        if self is GetCreateStackSetRequestPermissionModel.SELF_MANAGED:
            return self_managed()
