

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_status_statuses_find200response_ocs import UserStatusStatusesFind200ResponseOcs


class UserStatusStatusesFind200Response(UniversalBaseModel):
    ocs: UserStatusStatusesFind200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
