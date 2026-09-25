

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehiclesExtensionTypeItem(enum.StrEnum):
    BRANDING = "branding"
    PICTURES = "pictures"

    def visit(self, branding: typing.Callable[[], T_Result], pictures: typing.Callable[[], T_Result]) -> T_Result:
        if self is VehiclesExtensionTypeItem.BRANDING:
            return branding()
        if self is VehiclesExtensionTypeItem.PICTURES:
            return pictures()
