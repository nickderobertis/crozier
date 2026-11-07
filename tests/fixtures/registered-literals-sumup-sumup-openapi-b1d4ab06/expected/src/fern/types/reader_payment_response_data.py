

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReaderPaymentResponseData(UniversalBaseModel):
    client_transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Caller-supplied correlation identifier that was provided in the request.
    """

    transaction_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transaction code returned by the acquirer/processing entity after processing the transaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
