

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .create_order_limit_for_subscription_validation_response_properties_status import (
    CreateOrderLimitForSubscriptionValidationResponsePropertiesStatus,
)
from .validation_input_response import ValidationInputResponse


class CreateOrderLimitForSubscriptionValidationResponseProperties(ValidationInputResponse):
    """
    Properties of create order limit for subscription validation response.
    """

    status: typing.Optional[CreateOrderLimitForSubscriptionValidationResponsePropertiesStatus] = pydantic.Field(
        default=None
    )
    """
    Create order limit validation status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
