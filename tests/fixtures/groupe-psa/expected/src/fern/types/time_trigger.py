

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .time_trigger_entry import TimeTriggerEntry


class TimeTrigger(UniversalBaseModel):
    """
    Temporal monitor for triggering vehicle moving event within a time interval.
    """

    times: typing.List[TimeTriggerEntry]
    time_zone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="timeZone"),
        pydantic.Field(
            alias="timeZone",
            description="The standard time [zone code](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the region where to apply this time trigger monitor. This allows to adapt this trigger to the time change according to local (region/country) criteria/rules.",
        ),
    ] = None
    """
    The standard time [zone code](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the region where to apply this time trigger monitor. This allows to adapt this trigger to the time change according to local (region/country) criteria/rules.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
