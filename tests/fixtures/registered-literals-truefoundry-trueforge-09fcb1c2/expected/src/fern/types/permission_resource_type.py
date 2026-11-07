

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PermissionResourceType(enum.StrEnum):
    """
    Resource type to evaluate permissions for.
    """

    AGENT = "agent"
    SCHEDULE = "schedule"
    SESSION = "session"
    TENANT = "tenant"

    def visit(
        self,
        agent: typing.Callable[[], T_Result],
        schedule: typing.Callable[[], T_Result],
        session: typing.Callable[[], T_Result],
        tenant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PermissionResourceType.AGENT:
            return agent()
        if self is PermissionResourceType.SCHEDULE:
            return schedule()
        if self is PermissionResourceType.SESSION:
            return session()
        if self is PermissionResourceType.TENANT:
            return tenant()
