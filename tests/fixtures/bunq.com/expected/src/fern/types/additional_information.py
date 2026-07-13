

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attachment_master_card_action_refund import AttachmentMasterCardActionRefund


class AdditionalInformation(UniversalBaseModel):
    attachment: typing.Optional[typing.List[AttachmentMasterCardActionRefund]] = pydantic.Field(default=None)
    """
    The Attachments to attach to the refund request.
    """

    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    The category of the refund, required for chargeback.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comment about the refund.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason to refund, required for chargeback.
    """

    terms_and_conditions: typing.Optional[str] = pydantic.Field(default=None)
    """
    Proof that the user acknowledged the terms and conditions for chargebacks.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
