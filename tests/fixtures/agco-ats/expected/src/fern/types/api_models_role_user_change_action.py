

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiModelsRoleUserChangeAction(enum.StrEnum):
    """
    The action to take with the user
    """

    GRANT = "Grant"
    REVOKE = "Revoke"

    def visit(self, grant: typing.Callable[[], T_Result], revoke: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiModelsRoleUserChangeAction.GRANT:
            return grant()
        if self is ApiModelsRoleUserChangeAction.REVOKE:
            return revoke()
