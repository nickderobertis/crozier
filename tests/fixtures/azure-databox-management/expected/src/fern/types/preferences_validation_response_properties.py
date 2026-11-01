

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .preferences_validation_response_properties_status import PreferencesValidationResponsePropertiesStatus
from .validation_input_response import ValidationInputResponse


class PreferencesValidationResponseProperties(ValidationInputResponse):
    """
    Properties of data center and transport preference validation response.
    """

    status: typing.Optional[PreferencesValidationResponsePropertiesStatus] = pydantic.Field(default=None)
    """
    Validation status of requested data center and transport.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
