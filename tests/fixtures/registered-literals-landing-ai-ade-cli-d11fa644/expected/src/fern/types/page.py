

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .grounding import Grounding
from .page_status import PageStatus
from .page_type import PageType


class Page(UniversalBaseModel):
    type: typing.Optional[PageType] = pydantic.Field(default=None)
    """
    The node type. Identifies this node as a page in the structure tree.
    """

    grounding: Grounding = pydantic.Field()
    """
    The page's spatial data: `page` is the 1-indexed page number in the source document (not contiguous when `options.pages` filters out some pages); `range` covers this page's content in the top-level `markdown` string (zero-length `start == end` for failed pages); `box` is always the full page `{0, 0, 1, 1}`.
    """

    status: typing.Optional[PageStatus] = pydantic.Field(default=None)
    """
    Whether this page was parsed successfully (`ok`) or failed (`failed`).
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Failure reason. Present only when `status` is `failed`.
    """

    children: typing.Optional[typing.List["Element"]] = pydantic.Field(default=None)
    """
    The elements detected on this page, in reading order. Empty for failed pages.
    """

    markdown: typing.Optional[str] = pydantic.Field(default=None)
    """
    This page's slice of the top-level `markdown` string (`markdown[grounding.range.start:grounding.range.end]`). `""` for failed pages. Present only when `options.inline_markdown` is `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .element import Element

update_forward_refs(Page, Element=Element)
