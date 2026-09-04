

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_authorization_generate_link_code_response_errors_item import (
    GetAuthorizationGenerateLinkCodeResponseErrorsItem,
)
from .get_authorization_generate_link_code_response_response import GetAuthorizationGenerateLinkCodeResponseResponse


class GetAuthorizationGenerateLinkCodeResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ] = None
    response: typing.Optional[GetAuthorizationGenerateLinkCodeResponseResponse] = None
    errors: typing.Optional[typing.List[GetAuthorizationGenerateLinkCodeResponseErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
