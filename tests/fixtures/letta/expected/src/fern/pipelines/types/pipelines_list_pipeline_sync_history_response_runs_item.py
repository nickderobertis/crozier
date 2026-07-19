

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_list_pipeline_sync_history_response_runs_item_error import (
    PipelinesListPipelineSyncHistoryResponseRunsItemError,
)
from .pipelines_list_pipeline_sync_history_response_runs_item_status import (
    PipelinesListPipelineSyncHistoryResponseRunsItemStatus,
)


class PipelinesListPipelineSyncHistoryResponseRunsItem(UniversalBaseModel):
    workflow_id: str
    status: PipelinesListPipelineSyncHistoryResponseRunsItemStatus
    started_at: dt.datetime
    completed_at: typing.Optional[dt.datetime] = None
    error: typing.Optional[PipelinesListPipelineSyncHistoryResponseRunsItemError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
