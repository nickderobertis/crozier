

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote_networks_configuration import RemoteNetworksConfiguration
from .remote_networks_ipsec_tunnel_response import RemoteNetworksIpsecTunnelResponse


class RemoteNetworksReadResult(UniversalBaseModel):
    configuration: typing.Optional[RemoteNetworksConfiguration] = None
    error: typing.Optional[typing.Dict[str, typing.Any]] = None
    name: str
    network_details: typing_extensions.Annotated[
        typing.Optional[RemoteNetworksIpsecTunnelResponse],
        FieldMetadata(alias="networkDetails"),
        pydantic.Field(alias="networkDetails"),
    ] = None
    status: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
