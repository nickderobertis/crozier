

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_a_comment_request_rich_text_item_text import CreateACommentRequestRichTextItemText


class CreateACommentRequestRichTextItem(UniversalBaseModel):
    text: CreateACommentRequestRichTextItemText

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
