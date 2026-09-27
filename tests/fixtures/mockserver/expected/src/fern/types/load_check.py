

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .load_check_comparator import LoadCheckComparator
from .load_check_source import LoadCheckSource


class LoadCheck(UniversalBaseModel):
    """
    a per-step response assertion (the load equivalent of a k6 check). Extracts a value from a step's response (status code, a header, or a body JSONPath) and compares it against an expected value with a comparator. Observational: a failing check is counted (metric + report + CHECK_FAILURE_RATE threshold) but never fails the individual request. Extraction reuses the same primitives as LoadCapture.
    """

    source: LoadCheckSource = pydantic.Field()
    """
    where to read the observed value from: the response status code, a response header (headerName), or a JSONPath over the response body (jsonPath)
    """

    header_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="headerName"),
        pydantic.Field(
            alias="headerName", description="the response header name to read (required when source is HEADER)"
        ),
    ] = None
    """
    the response header name to read (required when source is HEADER)
    """

    json_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jsonPath"),
        pydantic.Field(
            alias="jsonPath",
            description="the JSONPath to evaluate over the response body (required when source is BODY_JSONPATH)",
        ),
    ] = None
    """
    the JSONPath to evaluate over the response body (required when source is BODY_JSONPATH)
    """

    comparator: LoadCheckComparator = pydantic.Field()
    """
    how the observed value is compared to value: string comparators (EQUALS/NOT_EQUALS/CONTAINS/MATCHES — MATCHES is a full-match regex) operate on the raw string; numeric comparators (GT/LT/GTE/LTE) parse both sides as numbers and fail the check when either side is not a number
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    the expected value / comparand the observed value is compared against
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
