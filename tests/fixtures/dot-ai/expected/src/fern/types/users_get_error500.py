

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_get_error500error import UsersGetError500Error
from .users_get_error500meta import UsersGetError500Meta


class UsersGetError500(UniversalBaseModel):
    success: bool
    error: UsersGetError500Error
    meta: typing.Optional[UsersGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
