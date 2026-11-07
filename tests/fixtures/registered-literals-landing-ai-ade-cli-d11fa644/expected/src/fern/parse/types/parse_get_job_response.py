

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...types.parse_response import ParseResponse
from .parse_get_job_response_error import ParseGetJobResponseError
from .parse_get_job_response_status import ParseGetJobResponseStatus


class ParseGetJobResponse(UniversalBaseModel):
    job_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for this parse job. Format: ``<service>-<26-character Crockford base32 ULID>`` matching ``^(parse|extract)-[0-9a-hjkmnp-tv-z]{26}$``. Opaque, server-minted, and stable for the life of the job — the same id is returned on the sync response, the async 202, and every poll. Treat it as opaque; older id formats remain accepted indefinitely and are never re-issued.
    """

    status: typing.Optional[ParseGetJobResponseStatus] = pydantic.Field(default=None)
    """
    The job's current status: ``pending``, ``processing``, ``completed``, or ``failed``.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO-8601 timestamp for when the job was created.
    """

    completed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO-8601 timestamp; present once the job is terminal.
    """

    progress: typing.Optional[float] = pydantic.Field(default=None)
    """
    Job completion as a decimal from 0 (not started) to 1 (complete). Present while ``processing``.
    """

    result: typing.Optional[ParseResponse] = pydantic.Field(default=None)
    """
    The parse response, present once the job has ``completed`` and ``output_save_url`` was not set. When ``output_save_url`` was set, the result is delivered there and ``output_url`` is returned instead.
    """

    output_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL the result was delivered to. Present once the job has ``completed`` and ``output_save_url`` was set, instead of inline ``result``.
    """

    error: typing.Optional[ParseGetJobResponseError] = pydantic.Field(default=None)
    """
    Present once the job has ``failed`` — the failure code + message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ParseGetJobResponse)
