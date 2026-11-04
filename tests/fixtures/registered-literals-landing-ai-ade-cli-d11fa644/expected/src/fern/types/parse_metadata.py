

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parse_billing import ParseBilling
from .parse_metadata_range_units import ParseMetadataRangeUnits


class ParseMetadata(UniversalBaseModel):
    """
    Information about a parse request. This is the customer-facing shape —
    the internal billing-canonical metadata (``aide_common.parse_schema.ParseMetadata``)
    is projected into it at the render boundary (``project_customer_metadata``).
    """

    job_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The parse job identifier — always server-minted and unique per submit. On the async `/jobs` route this is the id the caller polls. Correlates with the job's entry in your billing dashboard. Format: ``<service>-<26-character Crockford base32 ULID>`` matching ``^(parse|extract)-[0-9a-hjkmnp-tv-z]{26}$``. Opaque, server-minted, and stable for the life of the job — the same id is returned on the sync response, the async 202, and every poll. Treat it as opaque; older id formats remain accepted indefinitely and are never re-issued.
    """

    model_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The exact model snapshot that parsed the document, e.g. `dpt-3-pro-20260710`.
    """

    page_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of pages in the source document. Includes pages filtered out by `options.pages`; the actual returned pages are in `structure.children`.
    """

    output_markdown_chars: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of Unicode code points in the returned `markdown` string.
    """

    range_units: ParseMetadataRangeUnits = pydantic.Field()
    """
    Units of every `range` offset in the response. Always `"unicode_codepoints"` (Unicode code points into `markdown`). Declared explicitly so consumers know how to slice the string — e.g. JavaScript strings are UTF-16, so a naive `.slice()` drifts when the markdown contains astral characters; such consumers must convert code-point offsets to UTF-16 indices first.
    """

    openapi_spec: str = pydantic.Field()
    """
    URL of the OpenAPI spec covering this API, for inspection and client generation.
    """

    failed_pages: typing.List[int] = pydantic.Field()
    """
    1-indexed page numbers that failed to parse. Empty when all pages succeed; failed pages also appear in `structure.children` with `status: failed`.
    """

    duration_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total processing time in milliseconds.
    """

    billing: ParseBilling = pydantic.Field()
    """
    Billing summary: the service tier and the credits charged.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
