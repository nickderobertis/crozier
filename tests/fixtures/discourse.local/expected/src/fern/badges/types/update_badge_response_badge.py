

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateBadgeResponseBadge(UniversalBaseModel):
    allow_title: bool
    auto_revoke: bool
    badge_grouping_id: int
    badge_type_id: int
    description: str
    enabled: bool
    grant_count: int
    icon: str
    id: int
    image_url: typing.Optional[str] = None
    listable: bool
    long_description: str
    manually_grantable: bool
    multiple_grant: bool
    name: str
    query: typing.Optional[str] = None
    show_posts: bool
    slug: str
    system: bool
    target_posts: bool
    trigger: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
