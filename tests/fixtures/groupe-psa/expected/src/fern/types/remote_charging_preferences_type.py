

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteChargingPreferencesType(enum.StrEnum):
    """
    Configure charging type preferences.
    """

    PARTIAL = "Partial"
    FULL = "Full"

    def visit(self, partial: typing.Callable[[], T_Result], full: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemoteChargingPreferencesType.PARTIAL:
            return partial()
        if self is RemoteChargingPreferencesType.FULL:
            return full()
