

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credential_requests_submit_response_error_error_code import CredentialRequestsSubmitResponseErrorErrorCode


class CredentialRequestsSubmitResponseErrorError(UniversalBaseModel):
    code: CredentialRequestsSubmitResponseErrorErrorCode
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
