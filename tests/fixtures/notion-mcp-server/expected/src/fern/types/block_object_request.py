

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bulleted_list_item_block_request_bulleted_list_item import BulletedListItemBlockRequestBulletedListItem
from .paragraph_block_request_paragraph import ParagraphBlockRequestParagraph


class BlockObjectRequest_Paragraph(UniversalBaseModel):
    type: typing.Literal["paragraph"] = "paragraph"
    paragraph: typing.Optional[ParagraphBlockRequestParagraph] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BlockObjectRequest_BulletedListItem(UniversalBaseModel):
    type: typing.Literal["bulleted_list_item"] = "bulleted_list_item"
    bulleted_list_item: typing.Optional[BulletedListItemBlockRequestBulletedListItem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


BlockObjectRequest = typing_extensions.Annotated[
    typing.Union[BlockObjectRequest_Paragraph, BlockObjectRequest_BulletedListItem],
    pydantic.Field(discriminator="type"),
]
