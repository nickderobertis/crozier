

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .onboard_capabilities_remote_charging import OnboardCapabilitiesRemoteCharging
from .onboard_capabilities_remote_door import OnboardCapabilitiesRemoteDoor
from .onboard_capabilities_remote_horn import OnboardCapabilitiesRemoteHorn
from .onboard_capabilities_remote_lights import OnboardCapabilitiesRemoteLights
from .onboard_capabilities_remote_navigation import OnboardCapabilitiesRemoteNavigation
from .onboard_capabilities_remote_preconditioning import OnboardCapabilitiesRemotePreconditioning
from .onboard_capabilities_remote_stolen import OnboardCapabilitiesRemoteStolen
from .onboard_capabilities_remote_wakeup import OnboardCapabilitiesRemoteWakeup


class OnboardCapabilitiesRemote(UniversalBaseModel):
    """
    List of callable remote functions and associated supported properties.
    """

    preconditioning: OnboardCapabilitiesRemotePreconditioning
    charging: OnboardCapabilitiesRemoteCharging
    door: OnboardCapabilitiesRemoteDoor
    horn: OnboardCapabilitiesRemoteHorn
    lights: OnboardCapabilitiesRemoteLights
    wakeup: OnboardCapabilitiesRemoteWakeup
    navigation: OnboardCapabilitiesRemoteNavigation
    stolen: OnboardCapabilitiesRemoteStolen

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
