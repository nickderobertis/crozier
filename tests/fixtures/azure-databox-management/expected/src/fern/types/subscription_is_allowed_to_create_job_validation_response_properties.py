

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .subscription_is_allowed_to_create_job_validation_response_properties_status import (
    SubscriptionIsAllowedToCreateJobValidationResponsePropertiesStatus,
)
from .validation_input_response import ValidationInputResponse


class SubscriptionIsAllowedToCreateJobValidationResponseProperties(ValidationInputResponse):
    """
    Properties of subscription permission to create job validation response.
    """

    status: typing.Optional[SubscriptionIsAllowedToCreateJobValidationResponsePropertiesStatus] = pydantic.Field(
        default=None
    )
    """
    Validation status of subscription permission to create job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
