

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.split_view_alert import SplitViewAlert
from .get_gossip_peers_response_peers_item import GetGossipPeersResponsePeersItem


class GetGossipPeersResponse(UniversalBaseModel):
    log_id: typing.Optional[str] = None
    peers: typing.Optional[typing.List[GetGossipPeersResponsePeersItem]] = None
    alerts: typing.Optional[typing.List[SplitViewAlert]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
