

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .box import Box
from .range import Range


class Grounding(UniversalBaseModel):
    """
    Where a node lives: its page, its slice of `markdown`, and its box.

    The same shape is used for page nodes, element nodes, and each
    `atomic_grounding` entry, so any grounding object is self-contained — it
    can be lifted out of the tree and still locates its content.
    """

    page: int = pydantic.Field()
    """
    1-indexed page number this grounding is on. On a page node, the page's own number.
    """

    range: Range = pydantic.Field()
    """
    `[start, end)` offsets into the top-level `markdown` string covered by this node or segment.
    """

    box: Box = pydantic.Field()
    """
    Bounding box in normalized page coordinates (`0`–`1` fractions of page width/height, at most 8 decimal places). A page node's box is always the full page `{0, 0, 1, 1}`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
