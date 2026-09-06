

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin import Admin
from .api_key import ApiKey
from .base_virtual_folder import BaseVirtualFolder
from .event_action import EventAction
from .event_rule import EventRule
from .group import Group
from .role import Role
from .share import Share
from .user import User


class BackupData(UniversalBaseModel):
    users: typing.Optional[typing.List[User]] = None
    folders: typing.Optional[typing.List[BaseVirtualFolder]] = None
    groups: typing.Optional[typing.List[Group]] = None
    admins: typing.Optional[typing.List[Admin]] = None
    api_keys: typing.Optional[typing.List[ApiKey]] = None
    shares: typing.Optional[typing.List[Share]] = None
    event_actions: typing.Optional[typing.List[EventAction]] = None
    event_rules: typing.Optional[typing.List[EventRule]] = None
    roles: typing.Optional[typing.List[Role]] = None
    version: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
