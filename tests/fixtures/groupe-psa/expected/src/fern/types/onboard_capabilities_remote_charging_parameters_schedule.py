

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .onboard_capabilities_remote_charging_parameters_schedule_programs import (
    OnboardCapabilitiesRemoteChargingParametersSchedulePrograms,
)


class OnboardCapabilitiesRemoteChargingParametersSchedule(UniversalBaseModel):
    programs: OnboardCapabilitiesRemoteChargingParametersSchedulePrograms
    next_delayed_time: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="nextDelayedTime"),
        pydantic.Field(
            alias="nextDelayedTime", description="true means remote charging schedule[nextDelayedTime] is supported."
        ),
    ]
    """
    true means remote charging schedule[nextDelayedTime] is supported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
