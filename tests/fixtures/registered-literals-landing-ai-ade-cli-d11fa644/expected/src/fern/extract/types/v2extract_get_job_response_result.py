

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.v2extract_metadata import V2ExtractMetadata


class V2ExtractGetJobResponseResult(UniversalBaseModel):
    """
    Result returned by V2ExtractOperationWorkflow — the ``/v2/extract``
    response body (``docs/extract-v2-proposal.md`` → Response).

    ``extraction`` and ``extraction_metadata`` mirror each other structurally:
    leaf values in ``extraction`` are replaced by ``ExtractionFieldMetadata``
    objects in ``extraction_metadata``.
    """

    extraction: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Extracted values conforming to the request ``schema``.
    """

    extraction_metadata: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Per-field metadata, mirroring ``extraction`` with leaf values replaced by ``{value, ranges}`` objects.
    """

    markdown: str = pydantic.Field()
    """
    Echoed input markdown.
    """

    metadata: V2ExtractMetadata = pydantic.Field()
    """
    Request metadata (job_id, model_version, duration_ms, doc_id, billing).
    """

    schema_violation_error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Set when ``options.strict`` is false and the schema contained fields the model could not extract — the extraction is partial.
    """

    warnings: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    Non-fatal warnings emitted during extraction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
