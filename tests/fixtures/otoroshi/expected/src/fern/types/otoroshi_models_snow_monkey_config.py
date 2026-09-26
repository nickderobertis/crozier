

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiModelsSnowMonkeyConfig(UniversalBaseModel):
    """
    Settings for the snow monkey (chaos engineering)
    """

    dry_run: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="dryRun"),
        pydantic.Field(alias="dryRun", description="Whether or not outages will actualy impact requests"),
    ] = None
    """
    Whether or not outages will actualy impact requests
    """

    outage_duration_to: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="outageDurationTo"),
        pydantic.Field(alias="outageDurationTo", description="End of outage duration range"),
    ] = None
    """
    End of outage duration range
    """

    chaos_config: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="chaosConfig"), pydantic.Field(alias="chaosConfig")
    ] = None
    times_per_day: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="timesPerDay"),
        pydantic.Field(alias="timesPerDay", description="Number of time per day each service will be outage"),
    ] = None
    """
    Number of time per day each service will be outage
    """

    outage_duration_from: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="outageDurationFrom"),
        pydantic.Field(alias="outageDurationFrom", description="Start of outage duration range"),
    ] = None
    """
    Start of outage duration range
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="Start time of Snow Monkey each day"),
    ] = None
    """
    Start time of Snow Monkey each day
    """

    include_user_facing_descriptors: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="includeUserFacingDescriptors"),
        pydantic.Field(
            alias="includeUserFacingDescriptors",
            description="Whether or not user facing apps. will be impacted by Snow Monkey",
        ),
    ] = None
    """
    Whether or not user facing apps. will be impacted by Snow Monkey
    """

    target_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="targetGroups"),
        pydantic.Field(
            alias="targetGroups", description="Groups impacted by Snow Monkey. If empty, all groups will be impacted"
        ),
    ] = None
    """
    Groups impacted by Snow Monkey. If empty, all groups will be impacted
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this config is enabled
    """

    stop_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="stopTime"),
        pydantic.Field(alias="stopTime", description="Stop time of Snow Monkey each day"),
    ] = None
    """
    Stop time of Snow Monkey each day
    """

    outage_strategy: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="outageStrategy"), pydantic.Field(alias="outageStrategy")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
