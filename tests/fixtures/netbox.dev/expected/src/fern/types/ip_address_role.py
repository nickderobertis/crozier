

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ip_address_role_label import IpAddressRoleLabel
from .ip_address_role_value import IpAddressRoleValue


class IpAddressRole(UniversalBaseModel):
    label: IpAddressRoleLabel
    value: IpAddressRoleValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
