

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .http_override_forwarded_request_request_modifier_request_modifier_cookies import (
    HttpOverrideForwardedRequestRequestModifierRequestModifierCookies,
)
from .http_override_forwarded_request_request_modifier_request_modifier_headers import (
    HttpOverrideForwardedRequestRequestModifierRequestModifierHeaders,
)
from .http_override_forwarded_request_request_modifier_request_modifier_path import (
    HttpOverrideForwardedRequestRequestModifierRequestModifierPath,
)
from .http_override_forwarded_request_request_modifier_request_modifier_query_string_parameters import (
    HttpOverrideForwardedRequestRequestModifierRequestModifierQueryStringParameters,
)


class HttpOverrideForwardedRequestRequestModifierRequestModifier(UniversalBaseModel):
    path: typing.Optional[HttpOverrideForwardedRequestRequestModifierRequestModifierPath] = None
    query_string_parameters: typing_extensions.Annotated[
        typing.Optional[HttpOverrideForwardedRequestRequestModifierRequestModifierQueryStringParameters],
        FieldMetadata(alias="queryStringParameters"),
        pydantic.Field(alias="queryStringParameters"),
    ] = None
    headers: typing.Optional[HttpOverrideForwardedRequestRequestModifierRequestModifierHeaders] = None
    cookies: typing.Optional[HttpOverrideForwardedRequestRequestModifierRequestModifierCookies] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
