

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_tui_command_execute_properties_command import EventTuiCommandExecutePropertiesCommand


class EventTuiCommandExecuteProperties(UniversalBaseModel):
    command: EventTuiCommandExecutePropertiesCommand

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
