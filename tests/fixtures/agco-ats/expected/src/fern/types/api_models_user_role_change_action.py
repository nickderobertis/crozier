

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiModelsUserRoleChangeAction(enum.StrEnum):
    """
    The action to take with the role
    """

    GRANT = "Grant"
    REVOKE = "Revoke"

    def visit(self, grant: typing.Callable[[], T_Result], revoke: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiModelsUserRoleChangeAction.GRANT:
            return grant()
        if self is ApiModelsUserRoleChangeAction.REVOKE:
            return revoke()
