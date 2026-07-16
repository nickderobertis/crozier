

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wireless_lan_status_label import WirelessLanStatusLabel
from .wireless_lan_status_value import WirelessLanStatusValue


class WirelessLanStatus(UniversalBaseModel):
    label: WirelessLanStatusLabel
    value: WirelessLanStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
