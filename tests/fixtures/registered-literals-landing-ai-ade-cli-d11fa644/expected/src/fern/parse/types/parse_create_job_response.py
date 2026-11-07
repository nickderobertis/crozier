

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parse_create_job_response_status import ParseCreateJobResponseStatus


class ParseCreateJobResponse(UniversalBaseModel):
    job_id: str = pydantic.Field()
    """
    The unique identifier for the created parse job. Poll ``GET /v2/parse/jobs/{job_id}`` for its status and result. Format: ``<service>-<26-character Crockford base32 ULID>`` matching ``^(parse|extract)-[0-9a-hjkmnp-tv-z]{26}$``. Opaque, server-minted, and stable for the life of the job — the same id is returned on the sync response, the async 202, and every poll. Treat it as opaque; older id formats remain accepted indefinitely and are never re-issued.
    """

    status: ParseCreateJobResponseStatus = pydantic.Field()
    """
    The job's status at creation — normally ``pending`` (a just-created job that is still running is reported as ``pending``), but may already be a terminal ``completed`` / ``failed`` if the job finished before the create response was rendered.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO-8601 timestamp for when the job was created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
