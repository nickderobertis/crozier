

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiModelsRolePermissionChangeAction(enum.StrEnum):
    """
    The action to take.
    """

    GRANT = "Grant"
    REVOKE = "Revoke"

    def visit(self, grant: typing.Callable[[], T_Result], revoke: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiModelsRolePermissionChangeAction.GRANT:
            return grant()
        if self is ApiModelsRolePermissionChangeAction.REVOKE:
            return revoke()
