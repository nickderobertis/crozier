

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wireless_lan_auth_type_label import WirelessLanAuthTypeLabel
from .wireless_lan_auth_type_value import WirelessLanAuthTypeValue


class WirelessLanAuthType(UniversalBaseModel):
    label: WirelessLanAuthTypeLabel
    value: WirelessLanAuthTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
