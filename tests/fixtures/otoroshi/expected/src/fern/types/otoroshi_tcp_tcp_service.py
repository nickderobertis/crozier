

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_tcp_tcp_rule import OtoroshiTcpTcpRule


class OtoroshiTcpTcpService(UniversalBaseModel):
    """
    Model for a TCP proxy
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Service enabled
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity description
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Entity metadata
    """

    port: typing.Optional[int] = pydantic.Field(default=None)
    """
    network port
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity tags
    """

    rules: typing.Optional[typing.List[OtoroshiTcpTcpRule]] = pydantic.Field(default=None)
    """
    Routing rules
    """

    client_auth: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="clientAuth"), pydantic.Field(alias="clientAuth")
    ] = None
    interface: typing.Optional[str] = pydantic.Field(default=None)
    """
    Network interface
    """

    sni: typing.Optional[typing.Any] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity id
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity name
    """

    tls: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
