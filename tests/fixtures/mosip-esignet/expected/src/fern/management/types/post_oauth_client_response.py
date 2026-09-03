

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_oauth_client_response_errors_item import PostOauthClientResponseErrorsItem
from .post_oauth_client_response_response import PostOauthClientResponseResponse


class PostOauthClientResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="responseTime"),
        pydantic.Field(alias="responseTime", description="Date and time when the response is generated"),
    ] = None
    """
    Date and time when the response is generated
    """

    response: typing.Optional[PostOauthClientResponseResponse] = None
    errors: typing.Optional[typing.List[PostOauthClientResponseErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
