

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodeInfoResponse(UniversalBaseModel):
    pubkey: str
    num_channels: int
    num_usable_channels: int
    local_balance_sat: int
    eventual_close_fees_sat: int
    pending_outbound_payments_sat: int
    num_peers: int
    account_xpub_vanilla: str
    account_xpub_colored: str
    max_media_upload_size_mb: int
    rgb_htlc_min_msat: int
    rgb_channel_capacity_min_sat: int
    channel_capacity_min_sat: int
    channel_capacity_max_sat: int
    channel_asset_min_amount: int
    channel_asset_max_amount: int
    network_nodes: int
    network_channels: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
