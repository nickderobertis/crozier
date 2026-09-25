

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok37(UniversalBaseModel):
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    is_required: typing_extensions.Annotated[str, FieldMetadata(alias="isRequired"), pydantic.Field(alias="isRequired")]
    acknowledged: str
    severity_level: typing_extensions.Annotated[
        str, FieldMetadata(alias="severityLevel"), pydantic.Field(alias="severityLevel")
    ]
    description: str
    entity_name: typing_extensions.Annotated[str, FieldMetadata(alias="entityName"), pydantic.Field(alias="entityName")]
    event_type: typing_extensions.Annotated[str, FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")]
    source_id: typing_extensions.Annotated[str, FieldMetadata(alias="sourceId"), pydantic.Field(alias="sourceId")]
    cause: str
    warning_detail: typing_extensions.Annotated[
        str, FieldMetadata(alias="warningDetail"), pydantic.Field(alias="warningDetail")
    ]
    warning_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="warningType"), pydantic.Field(alias="warningType")
    ]
    warning: str
    cause_text: typing_extensions.Annotated[str, FieldMetadata(alias="causeText"), pydantic.Field(alias="causeText")]
    override_text: typing_extensions.Annotated[
        str, FieldMetadata(alias="overrideText"), pydantic.Field(alias="overrideText")
    ]
    dur_audit_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="durAuditKey"), pydantic.Field(alias="durAuditKey")
    ]
    is_suppressed: typing_extensions.Annotated[
        str, FieldMetadata(alias="isSuppressed"), pydantic.Field(alias="isSuppressed")
    ]
    is_recorded_else_where: typing_extensions.Annotated[
        str, FieldMetadata(alias="isRecordedElseWhere"), pydantic.Field(alias="isRecordedElseWhere")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    display: str
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
