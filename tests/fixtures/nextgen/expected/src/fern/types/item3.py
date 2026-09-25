

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item3(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    encounter_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterDate"), pydantic.Field(alias="encounterDate")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    aip: str
    aip_priority: typing_extensions.Annotated[
        str, FieldMetadata(alias="aipPriority"), pydantic.Field(alias="aipPriority")
    ]
    description: str
    diagnosis_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCode"), pydantic.Field(alias="diagnosisCode")
    ]
    diagnosis_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisId"), pydantic.Field(alias="diagnosisId")
    ]
    encounter_diagnosis_priority: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterDiagnosisPriority"), pydantic.Field(alias="encounterDiagnosisPriority")
    ]
    icd9cm_code_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="icd9cmCodeId"), pydantic.Field(alias="icd9cmCodeId")
    ]
    report_display: typing_extensions.Annotated[
        str, FieldMetadata(alias="reportDisplay"), pydantic.Field(alias="reportDisplay")
    ]
    axis: str
    chief_complaint: typing_extensions.Annotated[
        str, FieldMetadata(alias="chiefComplaint"), pydantic.Field(alias="chiefComplaint")
    ]
    detail_type: typing_extensions.Annotated[str, FieldMetadata(alias="detailType"), pydantic.Field(alias="detailType")]
    detail_type_priority: typing_extensions.Annotated[
        str, FieldMetadata(alias="detailTypePriority"), pydantic.Field(alias="detailTypePriority")
    ]
    differential_diagnosis: typing_extensions.Annotated[
        str, FieldMetadata(alias="differentialDiagnosis"), pydantic.Field(alias="differentialDiagnosis")
    ]
    episode: str
    side: str
    site: str
    has_history_record: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasHistoryRecord"), pydantic.Field(alias="hasHistoryRecord")
    ]
    specifiers: str
    is_supplemental: typing_extensions.Annotated[
        str, FieldMetadata(alias="isSupplemental"), pydantic.Field(alias="isSupplemental")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
