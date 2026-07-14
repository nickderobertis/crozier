

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListUserBadgesResponseUserBadgesItem(UniversalBaseModel):
    badge_id: int
    can_favorite: bool
    granted_at: str
    granted_by_id: int
    grouping_position: int
    id: int
    is_favorite: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
