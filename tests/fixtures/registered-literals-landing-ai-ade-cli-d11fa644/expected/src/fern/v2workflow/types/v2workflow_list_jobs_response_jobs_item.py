

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2workflow_list_jobs_response_jobs_item_status import V2WorkflowListJobsResponseJobsItemStatus


class V2WorkflowListJobsResponseJobsItem(UniversalBaseModel):
    job_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for this v2-workflow job. Format: ``v2-workflow-<26-character Crockford base32 ULID>`` (``[0-9a-hjkmnp-tv-z]{26}`` tail). Opaque, server-minted, and stable for the life of the job — the same id is returned on the sync response, the async 202, and every poll. Treat it as opaque; older id formats remain accepted indefinitely and are never re-issued.
    """

    status: typing.Optional[V2WorkflowListJobsResponseJobsItemStatus] = None
    created_at: typing.Optional[str] = None
    completed_at: typing.Optional[str] = None
    model_version: typing.Optional[str] = None
    failure_reason: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
