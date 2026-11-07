

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TunnelProperties(UniversalBaseModel):
    cluster_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="clusterId"), pydantic.Field(alias="clusterId")
    ] = None
    connect_access_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="connectAccessToken"), pydantic.Field(alias="connectAccessToken")
    ] = None
    domain: typing.Optional[str] = None
    manage_ports_access_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="managePortsAccessToken"),
        pydantic.Field(alias="managePortsAccessToken"),
    ] = None
    service_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="serviceUri"), pydantic.Field(alias="serviceUri")
    ] = None
    tunnel_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tunnelId"), pydantic.Field(alias="tunnelId")
    ] = None
    tunnel_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tunnelName"), pydantic.Field(alias="tunnelName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
