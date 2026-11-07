

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SingleValueChart(UniversalBaseModel):
    """
    A chart that can render a single number.  This chart works with a single metric and no dimensions.
    """

    chart_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the chart, which is displayed in the tile's header.
    """

    decimal_points: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of figures to render after the decimal.  Most metrics only support up to 2 decimals, but some may support more.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
