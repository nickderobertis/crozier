

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConfigProxy(UniversalBaseModel):
    tcp_nodelay: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="TCP_NODELAY"), pydantic.Field(alias="TCP_NODELAY")
    ] = None
    client_to_server: typing.Optional[str] = None
    disconnect_delay: typing.Optional[int] = None
    max_connects: typing.Optional[int] = None
    portno: typing.Optional[int] = None
    pre_connect: typing.Optional[str] = None
    server_to_client: typing.Optional[str] = None
    target: typing.Optional[str] = None
    transport: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
