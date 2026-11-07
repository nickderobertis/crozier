

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .control_message_control_destination_config_destination_config import (
    ControlMessageControlDestinationConfigDestinationConfig,
)
from .control_message_control_source_config_source_config import ControlMessageControlSourceConfigSourceConfig


class ControlMessageControl_SourceConfig(UniversalBaseModel):
    """
    Control signal from a connector to the orchestrator.
    """

    control_type: typing.Literal["source_config"] = "source_config"
    source_config: ControlMessageControlSourceConfigSourceConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ControlMessageControl_DestinationConfig(UniversalBaseModel):
    """
    Control signal from a connector to the orchestrator.
    """

    control_type: typing.Literal["destination_config"] = "destination_config"
    destination_config: ControlMessageControlDestinationConfigDestinationConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ControlMessageControl = typing_extensions.Annotated[
    typing.Union[ControlMessageControl_SourceConfig, ControlMessageControl_DestinationConfig],
    pydantic.Field(discriminator="control_type"),
]
