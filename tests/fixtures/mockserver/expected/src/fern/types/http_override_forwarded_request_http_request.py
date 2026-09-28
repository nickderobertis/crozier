

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .delay import Delay
from .http_request import HttpRequest


class HttpOverrideForwardedRequestHttpRequest(UniversalBaseModel):
    delay: typing.Optional[Delay] = None
    http_request: typing_extensions.Annotated[
        typing.Optional[HttpRequest], FieldMetadata(alias="httpRequest"), pydantic.Field(alias="httpRequest")
    ] = None
    http_response: typing_extensions.Annotated[
        typing.Optional["HttpResponse"], FieldMetadata(alias="httpResponse"), pydantic.Field(alias="httpResponse")
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

update_forward_refs(HttpOverrideForwardedRequestHttpRequest, HttpResponse=HttpResponse, RecoverAfter=RecoverAfter)
