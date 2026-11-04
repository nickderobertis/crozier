

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Highlight(UniversalBaseModel):
    """
    Specifies the number and size of fragments (snippets, summaries) to generate from each specified field to provide a "keyword in context" (KWIC) functionality.
    With highlight_markup the matching query terms within the fragments can be highlighted with HTML markup.
    """

    field: str = pydantic.Field()
    """
    Specifies the field from which the fragments  (snippets, summaries) are created.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Allows to specifiy multiple highlight result fields from the same source field, leaving the original field intact,
    Default: if name is empty then field is used instead, i.e the original field is overwritten with the highlight.
    """

    fragment_number: typing.Optional[int] = pydantic.Field(default=None)
    """
    If 0/default then return the full original text without fragmenting.
    """

    fragment_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Specifies the length of a highlight fragment.
    The default 0 returns the full original text without truncating, but still with highlighting if highlight_markup is enabled.
    """

    highlight_markup: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if true, the matching query terms within the fragments are highlighted with HTML markup **\\<b\\>term\\<\\/b\\>**.
    """

    pre_tags: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the markup tags to insert **before** each highlighted term (e.g. \\"\\<b\\>\\" or \\"\\<em\\>\\"). This can be any string, but is most often an HTML or XML tag.
    Only used when **highlight_markup** is set to true.
    """

    post_tags: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the markup tags to insert **after** each highlighted term. (e.g. \\"\\<\\/b\\>\\" or \\"\\<\\/em\\>\\"). This can be any string, but is most often an HTML or XML tag.
    Only used when **highlight_markup** is set to true.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
