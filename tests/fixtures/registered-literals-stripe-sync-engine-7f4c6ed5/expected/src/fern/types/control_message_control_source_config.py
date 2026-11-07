

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .control_message_control_source_config_source_config import ControlMessageControlSourceConfigSourceConfig


class ControlMessageControlSourceConfig(UniversalBaseModel):
    source_config: ControlMessageControlSourceConfigSourceConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
