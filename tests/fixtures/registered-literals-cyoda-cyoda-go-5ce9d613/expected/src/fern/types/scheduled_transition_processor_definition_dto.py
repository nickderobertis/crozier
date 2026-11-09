

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .processor_definition_dto import ProcessorDefinitionDto
from .scheduled_transition_config_dto import ScheduledTransitionConfigDto


class ScheduledTransitionProcessorDefinitionDto(ProcessorDefinitionDto):
    config: ScheduledTransitionConfigDto

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
