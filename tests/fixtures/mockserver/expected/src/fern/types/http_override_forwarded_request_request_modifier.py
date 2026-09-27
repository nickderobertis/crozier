

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .delay import Delay
from .http_override_forwarded_request_request_modifier_request_modifier import (
    HttpOverrideForwardedRequestRequestModifierRequestModifier,
)
from .http_override_forwarded_request_request_modifier_response_modifier import (
    HttpOverrideForwardedRequestRequestModifierResponseModifier,
)
from .http_request import HttpRequest
from .http_template import HttpTemplate


class HttpOverrideForwardedRequestRequestModifier(UniversalBaseModel):
    delay: typing.Optional[Delay] = None
    request_override: typing_extensions.Annotated[
        typing.Optional[HttpRequest], FieldMetadata(alias="requestOverride"), pydantic.Field(alias="requestOverride")
    ] = None
    request_modifier: typing_extensions.Annotated[
        typing.Optional[HttpOverrideForwardedRequestRequestModifierRequestModifier],
        FieldMetadata(alias="requestModifier"),
        pydantic.Field(alias="requestModifier"),
    ] = None
    response_override: typing_extensions.Annotated[
        typing.Optional["HttpResponse"],
        FieldMetadata(alias="responseOverride"),
        pydantic.Field(alias="responseOverride"),
    ] = None
    response_modifier: typing_extensions.Annotated[
        typing.Optional[HttpOverrideForwardedRequestRequestModifierResponseModifier],
        FieldMetadata(alias="responseModifier"),
        pydantic.Field(alias="responseModifier"),
    ] = None
    response_template: typing_extensions.Annotated[
        typing.Optional[HttpTemplate], FieldMetadata(alias="responseTemplate"), pydantic.Field(alias="responseTemplate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .http_response import HttpResponse
from .recover_after import RecoverAfter

update_forward_refs(HttpOverrideForwardedRequestRequestModifier, HttpResponse=HttpResponse, RecoverAfter=RecoverAfter)
