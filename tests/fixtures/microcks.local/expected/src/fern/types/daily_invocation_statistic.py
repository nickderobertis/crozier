

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DailyInvocationStatistic(UniversalBaseModel):
    """
    The daily statistic of a service mock invocations
    """

    daily_count: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="dailyCount"),
        pydantic.Field(alias="dailyCount", description="The number of service mock invocations on this day"),
    ]
    """
    The number of service mock invocations on this day
    """

    day: str = pydantic.Field()
    """
    The day (formatted as yyyyMMdd string) represented by this statistic
    """

    hourly_count: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="hourlyCount"),
        pydantic.Field(
            alias="hourlyCount",
            description="The number of service mock invocations per hour of the day (keys range from 0 to 23)",
        ),
    ] = None
    """
    The number of service mock invocations per hour of the day (keys range from 0 to 23)
    """

    id: str = pydantic.Field()
    """
    Unique identifier of this statistic object
    """

    minute_count: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="minuteCount"),
        pydantic.Field(
            alias="minuteCount",
            description="The number of service mock invocations per minute of the day (keys range from 0 to 1439)",
        ),
    ] = None
    """
    The number of service mock invocations per minute of the day (keys range from 0 to 1439)
    """

    service_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceName"),
        pydantic.Field(alias="serviceName", description="The name of the service this statistic is related to"),
    ]
    """
    The name of the service this statistic is related to
    """

    service_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceVersion"),
        pydantic.Field(alias="serviceVersion", description="The version of the service this statistic is related to"),
    ]
    """
    The version of the service this statistic is related to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
