

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SystemMessageItemParamRole(enum.StrEnum):
    """
    The message role. Always `system`.
    """

    SYSTEM = "system"

    def visit(self, system: typing.Callable[[], T_Result]) -> T_Result:
        if self is SystemMessageItemParamRole.SYSTEM:
            return system()
