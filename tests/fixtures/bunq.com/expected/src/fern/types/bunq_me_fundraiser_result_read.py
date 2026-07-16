

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .bunq_me_fundraiser_profile import BunqMeFundraiserProfile


class BunqMeFundraiserResultRead(UniversalBaseModel):
    bunqme_fundraiser_profile: typing.Optional[BunqMeFundraiserProfile] = pydantic.Field(default=None)
    """
    The bunq.me fundraiser profile.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the bunq.me was created.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the bunq.me.
    """

    payments: typing.Optional[typing.List["Payment"]] = pydantic.Field(default=None)
    """
    The list of payments, paid to the bunq.me fundraiser profile.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the bunq.me was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .payment import Payment
from .payment_auto_allocate_instance import PaymentAutoAllocateInstance
from .payment_batch import PaymentBatch
from .payment_batch_anchored_payment import PaymentBatchAnchoredPayment

update_forward_refs(
    BunqMeFundraiserResultRead,
    Payment=Payment,
    PaymentAutoAllocateInstance=PaymentAutoAllocateInstance,
    PaymentBatch=PaymentBatch,
    PaymentBatchAnchoredPayment=PaymentBatchAnchoredPayment,
)
