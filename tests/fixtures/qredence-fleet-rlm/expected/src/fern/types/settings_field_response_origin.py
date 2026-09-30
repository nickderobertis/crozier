

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SettingsFieldResponseOrigin(enum.StrEnum):
    DEFAULT = "default"
    INHERITED = "inherited"
    OVERRIDE = "override"

    def visit(
        self,
        default: typing.Callable[[], T_Result],
        inherited: typing.Callable[[], T_Result],
        override: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SettingsFieldResponseOrigin.DEFAULT:
            return default()
        if self is SettingsFieldResponseOrigin.INHERITED:
            return inherited()
        if self is SettingsFieldResponseOrigin.OVERRIDE:
            return override()
