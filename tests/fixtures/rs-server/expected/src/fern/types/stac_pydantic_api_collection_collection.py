

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset import Asset
from .extent import Extent
from .provider import Provider
from .stac_pydantic_api_collection_collection_summaries_value import StacPydanticApiCollectionCollectionSummariesValue
from .stac_pydantic_api_collection_collection_type import StacPydanticApiCollectionCollectionType
from .stac_pydantic_links_links import StacPydanticLinksLinks


class StacPydanticApiCollectionCollection(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-api-spec/tree/v1.0.0/ogcapi-features#collection-collectionscollectionid
    """

    id: str
    description: str
    stac_version: typing.Optional[str] = None
    links: StacPydanticLinksLinks
    stac_extensions: typing.Optional[typing.List[str]] = None
    title: typing.Optional[str] = None
    type: StacPydanticApiCollectionCollectionType
    assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = None
    license: str
    extent: Extent
    keywords: typing.Optional[typing.List[str]] = None
    providers: typing.Optional[typing.List[Provider]] = None
    summaries: typing.Optional[typing.Dict[str, typing.Optional[StacPydanticApiCollectionCollectionSummariesValue]]] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
