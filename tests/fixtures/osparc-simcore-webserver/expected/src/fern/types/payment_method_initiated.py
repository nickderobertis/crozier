

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .wallet_id_int import WalletIdInt


class PaymentMethodInitiated(UniversalBaseModel):
    wallet_id: typing_extensions.Annotated[
        WalletIdInt, FieldMetadata(alias="walletId"), pydantic.Field(alias="walletId")
    ]
    payment_method_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="paymentMethodId"), pydantic.Field(alias="paymentMethodId")
    ]
    payment_method_form_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="paymentMethodFormUrl"),
        pydantic.Field(
            alias="paymentMethodFormUrl", description="Link to external site that holds the payment submission form"
        ),
    ]
    """
    Link to external site that holds the payment submission form
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
