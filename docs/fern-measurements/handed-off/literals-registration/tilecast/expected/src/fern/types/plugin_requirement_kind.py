

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PluginRequirementKind(enum.StrEnum):
    PLATFORM = "platform"
    HARDWARE = "hardware"
    REGION = "region"
    NETWORK = "network"
    PROVIDER = "provider"
    PLAYER = "player"

    def visit(
        self,
        platform: typing.Callable[[], T_Result],
        hardware: typing.Callable[[], T_Result],
        region: typing.Callable[[], T_Result],
        network: typing.Callable[[], T_Result],
        provider: typing.Callable[[], T_Result],
        player: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PluginRequirementKind.PLATFORM:
            return platform()
        if self is PluginRequirementKind.HARDWARE:
            return hardware()
        if self is PluginRequirementKind.REGION:
            return region()
        if self is PluginRequirementKind.NETWORK:
            return network()
        if self is PluginRequirementKind.PROVIDER:
            return provider()
        if self is PluginRequirementKind.PLAYER:
            return player()
