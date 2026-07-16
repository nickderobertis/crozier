

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dispute_evidence_created_webhook_data import DisputeEvidenceCreatedWebhookData


class DisputeEvidenceCreatedWebhook(UniversalBaseModel):
    """
    Published when evidence is added to a [Dispute](https://developer.squareup.com/reference/square_2021-08-18/objects/Dispute)
    from the Disputes Dashboard in the Seller Dashboard, the Square Point of Sale app,
    or by calling either [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) or [CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text).
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timestamp of when the webhook event was created, in RFC 3339 format.
    """

    data: typing.Optional[DisputeEvidenceCreatedWebhookData] = None
    event_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID for the webhook event.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the target location associated with the event.
    """

    merchant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the target merchant associated with the event.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of event this represents.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
