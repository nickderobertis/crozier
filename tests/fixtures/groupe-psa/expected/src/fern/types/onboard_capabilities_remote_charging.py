

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .onboard_capabilities_remote_charging_parameters import OnboardCapabilitiesRemoteChargingParameters
from .onboard_capabilities_remote_charging_scope_name import OnboardCapabilitiesRemoteChargingScopeName


class OnboardCapabilitiesRemoteCharging(UniversalBaseModel):
    supported: bool = pydantic.Field()
    """
    true means remote charging is supported.
    """

    scope_name: typing_extensions.Annotated[
        OnboardCapabilitiesRemoteChargingScopeName, FieldMetadata(alias="scopeName"), pydantic.Field(alias="scopeName")
    ]
    parameters: OnboardCapabilitiesRemoteChargingParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
