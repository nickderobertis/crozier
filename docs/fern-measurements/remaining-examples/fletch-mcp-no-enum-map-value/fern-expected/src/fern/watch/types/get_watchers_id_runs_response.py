

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_watchers_id_runs_response_runs_item import GetWatchersIdRunsResponseRunsItem


class GetWatchersIdRunsResponse(UniversalBaseModel):
    runs: typing.Optional[typing.List[GetWatchersIdRunsResponseRunsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
