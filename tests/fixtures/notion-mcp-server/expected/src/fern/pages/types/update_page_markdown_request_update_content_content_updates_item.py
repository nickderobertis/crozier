

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdatePageMarkdownRequestUpdateContentContentUpdatesItem(UniversalBaseModel):
    old_str: str = pydantic.Field()
    """
    Exact existing Markdown text to find.
    """

    new_str: str = pydantic.Field()
    """
    Replacement Markdown text.
    """

    replace_all_matches: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Replace every occurrence of old_str instead of just the first (default false).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
