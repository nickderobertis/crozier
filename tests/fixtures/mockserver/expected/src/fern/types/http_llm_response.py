

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay
from .http_llm_response_chaos import HttpLlmResponseChaos
from .http_llm_response_completion import HttpLlmResponseCompletion
from .http_llm_response_content_filter import HttpLlmResponseContentFilter
from .http_llm_response_conversation_predicates import HttpLlmResponseConversationPredicates
from .http_llm_response_embedding import HttpLlmResponseEmbedding
from .http_llm_response_moderation import HttpLlmResponseModeration
from .http_llm_response_provider import HttpLlmResponseProvider
from .http_llm_response_rerank import HttpLlmResponseRerank


class HttpLlmResponse(UniversalBaseModel):
    """
    LLM response to return
    """

    delay: typing.Optional[Delay] = None
    provider: typing.Optional[HttpLlmResponseProvider] = None
    model: typing.Optional[str] = None
    completion: typing.Optional[HttpLlmResponseCompletion] = None
    embedding: typing.Optional[HttpLlmResponseEmbedding] = None
    rerank: typing.Optional[HttpLlmResponseRerank] = None
    moderation: typing.Optional[HttpLlmResponseModeration] = None
    content_filter: typing_extensions.Annotated[
        typing.Optional[HttpLlmResponseContentFilter],
        FieldMetadata(alias="contentFilter"),
        pydantic.Field(alias="contentFilter"),
    ] = None
    conversation_predicates: typing_extensions.Annotated[
        typing.Optional[HttpLlmResponseConversationPredicates],
        FieldMetadata(alias="conversationPredicates"),
        pydantic.Field(alias="conversationPredicates"),
    ] = None
    chaos: typing.Optional[HttpLlmResponseChaos] = None
    primary: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
