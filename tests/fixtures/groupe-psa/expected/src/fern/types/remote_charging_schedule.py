

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote_charging_schedule_programs_item import RemoteChargingScheduleProgramsItem


class RemoteChargingSchedule(UniversalBaseModel):
    """
    Charge scheduling. Only one of the two modes, programs or nexDelayedTime, should be provided.
    """

    next_delayed_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextDelayedTime"),
        pydantic.Field(
            alias="nextDelayedTime",
            description="Timestamp (as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)) of the next battery charging time.",
        ),
    ] = None
    """
    Timestamp (as defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)) of the next battery charging time.
    """

    programs: typing.Optional[typing.List[RemoteChargingScheduleProgramsItem]] = pydantic.Field(default=None)
    """
    Scheduled charging programs list.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
