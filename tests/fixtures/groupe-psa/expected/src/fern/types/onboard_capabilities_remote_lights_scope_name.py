

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OnboardCapabilitiesRemoteLightsScopeName(enum.StrEnum):
    REMOTE_LIGHTS_WRITE = "remote:lights:write"

    def visit(self, remote_lights_write: typing.Callable[[], T_Result]) -> T_Result:
        if self is OnboardCapabilitiesRemoteLightsScopeName.REMOTE_LIGHTS_WRITE:
            return remote_lights_write()
