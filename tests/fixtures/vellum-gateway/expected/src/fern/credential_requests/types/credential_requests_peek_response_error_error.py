

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credential_requests_peek_response_error_error_code import CredentialRequestsPeekResponseErrorErrorCode


class CredentialRequestsPeekResponseErrorError(UniversalBaseModel):
    code: CredentialRequestsPeekResponseErrorErrorCode
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
