

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay


class ConnectionOptions(UniversalBaseModel):
    """
    connection options
    """

    suppress_content_length_header: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="suppressContentLengthHeader"),
        pydantic.Field(alias="suppressContentLengthHeader"),
    ] = None
    content_length_header_override: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="contentLengthHeaderOverride"),
        pydantic.Field(alias="contentLengthHeaderOverride"),
    ] = None
    suppress_connection_header: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="suppressConnectionHeader"),
        pydantic.Field(alias="suppressConnectionHeader"),
    ] = None
    chunk_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="chunkSize"), pydantic.Field(alias="chunkSize")
    ] = None
    keep_alive_override: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="keepAliveOverride"), pydantic.Field(alias="keepAliveOverride")
    ] = None
    close_socket: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="closeSocket"), pydantic.Field(alias="closeSocket")
    ] = None
    close_socket_delay: typing_extensions.Annotated[
        typing.Optional[Delay], FieldMetadata(alias="closeSocketDelay"), pydantic.Field(alias="closeSocketDelay")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
