

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.protocol_error_error import ProtocolErrorError
from ...types.protocol_response_meta import ProtocolResponseMeta


class ProtocolThreadCommandPostResponse_Success(UniversalBaseModel):
    type: typing.Literal["success"] = "success"
    id: int
    result: typing.Dict[str, typing.Any]
    meta: typing.Optional[ProtocolResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProtocolThreadCommandPostResponse_Error(UniversalBaseModel):
    type: typing.Literal["error"] = "error"
    id: typing.Optional[int] = None
    error: ProtocolErrorError
    message: str
    stacktrace: typing.Optional[str] = None
    meta: typing.Optional[ProtocolResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ProtocolThreadCommandPostResponse = typing_extensions.Annotated[
    typing.Union[ProtocolThreadCommandPostResponse_Success, ProtocolThreadCommandPostResponse_Error],
    pydantic.Field(discriminator="type"),
]
