

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .wallet_id_int import WalletIdInt


class PaymentMethodGet(UniversalBaseModel):
    idr: str
    wallet_id: typing_extensions.Annotated[
        WalletIdInt, FieldMetadata(alias="walletId"), pydantic.Field(alias="walletId")
    ]
    card_holder_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardHolderName"), pydantic.Field(alias="cardHolderName")
    ] = None
    card_number_masked: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardNumberMasked"), pydantic.Field(alias="cardNumberMasked")
    ] = None
    card_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardType"), pydantic.Field(alias="cardType")
    ] = None
    expiration_month: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="expirationMonth"), pydantic.Field(alias="expirationMonth")
    ] = None
    expiration_year: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="expirationYear"), pydantic.Field(alias="expirationYear")
    ] = None
    created: dt.datetime
    auto_recharge: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoRecharge"),
        pydantic.Field(alias="autoRecharge", description="If true, this payment-method is used for auto-recharge"),
    ] = None
    """
    If true, this payment-method is used for auto-recharge
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
