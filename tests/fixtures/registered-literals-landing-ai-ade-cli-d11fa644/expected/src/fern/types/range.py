

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Range(UniversalBaseModel):
    """
    A `[start, end)` slice of the top-level `markdown` string.
    """

    start: int = pydantic.Field()
    """
    Inclusive start offset into the top-level `markdown` string, in the units declared by `metadata.range_units` (Unicode code points).
    """

    end: int = pydantic.Field()
    """
    Exclusive end offset into the top-level `markdown` string, in the units declared by `metadata.range_units` (Unicode code points).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
