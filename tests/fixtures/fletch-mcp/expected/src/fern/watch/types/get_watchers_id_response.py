

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_watchers_id_response_watcher import GetWatchersIdResponseWatcher


class GetWatchersIdResponse(UniversalBaseModel):
    watcher: typing.Optional[GetWatchersIdResponseWatcher] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
