

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_post_error400error import UsersPostError400Error
from .users_post_error400meta import UsersPostError400Meta


class UsersPostError400(UniversalBaseModel):
    success: bool
    error: UsersPostError400Error
    meta: typing.Optional[UsersPostError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
