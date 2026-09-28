

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay


class HttpLlmResponseCompletionStreamingPhysics(UniversalBaseModel):
    time_to_first_token: typing_extensions.Annotated[
        typing.Optional[Delay], FieldMetadata(alias="timeToFirstToken"), pydantic.Field(alias="timeToFirstToken")
    ] = None
    tokens_per_second: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="tokensPerSecond"), pydantic.Field(alias="tokensPerSecond")
    ] = None
    jitter: typing.Optional[float] = None
    seed: typing.Optional[int] = None
    subword_streaming: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="subwordStreaming"), pydantic.Field(alias="subwordStreaming")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
