

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_wallet_payment_price_dollars import CreateWalletPaymentPriceDollars


class CreateWalletPayment(UniversalBaseModel):
    price_dollars: typing_extensions.Annotated[
        CreateWalletPaymentPriceDollars, FieldMetadata(alias="priceDollars"), pydantic.Field(alias="priceDollars")
    ]
    comment: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
