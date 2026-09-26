

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdRequest(UniversalBaseModel):
    comments: str
    category: str
    description: str
    secondary_to: typing_extensions.Annotated[
        str, FieldMetadata(alias="secondaryTo"), pydantic.Field(alias="secondaryTo")
    ]
    identified_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="identifiedDate"), pydantic.Field(alias="identifiedDate")
    ]
    resolved_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedDate"), pydantic.Field(alias="resolvedDate")
    ]
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
