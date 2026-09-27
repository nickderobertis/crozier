

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class RecoverAfter(UniversalBaseModel):
    """
    fail the first failTimes matches then serve the configured response (deterministic retry/backoff recovery primitive)
    """

    fail_times: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="failTimes"),
        pydantic.Field(
            alias="failTimes",
            description="number of leading matches that serve the failure response before the configured response is served; null or <= 0 makes this inert",
        ),
    ] = None
    """
    number of leading matches that serve the failure response before the configured response is served; null or <= 0 makes this inert
    """

    fail_response: typing_extensions.Annotated[
        typing.Optional["HttpResponse"], FieldMetadata(alias="failResponse"), pydantic.Field(alias="failResponse")
    ] = None
    idempotency_header: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="idempotencyHeader"),
        pydantic.Field(
            alias="idempotencyHeader",
            description="optional request header whose value keys an independent failure window per (expectation, header-value); when absent on a request the per-expectation match count is used",
        ),
    ] = None
    """
    optional request header whose value keys an independent failure window per (expectation, header-value); when absent on a request the per-expectation match count is used
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .http_response import HttpResponse

update_forward_refs(RecoverAfter, HttpResponse=HttpResponse)
