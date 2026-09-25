

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok15(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    description: str
    item_type: typing_extensions.Annotated[str, FieldMetadata(alias="itemType"), pydantic.Field(alias="itemType")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    modify_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimezone"), pydantic.Field(alias="modifyTimestampTimezone")
    ]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    categories: typing.List[str]
    total_pages: typing_extensions.Annotated[str, FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages")]
    ics_date_of_service: typing_extensions.Annotated[
        str, FieldMetadata(alias="icsDateOfService"), pydantic.Field(alias="icsDateOfService")
    ]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    app_created_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="appCreatedBy"), pydantic.Field(alias="appCreatedBy")
    ]
    doc_type_id: typing_extensions.Annotated[str, FieldMetadata(alias="docTypeId"), pydantic.Field(alias="docTypeId")]
    is_restricted: typing_extensions.Annotated[
        str, FieldMetadata(alias="isRestricted"), pydantic.Field(alias="isRestricted")
    ]
    signoff_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="signoffStatus"), pydantic.Field(alias="signoffStatus")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
