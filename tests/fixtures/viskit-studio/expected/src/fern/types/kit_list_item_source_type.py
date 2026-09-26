

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KitListItemSourceType(enum.StrEnum):
    KIT = "kit"
    ASSET = "asset"

    def visit(self, kit: typing.Callable[[], T_Result], asset: typing.Callable[[], T_Result]) -> T_Result:
        if self is KitListItemSourceType.KIT:
            return kit()
        if self is KitListItemSourceType.ASSET:
            return asset()
