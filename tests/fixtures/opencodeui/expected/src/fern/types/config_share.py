

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfigShare(enum.StrEnum):
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto' enables automatic sharing, 'disabled' disables all sharing
    """

    MANUAL = "manual"
    AUTO = "auto"
    DISABLED = "disabled"

    def visit(
        self,
        manual: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConfigShare.MANUAL:
            return manual()
        if self is ConfigShare.AUTO:
            return auto()
        if self is ConfigShare.DISABLED:
            return disabled()
