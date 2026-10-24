

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .swap_status import SwapStatus


class Swap(UniversalBaseModel):
    qty_from: int
    qty_to: int
    from_asset: typing.Optional[str] = None
    to_asset: typing.Optional[str] = None
    payment_hash: str
    status: SwapStatus
    requested_at: int
    initiated_at: typing.Optional[int] = None
    expires_at: int
    completed_at: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
