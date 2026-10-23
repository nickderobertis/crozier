

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...core.serialization import FieldMetadata
from .get_tokens_address_response_impersonates import GetTokensAddressResponseImpersonates
from .get_tokens_address_response_market import GetTokensAddressResponseMarket
from .get_tokens_address_response_reading import GetTokensAddressResponseReading
from .get_tokens_address_response_source import GetTokensAddressResponseSource
from .get_tokens_address_response_trust import GetTokensAddressResponseTrust


class GetTokensAddressResponse(UniversalBaseModel):
    chain_id: typing_extensions.Annotated[int, FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")]
    address: str
    trust: GetTokensAddressResponseTrust
    label: str
    detail: str
    impersonates: typing.Optional[GetTokensAddressResponseImpersonates] = None
    symbol: typing.Optional[str] = None
    name: typing.Optional[str] = None
    decimals: typing.Optional[int] = None
    source: GetTokensAddressResponseSource
    first_seen_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="firstSeenAt"), pydantic.Field(alias="firstSeenAt")
    ] = None
    read_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="readAt"), pydantic.Field(alias="readAt")
    ] = None
    registry_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="registryUrl"), pydantic.Field(alias="registryUrl")
    ] = None
    explorer_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="explorerUrl"), pydantic.Field(alias="explorerUrl")
    ]
    reading: typing.Optional[GetTokensAddressResponseReading] = None
    market: typing.Optional[GetTokensAddressResponseMarket] = None
    note: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GetTokensAddressResponse)
