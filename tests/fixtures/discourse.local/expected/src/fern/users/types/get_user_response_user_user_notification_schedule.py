

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetUserResponseUserUserNotificationSchedule(UniversalBaseModel):
    day0end_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_0_end_time"), pydantic.Field(alias="day_0_end_time")
    ]
    day0start_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_0_start_time"), pydantic.Field(alias="day_0_start_time")
    ]
    day1end_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_1_end_time"), pydantic.Field(alias="day_1_end_time")
    ]
    day1start_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_1_start_time"), pydantic.Field(alias="day_1_start_time")
    ]
    day2end_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_2_end_time"), pydantic.Field(alias="day_2_end_time")
    ]
    day2start_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_2_start_time"), pydantic.Field(alias="day_2_start_time")
    ]
    day3end_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_3_end_time"), pydantic.Field(alias="day_3_end_time")
    ]
    day3start_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_3_start_time"), pydantic.Field(alias="day_3_start_time")
    ]
    day4end_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_4_end_time"), pydantic.Field(alias="day_4_end_time")
    ]
    day4start_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_4_start_time"), pydantic.Field(alias="day_4_start_time")
    ]
    day5end_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_5_end_time"), pydantic.Field(alias="day_5_end_time")
    ]
    day5start_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_5_start_time"), pydantic.Field(alias="day_5_start_time")
    ]
    day6end_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_6_end_time"), pydantic.Field(alias="day_6_end_time")
    ]
    day6start_time: typing_extensions.Annotated[
        int, FieldMetadata(alias="day_6_start_time"), pydantic.Field(alias="day_6_start_time")
    ]
    enabled: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
