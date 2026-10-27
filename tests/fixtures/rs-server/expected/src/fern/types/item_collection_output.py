

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .item_collection_output_type import ItemCollectionOutputType
from .stac_pydantic_api_item_item import StacPydanticApiItemItem
from .stac_pydantic_api_links_links import StacPydanticApiLinksLinks


class ItemCollectionOutput(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-api-spec/blob/v1.0.0/fragments/itemcollection/README.md
    https://github.com/radiantearth/stac-api-spec/blob/v1.0.0/item-search/README.md#link-relations
    """

    bbox: typing.Optional[typing.List[typing.Any]] = None
    type: ItemCollectionOutputType
    features: typing.List[StacPydanticApiItemItem]
    links: typing.Optional[StacPydanticApiLinksLinks] = None
    number_matched: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberMatched"), pydantic.Field(alias="numberMatched")
    ] = None
    number_returned: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberReturned"), pydantic.Field(alias="numberReturned")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ItemCollectionOutput)
