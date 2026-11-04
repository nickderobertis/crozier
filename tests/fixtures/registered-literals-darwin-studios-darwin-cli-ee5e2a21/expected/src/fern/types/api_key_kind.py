

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiKeyKind(enum.StrEnum):
    """
    New keys identify an application; legacy keys retain their previous user-bound behavior until revoked.
    """

    APPLICATION = "application"
    LEGACY_USER = "legacy_user"

    def visit(self, application: typing.Callable[[], T_Result], legacy_user: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiKeyKind.APPLICATION:
            return application()
        if self is ApiKeyKind.LEGACY_USER:
            return legacy_user()
