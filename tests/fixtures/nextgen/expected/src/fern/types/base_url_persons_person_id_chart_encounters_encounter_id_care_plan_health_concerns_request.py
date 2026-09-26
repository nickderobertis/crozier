

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsRequest(UniversalBaseModel):
    category: str
    other_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="otherCategory"), pydantic.Field(alias="otherCategory")
    ]
    comments: str
    health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="healthConcern"), pydantic.Field(alias="healthConcern")
    ]
    secondary_to: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryTo"), pydantic.Field(alias="secondaryTo")
    ]
    identified_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="identifiedDate"), pydantic.Field(alias="identifiedDate")
    ]
    category_id: typing_extensions.Annotated[str, FieldMetadata(alias="categoryId"), pydantic.Field(alias="categoryId")]
    resolved_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedDate"), pydantic.Field(alias="resolvedDate")
    ]
    code_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="codeDescription"), pydantic.Field(alias="codeDescription")
    ]
    code_system: typing_extensions.Annotated[str, FieldMetadata(alias="codeSystem"), pydantic.Field(alias="codeSystem")]
    code_value: typing_extensions.Annotated[str, FieldMetadata(alias="codeValue"), pydantic.Field(alias="codeValue")]
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
