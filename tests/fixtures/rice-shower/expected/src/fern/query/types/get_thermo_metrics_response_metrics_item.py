

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_thermo_metrics_response_metrics_item_channels_item import GetThermoMetricsResponseMetricsItemChannelsItem


class GetThermoMetricsResponseMetricsItem(UniversalBaseModel):
    time: dt.datetime = pydantic.Field()
    """
    Timestamp of the metric
    """

    channels: typing.List[GetThermoMetricsResponseMetricsItemChannelsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
