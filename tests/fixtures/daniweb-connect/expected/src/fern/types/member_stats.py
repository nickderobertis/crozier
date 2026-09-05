

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MemberStats(UniversalBaseModel):
    answered_count: typing.Optional[int] = None
    endorsements_count: typing.Optional[int] = None
    posts_count: typing.Optional[int] = None
    reputation_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
