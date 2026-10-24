

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_balance_response import AssetBalanceResponse
from .media import Media


class AssetCfa(UniversalBaseModel):
    asset_id: str
    name: str
    details: typing.Optional[str] = None
    precision: int
    issued_supply: int
    timestamp: int
    added_at: int
    balance: AssetBalanceResponse
    media: typing.Optional[Media] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
