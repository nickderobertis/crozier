

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .branch_response_output_preview_project_status import BranchResponseOutputPreviewProjectStatus
from .branch_response_output_status import BranchResponseOutputStatus


class BranchResponseOutput(UniversalBaseModel):
    id: str
    name: str
    project_ref: str
    parent_project_ref: str
    is_default: bool
    git_branch: typing.Optional[str] = None
    pr_number: typing.Optional[int] = None
    latest_check_run_id: typing.Optional[float] = pydantic.Field(default=None)
    """
    This field is deprecated and will not be populated.
    """

    persistent: bool
    status: BranchResponseOutputStatus = pydantic.Field()
    """
    This field is deprecated. List action runs to get branch status instead.
    """

    created_at: dt.datetime
    updated_at: dt.datetime
    review_requested_at: typing.Optional[dt.datetime] = None
    with_data: bool
    notify_url: typing.Optional[str] = None
    deletion_scheduled_at: typing.Optional[dt.datetime] = None
    preview_project_status: typing.Optional[BranchResponseOutputPreviewProjectStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
