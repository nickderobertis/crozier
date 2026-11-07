

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HistogramAnalyticsBar(UniversalBaseModel):
    label: str
    query_count: typing_extensions.Annotated[int, FieldMetadata(alias="queryCount"), pydantic.Field(alias="queryCount")]
    conversation_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="conversationCount"), pydantic.Field(alias="conversationCount")
    ]
    conversations_positive_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="conversationsPositiveCount"), pydantic.Field(alias="conversationsPositiveCount")
    ]
    conversations_negative_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="conversationsNegativeCount"), pydantic.Field(alias="conversationsNegativeCount")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
