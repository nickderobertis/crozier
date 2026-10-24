

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_balance_response import AssetBalanceResponse
from .token_light import TokenLight


class AssetUda(UniversalBaseModel):
    asset_id: str
    ticker: str
    name: str
    details: typing.Optional[str] = None
    precision: int
    timestamp: int
    added_at: int
    balance: AssetBalanceResponse
    token: typing.Optional[TokenLight] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
