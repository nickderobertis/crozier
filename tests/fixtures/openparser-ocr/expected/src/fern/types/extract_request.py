

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .extract_request_grounding import ExtractRequestGrounding
from .extract_request_llm_options import ExtractRequestLlmOptions
from .extract_request_output_format import ExtractRequestOutputFormat


class ExtractRequest(UniversalBaseModel):
    """
    Single extract config. Provide either `pipeline_id` or inline extraction config.
    The source is exactly one of multipart file bytes, `file_id`, or tenant-owned succeeded
    `parse_job_id`. Parse reuse is single-extract-only, forbids `ocr_model` / `ocr_options`,
    does not run OCR, and adds no page charge. `parse_job_id` is part of idempotency identity.
    """

    pipeline_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Saved extraction pipeline id (`oppl_…`). Inline extraction fields are forbidden.
    Admission records pipeline id/version provenance and snapshots the effective extraction
    configuration; the worker never re-reads the pipeline. With `parse_job_id`, source-parse
    provenance is recorded separately and the pipeline's OCR settings are not executed.
    """

    ocr_model: typing.Optional[str] = None
    ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = None
    llm_model: typing.Optional[str] = None
    llm_options: typing.Optional[ExtractRequestLlmOptions] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    repair_attempts: typing.Optional[int] = None
    grounding: typing.Optional[ExtractRequestGrounding] = pydantic.Field(default=None)
    """
    Optional field grounding mode. Defaults to `none` for inline requests. Changing
    grounding with the same Idempotency-Key returns `409 idempotency_conflict`.
    Unsupported schemas return `422 grounding_unsupported_schema`.
    """

    file_id: typing.Optional[str] = None
    parse_job_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tenant-owned succeeded `parse` job (`opj_…`) whose canonical `openparser@1` ParsedDocument
    is reused. Mutually exclusive with multipart bytes and `file_id`; forbidden in batch.
    """

    output_format: typing.Optional[ExtractRequestOutputFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
