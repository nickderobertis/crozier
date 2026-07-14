

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_badge_response_badge import UpdateBadgeResponseBadge
from .update_badge_response_badge_types_item import UpdateBadgeResponseBadgeTypesItem


class UpdateBadgeResponse(UniversalBaseModel):
    badge: UpdateBadgeResponseBadge
    badge_types: typing.List[UpdateBadgeResponseBadgeTypesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
