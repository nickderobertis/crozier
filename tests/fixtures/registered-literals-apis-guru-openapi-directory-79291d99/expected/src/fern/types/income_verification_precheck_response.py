

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .income_verification_precheck_confidence import IncomeVerificationPrecheckConfidence
from .request_id import RequestId


class IncomeVerificationPrecheckResponse(UniversalBaseModel):
    """
    IncomeVerificationPrecheckResponse defines the response schema for `/income/verification/precheck`.
    """

    confidence: IncomeVerificationPrecheckConfidence
    precheck_id: str = pydantic.Field()
    """
    ID of the precheck. Provide this value when calling `/link/token/create` in order to optimize Link conversion.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
