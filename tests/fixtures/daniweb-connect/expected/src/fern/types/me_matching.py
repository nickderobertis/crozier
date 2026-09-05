

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MeMatching(UniversalBaseModel):
    goals: typing.Optional[typing.List[str]] = None
    interest_tags: typing.Optional[typing.List[str]] = None
    location_importance: typing.Optional[str] = None
    targeted_industry: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
