

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaymentMeta(UniversalBaseModel):
    """
    Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.

    If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
    """

    by_order_of: typing.Optional[str] = pydantic.Field(default=None)
    """
    The party initiating a wire transfer. Will be `null` if the transaction is not a wire transfer.
    """

    payee: typing.Optional[str] = pydantic.Field(default=None)
    """
    For transfers, the party that is receiving the transaction.
    """

    payer: typing.Optional[str] = pydantic.Field(default=None)
    """
    For transfers, the party that is paying the transaction.
    """

    payment_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of transfer, e.g. 'ACH'
    """

    payment_processor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the payment processor
    """

    ppd_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ACH PPD ID for the payer.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The payer-supplied description of the transfer.
    """

    reference_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The transaction reference number supplied by the financial institution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
