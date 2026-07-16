

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interface_mode_label import InterfaceModeLabel
from .interface_mode_value import InterfaceModeValue


class InterfaceMode(UniversalBaseModel):
    label: InterfaceModeLabel
    value: InterfaceModeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
