

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FapiConfigurationFapiSecurityProfile(enum.StrEnum):
    BASELINE = "baseline"
    ADVANCED = "advanced"

    def visit(self, baseline: typing.Callable[[], T_Result], advanced: typing.Callable[[], T_Result]) -> T_Result:
        if self is FapiConfigurationFapiSecurityProfile.BASELINE:
            return baseline()
        if self is FapiConfigurationFapiSecurityProfile.ADVANCED:
            return advanced()
