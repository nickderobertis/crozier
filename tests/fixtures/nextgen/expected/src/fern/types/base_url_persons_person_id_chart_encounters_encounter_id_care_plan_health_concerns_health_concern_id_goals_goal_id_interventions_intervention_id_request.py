

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdRequest(
    UniversalBaseModel
):
    name: str
    category: str
    category_id: typing_extensions.Annotated[str, FieldMetadata(alias="categoryId"), pydantic.Field(alias="categoryId")]
    status: str
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")]
    frequency: str
    next_review_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="nextReviewDate"), pydantic.Field(alias="nextReviewDate")
    ]
    intervention_progress: typing_extensions.Annotated[
        str, FieldMetadata(alias="interventionProgress"), pydantic.Field(alias="interventionProgress")
    ]
    code_system: typing_extensions.Annotated[str, FieldMetadata(alias="codeSystem"), pydantic.Field(alias="codeSystem")]
    code_value: typing_extensions.Annotated[str, FieldMetadata(alias="codeValue"), pydantic.Field(alias="codeValue")]
    code_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="codeDescription"), pydantic.Field(alias="codeDescription")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
