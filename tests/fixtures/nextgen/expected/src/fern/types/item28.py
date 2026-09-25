

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item28(UniversalBaseModel):
    panel_id: typing_extensions.Annotated[str, FieldMetadata(alias="panelId"), pydantic.Field(alias="panelId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    observation_sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="observationSequenceNumber"), pydantic.Field(alias="observationSequenceNumber")
    ]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    observation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="observationId"), pydantic.Field(alias="observationId")
    ]
    result_code: typing_extensions.Annotated[str, FieldMetadata(alias="resultCode"), pydantic.Field(alias="resultCode")]
    result_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="resultDescription"), pydantic.Field(alias="resultDescription")
    ]
    code_system: typing_extensions.Annotated[str, FieldMetadata(alias="codeSystem"), pydantic.Field(alias="codeSystem")]
    observation_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="observationValue"), pydantic.Field(alias="observationValue")
    ]
    abnormality_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="abnormalityCode"), pydantic.Field(alias="abnormalityCode")
    ]
    abnormality: str
    result_type: typing_extensions.Annotated[str, FieldMetadata(alias="resultType"), pydantic.Field(alias="resultType")]
    units: str
    reference_range: typing_extensions.Annotated[
        str, FieldMetadata(alias="referenceRange"), pydantic.Field(alias="referenceRange")
    ]
    observation_result_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="observationResultStatus"), pydantic.Field(alias="observationResultStatus")
    ]
    clinical_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="clinicalName"), pydantic.Field(alias="clinicalName")
    ]
    observation_date_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="observationDateTime"), pydantic.Field(alias="observationDateTime")
    ]
    observation_date_time_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="observationDateTimeTimezone"), pydantic.Field(alias="observationDateTimeTimezone")
    ]
    loinc_code: typing_extensions.Annotated[str, FieldMetadata(alias="loincCode"), pydantic.Field(alias="loincCode")]
    result_sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="resultSequenceNumber"), pydantic.Field(alias="resultSequenceNumber")
    ]
    has_comment: typing_extensions.Annotated[str, FieldMetadata(alias="hasComment"), pydantic.Field(alias="hasComment")]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    is_signed_off: typing_extensions.Annotated[
        str, FieldMetadata(alias="isSignedOff"), pydantic.Field(alias="isSignedOff")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
