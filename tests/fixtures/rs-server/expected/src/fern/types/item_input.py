

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .asset import Asset
from .item_input_geometry import ItemInputGeometry
from .item_input_type import ItemInputType
from .item_properties import ItemProperties
from .links_input import LinksInput


class ItemInput(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/item-spec/item-spec.md
    """

    bbox: typing.Optional[typing.List[typing.Any]] = None
    type: ItemInputType
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


update_forward_refs(ItemInput)
