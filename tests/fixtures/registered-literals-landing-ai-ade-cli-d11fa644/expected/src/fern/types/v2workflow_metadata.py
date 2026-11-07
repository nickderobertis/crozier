

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2billing import V2Billing


class V2WorkflowMetadata(UniversalBaseModel):
    """
    Response metadata for a v2 workflow call
    (``docs/pipeline-v2-proposal.md`` → Top-level metadata).
    """

    job_id: str = pydantic.Field()
    """
    Gateway job id (workflow id).
    """

    duration_ms: int = pydantic.Field()
    """
    Total end-to-end duration across all stages in milliseconds.
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
