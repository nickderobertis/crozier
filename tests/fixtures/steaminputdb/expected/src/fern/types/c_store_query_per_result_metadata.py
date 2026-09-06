

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .store_item_id import StoreItemId


class CStoreQueryPerResultMetadata(UniversalBaseModel):
    id: typing.Optional[StoreItemId] = None
    score: typing.Optional[float] = None
    spellcheck_generated_result: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
