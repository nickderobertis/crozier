

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .group_id_int import GroupIdInt


class ProjectGroupGet(UniversalBaseModel):
    gid: GroupIdInt
    read: bool
    write: bool
    delete: bool
    created: dt.datetime
    modified: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
