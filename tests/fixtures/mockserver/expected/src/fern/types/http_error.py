

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay


class HttpError(UniversalBaseModel):
    """
    error behaviour
    """

    delay: typing.Optional[Delay] = None
    drop_connection: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="dropConnection"),
        pydantic.Field(
            alias="dropConnection",
            description="drop the connection; ignored when streamError is set (streamError takes precedence)",
        ),
    ] = None
    """
    drop the connection; ignored when streamError is set (streamError takes precedence)
    """

    response_bytes: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseBytes"), pydantic.Field(alias="responseBytes")
    ] = None
    stream_error: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="streamError"),
        pydantic.Field(
            alias="streamError",
            description="reset the matched request stream with this error code (HTTP/2 RST_STREAM / HTTP/3 RESET_STREAM) instead of returning a response; HTTP/1.1 has no stream concept so this falls back to dropping the connection",
        ),
    ] = None
    """
    reset the matched request stream with this error code (HTTP/2 RST_STREAM / HTTP/3 RESET_STREAM) instead of returning a response; HTTP/1.1 has no stream concept so this falls back to dropping the connection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
