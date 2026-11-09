

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_uid_list import AppUidList
from .fleets_uid_list import FleetsUidList


class Repository(UniversalBaseModel):
    fleet_uids: typing.Optional[FleetsUidList] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    repository name
    """

    project_uids: typing.Optional[AppUidList] = None
    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the data repository
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
