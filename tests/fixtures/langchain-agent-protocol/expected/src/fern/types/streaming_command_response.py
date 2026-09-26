

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .streaming_success_response_meta import StreamingSuccessResponseMeta


class StreamingCommandResponse_Success(UniversalBaseModel):
    """
    Server response to a streaming protocol command.
    """

    type: typing.Literal["success"] = "success"
    id: int
    result: typing.Dict[str, typing.Any]
    meta: typing.Optional[StreamingSuccessResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamingCommandResponse_Error(UniversalBaseModel):
    """
    Server response to a streaming protocol command.
    """

    type: typing.Literal["error"] = "error"
    id: typing.Optional[int] = None
    error: str
    message: str
    stacktrace: typing.Optional[str] = None
    meta: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StreamingCommandResponse = typing_extensions.Annotated[
    typing.Union[StreamingCommandResponse_Success, StreamingCommandResponse_Error], pydantic.Field(discriminator="type")
]
