

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_get_response_data import UsersGetResponseData
from .users_get_response_meta import UsersGetResponseMeta


class UsersGetResponse(UniversalBaseModel):
    success: bool
    data: UsersGetResponseData
    meta: typing.Optional[UsersGetResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
