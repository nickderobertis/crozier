

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .asset import Asset
from .item_properties import ItemProperties
from .stac_pydantic_item_item_output_geometry import StacPydanticItemItemOutputGeometry
from .stac_pydantic_item_item_output_type import StacPydanticItemItemOutputType
from .stac_pydantic_links_links import StacPydanticLinksLinks


class StacPydanticItemItemOutput(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/item-spec/item-spec.md
    """

    bbox: typing.Optional[typing.List[typing.Any]] = None
    type: StacPydanticItemItemOutputType
    geometry: typing.Optional[StacPydanticItemItemOutputGeometry] = None
    properties: ItemProperties
    id: str
    stac_version: typing.Optional[str] = None
    assets: typing.Dict[str, Asset]
    links: StacPydanticLinksLinks
    stac_extensions: typing.Optional[typing.List[str]] = None
    collection: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(StacPydanticItemItemOutput)
