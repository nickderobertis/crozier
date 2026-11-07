

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_status_statuses_find_all200response_ocs import UserStatusStatusesFindAll200ResponseOcs


class UserStatusStatusesFindAll200Response(UniversalBaseModel):
    ocs: UserStatusStatusesFindAll200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
