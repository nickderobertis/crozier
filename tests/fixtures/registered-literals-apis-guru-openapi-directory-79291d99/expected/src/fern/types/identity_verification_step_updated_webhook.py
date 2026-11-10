

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_environment_values import WebhookEnvironmentValues


class IdentityVerificationStepUpdatedWebhook(UniversalBaseModel):
    """
    Fired when an end user has completed a step of the Identity Verification process.
    """

    environment: WebhookEnvironmentValues
    identity_verification_id: str = pydantic.Field()
    """
    The ID of the associated Identity Verification attempt.
    """

    webhook_code: str = pydantic.Field()
    """
    `STEP_UPDATED`
    """

    webhook_type: str = pydantic.Field()
    """
    `IDENTITY_VERIFICATION`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
