

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .badge_code import BadgeCode
from .collar_code import CollarCode
from .hound import Hound
from .leash_code import LeashCode
from .tag_code import TagCode


class Kennel(UniversalBaseModel):
    tag: typing.Optional[TagCode] = None
    badge: typing.Optional[BadgeCode] = None
    collar: typing.Optional[CollarCode] = None
    leash: typing.Optional[LeashCode] = None
    resident: typing.Optional[Hound] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
