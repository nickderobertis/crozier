

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_page_markdown_request_update_content_content_updates_item import (
    UpdatePageMarkdownRequestUpdateContentContentUpdatesItem,
)


class UpdatePageMarkdownRequestUpdateContent(UniversalBaseModel):
    """
    Provide when type is `update_content`. Applies targeted find-and-replace edits.
    """

    content_updates: typing.List[UpdatePageMarkdownRequestUpdateContentContentUpdatesItem] = pydantic.Field()
    """
    Up to 100 find-and-replace edits applied in order.
    """

    allow_deleting_content: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Permit deletion of existing child pages/databases removed by the edits.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
