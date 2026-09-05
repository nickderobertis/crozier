

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LicensedResourceType(enum.StrEnum):
    VIP_MODEL = "VIP_MODEL"

    def visit(self, vip_model: typing.Callable[[], T_Result]) -> T_Result:
        if self is LicensedResourceType.VIP_MODEL:
            return vip_model()
