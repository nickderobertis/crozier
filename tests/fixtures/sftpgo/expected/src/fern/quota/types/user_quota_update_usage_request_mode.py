

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UserQuotaUpdateUsageRequestMode(enum.StrEnum):
    """
    Update type:
        * `add` - add the specified quota limits to the current used ones
        * `reset` - reset the values to the specified ones. This is the default
    """

    ADD = "add"
    RESET = "reset"

    def visit(self, add: typing.Callable[[], T_Result], reset: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserQuotaUpdateUsageRequestMode.ADD:
            return add()
        if self is UserQuotaUpdateUsageRequestMode.RESET:
            return reset()
