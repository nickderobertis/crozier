

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok46(UniversalBaseModel):
    vaccine_vis_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="vaccineVisId"), pydantic.Field(alias="vaccineVisId")
    ]
    order_vaccine_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderVaccineId"), pydantic.Field(alias="orderVaccineId")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    vis_give_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="visGiveDate"), pydantic.Field(alias="visGiveDate")
    ]
    vis_give_date_time_zone: typing_extensions.Annotated[
        str, FieldMetadata(alias="visGiveDateTimeZone"), pydantic.Field(alias="visGiveDateTimeZone")
    ]
    vis_publish_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="visPublishDate"), pydantic.Field(alias="visPublishDate")
    ]
    given_vis_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="givenVisId"), pydantic.Field(alias="givenVisId")
    ]
    vaccine_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="vaccineType"), pydantic.Field(alias="vaccineType")
    ]
    vis_document_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="visDocumentType"), pydantic.Field(alias="visDocumentType")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    vis_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="visDescription"), pydantic.Field(alias="visDescription")
    ]
    language_id: typing_extensions.Annotated[str, FieldMetadata(alias="languageId"), pydantic.Field(alias="languageId")]
    given_by: typing_extensions.Annotated[str, FieldMetadata(alias="givenBy"), pydantic.Field(alias="givenBy")]
    language_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="languageName"), pydantic.Field(alias="languageName")
    ]
    vis_history_publish_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="visHistoryPublishDate"), pydantic.Field(alias="visHistoryPublishDate")
    ]
    given_vis_vaccine_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="givenVisVaccineType"), pydantic.Field(alias="givenVisVaccineType")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
