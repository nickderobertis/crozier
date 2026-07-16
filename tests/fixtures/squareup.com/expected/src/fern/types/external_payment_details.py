

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class ExternalPaymentDetails(UniversalBaseModel):
    """
    Stores details about an external payment. Contains only non-confidential information.
    For more information, see
    [Take External Payments](https://developer.squareup.com/docs/payments-api/take-payments/external-payments).
    """

    source: str = pydantic.Field()
    """
    A description of the external payment source. For example, 
    "Food Delivery Service".
    """

    source_fee_money: typing.Optional[Money] = None
    source_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An ID to associate the payment to its originating source.
    """

    type: str = pydantic.Field()
    """
    The type of external payment the seller received. It can be one of the following:
    - CHECK - Paid using a physical check.
    - BANK_TRANSFER - Paid using external bank transfer.
    - OTHER\\_GIFT\\_CARD - Paid using a non-Square gift card.
    - CRYPTO - Paid using a crypto currency.
    - SQUARE_CASH - Paid using Square Cash App.
    - SOCIAL - Paid using peer-to-peer payment applications.
    - EXTERNAL - A third-party application gathered this payment outside of Square.
    - EMONEY - Paid using an E-money provider.
    - CARD - A credit or debit card that Square does not support.
    - STORED_BALANCE - Use for house accounts, store credit, and so forth.
    - FOOD_VOUCHER - Restaurant voucher provided by employers to employees to pay for meals
    - OTHER - A type not listed here.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
