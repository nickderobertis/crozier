

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .draft_payment_entry import DraftPaymentEntry
from .schedule import Schedule


class DraftPayment(UniversalBaseModel):
    entries: typing.List[DraftPaymentEntry] = pydantic.Field()
    """
    The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.
    """

    number_of_required_accepts: int = pydantic.Field()
    """
    The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.
    """

    previous_updated_timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.
    """

    schedule: typing.Optional[Schedule] = pydantic.Field(default=None)
    """
    The schedule details when creating or updating a scheduled payment.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the DraftPayment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DraftPayment)
