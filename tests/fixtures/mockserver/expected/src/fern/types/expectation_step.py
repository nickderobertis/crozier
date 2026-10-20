

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .delay import Delay
from .expectation_step_failure_policy import ExpectationStepFailurePolicy
from .http_class_callback import HttpClassCallback
from .http_error import HttpError
from .http_forward import HttpForward
from .http_object_callback import HttpObjectCallback
from .http_override_forwarded_request import HttpOverrideForwardedRequest
from .http_request import HttpRequest


class ExpectationStep(UniversalBaseModel):
    """
    a single step of a multi-step expectation
    """

    http_request: typing_extensions.Annotated[
        typing.Optional[HttpRequest], FieldMetadata(alias="httpRequest"), pydantic.Field(alias="httpRequest")
    ] = None
    http_class_callback: typing_extensions.Annotated[
        typing.Optional[HttpClassCallback],
        FieldMetadata(alias="httpClassCallback"),
        pydantic.Field(alias="httpClassCallback"),
    ] = None
    http_object_callback: typing_extensions.Annotated[
        typing.Optional[HttpObjectCallback],
        FieldMetadata(alias="httpObjectCallback"),
        pydantic.Field(alias="httpObjectCallback"),
    ] = None
    http_forward: typing_extensions.Annotated[
        typing.Optional[HttpForward], FieldMetadata(alias="httpForward"), pydantic.Field(alias="httpForward")
    ] = None
    http_override_forwarded_request: typing_extensions.Annotated[
        typing.Optional[HttpOverrideForwardedRequest],
        FieldMetadata(alias="httpOverrideForwardedRequest"),
        pydantic.Field(alias="httpOverrideForwardedRequest"),
    ] = None
    http_response: typing_extensions.Annotated[
        typing.Optional["HttpResponse"], FieldMetadata(alias="httpResponse"), pydantic.Field(alias="httpResponse")
    ] = None
    http_error: typing_extensions.Annotated[
        typing.Optional[HttpError], FieldMetadata(alias="httpError"), pydantic.Field(alias="httpError")
    ] = None
    responder: typing.Optional[bool] = None
    delay: typing.Optional[Delay] = None
    blocking: typing.Optional[bool] = None
    timeout: typing.Optional[Delay] = None
    failure_policy: typing_extensions.Annotated[
        typing.Optional[ExpectationStepFailurePolicy],
        FieldMetadata(alias="failurePolicy"),
        pydantic.Field(alias="failurePolicy"),
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

update_forward_refs(ExpectationStep, HttpResponse=HttpResponse, RecoverAfter=RecoverAfter)
