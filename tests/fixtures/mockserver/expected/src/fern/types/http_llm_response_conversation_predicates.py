

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .http_llm_response_conversation_predicates_latest_message_role import (
    HttpLlmResponseConversationPredicatesLatestMessageRole,
)
from .http_llm_response_conversation_predicates_normalization import HttpLlmResponseConversationPredicatesNormalization


class HttpLlmResponseConversationPredicates(UniversalBaseModel):
    turn_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="turnIndex"), pydantic.Field(alias="turnIndex")
    ] = None
    latest_message_contains: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="latestMessageContains"),
        pydantic.Field(alias="latestMessageContains"),
    ] = None
    latest_message_matches: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="latestMessageMatches"), pydantic.Field(alias="latestMessageMatches")
    ] = None
    latest_message_role: typing_extensions.Annotated[
        typing.Optional[HttpLlmResponseConversationPredicatesLatestMessageRole],
        FieldMetadata(alias="latestMessageRole"),
        pydantic.Field(alias="latestMessageRole"),
    ] = None
    contains_tool_result_for: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="containsToolResultFor"),
        pydantic.Field(alias="containsToolResultFor"),
    ] = None
    semantic_match_against: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="semanticMatchAgainst"), pydantic.Field(alias="semanticMatchAgainst")
    ] = None
    normalization: typing.Optional[HttpLlmResponseConversationPredicatesNormalization] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
