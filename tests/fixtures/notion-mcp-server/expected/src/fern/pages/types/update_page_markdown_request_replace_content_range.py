

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdatePageMarkdownRequestReplaceContentRange(UniversalBaseModel):
    """
    Deprecated. Provide when type is `replace_content_range`. Replaces a selected range of Markdown.
    """

    content: str = pydantic.Field()
    """
    New Markdown content for the range.
    """

    content_range: str = pydantic.Field()
    """
    Ellipsis-format selection ("start text...end text") identifying the range to replace.
    """

    allow_deleting_content: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Permit deletion of child pages/databases within the replaced range.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
