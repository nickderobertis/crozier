

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleExtensionTypeItem(enum.StrEnum):
    ONBOARD_CAPABILITIES = "onboardCapabilities"
    BRANDING = "branding"
    PICTURES = "pictures"

    def visit(
        self,
        onboard_capabilities: typing.Callable[[], T_Result],
        branding: typing.Callable[[], T_Result],
        pictures: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VehicleExtensionTypeItem.ONBOARD_CAPABILITIES:
            return onboard_capabilities()
        if self is VehicleExtensionTypeItem.BRANDING:
            return branding()
        if self is VehicleExtensionTypeItem.PICTURES:
            return pictures()
