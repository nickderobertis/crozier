

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .delay import Delay
from .http_forward import HttpForward


class HttpForwardWithFallback(UniversalBaseModel):
    """
    forward with a fallback response on failure
    """

    delay: typing.Optional[Delay] = None
    http_forward: typing_extensions.Annotated[
        HttpForward, FieldMetadata(alias="httpForward"), pydantic.Field(alias="httpForward")
    ]
    fallback_response: typing_extensions.Annotated[
        "HttpResponse", FieldMetadata(alias="fallbackResponse"), pydantic.Field(alias="fallbackResponse")
    ]
    fallback_on_status_codes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="fallbackOnStatusCodes"),
        pydantic.Field(alias="fallbackOnStatusCodes"),
    ] = None
    fallback_on_timeout: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="fallbackOnTimeout"), pydantic.Field(alias="fallbackOnTimeout")
    ] = None
    primary: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .http_response import HttpResponse
from .recover_after import RecoverAfter

update_forward_refs(HttpForwardWithFallback, HttpResponse=HttpResponse, RecoverAfter=RecoverAfter)
