

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .store_item_wearable import StoreItemWearable


class StoreItem(UniversalBaseModel):
    id: str
    wearable: typing.Optional[StoreItemWearable] = pydantic.Field(default=None)
    """
    A shirt or a coat.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
