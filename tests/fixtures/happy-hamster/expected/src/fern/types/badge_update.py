

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .badge import Badge
from .badge_update_reason import BadgeUpdateReason


class BadgeUpdate(UniversalBaseModel):
    """
    latest Badges of a specific user
    """

    badges: typing.List[Badge]
    reason: BadgeUpdateReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
