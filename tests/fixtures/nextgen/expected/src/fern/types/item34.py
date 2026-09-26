

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item34(UniversalBaseModel):
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    check_in_date_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="checkInDateTime"), pydantic.Field(alias="checkInDateTime")
    ]
    check_in_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="checkInTimezone"), pydantic.Field(alias="checkInTimezone")
    ]
    check_out_date_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="checkOutDateTime"), pydantic.Field(alias="checkOutDateTime")
    ]
    check_out_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="checkOutTimezone"), pydantic.Field(alias="checkOutTimezone")
    ]
    encounter_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterNumber"), pydantic.Field(alias="encounterNumber")
    ]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    id: str
    is_locked: typing_extensions.Annotated[str, FieldMetadata(alias="isLocked"), pydantic.Field(alias="isLocked")]
    is_sensitive: typing_extensions.Annotated[
        str, FieldMetadata(alias="isSensitive"), pydantic.Field(alias="isSensitive")
    ]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    location_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="locationName"), pydantic.Field(alias="locationName")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    print_on_statements: typing_extensions.Annotated[
        str, FieldMetadata(alias="printOnStatements"), pydantic.Field(alias="printOnStatements")
    ]
    referring_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="referringProviderId"), pydantic.Field(alias="referringProviderId")
    ]
    referring_provider_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="referringProviderName"), pydantic.Field(alias="referringProviderName")
    ]
    rendering_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="renderingProviderId"), pydantic.Field(alias="renderingProviderId")
    ]
    rendering_provider_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="renderingProviderName"), pydantic.Field(alias="renderingProviderName")
    ]
    status: str
    suppress_outreach: typing_extensions.Annotated[
        str, FieldMetadata(alias="suppressOutreach"), pydantic.Field(alias="suppressOutreach")
    ]
    suppress_portal: typing_extensions.Annotated[
        str, FieldMetadata(alias="suppressPortal"), pydantic.Field(alias="suppressPortal")
    ]
    timestamp: str
    timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="timestampTimezone"), pydantic.Field(alias="timestampTimezone")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
