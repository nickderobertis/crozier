

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PublishedFileAuthorSnapshot(UniversalBaseModel):
    game_branch_max: typing.Optional[str] = None
    game_branch_min: typing.Optional[str] = None
    manifestid: typing.Optional[int] = None
    timestamp: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
