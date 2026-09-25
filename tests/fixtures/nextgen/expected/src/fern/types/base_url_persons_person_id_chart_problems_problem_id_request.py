

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .interaction import Interaction


class BaseUrlPersonsPersonIdChartProblemsProblemIdRequest(UniversalBaseModel):
    concept_id: typing_extensions.Annotated[str, FieldMetadata(alias="conceptId"), pydantic.Field(alias="conceptId")]
    description: str
    side: str
    site: str
    onset_date: typing_extensions.Annotated[str, FieldMetadata(alias="onsetDate"), pydantic.Field(alias="onsetDate")]
    last_addressed_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastAddressedDate"), pydantic.Field(alias="lastAddressedDate")
    ]
    resolved_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedDate"), pydantic.Field(alias="resolvedDate")
    ]
    resolved_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedReason"), pydantic.Field(alias="resolvedReason")
    ]
    problem_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="problemStatus"), pydantic.Field(alias="problemStatus")
    ]
    clinical_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="clinicalStatusId"), pydantic.Field(alias="clinicalStatusId")
    ]
    is_chronic: typing_extensions.Annotated[str, FieldMetadata(alias="isChronic"), pydantic.Field(alias="isChronic")]
    has_secondary_condition: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasSecondaryCondition"), pydantic.Field(alias="hasSecondaryCondition")
    ]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    is_recorded_elsewhere: typing_extensions.Annotated[
        str, FieldMetadata(alias="isRecordedElsewhere"), pydantic.Field(alias="isRecordedElsewhere")
    ]
    recorded_elsewhere_source: typing_extensions.Annotated[
        str, FieldMetadata(alias="recordedElsewhereSource"), pydantic.Field(alias="recordedElsewhereSource")
    ]
    responsible_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="responsibleProviderId"), pydantic.Field(alias="responsibleProviderId")
    ]
    is_comorbid: typing_extensions.Annotated[str, FieldMetadata(alias="isComorbid"), pydantic.Field(alias="isComorbid")]
    interactions: typing.List[Interaction]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
