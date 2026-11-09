

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_id import UserId
from .webhook_environment_values import WebhookEnvironmentValues


class IncomeVerificationStatusWebhook(UniversalBaseModel):
    """
    Fired when the status of an income verification instance has changed. It will typically take several minutes for this webhook to fire after the end user has uploaded their documents in the Document Income flow.
    """

    environment: WebhookEnvironmentValues
    item_id: str = pydantic.Field()
    """
    The Item ID associated with the verification.
    """

    user_id: typing.Optional[UserId] = None
    verification_status: str = pydantic.Field()
    """
    `VERIFICATION_STATUS_PROCESSING_COMPLETE`: The income verification status processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the `/income/verification/paystubs/get` endpoint and check the document metadata to see which documents were successfully parsed.
    
    `VERIFICATION_STATUS_PROCESSING_FAILED`: A failure occurred when attempting to process the verification documentation.
    
    `VERIFICATION_STATUS_PENDING_APPROVAL`: (deprecated) The income verification has been sent to the user for review.
    """

    webhook_code: str = pydantic.Field()
    """
    `INCOME_VERIFICATION`
    """

    webhook_type: str = pydantic.Field()
    """
    `"INCOME"`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
