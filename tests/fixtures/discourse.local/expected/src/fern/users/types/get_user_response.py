

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_response_user import GetUserResponseUser


class GetUserResponse(UniversalBaseModel):
    user: GetUserResponseUser
    user_badges: typing.List[typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
