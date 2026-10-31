

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LaunchLayerSecurityGroupType(enum.StrEnum):
    """
    Immutable. A virtual VPC can contain both kinds of groups.
    """

    BARE_METAL = "BARE_METAL"
    VIRTUALIZED = "VIRTUALIZED"

    def visit(self, bare_metal: typing.Callable[[], T_Result], virtualized: typing.Callable[[], T_Result]) -> T_Result:
        if self is LaunchLayerSecurityGroupType.BARE_METAL:
            return bare_metal()
        if self is LaunchLayerSecurityGroupType.VIRTUALIZED:
            return virtualized()
