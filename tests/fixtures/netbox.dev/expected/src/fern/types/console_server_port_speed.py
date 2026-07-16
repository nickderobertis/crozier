

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .console_server_port_speed_label import ConsoleServerPortSpeedLabel


class ConsoleServerPortSpeed(UniversalBaseModel):
    label: ConsoleServerPortSpeedLabel
    value: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
