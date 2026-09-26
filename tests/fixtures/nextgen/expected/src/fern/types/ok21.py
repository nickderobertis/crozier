

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok21(UniversalBaseModel):
    id: str
    health_concern_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="healthConcernId"), pydantic.Field(alias="healthConcernId")
    ]
    goal_id: typing_extensions.Annotated[str, FieldMetadata(alias="goalId"), pydantic.Field(alias="goalId")]
    detail: str
    category: str
    frequency: str
    progress: str
    review_date: typing_extensions.Annotated[str, FieldMetadata(alias="reviewDate"), pydantic.Field(alias="reviewDate")]
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")]
    status: str
    code_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="codeDescription"), pydantic.Field(alias="codeDescription")
    ]
    code_system: typing_extensions.Annotated[str, FieldMetadata(alias="codeSystem"), pydantic.Field(alias="codeSystem")]
    code_value: typing_extensions.Annotated[str, FieldMetadata(alias="codeValue"), pydantic.Field(alias="codeValue")]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    modify_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimezone"), pydantic.Field(alias="modifyTimestampTimezone")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
