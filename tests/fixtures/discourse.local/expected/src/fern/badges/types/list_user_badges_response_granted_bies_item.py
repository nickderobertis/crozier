

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListUserBadgesResponseGrantedBiesItem(UniversalBaseModel):
    admin: bool
    avatar_template: str
    flair_name: typing.Optional[str] = None
    id: int
    moderator: bool
    name: str
    trust_level: int
    username: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
