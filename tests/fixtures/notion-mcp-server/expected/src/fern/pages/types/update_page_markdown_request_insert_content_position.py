

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_page_markdown_request_insert_content_position_type import (
    UpdatePageMarkdownRequestInsertContentPositionType,
)


class UpdatePageMarkdownRequestInsertContentPosition(UniversalBaseModel):
    """
    Insert at the start or end of the page. Cannot be combined with after.
    """

    type: typing.Optional[UpdatePageMarkdownRequestInsertContentPositionType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
