

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .front_port_type_label import FrontPortTypeLabel
from .front_port_type_value import FrontPortTypeValue


class FrontPortType(UniversalBaseModel):
    label: FrontPortTypeLabel
    value: FrontPortTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
