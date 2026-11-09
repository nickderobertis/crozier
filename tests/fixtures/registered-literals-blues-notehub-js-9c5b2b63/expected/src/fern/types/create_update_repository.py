

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_uid_list import AppUidList
from .fleets_uid_list import FleetsUidList


class CreateUpdateRepository(UniversalBaseModel):
    fleet_uids: typing.Optional[FleetsUidList] = None
    name: typing.Optional[str] = None
    project_uids: typing.Optional[AppUidList] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
