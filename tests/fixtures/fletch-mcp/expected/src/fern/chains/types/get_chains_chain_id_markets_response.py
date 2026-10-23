

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_markets_response_catalog import GetChainsChainIdMarketsResponseCatalog
from .get_chains_chain_id_markets_response_catalog_matches_item import GetChainsChainIdMarketsResponseCatalogMatchesItem
from .get_chains_chain_id_markets_response_items_item import GetChainsChainIdMarketsResponseItemsItem


class GetChainsChainIdMarketsResponse(UniversalBaseModel):
    chain_id: typing_extensions.Annotated[int, FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")]
    items: typing.List[GetChainsChainIdMarketsResponseItemsItem]
    total: int
    catalog: typing.Optional[GetChainsChainIdMarketsResponseCatalog] = None
    catalog_matches: typing_extensions.Annotated[
        typing.Optional[typing.List[GetChainsChainIdMarketsResponseCatalogMatchesItem]],
        FieldMetadata(alias="catalogMatches"),
        pydantic.Field(alias="catalogMatches"),
    ] = None
    page: int
    page_size: typing_extensions.Annotated[int, FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")]
    sort: str
    as_of: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="asOf"), pydantic.Field(alias="asOf")]
    scope: typing.Optional[str] = None
    note: typing.Optional[str] = None
    applied_filters: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="appliedFilters"),
        pydantic.Field(
            alias="appliedFilters",
            description="Normalized non-default filter values; defaults are in filterDefinitionsUrl. Page and pageSize are returned separately.",
        ),
    ] = None
    """
    Normalized non-default filter values; defaults are in filterDefinitionsUrl. Page and pageSize are returned separately.
    """

    filter_definitions_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="filterDefinitionsUrl"), pydantic.Field(alias="filterDefinitionsUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GetChainsChainIdMarketsResponse)
