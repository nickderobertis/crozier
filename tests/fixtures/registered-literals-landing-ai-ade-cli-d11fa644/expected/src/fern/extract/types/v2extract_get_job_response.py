

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2extract_get_job_response_error import V2ExtractGetJobResponseError
from .v2extract_get_job_response_result import V2ExtractGetJobResponseResult
from .v2extract_get_job_response_status import V2ExtractGetJobResponseStatus


class V2ExtractGetJobResponse(UniversalBaseModel):
    job_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for this v2-extract job. Format: ``extract-<26-character Crockford base32 ULID>`` (``[0-9a-hjkmnp-tv-z]{26}`` tail). Opaque, server-minted, and stable for the life of the job — the same id is returned on the sync response, the async 202, and every poll. Treat it as opaque; older id formats remain accepted indefinitely and are never re-issued.
    """

    status: typing.Optional[V2ExtractGetJobResponseStatus] = None
    created_at: typing.Optional[str] = None
    completed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present once the job is terminal.
    """

    progress: typing.Optional[float] = pydantic.Field(default=None)
    """
    Job completion as a decimal from 0 (not started) to 1 (complete). Present while ``processing``.
    """

    result: typing.Optional[V2ExtractGetJobResponseResult] = pydantic.Field(default=None)
    """
    Present once status is ``completed`` and ``output_save_url`` was not set. When ``output_save_url`` was set, the result is delivered there and ``output_url`` is returned instead.
    """

    error: typing.Optional[V2ExtractGetJobResponseError] = pydantic.Field(default=None)
    """
    Present once status is ``failed``.
    """

    output_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL the result was delivered to. Present once the job has ``completed`` and ``output_save_url`` was set, instead of inline ``result``.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
