

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .item_input import ItemInput
from .links_input import LinksInput


class ItemCollectionInput(UniversalBaseModel):
    """
    This is a less strict implementation of ItemCollection.
    It only implements the FeatureCollection Specs
    not enforcing required links as specified in STAC-API-FEATURES specs.
    Use `stac_pydantic.api.ItemCollection` to enforce link relationships and extra fields.
    """

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


update_forward_refs(ItemCollectionInput)
