

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LaunchLayerClusterProviderVpcType(enum.StrEnum):
    """
    Network type for a managed or existing VPC. When omitted, CAPLL
    treats the VPC as VIRTUALIZED. A VIRTUALIZED security group needs a
    VIRTUALIZED VPC.
    """

    BARE_METAL = "BARE_METAL"
    VIRTUALIZED = "VIRTUALIZED"

    def visit(self, bare_metal: typing.Callable[[], T_Result], virtualized: typing.Callable[[], T_Result]) -> T_Result:
        if self is LaunchLayerClusterProviderVpcType.BARE_METAL:
            return bare_metal()
        if self is LaunchLayerClusterProviderVpcType.VIRTUALIZED:
            return virtualized()
