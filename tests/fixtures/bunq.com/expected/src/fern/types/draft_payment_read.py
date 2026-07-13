

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .draft_payment_anchor_object import DraftPaymentAnchorObject
from .draft_payment_entry import DraftPaymentEntry
from .draft_payment_response import DraftPaymentResponse
from .label_user import LabelUser
from .request_inquiry_reference import RequestInquiryReference
from .schedule import Schedule


class DraftPaymentRead(UniversalBaseModel):
    entries: typing.Optional[typing.List[DraftPaymentEntry]] = pydantic.Field(default=None)
    """
    The entries in the DraftPayment.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the created DrafPayment.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the MonetaryAccount the DraftPayment applies to.
    """

    object: typing.Optional[DraftPaymentAnchorObject] = pydantic.Field(default=None)
    """
    The Payment or PaymentBatch. This will only be present after the DraftPayment has been accepted.
    """

    request_reference_split_the_bill: typing.Optional[typing.List[RequestInquiryReference]] = pydantic.Field(
        default=None
    )
    """
    The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch
    """

    responses: typing.Optional[typing.List[DraftPaymentResponse]] = pydantic.Field(default=None)
    """
    All responses to this draft payment.
    """

    schedule: typing.Optional[Schedule] = pydantic.Field(default=None)
    """
    The schedule details.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the DraftPayment.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the DraftPayment.
    """

    user_alias_created: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The label of the User who created the DraftPayment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DraftPaymentRead)
