

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_oauth_details_v2response_errors_item import PostOauthDetailsV2ResponseErrorsItem
from .post_oauth_details_v2response_response import PostOauthDetailsV2ResponseResponse


class PostOauthDetailsV2Response(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ] = None
    response: typing.Optional[PostOauthDetailsV2ResponseResponse] = None
    errors: typing.Optional[typing.List[PostOauthDetailsV2ResponseErrorsItem]] = pydantic.Field(default=None)
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
