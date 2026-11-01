

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .preferences import Preferences
from .preferences_validation_request_device_type import PreferencesValidationRequestDeviceType
from .validation_input_request import ValidationInputRequest


class PreferencesValidationRequest(ValidationInputRequest):
    """
    Request to validate preference of transport and data center.
    """

    device_type: typing_extensions.Annotated[
        PreferencesValidationRequestDeviceType,
        FieldMetadata(alias="deviceType"),
        pydantic.Field(alias="deviceType", description="Device type to be used for the job."),
    ]
    """
    Device type to be used for the job.
    """

    preference: typing.Optional[Preferences] = pydantic.Field(default=None)
    """
    Preference requested with respect to transport type and data center
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
