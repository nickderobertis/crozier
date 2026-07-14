

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_badge_response_badge import CreateBadgeResponseBadge
from .create_badge_response_badge_types_item import CreateBadgeResponseBadgeTypesItem


class CreateBadgeResponse(UniversalBaseModel):
    badge: CreateBadgeResponseBadge
    badge_types: typing.List[CreateBadgeResponseBadgeTypesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
