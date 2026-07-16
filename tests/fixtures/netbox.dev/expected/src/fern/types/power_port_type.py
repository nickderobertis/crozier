

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .power_port_type_label import PowerPortTypeLabel
from .power_port_type_value import PowerPortTypeValue


class PowerPortType(UniversalBaseModel):
    label: PowerPortTypeLabel
    value: PowerPortTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
