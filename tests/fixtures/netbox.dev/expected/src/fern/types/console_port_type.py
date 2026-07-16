

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .console_port_type_label import ConsolePortTypeLabel
from .console_port_type_value import ConsolePortTypeValue


class ConsolePortType(UniversalBaseModel):
    label: ConsolePortTypeLabel
    value: ConsolePortTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
