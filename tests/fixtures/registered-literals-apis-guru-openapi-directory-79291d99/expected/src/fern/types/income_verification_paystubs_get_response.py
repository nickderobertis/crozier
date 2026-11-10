

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_metadata import DocumentMetadata
from .paystub import Paystub
from .plaid_error import PlaidError
from .request_id import RequestId


class IncomeVerificationPaystubsGetResponse(UniversalBaseModel):
    """
    IncomeVerificationPaystubsGetResponse defines the response schema for `/income/verification/paystubs/get`.
    """

    document_metadata: typing.Optional[typing.List[DocumentMetadata]] = pydantic.Field(default=None)
    """
    Metadata for an income document.
    """

    error: typing.Optional[PlaidError] = None
    paystubs: typing.List[Paystub]
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
