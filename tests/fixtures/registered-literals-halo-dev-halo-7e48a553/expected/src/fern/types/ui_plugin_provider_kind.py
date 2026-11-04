

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UiPluginProviderKind(enum.StrEnum):
    """
    Provider classification and loading mode.
    """

    LEGACY = "legacy"
    ESM = "esm"
    INVALID = "invalid"

    def visit(
        self,
        legacy: typing.Callable[[], T_Result],
        esm: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UiPluginProviderKind.LEGACY:
            return legacy()
        if self is UiPluginProviderKind.ESM:
            return esm()
        if self is UiPluginProviderKind.INVALID:
            return invalid()
