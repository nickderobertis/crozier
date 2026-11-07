

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateReaderCheckoutResponseData(UniversalBaseModel):
    checkout_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The checkout ID is a unique identifier for the checkout.
    """

    client_transaction_id: str = pydantic.Field()
    """
    The client transaction ID is a unique identifier for the transaction that is generated for the client.
    
    It can be used later to fetch the transaction details via the [Transactions API](https://developer.sumup.com/api/transactions/get).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
