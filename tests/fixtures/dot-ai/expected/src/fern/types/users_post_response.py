

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_post_response_data import UsersPostResponseData
from .users_post_response_meta import UsersPostResponseMeta


class UsersPostResponse(UniversalBaseModel):
    success: bool
    data: UsersPostResponseData
    meta: typing.Optional[UsersPostResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
