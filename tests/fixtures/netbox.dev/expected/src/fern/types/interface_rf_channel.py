

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interface_rf_channel_label import InterfaceRfChannelLabel
from .interface_rf_channel_value import InterfaceRfChannelValue


class InterfaceRfChannel(UniversalBaseModel):
    label: InterfaceRfChannelLabel
    value: InterfaceRfChannelValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
