

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateReaderCheckoutRequestAade(UniversalBaseModel):
    """
    Optional object containing data for transactions from ERP integrators in Greece that comply with the AADE 1155 protocol.
    When such regulatory/business requirements apply, this object must be provided and contains the data needed to validate the transaction with the AADE signature provider.
    """

    provider_id: str = pydantic.Field()
    """
    The identifier of the AADE signature provider.
    """

    signature: str = pydantic.Field()
    """
    The base64 encoded signature of the transaction data.
    """

    signature_data: str = pydantic.Field()
    """
    The string containing the signed transaction data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
