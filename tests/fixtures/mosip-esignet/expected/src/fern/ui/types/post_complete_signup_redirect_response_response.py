

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_complete_signup_redirect_response_response_status import PostCompleteSignupRedirectResponseResponseStatus


class PostCompleteSignupRedirectResponseResponse(UniversalBaseModel):
    """
    Successful message, or null if failed to deliver OTP.
    """

    status: typing.Optional[PostCompleteSignupRedirectResponseResponseStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
