

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class StoreItemIncludedItems(UniversalBaseModel):
    included_apps: typing.Optional[typing.List["StoreItem"]] = None
    included_packages: typing.Optional[typing.List["StoreItem"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .store_item import StoreItem

update_forward_refs(StoreItemIncludedItems, StoreItem=StoreItem)
