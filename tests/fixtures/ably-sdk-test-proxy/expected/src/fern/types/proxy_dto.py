

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProxyDto(UniversalBaseModel):
    """
    Describes how a Realtime client instance can connect to a proxy created by a fault simulation.
    """

    listen_port: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="listenPort"),
        pydantic.Field(
            alias="listenPort",
            description="The port that the proxy is listening on. In order to experience the fault whose simulation this proxy belongs to, an Ably realtime client should be configured to connect to this port on the same host as the web server hosting this API.",
        ),
    ] = None
    """
    The port that the proxy is listening on. In order to experience the fault whose simulation this proxy belongs to, an Ably realtime client should be configured to connect to this port on the same host as the web server hosting this API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
