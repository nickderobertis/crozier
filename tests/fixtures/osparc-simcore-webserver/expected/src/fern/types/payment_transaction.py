

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .payment_transaction_completed_status import PaymentTransactionCompletedStatus
from .wallet_id_int import WalletIdInt


class PaymentTransaction(UniversalBaseModel):
    payment_id: typing_extensions.Annotated[str, FieldMetadata(alias="paymentId"), pydantic.Field(alias="paymentId")]
    price_dollars: typing_extensions.Annotated[
        str, FieldMetadata(alias="priceDollars"), pydantic.Field(alias="priceDollars")
    ]
    wallet_id: typing_extensions.Annotated[
        WalletIdInt, FieldMetadata(alias="walletId"), pydantic.Field(alias="walletId")
    ]
    osparc_credits: typing_extensions.Annotated[
        str, FieldMetadata(alias="osparcCredits"), pydantic.Field(alias="osparcCredits")
    ]
    comment: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="completedAt"), pydantic.Field(alias="completedAt")
    ] = None
    completed_status: typing_extensions.Annotated[
        PaymentTransactionCompletedStatus,
        FieldMetadata(alias="completedStatus"),
        pydantic.Field(alias="completedStatus"),
    ]
    state_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stateMessage"), pydantic.Field(alias="stateMessage")
    ] = None
    invoice_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="invoiceUrl"), pydantic.Field(alias="invoiceUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
