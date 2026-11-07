

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .externalized_processor_config_dto import ExternalizedProcessorConfigDto
from .externalized_processor_definition_dto_execution_mode import ExternalizedProcessorDefinitionDtoExecutionMode
from .processor_definition_dto import ProcessorDefinitionDto


class ExternalizedProcessorDefinitionDto(ProcessorDefinitionDto):
    execution_mode: typing_extensions.Annotated[
        typing.Optional[ExternalizedProcessorDefinitionDtoExecutionMode],
        FieldMetadata(alias="executionMode"),
        pydantic.Field(alias="executionMode"),
    ] = None
    config: typing.Optional[ExternalizedProcessorConfigDto] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
