

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_metadata import DocumentMetadata
from .plaid_error import PlaidError
from .request_id import RequestId
from .taxform import Taxform


class IncomeVerificationTaxformsGetResponse(UniversalBaseModel):
    """
    IncomeVerificationTaxformsGetResponse defines the response schema for `/income/verification/taxforms/get`
    """

    document_metadata: typing.List[DocumentMetadata]
    error: typing.Optional[PlaidError] = None
    request_id: typing.Optional[RequestId] = None
    taxforms: typing.List[Taxform] = pydantic.Field()
    """
    A list of forms.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
