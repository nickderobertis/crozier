

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .conversation_threshold_put_response_threshold import ConversationThresholdPutResponseThreshold


class ConversationThresholdPutResponse(UniversalBaseModel):
    conversation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="conversationId"), pydantic.Field(alias="conversationId")
    ]
    threshold: ConversationThresholdPutResponseThreshold

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
