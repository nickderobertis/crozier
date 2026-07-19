

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_list_pipeline_sync_history_response_runs_item import PipelinesListPipelineSyncHistoryResponseRunsItem


class PipelinesListPipelineSyncHistoryResponse(UniversalBaseModel):
    runs: typing.List[PipelinesListPipelineSyncHistoryResponseRunsItem]
    next_page_token: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
