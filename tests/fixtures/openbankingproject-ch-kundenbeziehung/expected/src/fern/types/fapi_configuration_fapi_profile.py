

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FapiConfigurationFapiProfile(enum.StrEnum):
    TWO0 = "2.0"

    def visit(self, two0: typing.Callable[[], T_Result]) -> T_Result:
        if self is FapiConfigurationFapiProfile.TWO0:
            return two0()
