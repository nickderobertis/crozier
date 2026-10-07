

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KeymapConfigPreset(enum.StrEnum):
    DEFAULT = "default"
    VIM = "vim"

    def visit(self, default: typing.Callable[[], T_Result], vim: typing.Callable[[], T_Result]) -> T_Result:
        if self is KeymapConfigPreset.DEFAULT:
            return default()
        if self is KeymapConfigPreset.VIM:
            return vim()
