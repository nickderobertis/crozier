

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_marketplace_catalog_entry_region import AmazonMarketplaceCatalogEntryRegion


class AmazonMarketplaceCatalogEntry(UniversalBaseModel):
    id: str
    name: str
    country_code: str
    region: AmazonMarketplaceCatalogEntryRegion

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
