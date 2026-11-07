

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreatedApiKeyKind(enum.StrEnum):
    """
    New keys identify an application; legacy keys retain their previous user-bound behavior until revoked.
    """

    APPLICATION = "application"
    LEGACY_USER = "legacy_user"

    def visit(self, application: typing.Callable[[], T_Result], legacy_user: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreatedApiKeyKind.APPLICATION:
            return application()
        if self is CreatedApiKeyKind.LEGACY_USER:
            return legacy_user()
