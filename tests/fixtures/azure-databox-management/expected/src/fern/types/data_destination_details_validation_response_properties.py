

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .data_destination_details_validation_response_properties_status import (
    DataDestinationDetailsValidationResponsePropertiesStatus,
)
from .validation_input_response import ValidationInputResponse


class DataDestinationDetailsValidationResponseProperties(ValidationInputResponse):
    """
    Properties of data destination details validation response.
    """

    status: typing.Optional[DataDestinationDetailsValidationResponsePropertiesStatus] = pydantic.Field(default=None)
    """
    Data destination details validation status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
