

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListUserBadgesResponseBadgesItem(UniversalBaseModel):
    allow_title: bool
    badge_grouping_id: int
    badge_type_id: int
    description: str
    enabled: bool
    grant_count: int
    icon: str
    id: int
    image_url: typing.Optional[str] = None
    listable: bool
    manually_grantable: bool
    multiple_grant: bool
    name: str
    slug: str
    system: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
