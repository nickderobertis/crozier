

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2billing import V2Billing
from .v2extract_metadata_range_units import V2ExtractMetadataRangeUnits


class V2ExtractMetadata(UniversalBaseModel):
    """
    Response metadata for a v2 extract call.
    """

    job_id: str = pydantic.Field()
    """
    Gateway job id (workflow id). Matches the ``x-request-id`` the gateway minted for this request and the billing row id in vision-agent.
    """

    model_version: str = pydantic.Field()
    """
    Resolved model version.
    """

    duration_ms: int = pydantic.Field()
    """
    End-to-end request duration in milliseconds.
    """

    doc_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present when the input markdown contained a ``<!-- doc_id=<id> -->`` comment (embedded by ``POST /v2/parse``). Links this extract call to the originating parse job.
    """

    range_units: V2ExtractMetadataRangeUnits = pydantic.Field()
    """
    Units of every `range` offset in the response. Always `"unicode_codepoints"` (Unicode code points into `markdown`). Declared explicitly so consumers know how to slice the string — e.g. JavaScript strings are UTF-16, so a naive `.slice()` drifts when the markdown contains astral characters.
    """

    input_markdown_chars: typing.Optional[int] = pydantic.Field(default=None)
    """
    Characters (Unicode code points) in the input markdown as submitted — the input basis of the credit charge.
    """

    output_extraction_chars: typing.Optional[int] = pydantic.Field(default=None)
    """
    Characters in the serialized extraction output — the output basis of the credit charge.
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
