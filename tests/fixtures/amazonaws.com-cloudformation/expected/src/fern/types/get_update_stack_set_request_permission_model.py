

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetUpdateStackSetRequestPermissionModel(str, enum.Enum):
    SERVICE_MANAGED = "SERVICE_MANAGED"
    SELF_MANAGED = "SELF_MANAGED"

    def visit(
        self, service_managed: typing.Callable[[], T_Result], self_managed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetUpdateStackSetRequestPermissionModel.SERVICE_MANAGED:
            return service_managed()
        if self is GetUpdateStackSetRequestPermissionModel.SELF_MANAGED:
            return self_managed()
