

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LaunchLayerSecurityGroupNetworkType(enum.StrEnum):
    """
    Required for a VIRTUALIZED group and rejected for a BARE_METAL group.
    """

    PRIMARY = "primary"
    SECONDARY = "secondary"

    def visit(self, primary: typing.Callable[[], T_Result], secondary: typing.Callable[[], T_Result]) -> T_Result:
        if self is LaunchLayerSecurityGroupNetworkType.PRIMARY:
            return primary()
        if self is LaunchLayerSecurityGroupNetworkType.SECONDARY:
            return secondary()
