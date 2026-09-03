

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_linked_authenticate_v2response_errors_item import PostLinkedAuthenticateV2ResponseErrorsItem
from .post_linked_authenticate_v2response_response import PostLinkedAuthenticateV2ResponseResponse


class PostLinkedAuthenticateV2Response(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ] = None
    response: typing.Optional[PostLinkedAuthenticateV2ResponseResponse] = None
    errors: typing.Optional[typing.List[PostLinkedAuthenticateV2ResponseErrorsItem]] = pydantic.Field(default=None)
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
