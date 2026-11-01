

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdatePageMarkdownResponse(UniversalBaseModel):
    object: typing.Optional[str] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the page or block.
    """

    markdown: typing.Optional[str] = pydantic.Field(default=None)
    """
    Page content rendered as enhanced Markdown.
    """

    truncated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if content was truncated because the page exceeds the block limit.
    """

    unknown_block_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Block IDs that could not be rendered (e.g. due to permissions or truncation). Pass them back to this endpoint to fetch them individually.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
