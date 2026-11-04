

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reader_checkout_status_change_payload_status import ReaderCheckoutStatusChangePayloadStatus


class ReaderCheckoutStatusChangePayload(UniversalBaseModel):
    """
    The event payload.
    """

    client_transaction_id: str = pydantic.Field()
    """
    The unique client transaction id. It is the same returned by the Checkout.
    """

    merchant_code: str = pydantic.Field()
    """
    The merchant code associated with the transaction.
    """

    status: ReaderCheckoutStatusChangePayloadStatus = pydantic.Field()
    """
    The current status of the transaction.
    """

    transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The transaction id. Deprecated: use `client_transaction_id` instead.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
