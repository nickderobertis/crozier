

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_oauth_details_response_errors_item import PostOauthDetailsResponseErrorsItem
from .post_oauth_details_response_response import PostOauthDetailsResponseResponse


class PostOauthDetailsResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ] = None
    response: typing.Optional[PostOauthDetailsResponseResponse] = None
    errors: typing.Optional[typing.List[PostOauthDetailsResponseErrorsItem]] = pydantic.Field(default=None)
    """
    List of errors in case of request validation / processing failure in Idp server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
