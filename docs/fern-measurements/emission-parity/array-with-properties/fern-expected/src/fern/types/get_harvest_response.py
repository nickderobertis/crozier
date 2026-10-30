

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_harvest_response_plot import GetHarvestResponsePlot
from .get_harvest_response_weather import GetHarvestResponseWeather


class GetHarvestResponse(UniversalBaseModel):
    crates: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Crates filled, each one an object.
    """

    pickers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Pickers, declared with string items beside properties.
    """

    rows: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Rows walked, declared without items.
    """

    weather: typing.Optional[GetHarvestResponseWeather] = pydantic.Field(default=None)
    """
    No declared type, empty items and properties.
    """

    plot: typing.Optional[GetHarvestResponsePlot] = pydantic.Field(default=None)
    """
    A plain inline object beside them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
