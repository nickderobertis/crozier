

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartLabOrdersOrderIdScheduleRequest(UniversalBaseModel):
    schedule_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="ScheduleType"), pydantic.Field(alias="ScheduleType")
    ]
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="StartDate"), pydantic.Field(alias="StartDate")]
    end_date: typing_extensions.Annotated[str, FieldMetadata(alias="EndDate"), pydantic.Field(alias="EndDate")]
    interval: typing_extensions.Annotated[str, FieldMetadata(alias="Interval"), pydantic.Field(alias="Interval")]
    interval_mode: typing_extensions.Annotated[
        str, FieldMetadata(alias="IntervalMode"), pydantic.Field(alias="IntervalMode")
    ]
    is_auto_releasable: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsAutoReleasable"), pydantic.Field(alias="IsAutoReleasable")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
