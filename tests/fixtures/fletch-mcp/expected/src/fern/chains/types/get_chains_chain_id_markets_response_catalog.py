

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_markets_response_catalog_pairs_item import GetChainsChainIdMarketsResponseCatalogPairsItem


class GetChainsChainIdMarketsResponseCatalog(UniversalBaseModel):
    source: str
    observed_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="observedAt"), pydantic.Field(alias="observedAt")
    ] = None
    age_seconds: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ageSeconds"), pydantic.Field(alias="ageSeconds")
    ] = None
    stale: bool
    error: typing.Optional[str] = None
    pairs: typing.List[GetChainsChainIdMarketsResponseCatalogPairsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
