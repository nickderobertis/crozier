

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_email_delete_error404error import UsersEmailDeleteError404Error
from .users_email_delete_error404meta import UsersEmailDeleteError404Meta


class UsersEmailDeleteError404(UniversalBaseModel):
    success: bool
    error: UsersEmailDeleteError404Error
    meta: typing.Optional[UsersEmailDeleteError404Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
