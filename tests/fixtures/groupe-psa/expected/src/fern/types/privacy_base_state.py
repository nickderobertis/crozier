

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PrivacyBaseState(enum.StrEnum):
    NONE = "None"
    GEOLOCATION = "Geolocation"
    FULL = "Full"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        geolocation: typing.Callable[[], T_Result],
        full: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PrivacyBaseState.NONE:
            return none()
        if self is PrivacyBaseState.GEOLOCATION:
            return geolocation()
        if self is PrivacyBaseState.FULL:
            return full()
