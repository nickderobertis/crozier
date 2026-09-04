

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_authorization_prepare_signup_redirect_response_errors_item import (
    PostAuthorizationPrepareSignupRedirectResponseErrorsItem,
)
from .post_authorization_prepare_signup_redirect_response_response import (
    PostAuthorizationPrepareSignupRedirectResponseResponse,
)


class PostAuthorizationPrepareSignupRedirectResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ] = None
    response: typing.Optional[PostAuthorizationPrepareSignupRedirectResponseResponse] = None
    errors: typing.Optional[typing.List[PostAuthorizationPrepareSignupRedirectResponseErrorsItem]] = pydantic.Field(
        default=None
    )
    """
    List of Errors in case of request validation / processing failure in eSignet server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
