

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .me_business_card import MeBusinessCard
from .me_location import MeLocation
from .me_matching import MeMatching
from .me_profile import MeProfile
from .me_settings import MeSettings
from .me_usage import MeUsage
from .member import Member


class Me(UniversalBaseModel):
    business_card: typing.Optional[MeBusinessCard] = None
    community_persona: typing.Optional[Member] = None
    id: int
    location: typing.Optional[MeLocation] = None
    matching: typing.Optional[MeMatching] = None
    profile: typing.Optional[MeProfile] = None
    settings: typing.Optional[MeSettings] = None
    usage: typing.Optional[MeUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
