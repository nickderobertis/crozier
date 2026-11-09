

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataAdministrativeActionsArrayItem(UniversalBaseModel):
    case_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="caseNumber"), pydantic.Field(alias="caseNumber")
    ] = None
    description: typing.Optional[str] = None
    effective_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="effectiveDate"), pydantic.Field(alias="effectiveDate")
    ] = None
    resulting_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resultingStatus"), pydantic.Field(alias="resultingStatus")
    ] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
