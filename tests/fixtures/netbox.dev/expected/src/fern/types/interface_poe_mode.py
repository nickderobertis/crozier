

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interface_poe_mode_label import InterfacePoeModeLabel
from .interface_poe_mode_value import InterfacePoeModeValue


class InterfacePoeMode(UniversalBaseModel):
    label: InterfacePoeModeLabel
    value: InterfacePoeModeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
