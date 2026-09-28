

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_post_error500error import UsersPostError500Error
from .users_post_error500meta import UsersPostError500Meta


class UsersPostError500(UniversalBaseModel):
    success: bool
    error: UsersPostError500Error
    meta: typing.Optional[UsersPostError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
