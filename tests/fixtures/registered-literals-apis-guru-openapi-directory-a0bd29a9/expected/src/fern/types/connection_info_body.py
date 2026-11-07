

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tunnel_properties import TunnelProperties


class ConnectionInfoBody(UniversalBaseModel):
    connection_service_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="connectionServiceUri"), pydantic.Field(alias="connectionServiceUri")
    ] = None
    connection_session_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="connectionSessionId"), pydantic.Field(alias="connectionSessionId")
    ] = None
    connection_session_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="connectionSessionPath"),
        pydantic.Field(alias="connectionSessionPath"),
    ] = None
    host_public_keys: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="hostPublicKeys"), pydantic.Field(alias="hostPublicKeys")
    ] = None
    relay_endpoint: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="relayEndpoint"), pydantic.Field(alias="relayEndpoint")
    ] = None
    relay_sas_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="relaySasToken"), pydantic.Field(alias="relaySasToken")
    ] = None
    session_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sessionToken"), pydantic.Field(alias="sessionToken")
    ] = None
    tunnel_properties: typing_extensions.Annotated[
        typing.Optional[TunnelProperties],
        FieldMetadata(alias="tunnelProperties"),
        pydantic.Field(alias="tunnelProperties"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
