

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_internal_snapshot_jobs_job_id_fail_response_status import PostInternalSnapshotJobsJobIdFailResponseStatus


class PostInternalSnapshotJobsJobIdFailResponse(UniversalBaseModel):
    status: PostInternalSnapshotJobsJobIdFailResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
