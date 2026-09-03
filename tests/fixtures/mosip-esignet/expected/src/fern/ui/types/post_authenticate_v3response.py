

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_authenticate_v3response_errors_item import PostAuthenticateV3ResponseErrorsItem
from .post_authenticate_v3response_response import PostAuthenticateV3ResponseResponse


class PostAuthenticateV3Response(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ] = None
    response: typing.Optional[PostAuthenticateV3ResponseResponse] = None
    errors: typing.Optional[typing.List[PostAuthenticateV3ResponseErrorsItem]] = pydantic.Field(default=None)
    """
    List of Errors in case of request validation / processing failure in Idp server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
