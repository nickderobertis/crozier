

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_status import ChannelStatus


class Channel(UniversalBaseModel):
    channel_id: str
    funding_txid: typing.Optional[str] = None
    peer_pubkey: str
    peer_alias: typing.Optional[str] = None
    short_channel_id: typing.Optional[int] = None
    status: ChannelStatus
    ready: bool
    capacity_sat: int
    local_balance_sat: int
    outbound_balance_msat: int
    inbound_balance_msat: int
    next_outbound_htlc_limit_msat: int
    next_outbound_htlc_minimum_msat: int
    is_usable: bool
    public: bool
    asset_id: typing.Optional[str] = None
    asset_local_amount: typing.Optional[int] = None
    asset_remote_amount: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
