

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class MonitorDataMetricsResponse(UniversalBaseModel):
    recent1day_avg: typing_extensions.Annotated[
        float, FieldMetadata(alias="recent1DayAvg"), pydantic.Field(alias="recent1DayAvg")
    ]
    recent1day_online_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="recent1DayOnlineCount"), pydantic.Field(alias="recent1DayOnlineCount")
    ]
    recent1day_offline_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="recent1DayOfflineCount"), pydantic.Field(alias="recent1DayOfflineCount")
    ]
    recent30day_online_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="recent30DayOnlineCount"), pydantic.Field(alias="recent30DayOnlineCount")
    ]
    recent30day_offline_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="recent30DayOfflineCount"), pydantic.Field(alias="recent30DayOfflineCount")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
