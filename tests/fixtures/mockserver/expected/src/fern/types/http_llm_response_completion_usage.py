

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HttpLlmResponseCompletionUsage(UniversalBaseModel):
    input_tokens: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="inputTokens"), pydantic.Field(alias="inputTokens")
    ] = None
    output_tokens: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="outputTokens"), pydantic.Field(alias="outputTokens")
    ] = None
    cached_input_tokens: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="cachedInputTokens"), pydantic.Field(alias="cachedInputTokens")
    ] = None
    cache_creation_tokens: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="cacheCreationTokens"), pydantic.Field(alias="cacheCreationTokens")
    ] = None
    reasoning_tokens: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="reasoningTokens"), pydantic.Field(alias="reasoningTokens")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
