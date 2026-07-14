

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetTopicResponseDetailsParticipantsItem(UniversalBaseModel):
    admin: bool
    avatar_template: str
    flair_bg_color: typing.Optional[str] = None
    flair_color: typing.Optional[str] = None
    flair_name: typing.Optional[str] = None
    flair_url: typing.Optional[str] = None
    id: int
    moderator: bool
    name: str
    post_count: int
    primary_group_name: typing.Optional[str] = None
    trust_level: int
    username: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
