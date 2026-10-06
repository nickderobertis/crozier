

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DataSetWindow(UniversalBaseModel):
    """
    Data Window.

    Statistics of the time axis of a data set.
    Present with render option `include_window_spec=true`.",
    """

    until: int = pydantic.Field()
    """
    Exclusive higher bound of the time axis in unix epoch milliseconds.
    """

    window: str = pydantic.Field()
    """
    Time axis length as ISO8601 period.
    """

    freq: str = pydantic.Field()
    """
    Time axis aggregation interval as an ISO8601 period .
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
