

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .kit_list_item_source_type import KitListItemSourceType


class KitListItem(UniversalBaseModel):
    asset_id: typing.Optional[str] = None
    category: typing.Optional[str] = None
    created_at: typing.Optional[str] = None
    id: int
    image_ids: typing.Optional[typing.List[typing.Optional[str]]] = None
    locale: typing.Optional[str] = None
    name: str
    name_en: typing.Optional[str] = None
    score: typing.Optional[int] = None
    sku: str
    source_type: typing.Optional[KitListItemSourceType] = None
    status: str
    thumbs: typing.List[typing.Optional[str]]
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
