

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2billing import V2Billing


class V2GroundMetadata(UniversalBaseModel):
    """
    Response metadata for a v2 ground call.
    """

    job_id: str = pydantic.Field()
    """
    Gateway job id (workflow id). Matches the ``x-request-id`` the gateway minted for this request.
    """

    duration_ms: int = pydantic.Field()
    """
    End-to-end request duration in milliseconds.
    """

    openapi_spec: str = pydantic.Field()
    """
    URL of the OpenAPI spec covering this API, for inspection and client generation.
    """

    billing: typing.Optional[V2Billing] = pydantic.Field(default=None)
    """
    Billing summary: the service tier the request ran in and the credits charged.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
