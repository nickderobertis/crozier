

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item29(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    fdb_name: typing_extensions.Annotated[str, FieldMetadata(alias="fdbName"), pydantic.Field(alias="fdbName")]
    medication_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="medicationName"), pydantic.Field(alias="medicationName")
    ]
    generic_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="genericName"), pydantic.Field(alias="genericName")
    ]
    brand_name: typing_extensions.Annotated[str, FieldMetadata(alias="brandName"), pydantic.Field(alias="brandName")]
    is_generic_selected: typing_extensions.Annotated[
        str, FieldMetadata(alias="isGenericSelected"), pydantic.Field(alias="isGenericSelected")
    ]
    dose: str
    route: str
    dose_form: typing_extensions.Annotated[str, FieldMetadata(alias="doseForm"), pydantic.Field(alias="doseForm")]
    original_start_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="originalStartDate"), pydantic.Field(alias="originalStartDate")
    ]
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")]
    stop_date: typing_extensions.Annotated[str, FieldMetadata(alias="stopDate"), pydantic.Field(alias="stopDate")]
    sig_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="sigDescription"), pydantic.Field(alias="sigDescription")
    ]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    source_product_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceProductId"), pydantic.Field(alias="sourceProductId")
    ]
    last_audit_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastAuditType"), pydantic.Field(alias="lastAuditType")
    ]
    representative_ndc_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="representativeNdcIndicator"), pydantic.Field(alias="representativeNdcIndicator")
    ]
    privacy_indicator: typing_extensions.Annotated[
        str, FieldMetadata(alias="privacyIndicator"), pydantic.Field(alias="privacyIndicator")
    ]
    is_hidden: typing_extensions.Annotated[str, FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")]
    dea_class_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="deaClassCode"), pydantic.Field(alias="deaClassCode")
    ]
    medication_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="medicationId"), pydantic.Field(alias="medicationId")
    ]
    ndc_id: typing_extensions.Annotated[str, FieldMetadata(alias="ndcId"), pydantic.Field(alias="ndcId")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    rx_norm_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="rxNormCode"), pydantic.Field(alias="rxNormCode")
    ]
    status: str
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
