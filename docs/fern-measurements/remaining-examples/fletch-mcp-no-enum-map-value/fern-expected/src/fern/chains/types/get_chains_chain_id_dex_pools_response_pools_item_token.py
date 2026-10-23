

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetChainsChainIdDexPoolsResponsePoolsItemToken(UniversalBaseModel):
    """
    The unlisted side of a community pool, as its own contract describes it. Nothing here is verified.
    """

    address: typing.Optional[str] = None
    symbol: typing.Optional[str] = None
    name: typing.Optional[str] = None
    decimals: typing.Optional[int] = None
    total_supply_raw: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="totalSupplyRaw"),
        pydantic.Field(alias="totalSupplyRaw", description="Base units; divide by 10^decimals."),
    ] = None
    """
    Base units; divide by 10^decimals.
    """

    fdv_usd: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="fdvUsd"),
        pydantic.Field(alias="fdvUsd", description="Total supply times the pool's dollar price."),
    ] = None
    """
    Total supply times the pool's dollar price.
    """

    burned_raw: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="burnedRaw"),
        pydantic.Field(
            alias="burnedRaw", description="Sum of readable balances at the zero and dead addresses, in base units."
        ),
    ] = None
    """
    Sum of readable balances at the zero and dead addresses, in base units.
    """

    market_cap_usd: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="marketCapUsd"),
        pydantic.Field(
            alias="marketCapUsd",
            description="Total supply minus zero/dead-address balances, times the pool price. An upper bound on circulating value. Null without supply, burn balances, decimals or usable price, or when recorded burns exceed supply. Confirmed zero outstanding supply renders zero.",
        ),
    ] = None
    """
    Total supply minus zero/dead-address balances, times the pool price. An upper bound on circulating value. Null without supply, burn balances, decimals or usable price, or when recorded burns exceed supply. Confirmed zero outstanding supply renders zero.
    """

    supply_read_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="supplyReadAt"), pydantic.Field(alias="supplyReadAt")
    ] = None
    supply_expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="supplyExpiresAt"), pydantic.Field(alias="supplyExpiresAt")
    ] = None
    supply_current: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="supplyCurrent"),
        pydantic.Field(
            alias="supplyCurrent",
            description="Supply and recorded burn balances are at most five minutes old. FDV and capitalization are withheld otherwise.",
        ),
    ] = None
    """
    Supply and recorded burn balances are at most five minutes old. FDV and capitalization are withheld otherwise.
    """

    read_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="readAt"), pydantic.Field(alias="readAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
