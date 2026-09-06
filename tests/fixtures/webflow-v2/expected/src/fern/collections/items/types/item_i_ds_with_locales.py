

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_i_ds_with_locales_items_item import ItemIDsWithLocalesItemsItem


class ItemIDsWithLocales(UniversalBaseModel):
    """
    An array of Item IDs with included `cmsLocaleIds`
    """

    items: typing.Optional[typing.List[ItemIDsWithLocalesItemsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
