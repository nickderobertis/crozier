

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_page_markdown_request_insert_content_position import UpdatePageMarkdownRequestInsertContentPosition


class UpdatePageMarkdownRequestInsertContent(UniversalBaseModel):
    """
    Deprecated. Provide when type is `insert_content`. Inserts Markdown at a position.
    """

    content: str = pydantic.Field()
    """
    Enhanced Markdown to insert.
    """

    after: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ellipsis-format selection ("start text...end text") to insert after. Cannot be combined with position.
    """

    position: typing.Optional[UpdatePageMarkdownRequestInsertContentPosition] = pydantic.Field(default=None)
    """
    Insert at the start or end of the page. Cannot be combined with after.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
