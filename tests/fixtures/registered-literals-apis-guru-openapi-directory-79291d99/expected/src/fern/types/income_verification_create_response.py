

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class IncomeVerificationCreateResponse(UniversalBaseModel):
    """
    IncomeVerificationCreateResponse defines the response schema for `/income/verification/create`.
    """

    income_verification_id: str = pydantic.Field()
    """
    ID of the verification. This ID is persisted throughout the lifetime of the verification.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
