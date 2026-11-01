

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .create_order_limit_for_subscription_validation_request_device_type import (
    CreateOrderLimitForSubscriptionValidationRequestDeviceType,
)
from .validation_input_request import ValidationInputRequest


class CreateOrderLimitForSubscriptionValidationRequest(ValidationInputRequest):
    """
    Request to validate create order limit for current subscription.
    """

    device_type: typing_extensions.Annotated[
        CreateOrderLimitForSubscriptionValidationRequestDeviceType,
        FieldMetadata(alias="deviceType"),
        pydantic.Field(alias="deviceType", description="Device type to be used for the job."),
    ]
    """
    Device type to be used for the job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
