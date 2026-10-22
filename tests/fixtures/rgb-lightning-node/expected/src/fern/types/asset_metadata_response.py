

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_schema import AssetSchema
from .token import Token


class AssetMetadataResponse(UniversalBaseModel):
    asset_schema: AssetSchema
    initial_supply: int
    max_supply: int
    known_circulating_supply: int
    timestamp: int
    name: str
    precision: int
    ticker: typing.Optional[str] = None
    details: typing.Optional[str] = None
    token: typing.Optional[Token] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
