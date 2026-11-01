

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdatePageMarkdownRequestReplaceContent(UniversalBaseModel):
    """
    Provide when type is `replace_content`. Replaces the entire page content.
    """

    new_str: str = pydantic.Field()
    """
    The complete new page content as enhanced Markdown.
    """

    allow_deleting_content: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Permit deletion of existing child pages/databases that are no longer present in the new content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
