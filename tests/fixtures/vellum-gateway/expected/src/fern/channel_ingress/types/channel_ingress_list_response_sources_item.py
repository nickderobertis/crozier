

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .channel_ingress_list_response_sources_item_routes_item import ChannelIngressListResponseSourcesItemRoutesItem
from .channel_ingress_list_response_sources_item_state import ChannelIngressListResponseSourcesItemState


class ChannelIngressListResponseSourcesItem(UniversalBaseModel):
    source: str
    state: ChannelIngressListResponseSourcesItemState
    digest: str
    approved_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="approvedAt"), pydantic.Field(alias="approvedAt")
    ] = None
    approved_digest: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="approvedDigest"), pydantic.Field(alias="approvedDigest")
    ] = None
    routes: typing.List[ChannelIngressListResponseSourcesItemRoutesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
