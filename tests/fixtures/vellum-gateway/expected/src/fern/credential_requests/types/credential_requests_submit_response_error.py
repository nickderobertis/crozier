

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credential_requests_submit_response_error_error import CredentialRequestsSubmitResponseErrorError


class CredentialRequestsSubmitResponseError(UniversalBaseModel):
    error: CredentialRequestsSubmitResponseErrorError

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
