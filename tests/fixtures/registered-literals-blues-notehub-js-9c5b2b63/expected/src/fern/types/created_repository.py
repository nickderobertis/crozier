

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_uid_list import AppUidList
from .fleets_uid_list import FleetsUidList


class CreatedRepository(UniversalBaseModel):
    fleet_uids: typing.Optional[FleetsUidList] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    repository name
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    read-only password for the database, also used as X-Repository-Token header for subsequent API calls.  This value is only served once when the repository is created
    """

    project_uids: typing.Optional[AppUidList] = None
    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the data repository
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    read-only user for database
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
