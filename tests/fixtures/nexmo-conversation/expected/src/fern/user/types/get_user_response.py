

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.name_user import NameUser
from ...types.user_id import UserId


class GetUserResponse(UniversalBaseModel):
    href: typing.Optional[str] = None
    id: typing.Optional[UserId] = None
    name: typing.Optional[NameUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
