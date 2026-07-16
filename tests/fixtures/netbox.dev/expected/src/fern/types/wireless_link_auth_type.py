

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wireless_link_auth_type_label import WirelessLinkAuthTypeLabel
from .wireless_link_auth_type_value import WirelessLinkAuthTypeValue


class WirelessLinkAuthType(UniversalBaseModel):
    label: WirelessLinkAuthTypeLabel
    value: WirelessLinkAuthTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
