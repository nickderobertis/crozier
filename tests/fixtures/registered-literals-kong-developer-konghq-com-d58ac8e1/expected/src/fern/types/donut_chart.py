

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DonutChart(UniversalBaseModel):
    """
    A chart that can display one-dimensional data in a hollow, segmented circle.  To use this chart, ensure that
    the query includes only one dimension (not `time`).
    """

    chart_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the chart, which is displayed in the tile's header.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
