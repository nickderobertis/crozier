

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chaos_config import ChaosConfig
from .outage_strategy import OutageStrategy


class SnowMonkeyConfig(UniversalBaseModel):
    """
    Configuration for the faults that can be injected in requests. The name Snow Monkey is an hommage to Netflix's Chaos Monkey 😉
    """

    chaos_config: typing_extensions.Annotated[ChaosConfig, FieldMetadata(alias="chaosConfig")]
    dry_run: typing_extensions.Annotated[bool, FieldMetadata(alias="dryRun")] = pydantic.Field()
    """
    Whether or not outages will actualy impact requests
    """

    enabled: bool = pydantic.Field()
    """
    Whether or not this config is enabled
    """

    include_user_facing_descriptors: typing_extensions.Annotated[
        bool, FieldMetadata(alias="includeUserFacingDescriptors")
    ] = pydantic.Field()
    """
    Whether or not user facing apps. will be impacted by Snow Monkey
    """

    outage_duration_from: typing_extensions.Annotated[int, FieldMetadata(alias="outageDurationFrom")] = pydantic.Field()
    """
    Start of outage duration range
    """

    outage_duration_to: typing_extensions.Annotated[int, FieldMetadata(alias="outageDurationTo")] = pydantic.Field()
    """
    End of outage duration range
    """

    outage_strategy: typing_extensions.Annotated[OutageStrategy, FieldMetadata(alias="outageStrategy")] = (
        pydantic.Field()
    )
    """
    
    """

    start_time: typing_extensions.Annotated[str, FieldMetadata(alias="startTime")] = pydantic.Field()
    """
    Start time of Snow Monkey each day
    """

    stop_time: typing_extensions.Annotated[str, FieldMetadata(alias="stopTime")] = pydantic.Field()
    """
    Stop time of Snow Monkey each day
    """

    target_groups: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="targetGroups")] = pydantic.Field()
    """
    Groups impacted by Snow Monkey. If empty, all groups will be impacted
    """

    times_per_day: typing_extensions.Annotated[int, FieldMetadata(alias="timesPerDay")] = pydantic.Field()
    """
    Number of time per day each service will be outage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
