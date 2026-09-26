

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_email_delete_error500error import UsersEmailDeleteError500Error
from .users_email_delete_error500meta import UsersEmailDeleteError500Meta


class UsersEmailDeleteError500(UniversalBaseModel):
    success: bool
    error: UsersEmailDeleteError500Error
    meta: typing.Optional[UsersEmailDeleteError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
