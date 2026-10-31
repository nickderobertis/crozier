

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .sku_availability_validation_response_properties_status import SkuAvailabilityValidationResponsePropertiesStatus
from .validation_input_response import ValidationInputResponse


class SkuAvailabilityValidationResponseProperties(ValidationInputResponse):
    """
    Properties of sku availability validation response.
    """

    status: typing.Optional[SkuAvailabilityValidationResponsePropertiesStatus] = pydantic.Field(default=None)
    """
    Sku availability validation status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
