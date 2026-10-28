

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset import Asset
from .extent import Extent
from .provider import Provider
from .stac_pydantic_collection_collection_output_summaries_value import (
    StacPydanticCollectionCollectionOutputSummariesValue,
)
from .stac_pydantic_collection_collection_output_type import StacPydanticCollectionCollectionOutputType
from .stac_pydantic_links_links import StacPydanticLinksLinks


class StacPydanticCollectionCollectionOutput(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md
    """

    id: str
    description: str
    stac_version: typing.Optional[str] = None
    links: StacPydanticLinksLinks
    stac_extensions: typing.Optional[typing.List[str]] = None
    title: typing.Optional[str] = None
    type: StacPydanticCollectionCollectionOutputType
    assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = None
    license: str
    extent: Extent
    keywords: typing.Optional[typing.List[str]] = None
    providers: typing.Optional[typing.List[Provider]] = None
    summaries: typing.Optional[
        typing.Dict[str, typing.Optional[StacPydanticCollectionCollectionOutputSummariesValue]]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
