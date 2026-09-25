

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdRequest(UniversalBaseModel):
    id: str
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    test_code_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCodeId"), pydantic.Field(alias="testCodeId")
    ]
    test_code_text: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCodeText"), pydantic.Field(alias="testCodeText")
    ]
    test_code_system: typing_extensions.Annotated[
        str, FieldMetadata(alias="testCodeSystem"), pydantic.Field(alias="testCodeSystem")
    ]
    collection_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="collectionTime"), pydantic.Field(alias="collectionTime")
    ]
    volume_quantity: typing_extensions.Annotated[
        str, FieldMetadata(alias="volumeQuantity"), pydantic.Field(alias="volumeQuantity")
    ]
    volume_units: typing_extensions.Annotated[
        str, FieldMetadata(alias="volumeUnits"), pydantic.Field(alias="volumeUnits")
    ]
    spec_src_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="specSrcCode"), pydantic.Field(alias="specSrcCode")
    ]
    spec_src_desc: typing_extensions.Annotated[
        str, FieldMetadata(alias="specSrcDesc"), pydantic.Field(alias="specSrcDesc")
    ]
    spec_src_additives: typing_extensions.Annotated[
        str, FieldMetadata(alias="specSrcAdditives"), pydantic.Field(alias="specSrcAdditives")
    ]
    scheduled_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="scheduledTime"), pydantic.Field(alias="scheduledTime")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    generated_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="generatedBy"), pydantic.Field(alias="generatedBy")
    ]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    loinc_code: typing_extensions.Annotated[str, FieldMetadata(alias="loincCode"), pydantic.Field(alias="loincCode")]
    snomed_code: typing_extensions.Annotated[str, FieldMetadata(alias="snomedCode"), pydantic.Field(alias="snomedCode")]
    spec_src_body_site: typing_extensions.Annotated[
        str, FieldMetadata(alias="specSrcBodySite"), pydantic.Field(alias="specSrcBodySite")
    ]
    spec_src_site_modifier: typing_extensions.Annotated[
        str, FieldMetadata(alias="specSrcSiteModifier"), pydantic.Field(alias="specSrcSiteModifier")
    ]
    spec_src_role: typing_extensions.Annotated[
        str, FieldMetadata(alias="specSrcRole"), pydantic.Field(alias="specSrcRole")
    ]
    spec_src_storage: typing_extensions.Annotated[
        str, FieldMetadata(alias="specSrcStorage"), pydantic.Field(alias="specSrcStorage")
    ]
    spec_src_collection_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="specSrcCollectionMethod"), pydantic.Field(alias="specSrcCollectionMethod")
    ]
    collector_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="collectorId"), pydantic.Field(alias="collectorId")
    ]
    test_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="testComment"), pydantic.Field(alias="testComment")
    ]
    expected_result_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="expectedResultDate"), pydantic.Field(alias="expectedResultDate")
    ]
    collection_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="collectionTimezone"), pydantic.Field(alias="collectionTimezone")
    ]
    scheduled_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="scheduledTimezone"), pydantic.Field(alias="scheduledTimezone")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    modify_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimezone"), pydantic.Field(alias="modifyTimestampTimezone")
    ]
    charge_id: typing_extensions.Annotated[str, FieldMetadata(alias="chargeId"), pydantic.Field(alias="chargeId")]
    ordering_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderingReason"), pydantic.Field(alias="orderingReason")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
