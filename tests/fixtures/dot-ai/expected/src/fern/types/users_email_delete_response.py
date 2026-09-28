

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_email_delete_response_data import UsersEmailDeleteResponseData
from .users_email_delete_response_meta import UsersEmailDeleteResponseMeta


class UsersEmailDeleteResponse(UniversalBaseModel):
    success: bool
    data: UsersEmailDeleteResponseData
    meta: typing.Optional[UsersEmailDeleteResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
