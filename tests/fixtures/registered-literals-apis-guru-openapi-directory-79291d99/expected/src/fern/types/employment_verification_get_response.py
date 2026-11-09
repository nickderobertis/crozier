

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employment_verification import EmploymentVerification
from .request_id import RequestId


class EmploymentVerificationGetResponse(UniversalBaseModel):
    """
    EmploymentVerificationGetResponse defines the response schema for `/employment/verification/get`.
    """

    employments: typing.List[EmploymentVerification] = pydantic.Field()
    """
    A list of employment verification summaries.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
