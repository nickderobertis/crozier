

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok64(UniversalBaseModel):
    id: str
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    collection_date_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="collectionDateTime"), pydantic.Field(alias="collectionDateTime")
    ]
    collection_date_time_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="collectionDateTimeTimezone"), pydantic.Field(alias="collectionDateTimeTimezone")
    ]
    ordering_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderingProviderId"), pydantic.Field(alias="orderingProviderId")
    ]
    result_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="resultStatus"), pydantic.Field(alias="resultStatus")
    ]
    test_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="testDescription"), pydantic.Field(alias="testDescription")
    ]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    obr_comment: typing_extensions.Annotated[str, FieldMetadata(alias="obrComment"), pydantic.Field(alias="obrComment")]
    loinc_code: typing_extensions.Annotated[str, FieldMetadata(alias="loincCode"), pydantic.Field(alias="loincCode")]
    is_confidential: typing_extensions.Annotated[
        str, FieldMetadata(alias="isConfidential"), pydantic.Field(alias="isConfidential")
    ]
    order_test_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderTestId"), pydantic.Field(alias="orderTestId")
    ]
    is_microbiology: typing_extensions.Annotated[
        str, FieldMetadata(alias="isMicrobiology"), pydantic.Field(alias="isMicrobiology")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
