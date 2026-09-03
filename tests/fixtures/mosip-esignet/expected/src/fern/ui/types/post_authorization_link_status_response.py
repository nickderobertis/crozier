

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_authorization_link_status_response_errors_item import PostAuthorizationLinkStatusResponseErrorsItem
from .post_authorization_link_status_response_response import PostAuthorizationLinkStatusResponseResponse


class PostAuthorizationLinkStatusResponse(UniversalBaseModel):
    response_t_ime: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseTIme"), pydantic.Field(alias="responseTIme")
    ] = None
    response: typing.Optional[PostAuthorizationLinkStatusResponseResponse] = None
    errors: typing.Optional[typing.List[PostAuthorizationLinkStatusResponseErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
