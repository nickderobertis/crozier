

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rerun_detail import RerunDetail
from .rerun_priority_summary import RerunPrioritySummary


class RerunDetailsResponse(UniversalBaseModel):
    priority_summaries: typing.List[RerunPrioritySummary]
    selected_priority: typing.Optional[int] = None
    count: int
    selected_count: int
    limit: int
    offset: int
    reruns: typing.List[RerunDetail]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
