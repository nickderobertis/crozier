

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...types.asset import Asset
from ...types.item_input import ItemInput
from ...types.item_input_geometry import ItemInputGeometry
from ...types.item_properties import ItemProperties
from ...types.links_input import LinksInput


class CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature(UniversalBaseModel):
    type: typing.Literal["Feature"] = "Feature"
    bbox: typing.Optional[typing.List[typing.Any]] = None
    geometry: typing.Optional[ItemInputGeometry] = None
    properties: ItemProperties
    id: str
    stac_version: typing.Optional[str] = None
    assets: typing.Dict[str, Asset]
    links: LinksInput
    stac_extensions: typing.Optional[typing.List[str]] = None
    collection: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_FeatureCollection(UniversalBaseModel):
    type: typing.Literal["FeatureCollection"] = "FeatureCollection"
    bbox: typing.Optional[typing.List[typing.Any]] = None
    features: typing.List[ItemInput]
    links: typing.Optional[LinksInput] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody = typing_extensions.Annotated[
    typing.Union[
        CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature,
        CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_FeatureCollection,
    ],
    pydantic.Field(discriminator="type"),
]
update_forward_refs(CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature)
update_forward_refs(CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_FeatureCollection)
