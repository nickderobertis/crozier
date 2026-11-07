

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parse_list_jobs_response_jobs_item_status import ParseListJobsResponseJobsItemStatus


class ParseListJobsResponseJobsItem(UniversalBaseModel):
    job_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the parse job. Format: ``<service>-<26-character Crockford base32 ULID>`` matching ``^(parse|extract)-[0-9a-hjkmnp-tv-z]{26}$``. Opaque, server-minted, and stable for the life of the job — the same id is returned on the sync response, the async 202, and every poll. Treat it as opaque; older id formats remain accepted indefinitely and are never re-issued.
    """

    status: typing.Optional[ParseListJobsResponseJobsItemStatus] = pydantic.Field(default=None)
    """
    The job's current status: ``pending``, ``processing``, ``completed``, or ``failed``.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO-8601 timestamp for when the job was created.
    """

    completed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO-8601 timestamp for when the job finished, if terminal.
    """

    model_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model snapshot used to parse the document.
    """

    failure_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason the job failed. Present only when ``status`` is ``failed``.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
