

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1RemoveProjectAddonRequestAddonVariantThree(enum.StrEnum):
    IPV4DEFAULT = "ipv4_default"

    def visit(self, ipv4default: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1RemoveProjectAddonRequestAddonVariantThree.IPV4DEFAULT:
            return ipv4default()
