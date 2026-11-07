

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeveloperMessageItemParamRole(enum.StrEnum):
    """
    The message role. Always `developer`.
    """

    DEVELOPER = "developer"

    def visit(self, developer: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeveloperMessageItemParamRole.DEVELOPER:
            return developer()
