

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bulleted_list_item_block_request_bulleted_list_item import BulletedListItemBlockRequestBulletedListItem


class BulletedListItemBlockRequest(UniversalBaseModel):
    bulleted_list_item: typing.Optional[BulletedListItemBlockRequestBulletedListItem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
