

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interface_duplex_label import InterfaceDuplexLabel
from .interface_duplex_value import InterfaceDuplexValue


class InterfaceDuplex(UniversalBaseModel):
    label: InterfaceDuplexLabel
    value: InterfaceDuplexValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
