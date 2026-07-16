

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ip_address_status_label import IpAddressStatusLabel
from .ip_address_status_value import IpAddressStatusValue


class IpAddressStatus(UniversalBaseModel):
    label: IpAddressStatusLabel
    value: IpAddressStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
