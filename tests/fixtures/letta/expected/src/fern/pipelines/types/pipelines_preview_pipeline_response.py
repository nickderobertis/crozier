

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PipelinesPreviewPipelineResponse(UniversalBaseModel):
    sample_messages: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="sampleMessages"), pydantic.Field(alias="sampleMessages")
    ]
    message_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="messageCount"), pydantic.Field(alias="messageCount")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
