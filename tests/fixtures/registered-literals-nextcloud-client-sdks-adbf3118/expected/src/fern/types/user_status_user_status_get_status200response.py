

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_status_user_status_get_status200response_ocs import UserStatusUserStatusGetStatus200ResponseOcs


class UserStatusUserStatusGetStatus200Response(UniversalBaseModel):
    ocs: UserStatusUserStatusGetStatus200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
