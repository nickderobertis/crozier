

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cursor_pagination_info_dto import CursorPaginationInfoDto
from .entity_audit_events_response_dto_items_item import EntityAuditEventsResponseDtoItemsItem


class EntityAuditEventsResponseDto(UniversalBaseModel):
    pagination: CursorPaginationInfoDto
    items: typing.Optional[typing.List[EntityAuditEventsResponseDtoItemsItem]] = pydantic.Field(default=None)
    """
    Audit events for the entity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
