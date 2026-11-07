

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .audit_actor_info_dto import AuditActorInfoDto
from .audit_event_dto_severity import AuditEventDtoSeverity


class AuditEventDto(UniversalBaseModel):
    entity_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="entityId"),
        pydantic.Field(alias="entityId", description="Identifier of the entity related to this event"),
    ] = None
    """
    Identifier of the entity related to this event
    """

    entity_model: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="entityModel"),
        pydantic.Field(alias="entityModel", description="Type of the entity related to this event (model.version)"),
    ] = None
    """
    Type of the entity related to this event (model.version)
    """

    consistency_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="consistencyTime"),
        pydantic.Field(alias="consistencyTime", description="Cyoda consistency time"),
    ] = None
    """
    Cyoda consistency time
    """

    transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionId"),
        pydantic.Field(alias="transactionId", description="Transaction identifier related to this event"),
    ] = None
    """
    Transaction identifier related to this event
    """

    severity: AuditEventDtoSeverity = pydantic.Field()
    """
    Severity level of the event
    """

    details: typing.Optional[str] = pydantic.Field(default=None)
    """
    Details of the event
    """

    system: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Flag indicating whether this is a system-level event
    """

    utc_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="utcTime"),
        pydantic.Field(alias="utcTime", description="UTC time when the event occurred"),
    ]
    """
    UTC time when the event occurred
    """

    micros_time: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="microsTime"),
        pydantic.Field(alias="microsTime", description="time in microseconds when the event occurred"),
    ]
    """
    time in microseconds when the event occurred
    """

    actor: typing.Optional[AuditActorInfoDto] = pydantic.Field(default=None)
    """
    Actor related to this event
    """

    audit_event_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="auditEventType"), pydantic.Field(alias="auditEventType")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
