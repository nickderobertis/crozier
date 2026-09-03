

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_complete_signup_redirect_response_errors_item import PostCompleteSignupRedirectResponseErrorsItem
from .post_complete_signup_redirect_response_response import PostCompleteSignupRedirectResponseResponse


class PostCompleteSignupRedirectResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ] = None
    response: typing.Optional[PostCompleteSignupRedirectResponseResponse] = pydantic.Field(default=None)
    """
    Successful message, or null if failed to deliver OTP.
    """

    errors: typing.Optional[typing.List[PostCompleteSignupRedirectResponseErrorsItem]] = pydantic.Field(default=None)
    """
    List of Errors in case of request validation / processing failure in Idp server. if failure from IDA, the same error is relayed in this response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
