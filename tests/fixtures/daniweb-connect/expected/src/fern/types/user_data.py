

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app import App
from .user import User
from .user_data_content import UserDataContent
from .user_data_settings import UserDataSettings
from .user_data_status import UserDataStatus


class UserData(UniversalBaseModel):
    app: typing.Optional[App] = None
    content: typing.Optional[UserDataContent] = None
    id: int
    owner: typing.Optional[User] = None
    settings: typing.Optional[UserDataSettings] = None
    status: typing.Optional[UserDataStatus] = None
    user: typing.Optional[User] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
