

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserPaymentInfo(UniversalBaseModel):
    """
    Structure with the order’s payment data. Required only if `invoiceData` is defined.
    """

    payment_methods: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="paymentMethods"),
        pydantic.Field(
            alias="paymentMethods",
            description="List of strings with the payment methods used in the order. Required only if invoiceData is defined. The format and some possible values of payment methods accepted in this list can be found in the call [Fetching marketplace information with the Orders API](https://developers.vtex.com/vtex-rest-api/docs/get-marketplace-data-orders-api).",
        ),
    ]
    """
    List of strings with the payment methods used in the order. Required only if invoiceData is defined. The format and some possible values of payment methods accepted in this list can be found in the call [Fetching marketplace information with the Orders API](https://developers.vtex.com/vtex-rest-api/docs/get-marketplace-data-orders-api).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
