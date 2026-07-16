

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dispute_evidence_created_webhook_object import DisputeEvidenceCreatedWebhookObject


class DisputeEvidenceCreatedWebhookData(UniversalBaseModel):
    """ """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the affected dispute.
    """

    object: typing.Optional[DisputeEvidenceCreatedWebhookObject] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the affected dispute's type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
