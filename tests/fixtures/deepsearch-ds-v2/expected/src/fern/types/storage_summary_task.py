

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .storage_summary_task_kind import StorageSummaryTaskKind


class StorageSummaryTask(UniversalBaseModel):
    dc_key: typing.Optional[str] = None
    kg_key: typing.Optional[str] = None
    kind: StorageSummaryTaskKind
    proj_key: str
    task_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
