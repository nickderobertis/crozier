

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionGrantSubjectType(enum.StrEnum):
    """
    Kind of subject. A `tenant` subject shares the session with everyone in the tenant.
    """

    USER = "user"
    TENANT = "tenant"

    def visit(self, user: typing.Callable[[], T_Result], tenant: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionGrantSubjectType.USER:
            return user()
        if self is SessionGrantSubjectType.TENANT:
            return tenant()
