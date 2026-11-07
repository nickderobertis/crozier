

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .audit_event_dto import AuditEventDto
from .entity_change_audit_event_dto_change_type import EntityChangeAuditEventDtoChangeType
from .entity_changes_dto import EntityChangesDto


class EntityChangeAuditEventDto(AuditEventDto):
    change_type: typing_extensions.Annotated[
        EntityChangeAuditEventDtoChangeType,
        FieldMetadata(alias="changeType"),
        pydantic.Field(alias="changeType", description="Type of change that occurred"),
    ]
    """
    Type of change that occurred
    """

    changes: typing.Optional[EntityChangesDto] = pydantic.Field(default=None)
    """
    Changes made to the entity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
