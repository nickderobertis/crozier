

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .align_at import AlignAt
from .align_shift import AlignShift


class Alignment(UniversalBaseModel):
    """
    Aggregation Alignment Options.

    Specifies how the aggregation grid is aligned.
    """

    at: typing.Optional[AlignAt] = pydantic.Field(default=None)
    """
    Method used to align the aggregation grid. The default value is system-dependent (normally `grid`)
    """

    shift: typing.Optional[AlignShift] = pydantic.Field(default=None)
    """
    
    Specifies in what direction the query window is shifted
    to match the alignment specification.
    When not specified, defaults are:
    - `backward` when only the `from` boundary is specified.
    - `forward` when only the `until` boundary is specified.
    - `wrap` otherwise (_none_ or _both_ boundaries specified).
    """

    freq: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    Defines the grid used to align the aggregation window.
    The window will align at whole-unit multiples of this interval.
    
    For intervals like `PT1D`, that are timezone-dependent, use the 
    `align.timezone` to fix the absolute timestamp of the grid boundaries.
    
    If not specified, defaults to the `freq` aggregation interval.
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    The timezone to use when shifting boundaries, especially
    at day granularity.
    Also affects the rendering of timestamps when
    `render.iso_timestamp` is enabled.
    
    When not specified, the `UTC` timezone is used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
