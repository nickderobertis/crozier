

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetGroupAnalyticsResponse(UniversalBaseModel):
    member_count: typing.Optional[int] = None
    new_members: typing.Optional[int] = None
    active_members: typing.Optional[int] = None
    posts_count: typing.Optional[int] = None
    comments_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
