

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsRequest(UniversalBaseModel):
    test_code_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="TestCodeId"), pydantic.Field(alias="TestCodeId")
    ]
    is_next_gen_compendium_test: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsNextGenCompendiumTest"), pydantic.Field(alias="IsNextGenCompendiumTest")
    ]
    schedule_date_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="ScheduleDateTime"), pydantic.Field(alias="ScheduleDateTime")
    ]
    volume_quantity: typing_extensions.Annotated[
        str, FieldMetadata(alias="VolumeQuantity"), pydantic.Field(alias="VolumeQuantity")
    ]
    volume_unit: typing_extensions.Annotated[str, FieldMetadata(alias="VolumeUnit"), pydantic.Field(alias="VolumeUnit")]
    collection_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="CollectionDate"), pydantic.Field(alias="CollectionDate")
    ]
    source_site: typing_extensions.Annotated[str, FieldMetadata(alias="SourceSite"), pydantic.Field(alias="SourceSite")]
    source_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="SourceDescription"), pydantic.Field(alias="SourceDescription")
    ]
    additives: typing_extensions.Annotated[str, FieldMetadata(alias="Additives"), pydantic.Field(alias="Additives")]
    body_site: typing_extensions.Annotated[str, FieldMetadata(alias="BodySite"), pydantic.Field(alias="BodySite")]
    site_modifier: typing_extensions.Annotated[
        str, FieldMetadata(alias="SiteModifier"), pydantic.Field(alias="SiteModifier")
    ]
    specimen_role: typing_extensions.Annotated[
        str, FieldMetadata(alias="SpecimenRole"), pydantic.Field(alias="SpecimenRole")
    ]
    specimen_storage: typing_extensions.Annotated[
        str, FieldMetadata(alias="SpecimenStorage"), pydantic.Field(alias="SpecimenStorage")
    ]
    collection_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="CollectionMethod"), pydantic.Field(alias="CollectionMethod")
    ]
    comment: typing_extensions.Annotated[str, FieldMetadata(alias="Comment"), pydantic.Field(alias="Comment")]
    ordering_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderingReason"), pydantic.Field(alias="OrderingReason")
    ]
    expected_result_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="ExpectedResultDate"), pydantic.Field(alias="ExpectedResultDate")
    ]
    generated_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="GeneratedBy"), pydantic.Field(alias="GeneratedBy")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
