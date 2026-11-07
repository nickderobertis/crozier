

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Chart_Donut(UniversalBaseModel):
    """
    The type of chart to render.
    """

    type: typing.Literal["donut"] = "donut"
    chart_title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Chart_TimeseriesLine(UniversalBaseModel):
    """
    The type of chart to render.
    """

    type: typing.Literal["timeseries_line"] = "timeseries_line"
    chart_title: typing.Optional[str] = None
    stacked: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Chart_TimeseriesBar(UniversalBaseModel):
    """
    The type of chart to render.
    """

    type: typing.Literal["timeseries_bar"] = "timeseries_bar"
    chart_title: typing.Optional[str] = None
    stacked: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Chart_HorizontalBar(UniversalBaseModel):
    """
    The type of chart to render.
    """

    type: typing.Literal["horizontal_bar"] = "horizontal_bar"
    chart_title: typing.Optional[str] = None
    stacked: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Chart_VerticalBar(UniversalBaseModel):
    """
    The type of chart to render.
    """

    type: typing.Literal["vertical_bar"] = "vertical_bar"
    chart_title: typing.Optional[str] = None
    stacked: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Chart_SingleValue(UniversalBaseModel):
    """
    The type of chart to render.
    """

    type: typing.Literal["single_value"] = "single_value"
    chart_title: typing.Optional[str] = None
    decimal_points: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Chart = typing_extensions.Annotated[
    typing.Union[
        Chart_Donut,
        Chart_TimeseriesLine,
        Chart_TimeseriesBar,
        Chart_HorizontalBar,
        Chart_VerticalBar,
        Chart_SingleValue,
    ],
    pydantic.Field(discriminator="type"),
]
