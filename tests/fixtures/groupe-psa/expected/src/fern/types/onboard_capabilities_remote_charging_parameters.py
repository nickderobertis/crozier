

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .onboard_capabilities_remote_charging_parameters_immediate import (
    OnboardCapabilitiesRemoteChargingParametersImmediate,
)
from .onboard_capabilities_remote_charging_parameters_preferences import (
    OnboardCapabilitiesRemoteChargingParametersPreferences,
)
from .onboard_capabilities_remote_charging_parameters_schedule import (
    OnboardCapabilitiesRemoteChargingParametersSchedule,
)


class OnboardCapabilitiesRemoteChargingParameters(UniversalBaseModel):
    immediate: typing.Optional[OnboardCapabilitiesRemoteChargingParametersImmediate] = None
    schedule: typing.Optional[OnboardCapabilitiesRemoteChargingParametersSchedule] = None
    preferences: typing.Optional[OnboardCapabilitiesRemoteChargingParametersPreferences] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
