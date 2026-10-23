

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_tokens_address_response_market_price_source import GetTokensAddressResponseMarketPriceSource


class GetTokensAddressResponseMarket(UniversalBaseModel):
    pool_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="poolId"), pydantic.Field(alias="poolId")
    ] = None
    venue: typing.Optional[str] = None
    price_usd: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="priceUsd"), pydantic.Field(alias="priceUsd")
    ] = None
    depth_usd: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="depthUsd"), pydantic.Field(alias="depthUsd")
    ] = None
    swaps24h: typing.Optional[int] = None
    transactions24h: typing.Optional[int] = None
    metrics_as_of: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="metricsAsOf"), pydantic.Field(alias="metricsAsOf")
    ] = None
    price_source: typing_extensions.Annotated[
        typing.Optional[GetTokensAddressResponseMarketPriceSource],
        FieldMetadata(alias="priceSource"),
        pydantic.Field(alias="priceSource"),
    ] = None
    volume_usd24h: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="volumeUsd24h"), pydantic.Field(alias="volumeUsd24h")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
