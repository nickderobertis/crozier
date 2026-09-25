

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartMedicationsMedicationIdNotesRequest(UniversalBaseModel):
    type: typing_extensions.Annotated[str, FieldMetadata(alias="Type"), pydantic.Field(alias="Type")]
    note: typing_extensions.Annotated[str, FieldMetadata(alias="Note"), pydantic.Field(alias="Note")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
