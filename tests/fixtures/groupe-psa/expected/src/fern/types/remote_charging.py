

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote_charging_preferences import RemoteChargingPreferences
from .remote_charging_schedule import RemoteChargingSchedule


class RemoteCharging(UniversalBaseModel):
    """
    Remote electric battery charging action.

    - ```preferences``` cannot be used in the same remote than ```schedule``` and/or ```immediate```
    """

    next_delayed_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextDelayedTime"),
        pydantic.Field(
            alias="nextDelayedTime",
            description="(!Depricated; use schedule instead)  Timestamp (as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)) of the next battery charging time.",
        ),
    ] = None
    """
    (!Depricated; use schedule instead)  Timestamp (as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)) of the next battery charging time.
    """

    schedule: typing.Optional[RemoteChargingSchedule] = pydantic.Field(default=None)
    """
    Charge scheduling. Only one of the two modes, programs or nexDelayedTime, should be provided.
    """

    immediate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines if the charging will start immediately(```True```) or not.
    """

    preferences: typing.Optional[RemoteChargingPreferences] = pydantic.Field(default=None)
    """
    Set the charging preferences.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
