

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_post_error409error import UsersPostError409Error
from .users_post_error409meta import UsersPostError409Meta


class UsersPostError409(UniversalBaseModel):
    success: bool
    error: UsersPostError409Error
    meta: typing.Optional[UsersPostError409Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
