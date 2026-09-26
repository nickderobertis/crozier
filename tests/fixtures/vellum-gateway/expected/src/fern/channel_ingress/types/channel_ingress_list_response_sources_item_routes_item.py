

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .channel_ingress_list_response_sources_item_routes_item_verification import (
    ChannelIngressListResponseSourcesItemRoutesItemVerification,
)


class ChannelIngressListResponseSourcesItemRoutesItem(UniversalBaseModel):
    path: str
    public_path: typing_extensions.Annotated[str, FieldMetadata(alias="publicPath"), pydantic.Field(alias="publicPath")]
    kind: str
    signer: str
    handshake: str
    description: str
    credential: str
    served: bool
    delivers_inbound: typing_extensions.Annotated[
        bool, FieldMetadata(alias="deliversInbound"), pydantic.Field(alias="deliversInbound")
    ]
    verification: typing.Optional[ChannelIngressListResponseSourcesItemRoutesItemVerification] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
