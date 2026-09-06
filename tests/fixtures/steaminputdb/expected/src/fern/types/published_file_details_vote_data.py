

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PublishedFileDetailsVoteData(UniversalBaseModel):
    score: typing.Optional[float] = None
    trusted_score: typing.Optional[float] = None
    trusted_votes_down: typing.Optional[int] = None
    trusted_votes_up: typing.Optional[int] = None
    votes_down: typing.Optional[int] = None
    votes_up: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
